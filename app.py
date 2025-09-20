import streamlit as st

# Define app structure
def main():
    st.set_page_config(page_title="Portfólio de Aplicações | Application Portfolio", layout="wide")
    st.title("Portfólio de Aplicações | Application Portfolio")
    
    st.header("Aplicações | Applications")
    
    # --- PortExports ---
    st.subheader("Exportações Portuárias | PortExports")
    st.write("Este painel interativo apresenta uma visão geral das exportações marítimas movimentadas pelo setor portuário em 2023. Permite analisar volumes de exportação por país e produto, oferecendo insights sobre fluxos comerciais e a distribuição das cargas movimentadas pelos portos.  \n\n"
             "This interactive dashboard provides an overview of maritime exports handled by the port sector, specifically for the year 2023. The application allows users to analyse export volumes by country and product, offering insights into trade flows and the distribution of port-handled goods.")
    st.markdown("[Acessar o aplicativo | Explore the app](https://portexports.streamlit.app/)")
    
    # --- Global Maritime Trade Dashboard ---
    st.subheader("Painel Global de Comércio Marítimo | Global Maritime Trade Dashboard")
    st.write("O 'Painel Global de Comércio Marítimo' é uma ferramenta interativa para analisar e visualizar os fluxos de carga no setor hidroviário brasileiro por país e tipo de produto. Oferece insights sobre o comércio internacional, ajudando a compreender a distribuição e as tendências de volume.  \n\n"
             "The 'Global Maritime Trade Dashboard' is an interactive tool designed to analyse and visualise cargo movements in the Brazilian waterway sector by country and product type. It provides insights into international trade flows, helping users understand cargo distribution and volume trends.")
    st.markdown("[Acessar o aplicativo | Explore the app](https://globalmaritimetradedashboard.streamlit.app/)")
    
    # --- Port Cargo Movement Dashboard ---
    st.subheader("Painel de Movimentação de Cargas Portuárias | Port Cargo Movement Dashboard")
    st.write("O 'Painel de Movimentação de Cargas Portuárias' é uma ferramenta interativa para analisar e visualizar as movimentações de cargas nos portos brasileiros. Proporciona uma visão abrangente da atividade portuária, permitindo explorar tendências e insights relacionados à logística marítima.  \n\n"
             "The 'Port Cargo Movement Dashboard' is an interactive tool designed to analyse and visualise cargo movements across Brazilian ports. It provides a comprehensive overview of port activity, allowing users to explore key trends and insights related to maritime logistics.")
    st.markdown("[Acessar o aplicativo | Explore the app](https://observatorio1.streamlit.app/)")
    
    # --- Text Mining ---
    st.subheader("Assistente de Mineração de Texto | Text Mining Assistant")
    st.write("Este aplicativo facilita a análise de textos em arquivos PDF. Você pode selecionar até três palavras-chave, e o app identificará suas localizações, destacará os trechos e permitirá exportar os resultados em Word e Excel.  \n\n"
             "This app makes it easier to analyse text data within PDF files. You can select up to three keywords, and the app will identify their locations, highlight them, and extract the surrounding text. It also allows you to download a Word document with the extracted content and an Excel file showing keyword frequencies.")
    st.markdown("[Acessar o aplicativo | Explore the app](https://textmininginput.streamlit.app/)")
    
    # --- Modelo ODS ---
    st.subheader("Modelo ODS | SDG Model")
    st.write("Este aplicativo auxilia na inclusão e gestão de dados relacionados aos Objetivos de Desenvolvimento Sustentável (ODS). Ele organiza informações e facilita o acompanhamento de metas de sustentabilidade em projetos.  \n\n"
             "This app helps manage and track data related to Sustainable Development Goals (SDGs). It streamlines the process of organising sustainability attributes, making it easier to monitor progress across projects.")
    st.markdown("[Acessar o aplicativo | Explore the app](https://modeloods-ff6md9cyz5pfwinhzlupgm.streamlit.app/)")


if __name__ == "__main__":
    main()
