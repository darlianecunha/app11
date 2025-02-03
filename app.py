import streamlit as st

# Define app structure
def main():
    st.set_page_config(page_title="Application Portfolio", layout="wide")
    st.title("Application Portfolio")
    
    st.sidebar.title("Navigation")
    section = st.sidebar.radio("Select a category:", ("Port Sector", "Academic"))
    
    if section == "Port Sector":
        st.header("Port Sector Applications")
        
        st.subheader("PortExports")
        st.write("This interactive dashboard provides an overview of maritime exports handled by the port sector, specifically for the year 2023. The application allows users to analyse export volumes by country and product, offering insights into trade flows and the distribution of port-handled goods.")
        st.markdown("[Explore the app](https://portexports.streamlit.app/)")
        
        st.subheader("Global Maritime Trade Dashboard")
        st.write("The 'Global Maritime Trade Dashboard' is an interactive tool designed to analyse and visualise cargo movements in the Brazilian waterway sector by country and product type. It provides insights into international trade flows, helping users understand cargo distribution and volume trends.")
        st.markdown("[Explore the app](https://globalmaritimetradedashboard.streamlit.app/)")
        
        st.subheader("Brazilian Waterway Cargo Dashboard")
        st.write("The Brazilian Waterway Cargo Dashboard is an interactive tool designed to visualise and analyse the volume of goods handled by the Brazilian waterway sector.")
        st.markdown("[Explore the app](https://appbraziliancargoflow.streamlit.app/)")
        
        st.subheader("Port Cargo Movement Dashboard")
        st.write("The 'Port Cargo Movement Dashboard' is an interactive tool designed to analyse and visualise cargo movements across Brazilian ports. It provides a comprehensive overview of port activity, allowing users to explore key trends and insights related to maritime logistics.")
        st.markdown("[Explore the app](https://observatorio1.streamlit.app/)")
    
    elif section == "Academic":
        st.header("Academic Applications")
        
        st.subheader("Text Mining Assistant")
        st.write("This app makes it easier to analyse text data within PDF files. You can select up to three keywords, and the app will identify their locations, highlight them, and extract the surrounding text. It also allows you to download a Word document with the extracted content and an Excel file showing keyword frequencies.")
        st.markdown("[Explore the app](https://textmininginput.streamlit.app/)")
        
        st.subheader("SDG Data Manager")
        st.write("This app simplifies the inclusion and management of data related to Sustainable Development Goals (SDG) attributes. It streamlines tracking and organising sustainability goals, helping you stay on top of your projects.")
        st.markdown("[Explore the app](https://sdg7and13.streamlit.app/)")
        
        st.subheader("Academic Matchmaker")
        st.write("This app connects you to leading researchers in specific fields by displaying their name, number of citations, and affiliated university. It’s a fast and effective way to find experts in your area of interest.")
        st.markdown("[Explore the app](https://matchgscholar.streamlit.app/)")
        
        st.subheader("Scholar Search")
        st.write("This app simplifies searches on Google Scholar by allowing you to explore research areas of multiple scholars at once. Enter their names separated by commas, and the app does the rest.")
        st.markdown("[Explore the app](https://quicksearchgs.streamlit.app/)")
        
        st.subheader("H-index Checker")
        st.write("This app helps you quickly check the number of citations and h-index of researchers. Enter their names separated by commas, and it instantly displays all the information you need.")
        st.markdown("[Explore the app](https://h-index.streamlit.app/)")

if __name__ == "__main__":
    main()
