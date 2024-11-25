import streamlit as st
import pandas as pd

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
            gap: 8px;  /* Réduit l'espace entre les boutons */
            align-items: center;
        }
        .nav button {
            background: none;
            border: none; /* Supprime le contour des boutons */
            color: white;
            font-weight: bold;
            font-size: 18px;
            cursor: pointer;
            padding: 5px 10px;
        }
        .nav button:hover {
            color: rgb(250, 173, 65);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([1, 2]) 
    with col1:
        st.image("pictures/ternium_logo.png", width=200)
    with col2:
        st.markdown('<div class="nav">', unsafe_allow_html=True)
        col_nav1, col_nav2, col_nav3, col_nav4, col_nav5 = st.columns([1, 1, 1, 1, 1])
        with col_nav1:
            if st.button("home"):
                set_page("home")
        with col_nav2:
            if st.button("Analysis"):
                set_page("analysis")
        with col_nav3:
            if st.button("Project"):
                set_page("project")
        with col_nav4:
            if st.button("Overview"):
                set_page("overview")
        with col_nav5:
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

    st.markdown(
        """
        <iframe 
            src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d14289.999992074987!2d-99.1872339!3d25.7040476!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8662b175b8b54865%3A0x3fa0da31591b79ee!2sAv.%20Eugenio%20Garza%20Sada%202501%20Sur%2C%20Tecnol%C3%B3gico%2C%2064700%20Monterrey%2C%20N.L.%2C%20Mexico!5e0!3m2!1sen!2sus!4v1698676195356!5m2!1sen!2sus"
            width="100%" height="300" style="border:0;" allowfullscreen="" loading="lazy">
        </iframe>
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
    st.image("pictures/overview_ternium.png", caption="Key Performance Indicators (KPIs)", width=1200, align="center")

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
def render_analysis():
    st.markdown(
        """
        <div style="text-align: center; margin-top: 50px;">
            <h1 style="color: rgb(250, 173, 65);">Analysis of Defects and Delays</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div style="color: white; text-align: left; margin: 20px;">
            <h2>Key Insights</h2>
            <p>The analysis identified recurring bottlenecks and opportunities for optimization:</p>
            <ul>
                <li><strong>Maintenance Optimization:</strong> Predictive and optimized scheduled maintenance could reduce long delays.</li>
                <li><strong>Process Improvements:</strong> Workflow changes in the finishing mill, particularly around roller changes, could enhance efficiency.</li>
                <li><strong>Addressing Space Constraints:</strong> Optimizing evacuation spaces in the slab yard and cooling bay could minimize congestion.</li>
                <li><strong>Operational Coordination:</strong> Enhancing workflows across departments to mitigate delays caused by non-operational factors.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style="color: white; text-align: center; margin: 20px;">
            <h2>Distribution of Delay Durations</h2>
            <p>Delays are heavily skewed, with most durations below 10 minutes. However, long-duration delays (>30 minutes) are significant disruptions:</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style="color: white; text-align: center; margin: 20px;">
            <h2>Key Contributors to Long Delays</h2>
            <p>Mechanical failures and scheduled maintenance are leading causes of production delays:</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    st.markdown(
        """
        <div style="text-align: left; color: white; margin: 20px;">
            <h3>Recommendations</h3>
            <ul>
                <li>Implement <strong>predictive maintenance</strong> for critical equipment.</li>
                <li>Optimize <strong>space management</strong> in evacuation areas.</li>
                <li>Focus on <strong>finishing mill workflow enhancements</strong>.</li>
            </ul>
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
elif st.session_state.current_page == "analysis":
    render_analysis()

