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
video_file = open('/workspaces/bioscience4space/figures_and_videos/Intro_Video.mp4', 'rb')
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
    with st.expander(" **Explore the available data!**"):
        if st.session_state.selected_image in [1, 2, 3]: 
            st.write("*Unfortunately, the data is not available for now. Please return in the future.*")
        else:
            selected_image_info = image_info[st.session_state.selected_image]

            # Exibe um expander aninhado para selecionar o conjunto de dados
            # Adiciona essa seção dentro do expander onde o gráfico é exibido
            if st.session_state.selected_image == 0:  # Imagem 1
                dataset_option = st.selectbox("**Choose a dataset:**", ["OSD-379", "OSD-665"])
                
                # Verifica qual dataset foi escolhido e cria a seleção de colunas correspondente
                if dataset_option == "OSD-379":
                    parameter = st.selectbox("Escolha um parâmetro", ["Sample distribution by sample type", "Sample distribution by category", "RNA Fragment size by sample group"])
                    if parameter == "Sample distribution by sample type":
                        st.image("/workspaces/bioscience4space/figures_and_videos/graphic1.webp", use_column_width=True)
                    if parameter == "Sample distribution by category":
                        st.image("/workspaces/bioscience4space/figures_and_videos/graphic2.webp", use_column_width=True)
                    if parameter == "RNA Fragment size by sample group":
                        st.image("/workspaces/bioscience4space/figures_and_videos/graphic 3.webp", use_column_width=True)


                     # Adiciona a tabela com 3 colunas e 2 linhas
                    st.write("#### **Mission overview:** *Rodent Research Reference Mission (RRRM-1)*")
                    # Adiciona caixas de texto estilizadas com título e informação
                    st.markdown("""
                    <div style="border: 2px solid #D3D3D3; padding: 10px; margin-top: 1px;">
                        <strong>Objective:</strong> To examine the physiology of aging and the
                                        effect of age on disease progression using
                                        groups of young and old mice flown in space
                                        and kept on Earth.
                    </div>
                    <div style="border: 2px solid #D3D3D3; padding: 10px; margin-top: 10px;">
                        <strong>Pre-flight preparation:</strong> A total of 40 female BALB/cAnNTac mice were used in the study, consisting 
                                                                of 20 young mice (10 to 16 weeks) and 20 old mice (30 to 52 weeks), along with
                                                                 40 basal control mice, 40 Habitat Ground Control (HGC) mice, and 40 Vivarium Ground
                                                                 Control (VGC) mice. All mice were monitored daily and acclimated to environments 
                                                                similar to those of the flight. 

                    </div>
                    <div style="border: 2px solid #D3D3D3; padding: 10px; margin-top: 10px;">
                        <strong>During the experiment:</strong> The flight and HGC mice were exposed to mold in their food and were grouped
                                                                 by weight and age. After 30-40 days on Earth, 20 mice (10 young and 10 old)
                                                                 returned from space, while another 20 (10 young and 10 old) remained in orbit 
                                                                for approximately 62 days before euthanasia and sample collection, which included
                                                                 7 to 10 liver samples per group. 
                    </div>
                    <div style="border: 2px solid #D3D3D3; padding: 10px; margin-top: 10px; margin-bottom: 20px;">
                        <strong>Post-flight procedures:</strong> During the return, the mice faced stressors due to poor weather conditions, 
                                                                resulting in motion sickness-like symptoms, and were housed with 10 mice per
                                                                cage for 7 days instead of the expected 2-3 days for rescue. Basal control mice
                                                                 were sacrificed on the first day after launch, while the remaining mice were kept
                                                                 under observation on Earth.
                    </div>
                    """, unsafe_allow_html=True)

                if dataset_option == "OSD-665":
                    column_names = data_2.columns.tolist()  # Obtém os nomes das colunas do dataset OSD-665
                    selected_column = st.selectbox("**Select the parameter:**", column_names)  # Seleção da coluna
                    # Plota o gráfico da coluna selecionada
                    # Agrupa os dados
                    grouped_data = data_2[selected_column].value_counts()

                    # Verifica o tipo de dado e plota o gráfico adequado
                    if pd.api.types.is_numeric_dtype(data_2[selected_column]):
                        st.line_chart(grouped_data)  # Para dados numéricos
                    else:
                        st.bar_chart(grouped_data)  # Para dados categóricos

                    # Adiciona a tabela com 3 colunas e 2 linhas
                    st.write("#### **Mission overview:** *Rodent Research-23 mission*")
                     # Adiciona caixas de texto estilizadas com título e informação
                    st.markdown("""
                    <div style="border: 2px solid #D3D3D3; padding: 10px; margin-top: 1px;">
                        <strong>Objective:</strong> To better understand the effects of spaceflight
                                      on the eyes, specifically on the structure and function of the 
                                     arteries, veins, and lymphatic vessels that are needed to
                                      maintain vision.
                    </div>
                    <div style="border: 2px solid #D3D3D3; padding: 10px; margin-top: 10px;">
                        <strong>Pre-flight preparation:</strong> The Rodent Research-23 (RR-23) mission began with the preparation 
                                                                of twenty (20) male C57BL/6J mice, aged 16 to 17 weeks. These animals
                                                                 were selected to study the function of arteries, veins, and lymphatic
                                                                 structures in the eyes, as well as changes in the retina before and
                                                                 after spaceflight. The primary objective of the research is to clarify
                                                                 whether these vascular changes impair visual function, considering that
                                                                 at least 40% of astronauts experience visual impairment known as Spaceflight
                                                                 Associated Neuro-Ocular Syndrome (SANS) during long-duration spaceflights. Prior
                                                                 to launch, the protocol was approved by NASA's Institutional Animal Care and Use
                                                                 Committee (IACUC), and all recommendations from the Guide for the Care and Use of
                                                                 Laboratory Animals were followed.
                    </div>
                    <div style="border: 2px solid #D3D3D3; padding: 10px; margin-top: 10px;">
                        <strong>During the experiment:</strong> The twenty mice were launched in a transport carrier on SpaceX-21 on December 6,
                                                                 2020. After arriving at the International Space Station (ISS), they were transferred
                                                                to two rodent habitats, where they were maintained in microgravity for 38 days. It is
                                                                 important to note that no tests or procedures were conducted aboard the ISS. After
                                                                 returning to Earth for Live Animal Recovery (LAR) on January 13, 2021, the mice were
                                                                 transported by helicopter to the Kennedy Space Center and then transferred to Texas
                                                                 A&M University (TAMU) along with an additional 20 mice from the Habitat Control Group 
                                                                 (HGC) and 20 from the Vivarium Control Group (VGC).
                    </div>
                    <div style="border: 2px solid #D3D3D3; padding: 10px; margin-top: 10px; margin-bottom: 20px;">
                        <strong>Post-flight procedures:</strong> After arriving at the TAMU Animal Care Facility (ACF), the mice underwent post-flight 
                                                                procedures, followed by euthanasia and tissue collection by the principal investigator 
                                                                (PI) team. The collected data are of paramount importance, as they include measurements
                                                                 of Intraocular Pressure (IOP), ultrasound, and Optical Coherence Tomography (OCT) from
                                                                 a subset of each group of mice. The analysis of the collected tissues encompasses a variety
                                                                 of organs and structures, including adrenal glands, brain, brown adipose tissue, and the
                                                                extensor digitorum longus (EDL), among others. The RR-23 payload produced relevant data,
                                                                 such as the temperature of the animal enclosure, relative humidity, and environmental
                                                                 monitoring data from the ISS. This study may shed light on vascular complications connected
                                                                 to ocular diseases found in humans on Earth, enabling the development of more advanced
                                                                 preventive strategies and treatments for patients.
                    </div>
                    """, unsafe_allow_html=True)
           
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

