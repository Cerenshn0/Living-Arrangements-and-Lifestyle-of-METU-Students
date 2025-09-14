import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

df = pd.read_excel(r'C:\Users\Ceren\Desktop\STAT365_Project\student_behavior.xlsx')

contingency_table = pd.crosstab(
    [df["Where do you stay?"], df["What is your CGPA?"]],
    df["I attend classes?"])

chi2, p_value, dof, expected = chi2_contingency(contingency_table)
print("Chi-square:", chi2)
print("Degrees of freedom:", dof)
print("p-value:", p_value)



df["Group"] = np.where(
    df["Where do you stay?"].isin(["At home with family", "At home without family"]),
    "home","dorm")

homee = df[df["Group"] == "home"].copy()
dormm = df[df["Group"] == "dorm"].copy()


#Visualizations

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
