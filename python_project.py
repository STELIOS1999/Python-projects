#Script to plot the bottles sold for each zip code and item description
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df=pd.read_csv('python_project_csv.csv')

#Group by zip code and item description and aggregating the bottles sold
zip_group=df.groupby(['zip_code','item_description'])
bottles_sold=zip_group.agg({'bottles_sold': 'sum'})

#creating a list for iteration and plotting
columns_group=list(zip_group)
columns_value=list(bottles_sold)

length=len(columns_group)

for i in range(length):
    plt.scatter(columns_group[i][0][0],list(bottles_sold['bottles_sold'])[i])

plt.show()
plt.xlabel('Zip Code')
plt.ylabel('Bottles Sold')
plt.title('Bottles Sold')