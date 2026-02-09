import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

print("..........WELCOME TO DATA ANALYSIS AND VISUALIZATION SYSTEM.........")
app_data={
   
      "App": [
        "WhatsApp",
        "Instagram",
        "Facebook",
        "Snapchat",
        "Spotify",
        "Google Maps",
        "Amazon Shopping",
        "Flipkart",
        "Netflix",
        "Hotstar"
    ],
    "Category": [
        "Communication",
        "Social1",
        "Social2",
        "Social3",
        "Music",
        "Travel",
        "Shopping",
        "Shopping1",
        "Entertainment",
        "Entertainment1"
    ],
    "Rating": [
        4.1, 4.5, 4.1, 4.3, 4.4, 4.6, 4.2, 4.3, 4.4, 4.2
    ],
    "Reviews": [
        17000000,
        14000000,
        11000000,
        9000000,
        8000000,
        12000000,
        6000000,
        5000000,
        7000000,
        6500000
    ],
    "Size": [
        "28M", "30M", "40M", "35M", "28M",
        "45M", "50M", "42M", "55M", "50M"
    ],
    "Installs": [
        5000000,
        1000000,
        50000000,
        10000000,
        10000000,
        10000000,
        50000000,
        50000000,
        100000000,
        50000000
    ],
    "Type": [
        "Free", "Free", "Free", "Free", "Free",
        "Free", "Free", "Free", "Paid", "Free"
    ],
    "Price": [
        0, 30, 0, 0, 0, 40, 0, 0, 150, 210
    ]
}

data1=pd.DataFrame(app_data)
print(data1)
data1.to_csv('project.csv')

ask=input("DO YOU WANT TO EDIT ANY DATA(YES/NO):")

if ask=="YES" or ask=="yes":
    print(
    "1.App" "\n"
    "2.Category" "\n"
    "3.Rating" "\n"
    "4.Reviews" "\n"
    "5.Size" "\n"
    "6.Installs" "\n"
    "7.Type" "\n"
    "8.Price")
    ask1=input("WHAT YOU WANT TO EDIT CAN YOU TELL ME :" )

    if  ask1 in["App","1","APP","app"] :
        location=int(input("WHICH LOCATION YOU WANT TO CHANGE(0-9) :"))
        print("\n")
        what=input("WHAT YOU GIVE ?,ENTER HERE= ")
        data1.loc[location,"App"]=what
        print(data1)
     

    elif ask1 in["Category","2","CATEGORY","category"] :
        location=int(input("WHICH LOCATION YOU WANT TO CHANGE(0-9) :"))
        print("\n")
        what=input("WHAT YOU GIVE ?,ENTER HERE= ")
        data1.loc[location,"Category"]=what
        print(data1)


    elif ask1 in["Rating","3","RATING","rating"] :
        location=int(input("WHICH LOCATION YOU WANT TO CHANGE(0-9) :"))
        print("\n")
        what=float(input("WHAT YOU GIVE ?,ENTER HERE= "))
        data1.loc[location,"Rating"]=what
        print(data1)


    elif ask1 in["Reviews" ,"4","REVIEWS","reviews"] :
        location=int(input("WHICH LOCATION YOU WANT TO CHANGE(0-9) :"))
        print("\n")
        what=int(input("WHAT YOU GIVE ?,ENTER HERE= "))
        data1.loc[location,"Reviews"]=what
        print(data1)


    elif ask1 in["Size" ,"5","SIZE","size"] :
        location=int(input("WHICH LOCATION YOU WANT TO CHANGE(0-9) :"))
        print("\n")
        what=input("WHAT YOU GIVE ?,ENTER HERE= ")
        data1.loc[location,"Size"]=what
        print(data1)


    elif ask1 in["Installs","6","INSTALLS","installs"] :
        location=int(input("WHICH LOCATION YOU WANT TO CHANGE(0-9) :"))
        print("\n")
        what=int(input("WHAT YOU GIVE ?,ENTER HERE= "))
        data1.loc[location,"Installs"]=what
        print(data1)


    elif ask1 in["Type","7","TYPE","type"] :
        location=int(input("WHICH LOCATION YOU WANT TO CHANGE(0-9) :"))
        print("\n")
        what=input("WHAT YOU GIVE ?,ENTER HERE= ")
        data1.loc[location,"Type"]=what
        print(data1)


    elif ask1 in["Price","8","PRICE","price"] :
        location=int(input("WHICH LOCATION YOU WANT TO CHANGE(0-9) :"))
        print("\n")
        what=int(input("WHAT YOU GIVE ?,ENTER HERE= "))
        data1.loc[location,"Price"]=what
        print(data1)
  


