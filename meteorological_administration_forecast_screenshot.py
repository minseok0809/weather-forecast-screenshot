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

root = tk.Tk()
root.title("Meteorological Administration Forecast Screenshot")
root.geometry("1000x800")

def get_screenshot():
    wd = webdriver.Chrome()
    url = 'https://www.weather.go.kr/w/weather/forecast/short-term.do'
    wd.get(url)
    time.sleep(3)
    wd.save_screenshot('forecast.png')
    wd.quit()

def show_screenshot(root):
    img1_path = 'forecast.png'
    img1_orig = cv2.imread(img1_path) 
    img1_orig = img1_orig[0:img1_orig.shape[1]-260, 0:img1_orig.shape[0]-27]
    
    hotrizontal_ratio = img1_orig.shape[0] / 30
    vertical_ratio = img1_orig.shape[1] / 30

    fig = plt.figure(figsize=(hotrizontal_ratio, vertical_ratio))
    subplot = fig.add_subplot(1, 1, 1)
    
    bar = FigureCanvasTkAgg(fig, root)
    bar.get_tk_widget().pack(fill=tk.BOTH, expand=0)
    subplot.imshow(cv2.cvtColor(img1_orig, cv2.COLOR_BGR2RGB), interpolation='nearest', aspect='auto')
    subplot.axis('off')

get_screenshot()
show_screenshot(root)

root.mainloop()
