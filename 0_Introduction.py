import streamlit as st



st.set_page_config(
    page_title="Intoduction",
    layout="wide",
    page_icon="athletic-logo-spirit-mark.svg",
    menu_items={
      'Get Help': None,
      'Report a bug': None,
      'About': None
    }
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

    st.title("SmartField LA: An End-to-End Deep Learning Framework for Real-Time Strawberry Disease Detection in Louisiana")
    st.markdown(
        """

        </div>
        """,
        unsafe_allow_html=True
    )
    with st.expander("About", expanded=False):

# Author Info
      st.markdown("""
Developed by Asif Rasool<sup>*</sup>, Ph.D. <a href="mailto:asif.rasool@southeastern.edu">📧</a> 

> Business Research Center, College of Business, Southeastern Louisiana University, 1514 Martens Drive, Hammond, LA 70401, USA  

""", unsafe_allow_html=True)

# Citation
      st.markdown("""
> Last update: 03 June, 2025

>(This model belongs to **Business Research Center, College of Business, Southeastern Louisiana University**)

>*To whom correspondence should be addressed
                    """)
with col2:
  st.markdown("---")
  st.header("Introduction")
  # st.markdown("---")
  st.markdown("""

Agricultural production in Louisiana relies heavily on specialty crops such as strawberries, which contribute substantially to both local economies and cultural heritage. However, strawberry yields are frequently threatened by foliar and fruit diseases that, if left undetected, can trigger cascading economic losses—particularly for small and mid‐sized operations. Early, accurate detection of these diseases enables targeted interventions, minimizes unnecessary pesticide use, and preserves yields. Building upon existing deep‐learning approaches in related crops, our project aims to develop an end‐to‐end plant–disease classification system that first focuses on strawberries, then extends to potatoes, tomatoes, and peppers. The system will consist of both a web application and a mobile application powered by a convolutional neural network (CNN) model capable of classifying foliar and fruit diseases. Ultimately, we intend to publish our methodology in a high‐impact journal, documenting model performance, deployment strategies, and real‐world validation in Louisiana farming contexts.  

Louisiana strawberry producers face multiple disease pressures—such as angular leaf spot, gray mold, and powdery mildew—which can reduce fruit quality and lead to outright crop losses if not managed promptly. According to USDA estimates, Louisiana ranks among the top five U.S. states in winter strawberry production; even small disease outbreaks can reduce returns by 15–30 percent for individual growers. Early‐season disease detection is therefore essential to reducing spray costs and avoiding sizable yield declines. Moreover, many Louisiana farms operate within tight profit margins: over 60 percent of strawberry acreage is produced by small farms (fewer than 50 acres), and direct‐market sales (e.g., farmers’ markets, on‐farm sales) amplify each percentage point of lost yield. Given these stakes, a reliable, accessible disease‐detection tool—one that a farmer can deploy via smartphone in the field—would directly benefit rural livelihoods and strengthen regional food security.  

From a technical standpoint, existing systems for strawberry disease detection have tended to rely on object‐detection models (e.g., Faster R‐CNN), which output bounding boxes around lesions. While effective, such approaches often require high‐resolution images and a consistent imaging protocol (e.g., fixed distance, fixed lighting), limitations that reduce their utility for growers scouting plants in natural, heterogeneous environments. In contrast, instance segmentation models (Mask R‐CNN and its variants) can generate pixel‐level masks for each lesion class, enabling fine‐grained localization under varied backgrounds. Afzaal et al. (2021) introduced a Mask R‐CNN approach for seven strawberry diseases, reporting a mean average precision of over 82 percent on a curated dataset of 2,500 images. Their work demonstrates that robust segmentation of strawberry lesions under complex greenhouse and field conditions is achievable given appropriate data-augmentation strategies and careful tuning of backbone networks (ResNet50/101). Drawing inspiration from that study, our project will adapt and extend these methods to Louisiana’s specific cultivars, environmental conditions, and disease pressures.
""")
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
