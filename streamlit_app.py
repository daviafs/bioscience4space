import streamlit as st
import numpy as np
import pandas as pd

# Page configuration
st.set_page_config(page_title='Biosciences for Space', layout='wide')

# CSS customizado para aplicar fundo preto e letras brancas na página principal
st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
        color: white;
    }

     /* Estilo para o título principal dentro de um elemento <h1> */
    .main-title {
        color: white;  /* Cor do texto do título principal */
        font-size: 2.5em;  /* Tamanho da fonte do título principal */
    }

    /* Mantendo o estilo padrão da sidebar */
    .stApp header, .stApp footer, .css-18e3th9 {  /* Classes relacionadas à sidebar */
        background-color: inherit;  /* Mantém o estilo padrão da sidebar */
        color: inherit;  /* Mantém a cor padrão da sidebar */
    }

     .stExpander {
        border: 1px solid white;  /* Borda do expander */
        border-radius: 10px;  /* Cantos arredondados */
        background-color: white;  /* Fundo do expander */
        color: black;  /* Cor do texto do expander */
    }

    .stExpander > div {
        color: black;  /* Cor do texto dentro do expander */
    }

     /* Estilo para a sidebar */
    .sidebar{
        background-color: #2C2C2C;  /* Cor de fundo da sidebar (cinza escuro) */
    }
    
   .image-container {
        display: flex;
        justify-content: center; /* Centraliza as imagens horizontalmente */
        margin: 16px 0;
    }
    .image-box {
        text-align: center; /* Centraliza a legenda */
        cursor: pointer; /* Adiciona cursor de ponteiro */
        margin: 0 10px; /* Espaçamento entre as imagens */
    }
    .image-title {
        font-size: 1.8em; /* Tamanho menor para o título da seção de imagens */
        color: white; /* Cor do título */
    }
    .caption {
    color: black; /* Cor da legenda das imagens */
    text-align: center; /* Centraliza a legenda */
    background-color: white; /* Fundo branco para a legenda */
    border-radius: 5px; /* Cantos arredondados */
    padding: 5px; /* Espaçamento interno */
    }

    .stButton {
    color: black; /* Cor do texto do botão */
    display: block; /* Faz o botão ocupar toda a largura disponível */
    margin: 0 auto; /* Centraliza o botão */
    }
    
    </style>
    """,
    unsafe_allow_html=True
)

# Main title
st.markdown('<h1 class="main-title">Biosciences for Space 🐁🌱🦠🚀</h1>', unsafe_allow_html=True)

# Introduction section
st.write(""" 
    The **Biosciences for Space (B4S)** is a tool proposed for the challenge
    'Visualize Space Science', during the NASA Space Apps Challenge 2024.
    Are you ready to explore the Universe of opportunities in the realm of Space Biosciences?
    """
)

# Columns with content inside expanders
exp_col1, _, exp_col2 = st.columns([2, 0.2, 2])
with exp_col1:
    with st.expander("**🧬 Biological Experiments in Space**"):
        st.markdown("""
            The use of living organisms in space predates human space missions. 
            Scientists have been studying the effects of long-term exposure to the space 
            environment using animals, plants, bacteria, and other microorganisms.
            Space Biosciences aim to understand a range of effects and limitations of 
            biological systems in space. This includes:
            
            - Physiological adaptations
            - Gene expression and regulation
            - Cellular development and evolution
            - Health improvements and disease treatments

            These studies are crucial in understanding how long-term space travel will affect 
            astronauts and how we can develop innovative strategies to support human presence 
            in space while advancing Earth-based applied sciences.
        """)

with exp_col2:
    with st.expander("**🔎 Stressors of the Space Environment**"):
        st.markdown("""                  
            Dealing with stressors in the space environment is a complex task. There are 
            two main types of stress: biotic and abiotic. Biotic stresses on Earth are caused 
            by biological intermediates like viruses, fungi, bacteria, and other pathogens. 
            In space, bio-contaminants behave similarly, but now under space conditions.
            
            On the other hand, the abiotic stressors, such as radiation, microgravity,
            and extreme temperatures, represent the major environmental challenges. 
            Especially because they are imminent stresses that directly affect, depending
            on their severity and duration of exposure, how living organisms peform in space. These stressors affect organisms' 
            development, limiting their normal performance. Understanding and mitigating 
            these effects are key to ensuring successful space missions.
        """)

# Função para ler dados dos arquivos txt com codificação ajustada
def load_data(file_path):
    try:
        # Tenta carregar o arquivo com codificação ISO-8859-1
        data = pd.read_csv(file_path, delimiter=',', encoding='ISO-8859-1')  
        return data
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo {file_path}: {e}")
        return None

# Carregando os dados dos arquivos .txt
data_1 = load_data('dataset/OSD-379.txt')
data_2 = load_data('dataset/OSD-665.txt')
data_3 = load_data('dataset/OSD-678.txt')

# Verifica se os dados foram carregados corretamente e cria gráficos
if data_1 is not None:
    graph_data_1 = data_1
if data_2 is not None:
    graph_data_2 = data_2
if data_3 is not None:
    graph_data_3 = data_3

# Exibe o vídeo local
video_file = open('/workspaces/bioscience4space/figures_and_videos/background_video.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)

# Título para a seção de imagens
st.markdown('<h1 class="image-title">Space Biosciences datasets </h1>', unsafe_allow_html=True)
st.write("""Let's dive into NASA's Open Science Data Repository (OSDR)
            while analyzing many interesting data regarding biological
            experiments held in space. Click on the captions to further 
            check the available data. To access the full repository
          [*click here!*](https://www.spaceappschallenge.org/nasa-space-apps-2024/find-a-team/astrocactus/?tab=details)
         """)

# Adicionando imagens com interatividade
image_info = [
  {"url": "https://osdr.nasa.gov/geode-py/ws/studies/OSD-665/image", "caption": "**Animals**"},
    {"url": "https://osdr.nasa.gov/geode-py/ws/studies/OSD-678/image", "caption": "**Plants**"},
    {"url": "https://osdr.nasa.gov/geode-py/ws/studies/OSD-683/image", "caption": "**Bacteria** *(SOON)*"},
    {"url": "https://osdr.nasa.gov/geode-py/ws/studies/OSD-516/image", "caption": "**Humans** *(SOON)*"},
]

# Cria uma variável de sessão para armazenar a imagem clicada
if 'selected_image' not in st.session_state:
    st.session_state.selected_image = None

# Exibe as imagens lado a lado
col1, col2, col3, col4 = st.columns(4)
for idx, image in enumerate(image_info):
    with eval(f"col{idx + 1}"):
        st.image(image['url'], width=160)  # Reduzindo o tamanho da imagem
        
        # Usando um botão normal com a legenda e centralizando
        button_placeholder = st.empty()  # Cria um espaço para o botão
        with button_placeholder.container():  # Usando um container para centralizar
            if st.button(image['caption'], key=f"button_{idx}"):
                st.session_state.selected_image = idx


# Exibe o gráfico ou a mensagem com base na interação da imagem
if st.session_state.selected_image is not None:
    with st.expander("**Explore the available data!**"):
        if st.session_state.selected_image in [2, 3]:  # Imagens 3 e 4 (índices 2 e 3)
            st.write("*Unfortunately, the data is not available for now. Please return in the future.*")
        else:
            selected_image_info = image_info[st.session_state.selected_image]

            # Exibe um expander aninhado para selecionar o conjunto de dados
            if st.session_state.selected_image == 0:  # Imagem 1
                dataset_option = st.selectbox("**Choose a dataset:**", ["OSD-379", "OSD-665"])
                if dataset_option == "OSD-379":
                    st.line_chart(graph_data_1)  # Gráfico 1
                if dataset_option == "OSD-665":
                    st.line_chart(graph_data_2)  # Gráfico 2
            if st.session_state.selected_image == 1:  # Imagem 1
                dataset_option = st.selectbox("**Choose a dataset:**", ["OSD-678"])
                if dataset_option == "OSD-678":
                    st.line_chart(graph_data_3)  # Gráfico 1
           
# Sidebar content
st.sidebar.title("Biosciences for Space (B4S)")
st.sidebar.caption("Made by [g-Mouse Team](https://www.spaceappschallenge.org/nasa-space-apps-2024/find-a-team/astrocactus/?tab=details)")

with st.sidebar.expander("ℹ️ **About us**"):
    st.image("/workspaces/bioscience4space/figures_and_videos/team.webp", use_column_width=True )
    st.markdown("""    
        We are **g-Mouse**, a team of Brazilian researchers passionate 
        about space, science, technology, and innovation. Our mission is to
        develop creative solutions that transform complex data into accessible
        and impactful visualizations for scientists, engineers, and the public. 
        We promote a deeper understanding of discoveries that inspire the future of 
        interplanetary exploration and its benefits for Earth.
    """)

with st.sidebar.expander("ℹ️ **About the Challenge**"):
    st.markdown("""
        Biological experiments performed in space are critical to scientific discovery, 
        but they are complex to execute and conceptualize. These experiments must be 
        launched into space, performed using specialized hardware, and often returned 
        to Earth for analysis. The challenge is to create a tool that generates 
        informative and compelling visualizations of these experiments.
    """)