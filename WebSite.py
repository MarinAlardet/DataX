import streamlit as st

# Configuration globale
st.set_page_config(page_title="DataX", layout="wide")

# Gestion de la navigation via une variable de session
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"

# Fonction pour définir la page
def set_page(page):
    st.session_state.current_page = page

# Header avec navigation
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
            gap: 10px; /* Réduction de l'espacement entre les boutons */
            align-items: center;
            margin-left: 20px; /* Espace entre le logo et les boutons */
        }
        .nav button {
            background: none;
            border: none; /* Supprime le contour */
            color: white;
            font-weight: bold;
            font-size: 18px;
            cursor: pointer;
            padding: 5px 10px; /* Réduit la taille des boutons */
        }
        .nav button:hover {
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
        st.markdown('<div class="nav">', unsafe_allow_html=True)
        col_nav1, col_nav2, col_nav3, col_nav4 = st.columns([1, 1, 1, 1])
        with col_nav1:
            if st.button("Home"):
                set_page("home")
        with col_nav2:
            if st.button("Project"):
                set_page("project")
        with col_nav3:
            if st.button("Overview"):
                set_page("overview")
        with col_nav4:
            if st.button("Contact"):
                set_page("contact")
        st.markdown('</div>', unsafe_allow_html=True)

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
        </div>
        """,
        unsafe_allow_html=True,
    )

# Gestion de la navigation
render_header()

if st.session_state.current_page == "home":
    render_home()
elif st.session_state.current_page == "contact":
    render_contact()
elif st.session_state.current_page == "overview":
    render_overview()
elif st.session_state.current_page == "project":
    render_project()
