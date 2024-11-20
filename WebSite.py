import streamlit as st

# Configuration globale
st.set_page_config(page_title="DataX", layout="wide")

# Header de navigation
def render_header():
    st.markdown(
        """
        <style>
        .header-nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #333333;
            padding: 10px 20px;
        }
        .header-nav a {
            color: white;
            text-decoration: none;
            font-weight: bold;
            margin: 0 10px;
            font-size: 18px;
        }
        .header-nav a:hover {
            color: rgb(250, 173, 65);
        }
        .header-logo {
            height: 50px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div class="header-nav">
            <img src="pictures/ternium_logo.png" alt="Ternium Logo" class="header-logo">
            <div>
                <a href="?page=home">HOME</a>
                <a href="?page=contact">CONTACT</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Contenu des pages
def render_home():
    st.markdown(
        """
        <div style="
            background-image: url('pictures/Background.png');
            background-size: cover;
            background-position: center;
            min-height: 70vh;
            display: flex;
            align-items: center;
            justify-content: center;
        ">
            <h1 style="font-size: 60px; color: white; text-align: center;">
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
        <h1 style="
            text-align: center;
            color: rgb(250, 173, 65);
            margin-top: 50px;
        ">Contact Page</h1>
        """
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

    st.markdown(
        """
        <div style="
            background-color: black;
            color: white;
            text-align: center;
            padding: 20px;
            margin-top: 20px;
        ">
            <p>Contact: DataX | Email: DataX.contact@gmail.com</p>
            <p>© 2023 DataX All rights reserved.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Gestion de la navigation
query_params = st.experimental_get_query_params()
page = query_params.get("page", ["home"])[0]

render_header()

if page == "contact":
    render_contact()
else:
    render_home()
