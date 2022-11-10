# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 17:31:05 2022

@author: user
"""

#importing pandas and matplotlib library files
import pandas as pd
import matplotlib.pyplot as plt

#Reading the dataset 'performance-data.csv' file
data = pd.read_csv("C:\\Users\\user\\Desktop\\Visualisation asgmnt\\performance-data.csv")
#Choosing the first 10 rows for ploting the graphs
data = data[:10]


def line():  
    """This function plots a line graph of user satisfaction in various weeks"""
    
    plt.figure(figsize=(15,10))
    plt.plot(data['Week commencing'], data['Dissatisfied'], label="Dissatisfied")
    plt.plot(data['Week commencing'], data['Satisfied'], label="Satisfied")
    plt.plot(data['Week commencing'], data['Neither satisfied or dissatisfied'], label="Neither satisfied / dissatisfied")
    
    plt.xticks(rotation = 70)
    plt.title("Prison service data")
    plt.xlabel("Weeks")
    plt.ylabel("User satisfaction")
    plt.legend(fontsize = 14)
    plt.savefig("lineplot.png")
    plt.show()
line()

def bargraph():    
    """This function plots a bar graph about dissatisfied users in various weeks"""
    
    plt.figure()
    plt.bar(data["Week commencing"], data["Dissatisfied"])
    plt.xticks(rotation = 50)
    plt.xlabel("Week commencing")
    plt.ylabel("Dissatisfied")
    plt.title("Prison service data")
    #plt.legend()
    plt.savefig("bargraph.png", bbox_inches = "tight")
    plt.show()   
bargraph()


def pie():
    """This function plots a pie chart about satisfied users in different weeks"""
#Choosing the first 4 rows for ploting the graphs    
    data_pie = data[:4]
    plt.figure()
    plt.pie(data_pie["Satisfied"],labels=data_pie["Week commencing"],autopct='%1.1f%%',startangle=140)
    plt.title("Prison service data")
    plt.legend(bbox_to_anchor = (2,1))
    plt.savefig("piechart.png")
    plt.show()
pie()