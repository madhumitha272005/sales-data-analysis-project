import pandas as pd

# ---------- STEP 1: LOAD DATA ----------
# Load the sales dataset from CSV file
try:
    df = pd.read_csv("sales_data.csv")
    print("✅ Sales data loaded successfully.\n")
except FileNotFoundError:
    print("❌ Error: sales_data.csv file not found.")
    exit()

# ---------- STEP 2: EXPLORE DATA ----------
print("📌 Dataset Overview:")
print(df.head(), "\n")

print("📌 Dataset Information:")
print(df.info(), "\n")

print("📌 Dataset Shape:")
print(df.shape, "\n")

# ---------- STEP 3: CLEAN DATA ----------
# Handle missing values
df.fillna(0, inplace=True)

# Remove duplicate records
df.drop_duplicates(inplace=True)

print("✅ Data cleaning completed.\n")

# ---------- STEP 4: ANALYZE SALES ----------

# Calculate total revenue
total_revenue = df["Total_Sales"].sum()

# Find best-selling product based on total sales
best_selling_product = (
    df.groupby("Product")["Total_Sales"]
    .sum()
    .idxmax()
)

# Calculate average sales per transaction
average_sales = df["Total_Sales"].mean()

# Calculate total quantity sold
total_quantity = df["Quantity"].sum()

# ---------- STEP 5: CREATE REPORT ----------
print("📊 SALES ANALYSIS REPORT")
print("-" * 30)

print(f"💰 Total Revenue: ₹{total_revenue:,.2f}")
print(f"🏆 Best-Selling Product: {best_selling_product}")
print(f"📦 Total Quantity Sold: {int(total_quantity)}")
print(f"📈 Average Sales per Transaction: ₹{average_sales:,.2f}")

print("\n✅ Analysis completed successfully.")
print("🚀 Thank you for using the Sales Data Analysis Program!")
