# Web--Scraping
#This is a beginner level project which gives an introduction about Web-scraping .
import requests
import html5lib
import bs4
import sys
from tkinter import *
import requests
from bs4 import BeautifulSoup
import pandas as pd
from pymongo import MongoClient
from csv import writer
import os


win = Tk()
# win.configure("Tool") #only for its title 
win.geometry('500x260')
win.minsize(495,260)
win.maxsize(495,260)
win.title("Web Scrapper") #only for its title


def scrappin():
    url = requests.get(str(URL.get()))
    
    res = bs4.BeautifulSoup(url.text,"html.parser")
    # now you want 2 files one for text content of the web and secondly the code of the web
    saveFile1 = open("Web_Text.txt","a") # with a append mode
    for i in res.select('p'):
        saveFile1.write(i.getText())
    saveFile1.close() # most impact never forget to close your file after opening

    saveFile2 = open("Web_Code.txt","a") # with a append mode
    for i in res.select('p'):
        saveFile2.write(res.prettify())
    saveFile2.close()

    #TODO: pasting code from another file 
    soup = BeautifulSoup(url.text, 'html.parser')

    table = soup.find('tbody')
    print(table)

    A = []
    B = []
    C = []
    D = []
    E = []
    F = []

    for row in table.findAll('tr'):
        cells = row.findAll('td')
        A.append(cells[0].text)
        B.append(cells[1].text)
        C.append(cells[2].text)
        D.append(cells[3].text)
        E.append(cells[4].text)
        F.append(cells[5].text)
    df = pd.DataFrame(A, columns=['Country'])
    df['Gold'] = B
    df['Silver'] = C
    df['Bronze'] = D
    df['Total Medals'] = E
    df['2021 Population'] = F
    print(df)

    df.to_csv('data.csv')
    os.startfile('.\\data.csv')

#******
# var variable is also a String variable
var = StringVar()
# which contents the TEXT of the label
var.set("Website Scrapper Tool")
#Only for a label within the window
LABEL_OF_WEB = Label(win,textvariable=var,bd=8,bg="yellow",font=("Helvetica",35)).grid(row=0,column=0, pady=10)
# A StringVar which will pass the url to the function
URL=StringVar()
#EntryBox
E1 = Entry(win,bd=5,font=7,textvariable=URL, border=5).grid(row=1,column=0,ipadx=100)
#Button
button = Button(win,text = "Scrap it!",bd=5,command=scrappin,border=5,borderwidth=5, activebackground='green').grid(row=2,column=0,padx=8,pady=4)
#******

win.mainloop()
