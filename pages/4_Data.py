import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Data",
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
  st.header("Data")
  # st.markdown("---")
  st.markdown("""

Image data for our strawberry disease classifier were obtained from two publicly available, peer-reviewed repositories. The first source is the PlantVillage open-access image bank, which provides 1,565 annotated strawberry leaf images—1,109 depicting angular leaf spot (*Diplocarpon earlianum*) and 456 healthy leaves—captured under natural illumination against uniform backgrounds and oriented so that the leaf apex points upward [1]. All PlantVillage images are distributed under a Creative Commons Attribution-ShareAlike 3.0 license and were originally collected in field and experimental-station settings using standard digital cameras.

The second source is the instance-segmentation dataset introduced by Afzaal *et al.*, comprising 2,500 strawberry images annotated with pixel-level masks for seven disease categories (angular leaf spot, anthracnose fruit rot, blossom blight, gray mold, leaf spot, powdery mildew fruit, and powdery mildew leaf) [2]. Images were acquired in South Korean greenhouses under diverse lighting conditions and supplemented by roughly 20% online contributions. The dataset is partitioned into 1,450 training, 307 validation, and 743 test images at a native resolution of 419 × 419 px.

Prior to model training, all images were uniformly resized to 256 × 256 px, and pixel intensities were normalized to zero mean and unit variance. Disease labels were encoded as one-hot vectors for classification tasks, while the original pixel-level annotations were retained for segmentation objectives. By integrating the PlantVillage leaf dataset with the fine-grained instance-segmentation images, our corpus captures both broad phenotypic diversity and lesion-level detail, establishing a comprehensive foundation for developing a field-ready diagnostic tool.

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
