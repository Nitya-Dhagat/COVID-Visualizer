
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def menu():

    print()
    print("*"*20)
    print("COVID 19 in INDIA Project")
    print("*"*20)
    print()
    print("        0. KNOW ABOUT THE PROJECT")
    print("Working with Covid 19 in India file.")
    print("        1. Reading file Covid 19 in India")
    print("        2. Reading file Covid 19 in India without Index")
    print("        3. Assign new Colummns names")
    print("        3. Assign new Colummns names")
    print("Data Manipulation.")
    print("        4. Define specific colummns")
    print("        5. Read 6 records from file - Covid 19 in INDIA")
    print("        6. Read 3 records from top and 2 from the bottom")
    print("        7. Arrange them in ascending order by State/Union Territory")
    print("        8. Maximum number of deaths")
    print("        9. Minimum number of deaths")
    print("Data visualisation")
    print("        10. Line plot")
    print("        11. Bar plot")
    print("        12. Pie plot")
    print("        13. Barh plot")
    print()
    print()
    print('*'*20)

menu()

def about():
    print('In this project we have talk about a easier and simplier way of data analysis.It is though not so hard to code this althought it can efficiently help you visualise the big chunks of data.')

def csv():
    print("Reading file Covid 19 in INDIA")
    print()
    print()
    df = pd.read_csv(r'C:\Users\NityaDhagat\OneDrive\Documents\desktopitems\vscode\python\covid\Book1.csv')
    print(df)

def no_index():
    df = pd.read_csv(r'C:\Users\NityaDhagat\OneDrive\Documents\desktopitems\vscode\python\covid\Book1.csv',index_col=0)
    print()
    print()
    print(df)

def new_colummns():
    df = pd.read_csv(r'C:\Users\NityaDhagat\OneDrive\Documents\desktopitems\vscode\python\covid\Book1.csv',skiprows=1)
    print(df)

def spec_col():
    df = pd.read_csv(r'C:\Users\NityaDhagat\OneDrive\Desktop\New folder\covidC:\Users\NityaDhagat\OneDrive\Documents\desktopitems\vscode\python\covid\Book1.csv',usecols=['States','Total','Negative','Positive'])
    print(df)

def read_rows():
    df = pd.read_csv(r'C:\Users\NityaDhagat\OneDrive\Documents\desktopitems\vscode\python\covid\Book1.csv',nrows=6)
    print('Showing 6 records')
    print(df)

def top_bottom():
    df = pd.read_csv(r'C:\Users\NityaDhagat\OneDrive\Documents\desktopitems\vscode\python\covid\Book1.csv')
    print('Print top 3 rows')
    print(df.head(3))
    print()
    print()
    print('Print bottom 2 rows')
    print(df.tail(2))

def sort_states():
    print('Sorting members name in ascending order')
    df = pd.read_csv(r'C:\Users\NityaDhagat\OneDrive\Documents\desktopitems\vscode\python\covid\Book1.csv',index_col=0)
    df = df.sort_values('States/Union Territory')
    print(df)

def maxmaths():
    df = pd.read_csv(r'C:\Users\NityaDhagat\OneDrive\Documents\desktopitems\vscode\python\covid\Book1.csv')
    print(df)
    print('Highest Deaths')
    print(df.Deaths.max())


def minmaths():
    df = pd.read_csv(r'C:\Users\NityaDhagat\OneDrive\Documents\desktopitems\vscode\python\covid\Book1.csv')
    print(df)
    print('Lowest Deaths')
    print(df.Deaths.mmin())

def line_plot():
    print('Line plot')
    df = pd.read_csv(r'C:\Users\NityaDhagat\OneDrive\Documents\desktopitems\vscode\python\covid\Book1.csv')
    print(df)
    plt.title("Covid 19 records")
    df.plot()


def bar_plot():
    print('Bar plot')
    df = pd.read_csv(r'C:\Users\NityaDhagat\OneDrive\Documents\desktopitems\vscode\python\covid\Book1.csv')
    print(df)
    x=df['Cured']
    y = df['Deaths']
    plt.title('Cured and Death DAta in INDIA')
    plt.xlabel("Deaths")
    plt.ylabel("Cured")
    plt.bar(x,y,color='red')
    plt.show()

def pie_plot():
    print('Pie plot')
    df = pd.read_csv(r'C:\Users\NityaDhagat\OneDrive\Documents\desktopitems\vscode\python\covid\Book1.csv')
    print(df)
    plt.title('Cases in a State or Union Territory')
    z=eval(input('Enter values of states in square brackets   '))
    color = ['white','orange','purple']
    items = ['Cured','Deaths','Confirmed']
    expl = [0,0,0.2]
    plt.pie(z,colors=color,labels=items,explode=expl,autopct="%5.1f%%")
    plt.show()


def barh():
    print('Bar plot')
    df = pd.read_csv(r'C:\Users\NityaDhagat\OneDrive\Documents\desktopitems\vscode\python\covid\Book1.csv')
    print(df)
    x = df['Cured']
    y = df['States/Union Territories']
    plt.title('Cured in various States and UT')
    plt.xlabel('Deaths')
    plt.ylabel('Cured')
    plt.barh(x,y,color='yellowgreen')
    plt.show()

def statewisesample():
    print('Reading statewise sample report')
    print()
    df = pd.read_csv(r'C:\Users\NityaDhagat\OneDrive\Documents\desktopitems\vscode\python\covid\Book2.csv')
    print(df)

def totalnegative():
    print('Total negative cases')
    print()
    df = pd.read_csv(r'C:\Users\NityaDhagat\OneDrive\Documents\desktopitems\vscode\python\covid\Book2.csv')
    print(df['Negative'].count())
    
def pie_plot1():
    print("Pie Plot")
    df = pd.read_csv(r'C:\Users\NityaDhagat\OneDrive\Documents\desktopitems\vscode\python\covid\Book2.csv')
    print(df)
    plt.title("POsitive and Negative Cases or Union Territory")
    z = eval(input('eneter the values of a state in square bracket :- '))
    color=['blue','yellow','purple']
    items=['TotalSamples','Negative','Positive']
    expl=[0,0,0.4]
    plt.pie(z,colors=color,labels=items,explode=expl,autopct="XS.1fXX")
    plt.show()



opt=''
opt=int(input('Enter your choice :- '))
if opt==0:
    about()
elif opt==1:
    csv()
elif opt==2:
    no_index()
elif opt==3:
    new_colummns()
elif opt==4:
    spec_col()
elif opt==5:
    read_rows()
elif opt==6:
    top_bottom()
elif opt==7:
    sort_states()
elif opt==8:
    maxmaths()
elif opt==9:
    minmaths()
elif opt==10:
    line_plot()
elif opt==11:
    bar_plot()
elif opt==12:
    pie_plot()
elif opt==13:
    barh()
elif opt==14:
    statewisesample()
elif opt==15:
    totalnegative()
elif opt==16:
    pie_plot1()
else:
    print("invalid option")
    print("/a")


