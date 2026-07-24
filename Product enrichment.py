import pandas as pd
import random
from datetime import datetime, timedelta

# Load products
df = pd.read_excel("Products.xlsx")

# Suppliers by category
suppliers = {
    "Technology": [
        "Tech Solutions",
        "Digital World",
        "Global Electronics",
        "Innovate Tech",
        "Smart Devices Inc"
    ],

    "Furniture": [
        "Furniture Depot",
        "Urban Furnishings",
        "Home Comfort Ltd",
        "WoodCraft",
        "Elite Furniture"
    ],

    "Office Supplies": [
        "Office World",
        "Stationery Hub",
        "Paper Plus",
        "Office Essentials",
        "Business Supplies Co"
    ]
}

# Warranty by category
warranty = {
    "Technology": [12, 24, 36],
    "Furniture": [6, 12, 24],
    "Office Supplies": [0]
}

unit_cost = []
supplier = []
rating = []
launch_date = []
warranty_months = []

for _, row in df.iterrows():

    cat = row["Category"]

    supplier.append(random.choice(suppliers[cat]))

    price = random.uniform(20, 1000)

    cost = price * random.uniform(0.55, 0.80)

    unit_cost.append(round(cost, 2))

    rating.append(round(random.uniform(3.6, 5.0), 1))

    warranty_months.append(random.choice(warranty[cat]))

    random_days = random.randint(0, 365 * 5)

    launch = datetime.today() - timedelta(days=random_days)

    launch_date.append(launch.date())

df["Supplier"] = supplier
df["Unit Cost"] = unit_cost
df["Rating"] = rating
df["Warranty Months"] = warranty_months
df["Launch Date"] = launch_date

df.to_excel("Products_Enriched.xlsx", index=False)

print("Done!")