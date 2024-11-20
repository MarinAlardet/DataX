import streamlit as st

# Configuration globale
st.set_page_config(page_title="DataX", layout="wide")

# Gestion de la navigation via une variable de session
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"

def set_page(page):
    st.session_state.current_page = page

# Header avec le logo et navigation
def render_header():
    st.markdown(
        """
        <style>
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #333333;
            padding: 10px 20px;
        }
        .nav {
            display: flex;
            gap: 20px;
            align-items: center;
        }
        .nav a {
            cursor: pointer;
            color: white;
            font-weight: bold;
            font-size: 18px;
            text-decoration: none;
        }
        .nav a:hover {
            color: rgb(250, 173, 65);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("pictures/ternium_logo.png", width=100)
    with col2:
        st.markdown(
            """
            <div class="nav">
                <p style="cursor: pointer;" onclick="setPage('home')">Home</p>
                <p style="cursor: pointer;" onclick="setPage('project')">Project</p>
                <p style="cursor: pointer;" onclick="setPage('overview')">Overview</p>
                <p style="cursor: pointer;" onclick="setPage('contact')">Contact</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

# Contenu des pages
def render_home():
    st.image("pictures/Background.png", use_column_width=True)
    st.markdown(
        """
        <div style="text-align: center; margin-top: -400px;">
            <h1 style="font-size: 60px; color: white;">
                Let the <span style="color: rgb(250, 173, 65);">Data</span> lead the way.
            </h1>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style="
            background-color: black;
            color: white;
            text-align: center;
            padding: 20px;
            margin-top: 20px;
        ">
            <p>Email: <a href="mailto:DataX.contact@gmail.com" style="color: white;">DataX.contact@gmail.com</a></p>
            <p>© 2023 DataX All rights reserved.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_contact():
    st.markdown(
        """
        <div style="text-align: center; margin-top: 50px;">
            <h1 style="color: rgb(250, 173, 65);">Contact Page</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style="text-align: center; margin-top: 20px; color: white; background-color: #333333; padding: 20px;">
            <p>Email: <a href="mailto:DataX.contact@gmail.com" style="color: rgb(250, 173, 65);">DataX.contact@gmail.com</a></p>
            <p>Phone: +52 (55) 1234-5678</p>
            <p>Address: Av. Eugenio Garza Sada 2501 Sur, Tecnológico, 64700 Monterrey, N.L.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_overview():
    st.markdown(
        """
        <div style="text-align: center; margin-top: 50px;">
            <h1 style="color: white;">Overview Page</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.image("pictures/overview_ternium.png", caption="Key Performance Indicators (KPIs)", width=450)

def render_project():
    st.markdown(
        """
        <div style="text-align: center; margin-top: 50px;">
            <h1 style="color: white;">Ternium Project Overview</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image("pictures/ternium_team.png", use_column_width=True)
    with col2:
        st.image("pictures/datax.png", use_column_width=True)

    st.markdown(
        """
        <div style="color: white; text-align: center; margin-top: 20px;">
            <p>This project focuses on delivering a tailored solution for Ternium, concentrating on enhancing operational efficiency, streamlining processes, and incorporating innovative approaches.</p>
            <p>The report is structured into key components: the primary objectives, the CRISP-DM methodology used for implementation, proposed solutions, and actionable recommendations.</p>
            <h2>How we approached it?</h2>
            <p>We employed the CRISP-DM methodology, ensuring that every step was planned effectively to meet the deadlines and achieve the desired outcomes.</p>
            <h2>Key Phases of the Project</h2>
            <ul style="text-align: left; margin: auto; width: 50%;">
                <li><strong>Business Understanding:</strong> Defined Ternium's needs and challenges.</li>
                <li><strong>Data Understanding:</strong> Collected relevant data and performed exploratory analysis.</li>
                <li><strong>Data Preparation:</strong> Cleaned and transformed data for optimal model performance.</li>
                <li><strong>Modeling:</strong> Developed and tested models to identify key insights.</li>
                <li><strong>Evaluation:</strong> Assessed model performance and refined strategies.</li>
                <li><strong>Deployment:</strong> Implemented the final solution for real-world application.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Gestion de la navigation
query_params = st.experimental_get_query_params()
page = query_params.get("page", ["home"])[0]

render_header()

if st.session_state.current_page == "home":
    render_home()
elif st.session_state.current_page == "contact":
    render_contact()
elif st.session_state.current_page == "overview":
    render_overview()
elif st.session_state.current_page == "project":
    render_project()
