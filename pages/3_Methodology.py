import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Methodology",
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
  st.header("Methodology (draft)")
  # st.markdown("---")
  st.markdown("""

[*This is subject to change as we progress further into the project.*]  

We begin by building a base model in Phase 1 using publicly available, peer-reviewed strawberry disease datasets (for example, Afzaal et al. 2021). After collecting those existing image sets, we preprocess each photo by resizing it to a standard resolution, normalizing pixel values, and applying a set of data-augmentation techniques—random flips, rotations, color adjustments, and Gaussian blur—so that the Deep Learning network sees a wide variety of plant orientations and lighting conditions. We then initialize a Mask R-CNN (ResNet101 + FPN) with weights pre-trained on MS-COCO and fine-tune it on our curated dataset. During training, we monitor mean average precision (mAP) on a held-out validation split and adjust augmentation intensity and learning rate schedules as needed to meet our target of at least 80 percent mAP across disease classes.  

Once Phase 1 training achieves satisfactory performance, we export the best-performing checkpoint as a TensorFlow SavedModel. We package this SavedModel into a TensorFlow Serving container hosted on Google Cloud Run, exposing a simple REST endpoint for inference. A lightweight FastAPI service routes incoming image uploads to the TF Serving endpoint, parses its JSON response (class labels and mask coordinates), and returns this information to front-end clients. At the same time, we are developing a React-based web interface where users can drag and drop photos, view segmentation overlays directly in the browser, and download annotated images. Parallel to that, our React Native mobile application sends captured leaf photos to the same cloud endpoint and displays disease predictions on the farmer’s phone in near real time.  

Phase 2 focuses on local data collection and model refinement. Pending funding, we will form a small field team—consisting of agronomy students, extension agents, and a project coordinator—to visit strawberry farms in several Louisiana parishes (for instance, St. Mary, Iberia, and Terrebonne). Each annotator will photograph healthy foliage and visible disease symptoms at different growth stages and under varying daylight conditions. We plan to gather at least 5,000 in-field images that represent the state’s unique cultivars (such as ‘Camarosa,’ ‘Festival,’ and ‘Sweet Sensation’) and fluctuating weather patterns. Expert agronomists will review each image to confirm labels—healthy, early disease, or late disease—ensuring our dataset matches real-world conditions.  

With this locally sourced dataset in hand, we will resume training by initializing the Mask R-CNN with our Phase 1 weights and continuing the fine-tuning process. We expect that transfer learning on region-specific images, combined with a tailored augmentation pipeline (for example, adjusting brightness ranges to mimic Louisiana’s strong midday sun), will push our mAP target to 85 percent or higher on a held-out test set drawn from farms not used during training. After confirming performance in offline validation, we will export the refined model to TensorFlow Lite with post-training quantization, reducing its size to under 10 MB. Embedding this TFLite asset in the React Native application will enable fully offline, on-device inference on commodity smartphones—a critical feature for growers with limited or intermittent internet access.  

Throughout both phases, we will evaluate model quality not only with quantitative metrics (e.g., mAP at IoU ≥ 0.50) but also with visual inspections of predicted masks on real farm images. A small group of Louisiana growers and extension specialists will test the mobile app in their fields, providing feedback on interface clarity, prediction speed, and mask‐overlay accuracy. Based on this feedback, we will iterate on both the model and user interface: adjusting augmentation parameters, refining object segmentation thresholds, and streamlining the upload workflow to minimize latency. Each major change will be logged in our version control system, and we will document all architecture decisions, training settings, and deployment steps in a living project report. This report will form the backbone of our final manuscript for submission to a leading agricultural journal, ensuring full transparency of methods and enabling others to replicate or adapt our approach for their own crops and regions.  
""")
  
with col2:
  tech_arch = Image.open("TechArch2.png")
  st.image(tech_arch, caption="End-to-End Pipeline for Strawberry Disease Detection", use_container_width=True)

  st.markdown("""
We begin by gathering strawberry leaf images and applying a standardized preprocessing pipeline through TensorFlow’s `tf.data` API. This includes resizing, normalization, and data augmentation—such as flips, rotations, and color adjustments—to ensure the network sees diverse examples. Next, we train a Mask R-CNN model with a ResNet101 backbone and export the best checkpoint as a TensorFlow SavedModel.

For the web interface, this model runs in a TensorFlow Serving container behind FastAPI on Google Cloud Run, allowing our React frontend to upload photos and display segmentation overlays in real time. In parallel, we convert the SavedModel to a TensorFlow Lite format with post-training quantization and deploy it via a Google Cloud Function. The quantized model powers our React Native mobile app, enabling fully offline, on-device inference. This hybrid design balances scalability, low latency, and ease of use, giving growers immediate access to accurate disease detection through both web and mobile platforms.

""")
  
  tech_stack = Image.open("TechStack.png")
  st.image(
    tech_stack,
    caption="Technology Stack Overview",
    use_container_width=True
)

  st.markdown("""
In our project, we rely on TensorFlow for model development, leveraging the `tf.data` API and data augmentation methods to prepare inputs for a convolutional neural network. Once trained, the model runs in a TensorFlow Serving container behind a FastAPI endpoint on Google Cloud Run, powering our React-based web interface. To support offline, on-device inference, we apply post-training quantization and convert the network to TensorFlow Lite, which we invoke via a Google Cloud Function in our React Native mobile app. All components—training, serving, and front-end—are deployed on Google Cloud Platform, balancing scalability, low latency, and ease of use.

 
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
