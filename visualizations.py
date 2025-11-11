import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')
sns.set_palette('husl')

# Create a figure with 5 subplots
fig = plt.figure(figsize=(18, 14))

# KPI 1: Average Rating by Restaurant Type
ax1 = plt.subplot(3, 2, 1)
kpi1_data = df.groupby('listed_in(type)')['rate_numeric'].mean().sort_values(ascending=False)
bars1 = ax1.bar(kpi1_data.index, kpi1_data.values, color=sns.color_palette('husl', len(kpi1_data)))
ax1.set_title('KPI 1: Average Rating by Restaurant Type', fontsize=14, fontweight='bold')
ax1.set_ylabel('Average Rating', fontsize=11)
ax1.set_xlabel('Restaurant Type', fontsize=11)
ax1.set_ylim(0, 5)
for i, bar in enumerate(bars1):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height,
            f'{height:.2f}', ha='center', va='bottom', fontsize=10)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.grid(axis='y', linestyle='--', alpha=0.3)

# KPI 2: Online Delivery Adoption Rate
ax2 = plt.subplot(3, 2, 2)
online_data = df['online_order'].value_counts()
colors2 = ['#2ecc71', '#e74c3c']
wedges, texts, autotexts = ax2.pie(online_data.values, labels=online_data.index, autopct='%1.1f%%',
                                     colors=colors2, startangle=90, textprops={'fontsize': 11, 'weight': 'bold'})
ax2.set_title('KPI 2: Online Delivery Adoption Rate\n(58 restaurants out of 148 = 39.19%)',
              fontsize=14, fontweight='bold')

# KPI 3: Offline Dining Preference Rate
ax3 = plt.subplot(3, 2, 3)
offline_data = df['book_table'].value_counts()
colors3 = ['#e74c3c', '#3498db']
wedges, texts, autotexts = ax3.pie(offline_data.values, labels=offline_data.index, autopct='%1.1f%%',
                                     colors=colors3, startangle=90, textprops={'fontsize': 11, 'weight': 'bold'})
ax3.set_title('KPI 3: Offline Dining Preference Rate\n(Book Table Available: 8 restaurants = 5.41%)',
              fontsize=14, fontweight='bold')

# KPI 4: Average Cost for Two by Restaurant Type
ax4 = plt.subplot(3, 2, 4)
kpi4_data = df.groupby('listed_in(type)')['approx_cost(for two people)'].mean().sort_values(ascending=False)
bars4 = ax4.bar(kpi4_data.index, kpi4_data.values, color=sns.color_palette('husl', len(kpi4_data)))
ax4.set_title('KPI 4: Average Cost for Two by Restaurant Type', fontsize=14, fontweight='bold')
ax4.set_ylabel('Average Cost (₹)', fontsize=11)
ax4.set_xlabel('Restaurant Type', fontsize=11)
for i, bar in enumerate(bars4):
    height = bar.get_height()
    ax4.text(bar.get_x() + bar.get_width()/2., height,
            f'₹{height:.0f}', ha='center', va='bottom', fontsize=10)
ax4.spines['top'].set_visible(False)
ax4.spines['right'].set_visible(False)
ax4.grid(axis='y', linestyle='--', alpha=0.3)

# KPI 5: Popular Price Range
ax5 = plt.subplot(3, 2, 5)
price_order = ['Budget (≤400)', 'Mid-range (401-700)', 'Premium (>700)']
kpi5_ordered = df['price_range'].value_counts().reindex(price_order)
bars5 = ax5.bar(range(len(kpi5_ordered)), kpi5_ordered.values, color=sns.color_palette('husl', len(kpi5_ordered)))
ax5.set_title('KPI 5: Popular Price Range (Customer Spending Behavior)', fontsize=14, fontweight='bold')
ax5.set_ylabel('Number of Restaurants', fontsize=11)
ax5.set_xlabel('Price Range', fontsize=11)
ax5.set_xticks(range(len(kpi5_ordered)))
ax5.set_xticklabels(kpi5_ordered.index, rotation=15, ha='right')
for i, bar in enumerate(bars5):
    height = bar.get_height()
    ax5.text(bar.get_x() + bar.get_width()/2., height,
            f'{int(height)}\n({height/len(df)*100:.1f}%)', ha='center', va='bottom', fontsize=10)
ax5.spines['top'].set_visible(False)
ax5.spines['right'].set_visible(False)
ax5.grid(axis='y', linestyle='--', alpha=0.3)

# Add overall summary as a text box
ax6 = plt.subplot(3, 2, 6)
ax6.axis('off')
summary_text = f"""
ZOMATO RESTAURANT ANALYSIS - KEY INSIGHTS

KPI 1: Average Rating by Restaurant Type
• 'Other' category leads: 3.91/5
• Buffets: 3.84/5 | Cafes: 3.77/5 | Dining: 3.57/5

KPI 2: Online Delivery Adoption
• 39.19% of restaurants offer online delivery
• 60.81% do not have online delivery service

KPI 3: Offline Dining (Book Table)
• Only 5.41% of restaurants allow table booking
• 94.59% operate on first-come-first-serve basis

KPI 4: Average Cost for Two
• Buffets & Other: ~₹670 (Premium pricing)
• Cafes: ₹545 (Mid-range)
• Dining: ₹357 (Budget-friendly)

KPI 5: Customer Spending Behavior
• Budget (≤₹400): 57.43% (Most popular)
• Mid-range (₹401-700): 29.05%
• Premium (>₹700): 13.51%

Dataset: 148 restaurants analyzed
"""
ax6.text(0.05, 0.95, summary_text, transform=ax6.transAxes, fontsize=11,
         verticalalignment='top', fontfamily='monospace',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))

plt.tight_layout()
plt.savefig("/tmp/zomato_kpi_analysis.png", dpi=300, bbox_inches="tight")  # Saving in Temporary Folder
print("Figure saved in /tmp (temporary folder).")

from google.colab import files  # works in Colab / Vertex AI. 
files.download("/tmp/zomato_kpi_analysis.png") # Download file from Temporary Folder
