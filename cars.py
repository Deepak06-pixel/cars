#MPG cyliners 
import pandas as pd
da={
"mpg":[18,15,18,16,17],"cylinders":[8,8,6,4,8],"displacement":[307,350,318,304,302],
"horsepower":[130,165,150,150,140],"acceleration":[12.0,11.5,11.0,12.0,10.5],"model year":[70,71,70,80,70],
    "car name":["cheverlot","skylark","plymoth satellite","amc rebel sst","ford torino"]
}
df=pd.DataFrame(da)
sa=df.describe()
el=df[df["cylinders"]==8]
ye = df.groupby('model year')["model year"].count()
print("Statistical details:\n", sa)
print("\ncars with 8 cylinders:\n",el)
print("\n car manufactured in each year:\n",ye)

# MTcars dataset
import pandas as p
import matplotlib.pyplot as m
import seaborn as s

data=p.read_csv("C:\\Users\\Lenovo\\Desktop\\mtcars.csv")

#histogram
mpg=data['mpg']
m.hist(mpg,bins='auto',color='k')
m.xlabel('Miles per gallon (mpg)')
m.ylabel('Frequency')
m.title('frequency distribution of the variable mpg')
m.show()

#sactter plot
wt=data['wt']
iv=range(len(data))
m.scatter(iv,mpg,color = 'k',label='mpg')
m.scatter(iv,wt,color = 'g',label='wt')
m.title("to determine the relation between weight of car and mpg")
m.legend()
m.show()

#bar graph
c=data['am'].value_counts()
co=['k','g']
m.bar(c.index,c.values,color=co,width=0.4)
m.xticks([0,1],["0-Automatic","1-manual"])
m.xlabel("Transmission type")
m.ylabel("No of cars")
m.title("Frequency distribution of transmission of cars")
m.show()

#boxplot
s.boxplot(mpg,color='m')
m.xlabel("MPG")
m.ylabel("Values")
m.title('box plot to interpret the file number summary')
m.show()