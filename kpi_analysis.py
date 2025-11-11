# Calculate KPI 1: Average Rating by Restaurant Type
kpi1 = df.groupby('listed_in(type)')['rate_numeric'].agg(['mean', 'count']).round(2)
kpi1.columns = ['Average_Rating', 'Count']
print("KPI 1: Average Rating by Restaurant Type")
print(kpi1)
print()

# Calculate KPI 2: Online Delivery Adoption Rate
kpi2_calc = df['has_online_order'].value_counts()
online_delivery_rate = (df['has_online_order'].sum() / len(df) * 100)
print(f"KPI 2: Online Delivery Adoption Rate")
print(f"Restaurants with Online Delivery: {df['has_online_order'].sum()} out of {len(df)}")
print(f"Online Delivery Adoption Rate: {online_delivery_rate:.2f}%")
print()

# Calculate KPI 3: Offline Dining Preference Rate (book_table capability)
offline_dining_rate = (df['has_book_table'].sum() / len(df) * 100)
print(f"KPI 3: Offline Dining Preference Rate (Book Table Available)")
print(f"Restaurants with Book Table: {df['has_book_table'].sum()} out of {len(df)}")
print(f"Offline Dining Preference Rate: {offline_dining_rate:.2f}%")
print()

# Calculate KPI 4: Average Cost for Two by Restaurant Type
kpi4 = df.groupby('listed_in(type)')['approx_cost(for two people)'].agg(['mean', 'median', 'min', 'max']).round(2)
print("KPI 4: Average Cost for Two by Restaurant Type")
print(kpi4)
print()

# Calculate KPI 5: Popular Price Range (Customer Spending Behavior)
# Create price ranges
def categorize_price(cost):
    if cost <= 400:
        return 'Budget (≤400)'
    elif cost <= 700:
        return 'Mid-range (401-700)'
    else:
        return 'Premium (>700)'

df['price_range'] = df['approx_cost(for two people)'].apply(categorize_price)
kpi5 = df['price_range'].value_counts().sort_values(ascending=False)
kpi5_pct = (kpi5 / len(df) * 100).round(2)

print("KPI 5: Popular Price Range (Customer Spending Behavior)")
print("\nCount by Price Range:")
print(kpi5)
print("\nPercentage by Price Range:")
print(kpi5_pct)