print("DO YOU LIKE TO SEE:" "\n"
    "Number of non-null values""\n"
    "average value" "\n"
    "standard deviation""\n"
    "minimum value""\n"
    "first quartile (25%)""\n"
    "median (50%)""\n"
    "third quartile (75%)""\n"
    "maximum value")
print("\n")
new=input("YES OR NO:")
if new=="yes" or new=="YES":
      print(data1.describe())
else:
      print("")





graph=input("DO YOU LIKE TO PLOT ANY GRAPH (YES/NO): ")
if graph=="yes" or graph=="YES" or graph=="Yes" :
    print(".......WELCOME.......")
    print("1.BAR GRAPH""\n"
          "2.SCATTER PLOT""\n"
          "3.DONATE PIE CHART""\n"
          "4.HISTOGRAM PLOT""\n"
          "5.STEM PLOT""\n"
          "6.PIE CHART""\n")



    choice=input("ENTER WHICH TYPE OF GRAPH YOU WANT TO PLOT:")
    print("\n")

    if choice in ["bar chart","1","Bar chart","BAR CHART"] :
        print("WHAT YOU WANT TO GIVE IN X-AXIS:")

        print("1.APP""\n"
              "2.CATEGORY")
        
        xaxis=input("ENTER YOUR CHOICE: ")
        
        print("WHAT YOU WANT TO GIVE IN THE Y-AXIS:")
        print("1.RATING""\n"
              "2.REVIEWS""\n"
              "3.SIZE""\n"
              "4.INSTALLS""\n"
              "5.PRICE")
        yaxis=input("ENTER YOUR CHOICE: ")

        if xaxis in ["1","app","App","APP"] :
           x_col = "App"
           xaxis="APP"

        elif xaxis in ["2","Category","category","CATEGORY"] :
           x_col = "Category"
           xaxis="CATEGORY"


        if yaxis in ["1","Rating","rating","RATING"] :
           y_col = "Rating"
           yaxis="RARING"

        elif yaxis in ["2","REVIEWS","reviews","Reviews"] :
           y_col = "Reviews"
           yaxis="REVIEWS"

        elif yaxis in ["3","size","Size","SIZE"] :   
           data1["Size"] = data1["Size"].str.replace("M", "").astype(float)
           y_col = "Size"
           yaxis="SIZE"

        elif yaxis in ["4","INSTALLS","installs","Installs"] :
           y_col = "Installs"
           yaxis="INSTALLS"

        elif yaxis in ["5","price","Price","PRICE"] :
           y_col = "Price"
           yaxis="PRICE"




        x = data1[x_col].tolist()
        y = data1[y_col].tolist()
        plt.xlabel(xaxis,fontsize=15)
        plt.ylabel(yaxis,fontsize=15)
        plt.title("DATA 📊 ",fontsize=15)

        color1=input("DO YOU LIKE DIFFERENT COLOR IN GRAPH FOR UNDERSTANDING (YES/NO): ")

        if color1=="yes" or color1=="YES" or color1=="Yes":
            colors1=["red","blue","green","pink","orange","cyan","purple","yellow","brown","maroon"]
        else:
            colors1="blue"
        
        plt.bar(x,y,color=colors1,edgecolor="black",label="data")
        plt.legend()
        plt.show()




    elif choice=="scatter plot" or choice=="2" or choice=="Scatter plot" or choice=="SCATTER PLOT":
        print("WHAT YOU WANT TO GIVE IN X-AXIS:")
        print("1.APP""\n"
              "2.CATEGORY")
        xaxis=input("ENTER YOUR CHOICE: ")

        print("WHAT YOU WANT TO GIVE IN THE Y-AXIS:")
        print("1.RATING""\n"
              "2.REVIEWS""\n"
              "3.SIZE""\n"
              "4.INSTALLS""\n"
              "5.PRICE")
        
        yaxis=input("ENTER YOUR CHOICE: ")

        if xaxis in ["1","app","App","APP"] :
           x_col = "App"
           xaxis="APP"

        elif xaxis in ["2","Category","category","CATEGORY"] :
           x_col = "Category"
           xaxis="CATEGORY"


        if yaxis in ["1","Rating","rating","RATING"] :
           y_col = "Rating"
           yaxis="RARING"

        elif yaxis in ["2","REVIEWS","reviews","Reviews"] :
           y_col = "Reviews"
           yaxis="REVIEWS"

        elif yaxis in ["3","size","Size","SIZE"]:   
           data1["Size"] = data1["Size"].str.replace("M", "").astype(float)
           y_col = "Size"
           yaxis="SIZE"

        elif yaxis in ["4","INSTALLS","installs","Installs"] :
           y_col = "Installs"
           yaxis="INSTALLS"


        elif yaxis in ["5","price","Price","PRICE"] :
           y_col = "Price"
           yaxis="PRICE"




        x = data1[x_col].tolist()
        y = data1[y_col].tolist()
        plt.xlabel(xaxis,fontsize=15)
        plt.ylabel(yaxis,fontsize=15)
        plt.title("DATA",fontsize=15)
        size=[100,50,80,70,60,75,80,50,65,85]

        color1=input("DO YOU LIKE DIFFRENT COLOR IN GRAPH FOR UNDERSTANDING (YES/NO): ")
        if color1=="yes" or color1=="YES" or color1=="Yes":
            colors1=["red","blue","green","pink","orange","cyan","purple","yellow","brown","maroon"]
        else:
            colors1="blue"
        
        plt.scatter(x,y,color=colors1,edgecolor="black",s=size,label="data")
        t=plt.colorbar()
        t.set_label("COLOR BAR")
        plt.legend()
        plt.show()
    




    elif choice in ["DONATE PIE CHART","3","donate pie chart","Donate pie chart"] :
        
        print("WHAT YOU WANT TO GIVE IN X-AXIS:")
        print("1.APP""\n"
              "2.CATEGORY")
        xaxis=input("ENTER YOUR CHOICE: ")

        print("WHAT YOU WANT TO GIVE IN THE Y-AXIS:")
        print("1.RATING""\n"
              "2.REVIEWS""\n"
              "3.SIZE""\n"
              "4.INSTALLS""\n"
              "5.PRICE")
        yaxis=input("ENTER YOUR CHOICE: ")

        
        if xaxis in ["1","app","App","APP"] :
           x_col = "App"
           xaxis="APP"

        elif xaxis in ["2","Category","category","CATEGORY"] :
           x_col = "Category"
           xaxis="CATEGORY"


        if yaxis in ["1","Rating","rating","RATING"] :
           y_col = "Rating"
           yaxis="RARING"

        elif yaxis in ["2","REVIEWS","reviews","Reviews"] :
           y_col = "Reviews"
           yaxis="REVIEWS"

        elif yaxis in ["3","size","Size","SIZE"]:   
           data1["Size"] = data1["Size"].str.replace("M", "").astype(float)
           y_col = "Size"
           yaxis="SIZE"

        elif yaxis in ["4","INSTALLS","installs","Installs"] :
           y_col = "Installs"
           yaxis="INSTALLS"

        elif yaxis in ["5","price","Price","PRICE"] :
           y_col = "Price"
           yaxis="PRICE"




        x = data1[x_col].tolist()
        y = data1[y_col].tolist()
        plt.title("DATA",fontsize=15)

        color1=input("DO YOU LIKE DIFFRENT COLOR IN GRAPH FOR UNDERSTANDING (YES/NO): ")
        if color1=="yes" or color1=="YES" or color1=="Yes":
            colors1=["red","blue","green","pink","orange","cyan","purple","yellow","brown","maroon"]
        else:
            colors1="blue"
        
        plt.pie(y,labels=x,colors=colors1,radius=1.5)
        plt.pie([1],colors="w")

        plt.show()
    




    elif choice in ["HISTOGRAM PLOT","4","histogram plot","Histogram plot"] :
        print("WHAT YOU WANT TO GIVE IN X-AXIS:")
        print("1.APP""\n"
              "2.CATEGORY")
        xaxis=input("ENTER YOUR CHOICE: ")

        print("WHAT YOU WANT TO GIVE IN THE Y-AXIS:")
        print("1.RATING""\n"
              "2.REVIEWS""\n"
              "3.SIZE""\n"
              "4.INSTALLS""\n"
              "5.PRICE")
        yaxis=input("ENTER YOUR CHOICE: ")

        
        if xaxis in ["1","app","App","APP"] :
           x_col = "App"
           xaxis="APP"

        elif xaxis in ["2","Category","category","CATEGORY"] :
           x_col = "Category"
           xaxis="CATEGORY"


        if yaxis in ["1","Rating","rating","RATING"] :
           y_col = "Rating"
           yaxis="RARING"

        elif yaxis in ["2","REVIEWS","reviews","Reviews"] :
           y_col = "Reviews"
           yaxis="REVIEWS"

        elif yaxis in ["3","size","Size","SIZE"]:   
           data1["Size"] = data1["Size"].str.replace("M", "").astype(float)
           y_col = "Size"
           yaxis="SIZE"

        elif yaxis in ["4","INSTALLS","installs","Installs"] :
           y_col = "Installs"
           yaxis="INSTALLS"

        elif yaxis in ["5","price","Price","PRICE"] :
           y_col = "Price"
           yaxis="PRICE"


        x = data1[x_col].tolist()
        y = data1[y_col].tolist()
        plt.xlabel(xaxis,fontsize=15)
        plt.ylabel(yaxis,fontsize=15)
        plt.title("DATA",fontsize=15)
        
        plt.hist(y,color="skyblue",edgecolor="black",label="data")
        plt.legend()
        plt.show()





    elif choice in ["STEM PLOT","5","stem plot","Stem plot"]:
        print("WHAT YOU WANT TO GIVE IN X-AXIS:")
        print("1.APP""\n"
              "2.CATEGORY")
        xaxis=input("ENTER YOUR CHOICE: ")

        print("WHAT YOU WANT TO GIVE IN THE Y-AXIS:")
        print("1.RATING""\n"
              "2.REVIEWS""\n"
              "3.SIZE""\n"
              "4.INSTALLS""\n"
              "5.PRICE")
        yaxis=input("ENTER YOUR CHOICE: ")

        
        if xaxis in ["1","app","App","APP"] :
           x_col = "App"
           xaxis="APP"

        elif xaxis in ["2","Category","category","CATEGORY"] :
           x_col = "Category"
           xaxis="CATEGORY"


        if yaxis in ["1","Rating","rating","RATING"] :
           y_col = "Rating"
           yaxis="RARING"

        elif yaxis in ["2","REVIEWS","reviews","Reviews"] :
           y_col = "Reviews"
           yaxis="REVIEWS"

        elif yaxis in ["3","size","Size","SIZE"]:   
           data1["Size"] = data1["Size"].str.replace("M", "").astype(float)
           y_col = "Size"
           yaxis="SIZE"

        elif yaxis in ["4","INSTALLS","installs","Installs"] :
           y_col = "Installs"
           yaxis="INSTALLS"


        elif yaxis in ["5","price","Price","PRICE"] :
           y_col = "Price"
           yaxis="PRICE"


        x = data1[x_col].tolist()
        y = data1[y_col].tolist()
        plt.xlabel(xaxis,fontsize=15)
        plt.ylabel(yaxis,fontsize=15)
        plt.title("DATA",fontsize=15)
        
        plt.stem(x,y,markerfmt="ro",linefmt=":")
        plt.show()





    elif choice in ["PIE CHART","6","pie chart","Pie chart"]:
        print("WHAT YOU WANT TO GIVE IN X-AXIS:")
        print("1.APP""\n"
              "2.CATEGORY")
        xaxis=input("ENTER YOUR CHOICE: ")

        print("WHAT YOU WANT TO GIVE IN THE Y-AXIS:")
        print("1.RATING""\n"
              "2.REVIEWS""\n"
              "3.SIZE""\n"
              "4.INSTALLS""\n"
              "5.PRICE")
        yaxis=input("ENTER YOUR CHOICE: ")

        
        if xaxis in ["1","app","App","APP"] :
           x_col = "App"
           xaxis="APP"

        elif xaxis in ["2","Category","category","CATEGORY"] :
           x_col = "Category"
           xaxis="CATEGORY"


        if yaxis in ["1","Rating","rating","RATING"] :
           y_col = "Rating"
           yaxis="RARING"

        elif yaxis in ["2","REVIEWS","reviews","Reviews"] :
           y_col = "Reviews"
           yaxis="REVIEWS"

        elif yaxis in ["3","size","Size","SIZE"]:   
           data1["Size"] = data1["Size"].str.replace("M", "").astype(float)
           y_col = "Size"
           yaxis="SIZE"

        elif yaxis in ["4","INSTALLS","installs","Installs"] :
           y_col = "Installs"
           yaxis="INSTALLS"

        elif yaxis in ["5","price","Price","PRICE"] :
           y_col = "Price"
           yaxis="PRICE"

        

        
        separate=input("DO YOU LIKE TO SEE ANY DATA SEPARATELY (YES/NO): ")
        if separate in ["yes","YES","Yes"] :
           print("1.APP""\n"
                 "2.CATEGORY")
           

           sep1=input("ENTER THE NAME:")
           if sep1=="1" or sep1=="APP" or sep1=="App" or sep1=="app":
              
              print("1.WhatsApp""\n"
                    "2.Instagram""\n"
                    "3.Facebook""\n"
                    "4.Snapchat""\n"
                    "5.Spotify""\n"
                    "6.Google Maps""\n"
                    "7.Amazon Shopping""\n"
                    "8.Flipkart""\n"
                    "9.Netflix""\n"
                    "10.Hotstar")
              d=input("WHICH DATA YOU WANT TO SEE SEPARATELY ENTER HERE:")
              c=0

              if d=="whatsapp" or d=="WhatsApp" or d=="1":
                 c=[0.4,0,0,0,0,0,0,0,0,0]
              elif d=="instagram" or d=="Instagram"or d=="2":
                 c=[0,0.4,0,0,0,0,0,0,0,0]
              elif d=="facebook" or d=="Facebook" or d=="3":
                 c=[0,0,0.4,0,0,0,0,0,0,0]
              elif d=="snapchat" or d=="Snapchat" or d=="4":
                 c=[0,0,0,0.4,0,0,0,0,0,0]
              elif d=="spotify" or d=="Spotify" or d=="5":
                 c=[0,0,0,0,0.4,0,0,0,0,0]
              elif d=="google maps" or d=="Google Maps" or d=="6":
                 c=[0,0,0,0,0,0.4,0,0,0,0]
              elif d=="Amazon Shopping" or d=="amazon shopping" or d=="7":
                 c=[0,0,0,0,0,0,0.4,0,0,0]
              elif d=="flipkart" or d=="Flipkart" or d=="8":
                 c=[0,0,0,0,0,0,0,0.4,0,0]
              elif d=="netflit" or d=="Netflix" or d=="9":
                 c=[0,0,0,0,0,0,0,0,0.4,0]
              elif d=="hotstar" or d=="Hotstar" or d=="10":
                 c=[0,0,0,0,0,0,0,0,0,0.4]


           elif sep1=="2" or sep1=="category" or sep1=="Category" or sep1=="CATEGORY":
              print("1.Communication",
                    "2.Social1""\n"
                    "3.Social2""\n"
                    "4.Social3""\n"
                    "5.Music""\n"
                    "6.Travel""\n"
                    "7.Shopping""\n"
                    "8.Shopping1""\n"
                    "9.Entertainment""\n"
                    "10.Entertainment1")
              d=input("WHICH DATA YOU WANT TO SEE SEPARATELY ENTER HERE:")
              
              if d=="Communication" or d=="communication" or d=="1":
                 c=[0.4,0,0,0,0,0,0,0,0,0]
              elif d=="Social1" or d=="social1" or d=="2":
                c=[0,0.4,0,0,0,0,0,0,0,0]
              elif d=="Social2" or d=="social2" or d=="3":
                 c=[0,0,0.4,0,0,0,0,0,0,0]
              elif d=="Social3" or d=="social3" or d=="4":
                 c=[0,0,0,0.4,0,0,0,0,0,0]
              elif d=="Music" or d=="music" or d=="5":
                 c=[0,0,0,0,0.4,0,0,0,0,0]
              elif d=="Travel" or d=="travel" or d=="6":
                 c=[0,0,0,0,0,0.4,0,0,0,0]
              elif d=="Shopping" or d=="shopping" or d=="7":
                 c=[0,0,0,0,0,0,0.4,0,0,0]
              elif d=="Shopping1" or d=="shopping1" or d=="8":
                 c=[0,0,0,0,0,0,0,0.4,0,0]
              elif d=="Entertainment" or d=="entertainment" or d=="9":
                 c=[0,0,0,0,0,0,0,0,0.4,0]
              elif d=="Entertainment1" or d=="entertainment1" or d=="10":
                 c=[0,0,0,0,0,0,0,0,0,0.4]
        else:
           c=[0,0,0,0,0,0,0,0,0,0]
        ex=c
        x = data1[x_col].tolist()
        y = data1[y_col].tolist()
        plt.title("DATA",fontsize=15)
        
        color1=input("DO YOU LIKE DIFFRENT COLOR IN GRAPH FOR UNDERSTANDING (YES/NO): ")
        if color1=="yes" or color1=="YES" or color1=="Yes":
            colors1=["red","blue","green","pink","orange","cyan","purple","yellow","brown","maroon"]
        else:
            colors1="blue"
        
        plt.pie(y,labels=x,colors=colors1,labeldistance=1.5,explode=ex,textprops={"fontsize":10})
        
        plt.show()