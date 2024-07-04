# Reference: Sqlzealots
# Open and Read from an Excel File and plot a chart in Python using matplotlib and tkinter
# https://sqlzealots.com/2020/10/26/open-and-read-from-an-excel-file-and-plot-a-chart-in-python-using-matplotlib-and-tkinter/

import os
import cv2
import time
import tkinter as tk
from tkinter import *
import webbrowser
from selenium import webdriver
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# root.geometry("1000x800")

def get_screenshot():
    wd = webdriver.Chrome()
    url = 'https://www.weather.go.kr/w/weather/forecast/short-term.do'
    wd.get(url)
    time.sleep(3)
    wd.save_screenshot('forecast.png')
    wd.quit()

def show_screenshot():
    img1_path = 'forecast.png'
    img1_orig = cv2.imread(img1_path) 
    img1_width = img1_orig.shape[1]-90
    img1_height = img1_orig.shape[0]
    img1_orig = img1_orig[0:img1_width, 0:img1_height]

    geometry_text = str(img1_width + 120) + "x" + str(img1_height + 5)

    root = tk.Tk()
    root.title("Meteorological Administration Forecast Screenshot")
    root.geometry(geometry_text)

    hotrizontal_ratio = img1_width / 30
    vertical_ratio = img1_height / 30

    fig = plt.figure(figsize=(hotrizontal_ratio, vertical_ratio))
    subplot = fig.add_subplot(1, 1, 1)
    fig.subplots_adjust(left=0.05, bottom=0.07, right=0.95, top=0.95, wspace=0, hspace=0)
    bar = FigureCanvasTkAgg(fig, root)
    bar.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    subplot.imshow(cv2.cvtColor(img1_orig, cv2.COLOR_BGR2RGB), interpolation='nearest', aspect='auto')
    subplot.axis('off')

    root.mainloop()

get_screenshot()
show_screenshot()


