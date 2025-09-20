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

#Is there a statistically significant relationship between sparing time for yourself and where you stay?
from scipy.stats import kruskal
groups = [g["I_spare_enough_time_for_myself"].values 
          for _, g in df.groupby("Where_do_you_stay")] # Group by accommodation type

stat, p = kruskal(*groups)
print(f"Kruskal-Wallis (Spare time ~ Stay): H={stat:.3f}, p={p:.4f}")






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

#Is there a statistically significant relationship between satisfaction of accomodation and where you stay?
groups2 = [group["I_am_happy_with_my_accommodation"].values 
          for name, group in df.groupby("Where_do_you_stay")] # Group by accommodation type

stat2, p2 = kruskal(*groups2) # Kruskal–Wallis test
print(f"Kruskal-Wallis (Satisfaction of accomodation ~ Accomodation place): H={stat2:.3f}, p={p2:.4f}")




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


#Is there a statistically significant relationship between class attendance and where you stay?
groups3 = [g["I_attend_classes"].values 
          for _, g in df.groupby("Where_do_you_stay")]

stat3, p3 = kruskal(*groups3)
print(f"Kruskal-Wallis (Attendance ~ Stay): H={stat3:.3f}, p={p3:.4f}")



#Social Life Distribution with CGPA
stacked_data = pd.crosstab(
    df["How_much_time_do_you_spend_for_your_social_life_per_day"],
    df["What_is_your_CGPA"],
    normalize="index") #Normalize

stacked_data.plot(
    kind="bar",
    stacked=True,
    figsize=(10,6),
    colormap="tab20"
)
plt.title("Social Life Distribution with CGPA")
plt.xlabel("Social Life per Day")
plt.ylabel("Proportion")
plt.legend(title="CGPA", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

#Is there a statistically significant relationship between social life and CGPA?
groups4 = [g["How_much_time_do_you_spend_for_your_social_life_per_day"].values 
          for _, g in df.groupby("What_is_your_CGPA")]

stat4, p4 = kruskal(*groups4)
print(f"Kruskal-Wallis (Social life ~ CGPA): H={stat4:.3f}, p={p4:.4f}")
