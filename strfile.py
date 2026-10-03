import streamlit as st
st.title('My First website -- iqra')
st.header('Detail')
st.write('I have created my first website now')
st.text("It's for plain text. -- st.wrtie is for content.")
st.markdown('# Main Heading' )
st.markdown('## subheading')
st.markdown('**Hello**')
st.markdown('*Hello*')
#st.latex(r'''e^{i\pi}+1 = 0''')
st.title('New Heading')
st.subheader("Sub header content")
st.header('Header')
st.subheader("Sub header content")
st.code("[i for i in range(1,10)]") #only displays code
import pandas as pd
df : pd.DataFrame = pd.DataFrame({      #it doesnt display in website ye bs data frmae banata.. df is variable
    "Col1":[1,2,3],
    "Col2":['a','b','c']
})
st.write(df)
st.table(df)
st.json(df.to_dict())
st.metric('My metric', 42, 2)
st.title("Display Media")
st.video("https://youtu.be/_OVnXw2ldog?si=2qsVAd3WdTUAlRVH")
st.image('close-up-full-bloom-flower.jpg')

'''
# This is the document title

This is some _markdown_.
'''
df : pd.DataFrame = pd.DataFrame({
    'col1': [1,2,3],
    'col2': list('abc')
})

df
x=1000
'x',x
import matplotlib.pyplot as plt
import numpy as np
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=30)
st.pyplot(fig)
st.info("Your application is under review.")
st.warning("Warning")
st.error("Error")
exp = ZeroDivisionError("Trying to divide by Zero")

st.exception(exp)
st.write(range(10))
range(10)
from PIL import Image
img = Image.open('close-up-full-bloom-flower.jpg')
st.image(img, width=200)
if st.checkbox("Show/Hide"):
    st.text("Showing the widget")


