import streamlit as st

st.set_page_config(
    page_title="Overview",
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
  st.header("Project Overview")
  # st.markdown("---")
  st.markdown("""

Our project aims to develop a fully integrated, deep‐learning–based system that farmers can access through both web and mobile interfaces. This system will identify common strawberry diseases—such as angular leaf spot, gray mold, and powdery mildew—directly from canopy images, enabling early intervention and more efficient management.  

At the heart of any data‐driven solution lies the data collection strategy. In our case, three main approaches are possible. First, we can rely on ready‐made, peer‐reviewed datasets, acquired from academic or commercial sources; this option allows rapid prototyping without the overhead of fieldwork. Second, we could assemble a team of annotators to visit Louisiana farms, photograph healthy and diseased strawberry plants, and label each image in consultation with extension agents or agri‐research specialists. Although this “in‐house” approach yields data closely tailored to local cultivars, lighting conditions, and cultural practices, it also demands considerable financial and logistical resources. Finally, a hybrid path combines the first two approaches: begin with publicly available datasets to train and validate an initial model, then—assuming successful grant applications—gather our own Louisiana‐specific images to refine model accuracy. In this way, Phase 1 leverages existing data to establish proof of concept, while Phase 2 emphasizes proprietary data collection and model enhancement once funding is secured.
""")
  st.subheader("Phase 1: Base Model Development Using Public Datasets")
  st.markdown(""" 
In Phase 1, we will establish a base model by training a Mask R-CNN architecture (ResNet101 + FPN) on well‐curated, peer‐reviewed strawberry‐disease datasets (e.g., Afzaal et al. 2021). By leveraging transfer learning from MS-COCO weights and applying a carefully designed augmentation pipeline—random flips, rotations, color adjustments, and blur—we anticipate achieving a mean average precision (mAP) of at least 80 percent across key disease classes. Once the network attains this performance threshold, we will export the best checkpoint as a TensorFlow SavedModel and serve it via TensorFlow Serving on Google Cloud Run. A lightweight FastAPI backend will handle incoming image requests and return both disease labels and pixel‐level mask overlays. Concurrently, a React-based web interface will enable users to upload photos, view segmentation results, and download annotated images. To extend functionality to growers in the field, we will develop a React Native mobile application that sends captured images to the cloud endpoint and displays predictions in near real-time. Throughout Phase 1, we will record model metrics, deployment considerations, and user-interface design notes to support an initial workshop presentation and guide the transition into Phase 2.

""")
  st.subheader("Phase 2: Local Data Collection and Model Refinement")
  st.markdown(""" 
Building on the Phase 1 base model, Phase 2 focuses on gathering and annotating a proprietary image set from Louisiana strawberry farms—contingent upon securing state, federal, or institutional funding. A dedicated team (e.g., students and extension specialists) will photograph healthy foliage and fruit, as well as early and late disease symptoms, across multiple parishes (such as St. Mary, Iberia, and Terrebonne). Expert supervision will ensure that labels reflect local cultivar variations (e.g., ‘Camarosa,’ ‘Festival,’ ‘Sweet Sensation’) and the region’s diverse lighting conditions. Our goal is to assemble at least 5,000 high-quality, in-field images that capture Louisiana’s unique environmental factors.

Once this proprietary dataset is in hand, we will fine-tune the Phase 1 Mask R-CNN weights using transfer learning. By adapting our augmentation strategy to local farm conditions—variable sunlight angles and canopy densities—we expect the refined model to surpass an mAP of 85 percent on a held-out test set drawn from farms not used in training. This enhanced model will then be re-deployed to the cloud. We will also conduct field trials in collaboration with local growers to validate model performance under real-world conditions, iterating on both the model and user interface based on feedback. Finally, we will prepare a comprehensive report detailing our methodology, results, and deployment strategies for publication in a high-impact journal, thereby contributing to the broader agricultural technology landscape.

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