#----------------Gráfico

#####GRAFICO 1

import pandas as pd
import matplotlib.pyplot as plt

# Caminho para o arquivo Excel
file_path = '/content/a_OSD-379_transcription-profiling_rna-sequencing-(rna-seq)_Illumina NovaSeq.xlsx'

# Carregar os dados do Excel
df = pd.read_excel(file_path, sheet_name='a_OSD-379_transcription-profili')

# Exibir as primeiras linhas para verificar se os dados foram carregados corretamente
df.head()

# Caminho para o arquivo Excel
file_path = '/content/a_OSD-379_transcription-profiling_rna-sequencing-(rna-seq)_Illumina NovaSeq.xlsx'


def classify_sample_by_prefix(sample_name):
    if 'BSL' in sample_name:
        return 'Basal Control'
    elif 'FLT' in sample_name:
        return 'Flight'
    elif 'GC' in sample_name:
        return 'Ground Control'
    elif 'VIV' in sample_name:
        return 'Vivarium Control'
    else:
        return 'Unknown'

# Aplicar a classificação ao nome das amostras
df['Sample Classification'] = df['Sample Name'].apply(classify_sample_by_prefix)

# Contar o número de amostras em cada categoria
sample_counts = df['Sample Classification'].value_counts()

# Definir cores para os grupos
colors = {
    'Basal Control': 'blue',
    'Flight': 'red',
    'Ground Control': 'green',
    'Vivarium Control': 'orange'
}

