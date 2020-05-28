#Importing all the libraries

#Using streamlit to make front-end part of application
import streamlit as st 

import pandas as pd 
import plotly.express as px 
import nltk 

#Using corpus swadesh
from nltk.corpus import swadesh


#Heading to be provided with the help of streamlit 
st.title('Translate English words to various languages')
st.sidebar.title('Translate English words to various languages')

st.markdown('This is a dashboard where you can hover over the country in a map to know the language codes of that place\'s native language and then translate English words')


#Languages whose words are present in swadesh corpus
languages = swadesh.fileids()

#iso_alpha codes of countries to use them in form of locations in plotly_express map
country_codes = ['BLR' , 'BGR' , 'BIH' , 'AND' ,'CZE' , 'MNE','DEU' , 'USA' , 'URY' , 'FRA' , 'HRV' , 'CHE', 'ITA' , 'MKD' , 'ABW', 'POL',
 'PRT' , 'ROU' , 'RUS' ,'SVK' , 'SVN' , 'SRB', 'KEN' ,'UKR'  ]

#Country_codes converted to pandas dataframe so as to use them in maps
country_codes = pd.DataFrame(country_codes)

#list of words of different languages stored
x = []

#index of the particular language in the above list 
indx = dict()


i = 0 
for lang in languages:
	a = swadesh.entries(['en',lang])
	#storing words of each language in list
	x.append(swadesh.entries([lang]))
	#storing index of each language
	indx[lang] = i
	i = i + 1 

country_codes['lang'] = languages


#Check box on sidebar to be unchecked if user wants to see map 
if  st.sidebar.checkbox('Check to show the Map' ,False):
	st.subheader('Hover your mouse over countries to know the language code of various countries')
	#Map with country_codes being used as locations
	fig = px.choropleth(country_codes,locations =country_codes[:][0] ,
             projection = 'orthographic' , hover_name = country_codes[:][0],hover_data = ['lang' ])
	st.plotly_chart(fig)


#Checkbox to show the dictionary options
if  st.sidebar.checkbox('Check to show the dictionary options' ,True):
	#Select Box to select language codes
	select = st.sidebar.selectbox('Select language to convert English words to' ,(languages), key =1)
	st.subheader('The converted English words of the selected language are following:')
	k =[]
	#Printing English words and also translated Words
	for word in x[indx['en']]:
		words = word[0] 
		words = words.replace("(" , "") 
		words = words.replace(")" , "") 
		words = words.replace("\'" , "")
		words = words.replace("," , "") 
		p = words + " :"
		k.append(p)
	i = 0 
	for word in x[indx[select]]:
		words = word[0]
		words = words.replace("(" , "") 
		words = words.replace(")" , "") 
		words = words.replace("\'" , "")
		words = words.replace("," , "") 
		k[i] = str(i) + ") " + k[i] + " " +  words
		st.write(k[i])
		i = i+1
	
	
	


	
	