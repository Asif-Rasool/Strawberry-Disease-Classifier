import streamlit as st



st.set_page_config(
    page_title="Objectives",
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

    


with col2:
  st.markdown("---")
  st.header("Objectives")
  # st.markdown("---")
  st.markdown("""

Our project has three objectives:  

First, we are currently working on a Deep Learning model and want to deploy it in an easy‐to‐use web page and smartphone app so that any grower can snap a picture in the field and immediately know whether a plant is healthy or showing disease. By putting this reliable tool in the hands of farmers, we help them spot issues sooner and avoid unnecessary losses.  

Second, we intend to gather and label images directly from Louisiana farms—working side by side with growers, extension agents, and crop specialists—so that our final model reflects the exact varieties, lighting conditions, and management practices found here. This local data will make the system more accurate and trustworthy under real‐world conditions.  

Finally, we will document our methods, results, and lessons learned from both phases in a detailed report and submit it to a leading agricultural journal. By sharing exactly how we built, tested, and refined the system, we hope others can replicate or adapt our approach to protect their own crops.
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
