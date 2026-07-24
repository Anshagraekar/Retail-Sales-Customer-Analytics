import pandas as pd
import random

# =====================================================
# Load Orders
# =====================================================

INPUT_FILE = "Orders.xlsx"          # <-- change if needed
OUTPUT_FILE = "Orders_Updated.xlsx"

orders = pd.read_excel(INPUT_FILE)

random.seed(42)

# =====================================================
# Base Delivery Days by Courier
# =====================================================

courier_days = {
    "Blue Dart": (2, 4),
    "FedEx": (2, 5),
    "Delhivery": (3, 5),
    "UPS": (4, 6),
    "XpressBees": (5, 7),
    "DHL": (6, 8)
}

# =====================================================
# Ship Mode Adjustment
# =====================================================

ship_adjustment = {
    "Same Day": -2,
    "First Class": -1,
    "Second Class": 0,
    "Standard Class": 1
}

# =====================================================
# Generate Delivery Days
# =====================================================

delivery_days = []

for _, row in orders.iterrows():

    courier = row["Courier Partner"]
    ship_mode = row["Ship Mode"]

    # Base courier speed
    low, high = courier_days.get(courier, (3, 6))
    days = random.randint(low, high)

    # Ship mode adjustment
    days += ship_adjustment.get(ship_mode, 0)

    # Small random variation
    days += random.choice([-1, 0, 0, 1])

    # Keep realistic bounds
    days = max(1, min(days, 10))

    delivery_days.append(days)

orders["Delivery Days"] = delivery_days

# =====================================================
# Update Ship Date
# =====================================================

orders["Order Date"] = pd.to_datetime(orders["Order Date"])
orders["Ship Date"] = orders["Order Date"] + pd.to_timedelta(
    orders["Delivery Days"], unit="D"
)

# =====================================================
# Save
# =====================================================

orders.to_excel(OUTPUT_FILE, index=False)

print("Done!")
print("Saved as:", OUTPUT_FILE)

print("\nAverage Delivery Days by Courier:\n")
print(
    orders.groupby("Courier Partner")["Delivery Days"]
    .mean()
    .sort_values()
)