# Criar gráfico de barras
plt.figure(figsize=(8,6))

# Criar uma barra transparente de 40 amostras por baixo
plt.bar(sample_counts.index, [40]*len(sample_counts), color='gray', alpha=0.3, label='Max Samples (40)')

# Plotar as barras preenchidas com os dados reais
bars = plt.bar(sample_counts.index, sample_counts.values, color=[colors.get(group, 'black') for group in sample_counts.index])

# Adicionar títulos e rótulos
plt.title('Sample Distribution by Sample Type (Max 40 Samples)', fontsize=14)
plt.xlabel('Sample Type', fontsize=12)
plt.ylabel('Number of Samples', fontsize=12)

# Adicionar rótulos com os valores no topo das barras
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1, int(yval), ha='center', va='bottom', fontsize=8, color='black')

# Limitar o eixo y para 40
plt.ylim(0, 40)

# Adicionar legenda
plt.legend()

# Exibir o gráfico
plt.grid(True, axis='y')
plt.show()


#####GRAFICO 2
# Refazendo o código para puxar os dados de um arquivo Excel em vez de usar um DataFrame simulado

import pandas as pd
import matplotlib.pyplot as plt

# Caminho para o arquivo Excel (substitua pelo caminho correto do seu arquivo)
file_path = '/content/a_OSD-379_transcription-profiling_rna-sequencing-(rna-seq)_Illumina NovaSeq.xlsx'

# Carregar os dados do Excel
df = pd.read_excel(file_path)

# Função para classificar as amostras com base nos prefixos BSL, FLT, GC e VIV
def classify_sample_by_prefix(sample_name):
    if 'BSL' in sample_name:
        return 'Basal Control'
    elif 'FLT' in sample_name:
        return 'Flight'
    elif 'GC' in sample_name:
        return 'Ground Control'
    elif 'VIV' in sample_name:
        return 'Vivarium Control'
    else:
        return 'Unknown'

# Aplicar a classificação ao nome das amostras
df['Sample Classification'] = df['Sample Name'].apply(classify_sample_by_prefix)

# Contar o número de amostras em cada categoria
sample_counts = df['Sample Classification'].value_counts()

# Simulando subcategorias (por exemplo, jovens e velhos) para empilhamento
# Esta parte pode ser ajustada com dados reais ou de acordo com suas necessidades
stack_data = {
    'Young': [10, 15, 5, 8],  # Exemplo de valores de uma subcategoria
    'Old': [5, 7, 10, 9]      # Exemplo de outra subcategoria
}
stack_df = pd.DataFrame(stack_data, index=sample_counts.index)

