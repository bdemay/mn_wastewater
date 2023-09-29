# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 22:54:12 2023

@author: brad user

This takes data from the  Wastewater SARS-CoV2 Surveillance Study

https://experience.arcgis.com/experience/a8d269bd670a421e9fd45f967f23f13c

The files will be in the format ww_region_untransformed_ORF.csv
This is a CSV file with column names at the top
I will likley make it fragile until I can put in the work to make it dynamicly allocate columns 

I'm going to use a pandas data set for dealing with the data at runtime - info 'https://realpython.com/pandas-python-explore-dataset/

<a href="https://covidwastewater.ahc.umn.edu/jmp_files/ww_region_untransformed_ORF.csv">regional data</a>

"""

import pandas as pd
import matplotlib.pyplot as plt
import requests


## pull the data from the U of M 
url = "https://covidwastewater.ahc.umn.edu/jmp_files/ww_region_untransformed_ORF.csv"
r = requests.get(url, allow_redirects=True)
open('ww_region_untransformed_ORF.csv', 'wb').write(r.content)

name="ww_region_untransformed_ORF.csv" 

 
wasteData = pd.read_csv(name)


# get columns 
column_names = list(wasteData.columns.values)
#print(column_names)


#print(wasteData["Facility"].unique())
# pull the locations from this file 
locations=wasteData["Facility"].unique()

# create seperate frames for each location with the data 



for location in locations:
    print("location name: ", location)
    # data for a specific location 
    # need to limit by 2023 dates only as well as local facility 
    #localFacility= wasteData.query("Facility == 'Central' and SampleDate > '2023-01-01'")
    localFacility= wasteData.query("Facility == @location and SampleDate > '2023-01-01'")
    #print(localFacility)
    df = pd.DataFrame(data=localFacility[['SampleDate','ORFlab_Copies.L','S_Copies.L', 'N_Copies.L']])
    #print(df)
    #df.plot(x='SampleDate', y='ORFlab_Copies.L', kind='line',title=location)	
    df.plot(x='SampleDate', y=['ORFlab_Copies.L', 'S_Copies.L', 'N_Copies.L'], figsize=(10,5))
    # Set the x-axis label
    plt.xlabel('SampleDate')
    # Set the y-axis label
    plt.ylabel('Sample Counts')
    # Set the title of the plot
    plt.title(location)
    # Display the plot
    #plt.show()
    plotname=location.strip() + ".png"
    #print(plotname)
    plt.savefig(plotname, format='png', dpi=92) # save the plot out to the directory


## past this save for later in the case that I have to clean the data and build the dataframe from the cleaned data
#Open file 

#file_object = open(name, 'r')

#Read in header
#first_line = file_object.readline() 
#print (first_line)

#columns=first_line.replace('\"','').split(',') # remove quotes from column names 
#print(columns) 

#data = file_object.read()
#print(data)

# read in data and create data structure 

# get selection of filters 


#Calculate sort term trend 

 
#file_object.close()





"""
In this example, we have a simple HTML structure with 8 img elements, each displaying a different PNG image related to COVID wastewater test data. The images are placed inside a container div with some basic styling for layout.

Replace "image1.png", "image2.png", etc., with the actual file paths to your PNG images. You can customize the styling and layout further according to your preferences.

Make sure to have the PNG image files available in the same directory as this HTML file, or provide the correct file paths to the images in the src attributes of the img elements.

"""

# Define the HTML content as a Python string
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>COVID Wastewater Test Data Images</title>
    <style>
        /* Add your CSS styles here */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f0f0f0;
        }
        header {
            background-color: #007BFF;
            color: #fff;
            text-align: center;
            padding: 20px;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            text-align: center;
        }
        .image {
            margin: 20px;
        }
    </style>
</head>
<body>
    <header>
        <h1>Minnesota COVID Wastewater Testing Data</h1>
    </header>
    <div class="container">
        <div class="image">
            <img src="Metropolitan.png" alt="Image 1">
        </div>
        <div class="image">
            <img src="North_East.png" alt="Image 2">
        </div>
        <div class="image">
            <img src="North_West.png" alt="Image 3">
        </div>
        <div class="image">
            <img src="South_Central.png" alt="Image 4">
        </div>
        <div class="image">
            <img src="South_East.png" alt="Image 5">
        </div>
        <div class="image">
            <img src="Central.png" alt="Image 6">
        </div>
        <div class="image">
            <img src="South_West.png" alt="Image 7">
        </div>
        <div class="image">
            <img src="Entire State.png" alt="Image 8">
        </div>
    </div>
</body>
</html>
"""

# Specify the file name and path where you want to save the HTML file
file_path = "generated_watewater_page.html"

# Open the file for writing and write the HTML content
with open(file_path, "w") as html_file:
    html_file.write(html_content)

print(f"HTML page generated and saved as {file_path}")


