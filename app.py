import streamlit as st
import requests
import json

st.title("Fashion Stylist Chatbot 👗✨")

# Ask questions first
st.write("Welcome! Please answer a few questions so I can understand your style better.")

skin_tone = st.selectbox("What is your skin tone?", 
                         ["Fair", "Light", "Medium", "Olive", "Tan", "Deep"])

body_shape = st.selectbox("What is your body shape?", 
                          ["Hourglass", "Pear", "Rectangle", "Apple", "Inverted Triangle"])

hair_length = st.selectbox("What is your hair length?", 
                           ["Short", "Medium", "Long"])

color_pref = st.selectbox("What color palette do you prefer?", 
                          ["Neutrals", "Pastels", "Bold colors", "Dark colors"])

st.write("---")
user_input = st.text_input("Now ask me anything related to fashion, styling, or outfits:")

SERPER_API_KEY = "PUT-YOUR-KEY-HERE"   # <-- We will replace this later

def google_search(query):
    url = "https://google.serper.dev/search"
    headers = {"X-API-KEY": SERPER_API_KEY}
    payload = {"q": query}

    response = requests.post(url, headers=headers, json=payload)
    return response.json()

if st.button("Get Styling Advice"):
    profile = (
        f"Skin tone: {skin_tone}, "
        f"Body shape: {body_shape}, "
        f"Hair length: {hair_length}, "
        f"Color preference: {color_pref}."
    )
    
    search_query = f"{user_input} outfit ideas for {profile}"
    data = google_search(search_query)

    st.subheader("Your Personalized Styling Advice")
    st.write(data)
