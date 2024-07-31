import matplotlib.pyplot as m
import pandas as pd

data = pd.read_csv("C:\\Users\\Lenovo\\Desktop\\mtcars.csv")
mpg=data['mpg']
m.hist(mpg,bins='auto',color='k')
m.xlabel('Miles per gallon (mpg)');m.ylabel('Frequency')
m.title('Frequency Distribution of mpg')
m.show()

import pandas as p
import matplotlib.pyplot as m

data = pd.read_csv("C:\\Users\\Lenovo\\Desktop\\mtcars.csv")

wt = data['wt']
iv=range(len(data))
m.scatter(iv,mpg,color='k')
m.scatter(iv,wt,color='g',label='wt')
m.title("Relationship b/w weight and MPG")
m.legend()
m.show()

import pandas as p
import matplotlib.pyplot as m
data = pd.read_csv("C:\\Users\\Lenovo\\Desktop\\mtcars.csv")
c=data['am'].value_counts()
co=['k','g']
m.bar(c.index,c.values,color=co,width=0.2)
m.xticks([0,1],['0-Automatic','1-Manual'])
m.xlabel("Tranmisson Type");m.ylabel("No of Cars")
m.title("Frequency distribution of transmission type of cars")
m.show()

import pandas as p
import matplotlib.pyplot as m
import seaborn as s
data = pd.read_csv("C:\\Users\\Lenovo\\Desktop\\mtcars.csv")
s.boxplot(mpg,color='c')
m.xlabel("MPG");m.ylabel("Values")
m.title("BOX plot of MPG Vlues")