import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
st.beta_set_page_config(layout="wide")

st.title("Overview of historical weather in Pune")
st.text("dataset source - kaggle ")
st.subheader("hourly temperature ")

@st.cache
def load_data(nrows):
	data = pd.read_csv('pune.csv', nrows=nrows,infer_datetime_format = True)
	data['date_time'] = pd.to_datetime(data['date_time'], format='%Y-%m-%d %H:%M:%S')
	#data.set_index('date_time')
	return data

datelimits = st.date_input("dates range ",[datetime.date(2019, 7, 6), datetime.date(2019, 7, 15)],min_value=datetime.date(2009, 1, 1),max_value=datetime.date(2020, 1, 1))

data=load_data(None)

startindex=data[data['date_time']==str(datelimits[0])].index[0]
try:
	endindex=data[data['date_time']==str(datelimits[1])].index[0]
except:
	endindex=96432
steps=st.number_input('x axis steps', value=10,min_value=1)

st.write(startindex,endindex)
df = pd.DataFrame(data[startindex:endindex ], columns = ['tempC'])
fig=plt.figure()
plt.plot(df,figure=fig)
plt.xticks(rotation=90,ticks=[i  for i in range(startindex,endindex,steps)],labels=[data['date_time'][i].date()  for i in range(startindex,endindex,steps)],figure=fig)
st.pyplot(fig)

#st.altair_chart(df)
#st.line_chart(df)