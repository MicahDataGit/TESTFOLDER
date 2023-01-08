import os

from PIL import Image

import streamlit as st
import glob
 
wd = os.getcwd()
wd = wd.replace("\\","/")

def load_images():
    image_files = glob.glob("{}/Outputs/*/*.jpg".format(wd))
    #st.write(len(image_files))
    
    months = []
    for image_file in image_files:
        image_file = image_file.replace("\\", "/")
        parts = image_file.split("/")
        
        for x in range(len(parts)):                
            if parts[x].isdigit():                                   
                if parts[x] not in months:
                    months.append(parts[x])
    months.sort()
     
     #st.write(months)
    return image_files, months

st.title("Calendar")

image_files, months = load_images()

view_month = st.multiselect('Select Year(s)', months)

n = 1

view_images = []
for image_file in image_files:
    if any(month in image_file for month in view_month):
        view_images.append(image_file)
groups = []
for i in range(0, len(view_images), n):
    groups.append(view_images[i:i+n])


for group in groups:
    cols = st.columns(n)
    for i, image_file in enumerate(group):
        # cols[i].image(image_file)
        #st.write(i, image_file)
        image = Image.open(image_file)
        st.image(image) 
