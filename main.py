import streamlit as st


st.header("Fake news detection for Vietnamese")
col1, col2 = st.columns([6, 4])

with col1:
    news = st.text_area("Insert a piece of news here")
    entered_items = st.empty()

button = st.button("Predict if this is real or fake!")
if button:
    with st.spinner("Predicting..."):
        if not len(news):
            st.markdown("Input at least a piece of news")
        else:
            pred =1

            if pred == 1:
                st.markdown("Real news")
            else:
                st.markdown("Fake news!!!")