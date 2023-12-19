#script to create a periodic table of elements

#import libraries
import pandas as pd
import matplotlib.pyplot as plt


#read in data
df = pd.read_csv('Periodic Table of Elements.csv')

#set up figure
fig, ax = plt.subplots(figsize=(10,10))

#plot data
ax.scatter(df['AtomicNumber'], df['AtomicMass'], s=100, c='red')

#set axis labels
ax.set_xlabel('AtomicNumber')
ax.set_ylabel('AtomicMass')

#set title
ax.set_title('Periodic Table of Elements')

#show plot
plt.show()

