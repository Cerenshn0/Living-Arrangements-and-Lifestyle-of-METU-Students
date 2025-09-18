import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

df = pd.read_excel(r'C:\Users\Ceren\Desktop\STAT365_Project\student_behavior.xlsx')

# Clean column names (remove spaces, ? marks, etc.)
df.columns = (
    df.columns
    .str.strip()
    .str.replace(r'[^\w\s]', '', regex=True)  # remove special chars
    .str.replace(" ", "_")                    # replace spaces with underscore
)

print(df.columns)
print(df.isna().sum())

#Relationship between Sparing Time for Yourself and Where You Stay
plt.figure(figsize=(10,6))
sns.barplot(
    x="Where_do_you_stay",
    y="I_spare_enough_time_for_myself",
    data=df,
    order=df.groupby("Where_do_you_stay")["I_spare_enough_time_for_myself"]
         .mean().sort_values(ascending= False).index,
    color="blue"
)

plt.title("Relationship Between Where You Stay and Sparing Time for Yourself")
plt.xlabel("Where you stay")
plt.ylabel("Sparing Time for Yourself")
plt.show()


# Social Life Distribution
plt.figure(figsize=(8,5))
sns.barplot(
    data=df,
    x="Where do you stay?",
    y="How much time do you spend for your social life per day?",
    color="purple",
    order=["At dorm in campus", "At dorm out of campus", "At home with family", "At home without family"]
)
plt.title("Average Social Life by Stay Location")
plt.xlabel("Stay Location")
plt.ylabel("Average Social Life (hours per day)")
plt.show()

# Accommodation Satisfaction
plt.figure(figsize=(8,5))
sns.countplot(
    data=df,
    x="Where do you stay?",
    hue="I am happy with my accommodation.",
    palette="viridis",
    order=["At dorm in campus", "At dorm out of campus", "At home with family", "At home without family"]
)
plt.title("Accommodation Satisfaction by Stay Location")
plt.xlabel("Stay Location")
plt.ylabel("Count")
plt.legend(title="Satisfaction Level")
plt.show()


# Personal Time (faceted by Stay Location)
g = sns.catplot(
    data=df,
    x="Department",
    kind="count",            # count students per department
    col="Where do you stay?", # facet by stay location
    col_wrap=2,
    color="blue",
    height=4,
    order=sorted(df['Department'].unique()) # optional: order departments alphabetically
)
g.fig.subplots_adjust(top=0.85)
g.fig.suptitle("Number of Students by Department and Stay Location")
plt.show()
