import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_csv("C:/Users/Nishu/Desktop/matplotlib/amazon_sales_dataset.csv")


rating_counts=df["rating"].value_counts()
plt.figure(figsize=(8,6))
plt.pie(rating_counts,labels=rating_counts.index,autopct='%1.1f%%',startangle=90)
plt.tight_layout()
plt.title("Rating_given_by_Customer")
plt.savefig("Rating_Of_Products.png")
plt.show()

region=df["customer_region"].value_counts()
plt.figure(figsize=(8,6))
plt.pie(region,labels=region.index,autopct='%1.1f%%',startangle=90)
plt.tight_layout()
plt.title("Ordered by each region")
plt.savefig("Ordered_by each_region.png")
plt.show()


payment_way=df["payment_method"].value_counts()
plt.figure(figsize=(8,6))
plt.pie(payment_way,labels=payment_way.index,autopct='%1.1f%%',startangle=90)
plt.title("Payment Method")
plt.tight_layout()
plt.savefig("Payment_Method.png")
plt.show()

product_cate=df["product_category"].value_counts()
plt.figure(figsize=(8,6))
plt.bar(product_cate.index,product_cate.values)
plt.tight_layout()
plt.title("Product Saled")
plt.xlabel("Categories")
plt.ylabel("Counts")
plt.savefig("Product_Saled_by_Each_Categories.png")
plt.show()


plt.figure(figsize=(8,6))
plt.hist(df["price"],bins=12)
plt.tight_layout()
plt.title("Price Distribution")
plt.xlabel("Price Variation")
plt.ylabel("Counts")
plt.savefig("Price_Distribution.png")
plt.show()


quantity_pro=df["quantity_sold"].value_counts()
plt.figure(figsize=(8,6))
plt.pie(quantity_pro,labels=quantity_pro.index,autopct='%1.1f%%',startangle=90)
plt.tight_layout()
plt.title("Quantity Sold")
plt.savefig("Quantity_Sold.png")
plt.show()


#SHARING PERCENTAGE OF TOTAL REVENUE BY EACH PRODUCT CATEGORY 

revenue_sharing=df.groupby('product_category')['total_revenue'].sum()
plt.figure(figsize=(8,6))
plt.pie(revenue_sharing,labels=revenue_sharing.index,autopct='%1.1f%%',startangle=90)
plt.tight_layout()
plt.title("Revenue Shared by Each Category")
plt.savefig("Revenue_Shared_By_Each_Category.png")
plt.show()



#AVERAGE RATING OF EACH CATEGORY

avg_rating=df.groupby('product_category')['rating'].mean()
plt.figure(figsize=(8,6))
plt.bar(avg_rating.index,avg_rating.values)
plt.xlabel('Categories')
plt.ylabel('Average Rating')
plt.savefig('Average_Rating_Of_Each_Product.png')
plt.tight_layout()
plt.show()

#AVERAGE DISCOUNT ON EACH CATEGORY

avg_discount=df.groupby('product_category')['discounted_price'].mean()
plt.figure(figsize=(8,6))
plt.bar(avg_discount.index,avg_discount.values)
plt.xlabel('Categories')
plt.ylabel('Average Discount')
plt.savefig('Average_Discount_On_Each_Product.png')
plt.tight_layout()
plt.show()