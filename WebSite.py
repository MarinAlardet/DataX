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
                <a href="?page=home">HOME</a>
                <a href="?page=project">PROJECT</a>
                <a href="?page=overview">OVERVIEW</a>
                <a href="?page=contact">CONTACT</a>
            </div>
            """,
            unsafe_allow_html=True,
        )
