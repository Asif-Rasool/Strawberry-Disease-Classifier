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

# Disable text cursor and set default cursor for all Markdown and headings
st.markdown(
    """
    <style>
      .stMarkdown, .stMarkdown * {
          caret-color: transparent !important;
          cursor: default !important;
      }
      h1, h2, h3, h4, h5, h6 {
          caret-color: transparent !important;
          cursor: default !important;
      }
    </style>
    """,
    unsafe_allow_html=True
)

# ── HEADER ICONS ──
col1, col2, col3 = st.columns([1, 6, 1])
with col2:
    GITHUB_URL = "https://github.com/Asif-Rasool/strawberry-Disease-classifier"
    COLAB_URL  = "https://colab.research.google.com"
    header_icons = f"""
    <div style="float:right; margin:10px 0; display:flex; align-items:center; gap:8px;">
      <a href="{COLAB_URL}" target="_blank">
        <img src="https://colab.research.google.com/assets/colab-badge.svg"
             width="80" style="vertical-align:middle;" />
      </a>
      <span style="font-size:18px; line-height:1; color:#666;">|</span>
      <a href="{GITHUB_URL}" target="_blank">
        <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"
             width="30" style="vertical-align:middle;" />
      </a>
    </div>
    """
    st.markdown(header_icons, unsafe_allow_html=True)

# ── WEB AND MOBILE SECTION ──
with col2:
  st.markdown("---")
  st.header("Web and Mobile Application")
  # st.markdown("---")
  st.markdown("""

Our first base model is now live at [smartfield-la.web.app](https://smartfield-la.web.app/).
                
This application lets users upload plant leaf images and receive instant disease predictions powered by several deep learning models. A user can also generate concise health reports for their crops. Explore the web app today to see how AI can support disease management in the field.
              
Our base model application is now ready for testing. To try it, download the **Expo Go** app from the App Store or Google Play and scan the QR code below.

""")
  
# Create a 3-column layout
left, center, right = st.columns([2, 2, 1])
with center:
    mobile_img = Image.open("MobileApp.png")
    st.image(
        mobile_img,
        caption="SmartField-LA Mobile App Home Screen",
        use_container_width=False,
        width=200
    )

# ── QR CODE CENTERED ──
left, center, right = st.columns([2, 2, 1])
with center:
    qr_img = Image.open("QR.png")
    st.image(
        qr_img,
        caption="Scan to Open SmartField-LA in Expo Go",
        use_container_width=False,
        width=200
    )

# ── FOOTER ──
st.markdown("---")
st.markdown(
    """
    <style>
      /* Hide default Streamlit menu/footer */
      #MainMenu {visibility: hidden;}
      footer {visibility: hidden;}

      /* Custom footer */
      .custom-footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        text-align: right;
        font-size: 0.8rem;
        color: black;
        padding: 8px 16px;
        background: transparent;
      }
    </style>
    <div class="custom-footer">
      © Business Research Center, Southeastern Louisiana University
    </div>
    """,
    unsafe_allow_html=True
)
