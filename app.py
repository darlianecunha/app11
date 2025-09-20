import streamlit as st

# Define app structure
def main():
    st.set_page_config(page_title="Application Portfolio", layout="wide")
    st.title("Application Portfolio")
    
    st.sidebar.title("Navigation")
    section = st.sidebar.radio("Select a category:", ("Port Sector",))
    
    if section == "Port Sector":
        st.header("Port Sector Applications")
        
        st.subheader("PortExports")
        st.write("This interactive dashboard provides an overview of maritime exports handled by the port sector, specifically for the year 2023. The application allows users to analyse export volumes by country and product, offering insights into trade flows and the distribution of port-handled goods.")
        st.markdown("[Explore the app](https://portexports.streamlit.app/)")
        
        st.subheader("Global Maritime Trade Dashboard")
        st.write("The 'Global Maritime Trade Dashboard' is an interactive tool designed to analyse and visualise cargo movements in the Brazilian waterway sector by country and product type. It provides insights into international trade flows, helping users understand cargo distribution and volume trends.")
        st.markdown("[Explore the app](https://globalmaritimetradedashboard.streamlit.app/)")
        
        st.subheader("Port Cargo Movement Dashboard")
        st.write("The 'Port Cargo Movement Dashboard' is an interactive tool designed to analyse and visualise cargo movements across Brazilian ports. It provides a comprehensive overview of port activity, allowing users to explore key trends and insights related to maritime logistics.")
        st.markdown("[Explore the app](https://observatorio1.streamlit.app/)")


if __name__ == "__main__":
    main()
