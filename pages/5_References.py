import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="References",
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
  st.header("References")
  # st.markdown("---")
  st.markdown("""

1. Hughes, D. P.; Salathé, M. *An Open Access Repository of Images on Plant Health to Enable the Development of Mobile Disease Diagnostics*; PlantVillage.org, 2016; https://plantvillage.psu.edu/ (accessed July 15, 2025).  
2. PlantVillage. *Strawberry Information*; https://plantvillage.psu.edu/topics/strawberry/infos (accessed July 15, 2025).  
3. Afzaal, U.; Bhattarai, B.; Pandeya, Y. R.; Lee, J. An Instance Segmentation Model for Strawberry Diseases Based on Mask R-CNN. *Sensors* **2021**, *21*, 6565. https://doi.org/10.3390/s21196565.  

 
""")

 
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
