import streamlit as st
import os
import numpy as np
from image_meta_parce import img_get_location
from streamlit_image_select import image_select
from streamlit_folium import st_folium
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
import streamlit as st
import pandas as pd 
import folium
import base64
# data = []
# arr_loc = []
def ubdate_selector():
    # global list_imgs
    list_imgs = [f"./images/{i}" for i in os.listdir(r"./images")]
    return list_imgs

list_imgs = ubdate_selector()

@st.cache
def prepare_data():
    # global arr_loc, data
    arr_loc = []
    for i in list_imgs:
        tmp = img_get_location(i)
        if tmp[0] is None:
            arr_loc.append([52.190348191,20.796055962, i])
        else:
            tmp.append(i)
            arr_loc.append(tmp)

    # arr_loc[0] = [52.190348191,20.416055962]

    return pd.DataFrame(
        arr_loc,
        columns=['lat', 'lon', 'image_path']), arr_loc

data, arr_loc = prepare_data()

@st.cache
def prepare_ag_settings():
    global data
    gb = GridOptionsBuilder.from_dataframe(data)
    gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
    gb.configure_side_bar() #Add a sidebar
    gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
    return gb.build()
    
gridOptions = prepare_ag_settings()

def create_marker_from_img(image_path, m, loc=[52.190348191, 20.416055962]):
    encoded = base64.b64encode(open(image_path, 'rb').read())
    html = '<img src="data:image/png;base64, {}" style="width:200px; height:auto;">'.format
    popup_content = html(encoded.decode('UTF-8'))
    marker = folium.Marker(
    loc,
    popup = popup_content,
    tooltip="OK",
    icon=folium.Icon(color = 'red')
    )
    marker.add_to(m)
   

def update_selection(select, m):
    for i in select:
        create_marker_from_img(i['image_path'], m, loc=[i['lat'],i['lon']])
        # print(i)


st.title('Garbage photo locations')


grid_response = AgGrid(
    data,
    gridOptions=gridOptions,
    data_return_mode='AS_INPUT', 
    update_mode='MODEL_CHANGED', 
    fit_columns_on_grid_load=False,
    theme='streamlit', #Add theme color to the table
    enable_enterprise_modules=False,
    height=350, 
    width='100%',
    # reload_data=True
)

data = grid_response['data']
selected = grid_response['selected_rows'] 
# df = pd.DataFrame(selected)

m = folium.Map(location=[52.190348191,20.916055962], zoom_start=8)

update_selection(selected, m)

st_data = st_folium(m, width=725)

st.title('Garbage photo exaples')

# img = st.empty()
ubdate_selector()
img = image_select("Label", list_imgs)


st.image(img)


def save_uploadedfile(uploadedfile):
    path_new_file = os.path.join("images",uploadedfile.name)
    with open(path_new_file,"wb") as f:
        f.write(uploadedfile.getbuffer())
    return st.success("Saved File:{} to images".format(path_new_file.split('/'[-1])))



image_file = st.file_uploader("Upload An Image",type=['png','jpeg','jpg'])
if image_file is not None:
    save_uploadedfile(image_file)
    ubdate_selector()