# Definir cores para as subcategorias (diferentes partes da barra)
colors = ['blue', 'green']

# Criar um gráfico de barras empilhadas
plt.figure(figsize=(8,6))

# Empilhando as subcategorias
bars_bottom = None
for i, (category, color) in enumerate(zip(stack_df.columns, colors)):
    if bars_bottom is None:
        bars_bottom = plt.bar(stack_df.index, stack_df[category], color=color, label=category)
    else:
        bars_bottom = plt.bar(stack_df.index, stack_df[category], bottom=stack_df.iloc[:, :i].sum(axis=1), color=color, label=category)

# Adicionar limite no eixo y (máximo de 40)
plt.ylim(0, 40)

# Adicionar rótulos de valor no topo das barras empilhadas
for idx, row in stack_df.iterrows():
    total = row.sum()
    plt.text(idx, total + 1, int(total), ha='center', va='bottom', fontsize=12, color='black')

# Adicionar títulos e rótulos
plt.title('Stacked Bar Chart: Sample Distribution by Category', fontsize=14)
plt.xlabel('Sample Type', fontsize=12)
plt.ylabel('Number of Samples', fontsize=12)

# Adicionar legenda
plt.legend(title='Subcategories')

# Adicionar grid no eixo y
plt.grid(True, axis='y')

# Exibir o gráfico
plt.show()

#####GRAFICO 3

import pandas as pd
import matplotlib.pyplot as plt

# Caminho para o arquivo Excel
file_path = '/content/a_OSD-379_transcription-profiling_rna-sequencing-(rna-seq)_Illumina NovaSeq.xlsx'

# Carregar os dados do Excel
df = pd.read_excel(file_path)

# Função para classificar as amostras com base nos prefixos BSL, FLT, GC e VIV
def classify_sample_by_prefix(sample_name):
    if 'BSL' in sample_name:
        return 'Basal Control'
    elif 'FLT' in sample_name:
        return 'Flight'
    elif 'GC' in sample_name:
        return 'Ground Control'
    elif 'VIV' in sample_name:
        return 'Vivarium Control'
    else:
        return 'Unknown'

# Função para tratar valores múltiplos (ex: "313/397") separando-os
def split_fragment_size(value):
    if isinstance(value, str) and '/' in value:
        return list(map(int, value.split('/')))
    else:
        try:
            return [int(value)]
        except ValueError:
            return []

# Aplicar a classificação ao nome das amostras
df['Sample Classification'] = df['Sample Name'].apply(classify_sample_by_prefix)

# Tratar e separar os valores de "Fragment Size"
df['Fragment Size List'] = df['Parameter Value[Fragment Size]'].apply(split_fragment_size)

# Expandir as listas de fragmentos em várias linhas
df_expanded = df.explode('Fragment Size List').reset_index(drop=True)

# Converter a coluna de fragmentos para numérico
df_expanded['Fragment Size List'] = pd.to_numeric(df_expanded['Fragment Size List'])

# Agrupar os dados de "Fragment Size" por grupo de amostras
grouped_data = [df_expanded[df_expanded['Sample Classification'] == group]['Fragment Size List'].tolist() for group in df_expanded['Sample Classification'].unique()]

# Criar o gráfico boxplot com escala ajustada
plt.figure(figsize=(8,6))
plt.boxplot(grouped_data, labels=df_expanded['Sample Classification'].unique())

# Ajustar a escala do eixo Y para capturar a variação em torno dos tamanhos de fragmentos
plt.ylim(250, 400)  # Ajuste a escala conforme necessário

# Adicionar títulos e rótulos
plt.title('Boxplot of Fragment Size by Sample Group', fontsize=14)
plt.xlabel('Sample Group', fontsize=12)
plt.ylabel('Fragment Size (base pairs)', fontsize=12)

# Exibir o gráfico
plt.grid(True)
plt.show()


