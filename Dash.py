import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the page configuration (optional)
st.set_page_config(page_title="5G Smartphone Dashboard", layout="wide")

# Load your dataset
df = pd.read_csv(r"C:\Users\USER\Desktop\5g_smartphones_dataset.csv")

# Title for the dashboard
st.title("📊 5G Smartphone Dashboard")

# -----------------------------------------------
# 1. Correlation Heatmap of RAM, ROM, Battery, and Price
# -----------------------------------------------
st.header("Correlation Heatmap of RAM, ROM, Battery, and Price")
fig1, ax1 = plt.subplots(figsize=(12, 5 ))
sns.heatmap(df[["Battery (mAh)", "RAM (GB)", "ROM (GB)", "Price (Rs.)"]].corr(),
            annot=True, cmap='GnBu', ax = ax1)
ax1.set_title("Correlation Heatmap of RAM, ROM, Battery, and Price")
st.pyplot(fig1 )

# -----------------------------------------------
# 2. Brand Influence on Pricing
# -----------------------------------------------
st.header("Brand Influence on Pricing")
fig2, ax2 = plt.subplots(figsize=(12, 5))
df.groupby('Brand')['Price (Rs.)'].mean().astype(int).sort_values(ascending=False) \
  .plot(kind='bar', color="teal", edgecolor="black" , ax = ax2)
ax2.set_xlabel('Brand')
ax2.set_ylabel('Average Price (Rs.)')
ax2.set_title('Brand Influence on Pricing')
plt.xticks(rotation=45)
st.pyplot(fig2)

# -----------------------------------------------
# 3. Screen Size vs. Price
# -----------------------------------------------
st.header("Screen Size vs. Price")
fig3, ax3 = plt.subplots(figsize=(12, 5))
df.plot(kind='scatter', x='Screen Size (in)', y='Price (Rs.)', color='skyblue', ax=ax3)
ax3.set_title("Screen Size vs. Price of 5G Smartphones in India")
st.pyplot(fig3)

# -----------------------------------------------
# 4. Market Share of Top(5) 5G Smartphone Brands in India
# -----------------------------------------------
st.header("Market Share of Top(5) 5G Smartphone Brands in India")
fig4, ax4 = plt.subplots(figsize=(3,3))
df['Brand'].value_counts().nlargest(5).plot(kind='pie', autopct="%.0f%%", 
                                              colors=['teal', 'turquoise', 'darkturquoise', 
                                                      'lightseagreen', 'mediumturquoise'], ax=ax4)
ax4.set_title("Market Share of Top(5) 5G Smartphone Brands in India")
ax4.set_ylabel('')  # Remove the default ylabel
st.pyplot(fig4)

# -----------------------------------------------
# 5. Most Preferred Back Camera Configuration
# -----------------------------------------------
st.header("Most Preferred Back Camera Configuration")
fig5, ax5 = plt.subplots(figsize=(12, 5))
df['Back Camera (MP)'].value_counts().plot(kind='bar', edgecolor='black', 
                                             color='teal', ax=ax5)
ax5.set_title("Most Preferred Back Camera Configuration")
ax5.set_xlabel('Back Camera MP')
ax5.set_ylabel('Number of Smartphones')
st.pyplot(fig5)
bins = [2400, 3500, 4500, 5500, 6650]
labels = ["Low (2400-3499 mAh)", "Moderate (3500-4499 mAh)", 
          "High (4500-5499 mAh)", "Very High (5500-6650 mAh)"]

df["Battery (mAh) Categories"] = pd.cut(df["Battery (mAh)"], bins=bins, labels=labels, include_lowest=True)

# -----------------------------------------------
# 6. Battery Capacity Distribution
# -----------------------------------------------
st.header("Battery Capacity Distribution")
fig6, ax6 = plt.subplots(figsize=(12, 5))
sns.countplot(x=df["Battery (mAh) Categories"], palette="YlGnBu", ax=ax6)
ax6.set_title("Battery Capacity Distribution")
ax6.set_xlabel("Battery Category")
ax6.set_ylabel("Count")
plt.xticks(rotation=30)
st.pyplot(fig6)

# -----------------------------------------------
# 7. Distribution of Clock Speeds in 5G Smartphones
# -----------------------------------------------
st.header("Distribution of Clock Speeds in 5G Smartphones")
fig7, ax7 = plt.subplots(figsize=(12, 5))
df["Clock Speed (Ghz)"].plot(kind="hist", bins=10, color="teal", edgecolor="black", ax=ax7)
ax7.set_title("Distribution of Clock Speeds in 5G Smartphones")
ax7.set_xlabel("Clock Speed (GHz)")
ax7.set_ylabel("Frequency")
st.pyplot(fig7)




