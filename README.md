### 📊 Project Description

Understanding customer preferences and restaurant trends is vital for making informed business decisions in the food industry.
This project performs an in-depth analysis of Zomato’s restaurant dataset using Python to uncover meaningful insights and Key Performance Indicators (KPIs) that reflect 
customer behavior, restaurant performance and overall market dynamics. The objective is to explore dining patterns, online ordering behavior and pricing strategies that 
influence restaurant success. By leveraging data analytics, the project aims to provide actionable intelligence for restaurant owners, marketers and data professionals 
to make better data-driven decisions in a competitive food market.

### ⚙️ Setup

We used the following tools and platforms for data analysis and visualization:

  - **Google Cloud Platform (GCP)** — for cloud-based data storage and processing

  - **BigQuery Notebooks** — to query and manage large datasets efficiently

  - **Python** — for overall data analysis, transformation, and visualization

  - **Pandas & Numpy** — for data manipulation and exploratory analysis

  - **Matplotlib & Seaborn** — for creating static data visualizations

  - **Plotly** — for building interactive dashboards and visual insights

### 🪜 Steps Followed

The following steps were performed to complete the Restaurant Marketing Intelligence project:

**1. Dataset Ingestion to GCP**

  - Uploaded the Zomato restaurant dataset to Google Cloud Platform (GCP).
  - Retrieved the file path from Google Cloud Storage to use within BigQuery Notebook for analysis.

**2. Working in BigQuery Notebook**

  - Opened the dataset in BigQuery Notebook.
  - Initialized the notebook environment for data analysis and exploration using Python and related libraries.

**3. Data Analysis Workflow**

  - **Data Processing and Cleaning** — Handled missing values, standardized columns and converted data types.
    
    [🔗 View Code](https://github.com/BhavyaMehndiratta26/Restaurant-Market-Intelligence/blob/68aa687dcc7e735bc2f1da6f5e47cfda98c2ae95/data_processing.py)

  - **KPI Analysis** — This analysis examines 5 critical KPIs across restaurant types to uncover market opportunities and customer behavior patterns:

        1. Average Rating by Restaurant Type - Quality comparison
        2. Online Delivery Adoption Rate - Digital service penetration
        3. Offline Dining Preference Rate - Table booking trends
        4. Average Cost for Two by Restaurant Type - Pricing strategy analysis
        5. Popular Price Range - Customer spending behavior
    [🔗 View Code](https://github.com/BhavyaMehndiratta26/Restaurant-Market-Intelligence/blob/68aa687dcc7e735bc2f1da6f5e47cfda98c2ae95/kpi_analysis.py)

- 📈 **KPI Analysis Summary**

    The KPI analysis provided actionable insights into restaurant performance and customer preferences:

    - **Average Rating by Restaurant Type:** "Other" and Buffet restaurants deliver superior customer satisfaction, while traditional dining establishments have lower average ratings.
    - **Online Delivery Adoption Rate:** A significant opportunity exists—majority of restaurants lack online delivery, creating a gap in the market for those willing to adopt this service.  
    - **Offline Dining Preference Rate:** Table reservation infrastructure is severely underdeveloped, suggesting limited focus on offline dining experience enhancement. 
    - **Average Cost for Two:** Traditional dining dominates with budget-friendly pricing, while specialty restaurants command premium prices.
    - **Popular Price Range:** Majority of customers prefer budget-friendly (≤₹400) options, indicating price sensitivity in the market.

    
- **Visualization** — Created static and interactive charts using Matplotlib, Seaborn, and Plotly to represent insights visually.
    
    [🔗 View Code](https://github.com/BhavyaMehndiratta26/Restaurant-Market-Intelligence/blob/68aa687dcc7e735bc2f1da6f5e47cfda98c2ae95/visualizations.py)

**4. Dashboard Creation**  

A visual dashboard has been uploaded to highlight key performance metrics and interactive summaries of restaurant trends.

  ![image alt](https://github.com/BhavyaMehndiratta26/Restaurant-Market-Intelligence/blob/ec1be1522c0955a2fb081659b36c2a258f9d7e0c/zomato_kpi_analysis.png)

### 💡 Key Business Insights
   
  - **Market Opportunity:** Around **60% of restaurants lack online delivery** — adopting digital ordering could provide a strong competitive advantage.  
  - **Service Gap:** Only **5% of restaurants offer table bookings**; enhancing reservation infrastructure can improve overall customer experience.  
  - **Price-Conscious Market:** Approximately **57% of customers prefer budget dining options**, indicating that premium segments have a smaller market share.  
  - **Quality Leaders:** “**Other**” restaurants and buffet-style establishments maintain higher customer ratings — possibly due to value-driven pricing and variety.  
  - **Category Performance:** **Casual dining establishments** are the most common (≈110 restaurants) but tend to lag in customer satisfaction and ratings.

### 🧾 Conclusion: 

This project demonstrates how data analytics can uncover meaningful insights into restaurant performance, customer preferences and market gaps. By leveraging Zomato’s 
restaurant dataset, we identified actionable trends in online adoption, pricing strategies and service offerings. These insights can help restaurants, marketers, and business stakeholders make informed, data-driven decisions to enhance customer satisfaction and competitiveness in the food industry.
