import streamlit as st

# Define app structure
def main():
    st.set_page_config(page_title="Application Portfolio", layout="wide")
    st.title("Application Portfolio")
    
    st.sidebar.title("Navigation")
    section = st.sidebar.radio("Select a category:", ("Port Sector", "Academic"))
    
    if section == "Port Sector":
        st.header("Port Sector Applications")
        st.subheader("Port Data Explorer Brazil")
        st.write("This app provides fast and convenient access to cargo tonnage data for Brazilian ports and terminals. Using updated information from ANTAQ’s Aquaviary Statistics, it lets you explore port logistics effortlessly.")
        st.markdown("[Explore the app](https://movimentacaoportuaria.streamlit.app/)")
    
    elif section == "Academic":
        st.header("Academic Applications")
        
        st.subheader("Text Mining Assistant")
        st.write("The goal of this app is to make it easier to analyse text data within PDF files. You can select up to three keywords, and the app will identify their locations, highlight them, and extract the surrounding text. It also allows you to download a Word document with the extracted content and an Excel file showing the frequency of each keyword.")
        st.markdown("[Explore the app](https://textmininginput.streamlit.app/)")
        
        st.subheader("SDG Data Manager")
        st.write("This app is designed to simplify the inclusion and management of data related to Sustainable Development Goals (SDG) attributes. It streamlines the tracking and organisation of sustainability goals, helping you stay on top of your projects.")
        st.markdown("[Explore the app](https://sdg7and13.streamlit.app/)")
        
        st.subheader("Academic Matchmaker")
        st.write("This app connects you to leading researchers in specific fields by displaying their name, number of citations, and affiliated university. It’s a fast and effective way to find experts in your area of interest.")
        st.markdown("[Explore the app](https://matchgscholar.streamlit.app/)")
        
        st.subheader("Scholar Search")
        st.write("This app is designed to simplify searches on Google Scholar by allowing you to explore the research areas of multiple scholars at once. Just enter their names separated by commas, and the app does the rest.")
        st.markdown("[Explore the app](https://quicksearchgs.streamlit.app/)")
        
        st.subheader("H-index Checker")
        st.write("This app helps you quickly check the number of citations and h-index of researchers. Enter their names separated by commas, and it instantly displays all the information you need.")
        st.markdown("[Explore the app](https://h-index.streamlit.app/)")

if __name__ == "__main__":
    main()
