import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="WebApp",
    layout="wide",
    page_icon="athletic-logo-spirit-mark.svg",
    menu_items={
      'Get Help': None,
      'Report a bug': None,
      'About': None
    }
)

st.markdown(
    """
    <style>
    /* For general text blocks */
    .stMarkdown, .stMarkdown * {
        caret-color: transparent !important;   /* disables blinking text cursor */
        cursor: default !important;            /* normal arrow cursor */
    }

    /* For headings */
    h1, h2, h3, h4, h5, h6 {
        caret-color: transparent !important;
        cursor: default !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ── 3‑COL LAYOUT ──
col1, col2, col3 = st.columns([1, 6, 1])
with col2:
    GITHUB_URL = "https://github.com/Asif-Rasool/strawberry-Disease-classifier"
    COLAB_URL  = "https://colab.research.google.com"

    HEADER_ICONS = f"""
    <div style="float:right; margin:10px 0; display:flex; align-items:center; gap:8px;">
      <a href="{COLAB_URL}" target="_blank">
        <img src="https://colab.research.google.com/assets/colab-badge.svg"
            width="80"
            style="vertical-align:middle;" />
      </a>
      <span style="font-size:18px; line-height:1; color:#666;">|</span>
      <a href="{GITHUB_URL}" target="_blank">
        <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"
            width="30"
            style="vertical-align:middle;" />
      </a>
    </div>
    """

    st.markdown(HEADER_ICONS, unsafe_allow_html=True)

    


with col2:
  st.markdown("---")
  st.header("Web Application")
  # st.markdown("---")
  st.markdown("""

Our first first base model is now live at [smartfield.web.app](https://smartfield.web.app/).  
This application lets users upload plant leaf images and receive instant disease predictions powered by several deep learning models. A user can also generate concise health reports for their crops. Explore the web app today to see how AI can support disease management in the field.
              
Our base model mobile application is now ready for testing.

""")
  mobile_img = Image.open("MobileApp.png")
  st.image(
        mobile_img,
        caption="SmartField-LA Mobile App Home Screen",
        use_container_width=True
    )

 
####Footer####
  st.markdown("---")
    
st.markdown(
    """
    <style>
      /* hide default Streamlit footer/menu */
      #MainMenu {visibility: hidden;}
      footer {visibility: hidden;}

      /* custom footer styling without band */
      .custom-footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        text-align: right; 
        font-size: 0.8rem;
        color: black;  /* Set text color to black */
        padding: 8px 16px;
        background: transparent; 
      }
    </style>
    <div class="custom-footer">
      © Business Research Center, Southeastern Louisiana University
    </div>
    """,
    unsafe_allow_html=True,
)
