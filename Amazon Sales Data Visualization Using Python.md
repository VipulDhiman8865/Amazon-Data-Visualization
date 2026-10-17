# 📊 Amazon Sales Data Visualization Using Python

## 📌 Project Overview

This project analyzes an Amazon sales dataset using Python, Pandas, NumPy, and Matplotlib. It explores customer ratings, regional orders, payment methods, product categories, pricing, quantities sold, revenue contribution, average product ratings, and discounts.

The project uses different types of charts to transform raw sales data into visual insights that help understand customer behavior and product performance.

## 🎯 Project Objectives

- Analyze customer ratings for products.
- Explore orders across different customer regions.
- Understand customer payment method preferences.
- Visualize sales distribution across product categories.
- Analyze product price and quantity distributions.
- Compare revenue contributions by product category.
- Calculate average ratings for each product category.
- Compare average discounted prices across categories.

## 🛠️ Technologies Used

- **Python** — Programming language
- **Pandas** — Data manipulation and analysis
- **NumPy** — Numerical computing
- **Matplotlib** — Data visualization
- **CSV** — Dataset format

## 📈 Graphs and Visualizations

### 1. Customer Rating Distribution

A pie chart showing the distribution of customer ratings.

![Customer Rating Distribution](Rating_Of_Products.png)

### 2. Orders by Customer Region

Shows how orders are distributed across different customer regions.

![Orders by Region](Ordered_by%20each_region.png)

### 3. Payment Method Distribution

Visualizes the distribution of payment methods used by customers.

![Payment Method Distribution](Payment_Method.png)

### 4. Products Sold by Category

A bar chart comparing the number of records across product categories.

![Products Sold by Category](Product_Saled_by_Each_Categories.png)

### 5. Product Price Distribution

A histogram showing the distribution of product prices across 12 bins.

![Price Distribution](Price_Distribution.png)

### 6. Quantity Sold Distribution

A pie chart showing the frequency of different recorded quantities sold.

![Quantity Sold](Quantity_Sold.png)

### 7. Revenue Contribution by Product Category

Shows each product category's percentage contribution to total revenue.

![Revenue Contribution](Revenue_Shared_By_Each_Category.png)

### 8. Average Rating by Product Category

Compares the mean customer rating for each product category.

![Average Rating by Category](Average_Rating_Of_Each_Product.png)

### 9. Average Discounted Price by Product Category

Compares the average value of `discounted_price` across product categories.

![Average Discounted Price](Average_Discount_On_Each_Product.png)

## 📁 Project Structure

```text
Amazon-Data-Visualization/
│
├── amazon_sales_dataset.csv
├── amazon_sales_visualization.py
├── Rating_Of_Products.png
├── Ordered_by each_region.png
├── Payment_Method.png
├── Product_Saled_by_Each_Categories.png
├── Price_Distribution.png
├── Quantity_Sold.png
├── Revenue_Shared_By_Each_Category.png
├── Average_Rating_Of_Each_Product.png
├── Average_Discount_On_Each_Product.png
└── README.md
```

*Note: Ensure the filenames match the actual files in your repository.*

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/VipulDhiman8865/Amazon-Data-Visualization.git
```

### 2. Navigate to the project folder

```bash
cd Amazon-Data-Visualization
```

### 3. Install the required libraries

```bash
pip install pandas numpy matplotlib
```

### 4. Add the dataset

Place `amazon_sales_dataset.csv` in the project directory and update the CSV path in your Python script:

```python
df = pd.read_csv("amazon_sales_dataset.csv")
```

### 5. Run the script

```bash
python amazon_sales_visualization.py
```

The charts will be displayed and saved as PNG files in the project directory.

## 🧹 Data Analysis Techniques

- Frequency analysis using `value_counts()`.
- Category-wise aggregation using `groupby()`.
- Revenue aggregation using `sum()`.
- Average rating and discounted price calculations using `mean()`.
- Data visualization using pie charts, bar charts, and histograms.

## 📚 Key Learnings

- Reading and analyzing CSV datasets using Pandas.
- Exploring categorical and numerical data.
- Calculating category-wise sales and revenue summaries.
- Comparing customer ratings and payment methods.
- Creating and saving multiple visualizations using Matplotlib.
- Presenting data analysis results in a clear visual format.

## 🚀 Future Improvements

- Add sales comparisons across regions and product categories.
- Analyze relationships between discounts, prices, and quantities sold.
- Create an interactive sales dashboard.
- Add summary statistics and key findings.
- Improve chart formatting and labels for easier interpretation.

## 👨‍💻 Author

**Vipul Dhiman**

- GitHub: [VipulDhiman8865](https://github.com/VipulDhiman8865)

## 📄 License

This project is intended for educational and learning purposes.
