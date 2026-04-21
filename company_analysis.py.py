import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("updated_company.csv")

# Take first 50 rows
df50 = df.head(50)

# -------------------------------
# 1. Headquarters (10 companies)
# -------------------------------
hq_10 = df50[['name', 'hq']].drop_duplicates().head(10)

print("Headquarter Names (10 Companies):")
print(hq_10)


# -------------------------------
# 2. Bar Chart (Ratings - 10 companies)
# -------------------------------
rating_10 = df50[['name', 'ratings']].drop_duplicates().head(10)

plt.figure()

plt.bar(rating_10['name'], rating_10['ratings'])

plt.title("Ratings of 10 Companies")
plt.xlabel("Company")
plt.ylabel("Rating")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# -------------------------------
# 3. Funnel Chart (Reviews - 10 companies)
# -------------------------------

# Convert review_count to numeric
df50['review_count'] = df50['review_count'].astype(str).str.replace(',', '')
df50['review_count'] = pd.to_numeric(df50['review_count'], errors='coerce')

review_10 = df50[['name', 'review_count']].drop_duplicates().head(10)

# Sort for funnel effect
review_10 = review_10.sort_values(by='review_count', ascending=False)

plt.figure()

plt.bar(review_10['name'], review_10['review_count'])

plt.title("Funnel Chart (Reviews of 10 Companies)")
plt.xlabel("Company")
plt.ylabel("Review Count")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# -------------------------------
# 4. Line Chart (Employees - 10 companies)
# -------------------------------

emp_10 = df50[['name', 'employees']].drop_duplicates().head(10)

# Using index as numeric representation
plt.figure()

plt.plot(emp_10['name'], range(1, 11), marker='o')

plt.title("Employee Trend (10 Companies)")
plt.xlabel("Company")
plt.ylabel("Employee Index")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# -------------------------------
# 5. Pie Chart (Ratings - 10 companies)
# -------------------------------

plt.figure()

plt.pie(rating_10['ratings'],
        labels=rating_10['name'],
        autopct='%1.1f%%')

plt.title("Ratings Distribution (10 Companies)")

plt.tight_layout()
plt.show()