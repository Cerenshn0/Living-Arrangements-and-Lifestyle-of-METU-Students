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


#Satisfaction of Accomodation by Where You Stay
plt.figure(figsize=(8,5))
sns.countplot(x="Where_do_you_stay", 
              hue="I_am_happy_with_my_accommodation",
              data=df, 
              order=df["Where_do_you_stay"].value_counts().index)
plt.title("Satisfaction of Accomodation by Where You Stay")
plt.xlabel("Where do you stay?")
plt.ylabel("Count")
plt.show()



#Attendance Distribution by Stay Location
plt.figure(figsize=(8,5))
sns.boxplot(
    x="Where_do_you_stay",
    y="I_attend_classes",
    data=df,
    palette="Set2" )
plt.title("Attendance Distribution by Stay Location")
plt.xlabel("Where do you stay?")
plt.ylabel("Attendance (1–5)")
plt.show()

print(df.loc[df["Where_do_you_stay"]=="At home with family","I_attend_classes"].value_counts())






#
grades = df["What_grade_are_you_in"].unique()
fig, axes = plt.subplots(2, 3, figsize=(15,10), sharex=True)

for ax, grade in zip(axes.flat, grades):
    sns.barplot(
        data=df[df["What_grade_are_you_in"]==grade],
        x="What_is_your_CGPA",
        y="How_much_time_do_you_spend_for_your_social_life_per_day",
        estimator=lambda x: x.mean(),
        palette="coolwarm",
        orient="h",
        ax=ax
    )
    ax.set_title(f"Grade {grade}")
    ax.set_xlabel("Average CGPA")                     # x label
    ax.set_ylabel("Social Life per Day") 

plt.tight_layout()
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
