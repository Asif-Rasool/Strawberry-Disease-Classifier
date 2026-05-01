---
title: "Data"
summary: "Public strawberry disease image sources used to build the project corpus."
---

Image data for our strawberry disease classifier were obtained from two publicly available, peer-reviewed repositories. The first source is the PlantVillage open-access image bank, which provides 1,565 annotated strawberry leaf images, 1,109 depicting angular leaf spot (*Diplocarpon earlianum*) and 456 healthy leaves, captured under natural illumination against uniform backgrounds and oriented so that the leaf apex points upward [1]. All PlantVillage images are distributed under a Creative Commons Attribution-ShareAlike 3.0 license and were originally collected in field and experimental-station settings using standard digital cameras.

The second source is the instance-segmentation dataset introduced by Afzaal *et al.*, comprising 2,500 strawberry images annotated with pixel-level masks for seven disease categories: angular leaf spot, anthracnose fruit rot, blossom blight, gray mold, leaf spot, powdery mildew fruit, and powdery mildew leaf [2]. Images were acquired in South Korean greenhouses under diverse lighting conditions and supplemented by roughly 20% online contributions. The dataset is partitioned into 1,450 training, 307 validation, and 743 test images at a native resolution of 419 x 419 px.

Prior to model training, all images were uniformly resized to 256 x 256 px, and pixel intensities were normalized to zero mean and unit variance. Disease labels were encoded as one-hot vectors for classification tasks, while the original pixel-level annotations were retained for segmentation objectives. By integrating the PlantVillage leaf dataset with the fine-grained instance-segmentation images, our corpus captures both broad phenotypic diversity and lesion-level detail, establishing a comprehensive foundation for developing a field-ready diagnostic tool.
