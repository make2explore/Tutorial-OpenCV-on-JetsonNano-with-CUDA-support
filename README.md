# Tutorial : Installation of OpenCV on JetsonNano with CUDA support

How to install OpenCV on JetsonNano with CUDA support
  
<img src="/images/OpenCV-Nano-Thumb.jpg" height="250" >
  
**OpenCV** (Open Source Computer Vision Library) is an open-source software library used for **computer vision**, **machine learning**, and **image processing**. It provides a wide range of tools and functionalities that allow developers to process, analyze, and manipulate images and videos, making it a popular choice for tasks like object detection, image recognition, and facial recognition. 
  
The **NVIDIA Jetson Nano** is a small, powerful computing platform designed for edge AI applications, such as robotics, IoT devices, and computer vision projects. Despite its compact size, it includes a GPU based on NVIDIA's Maxwell architecture, which supports CUDA, making it capable of performing GPU-accelerated computing tasks.  
  
A **CUDA accelerator** refers to the use of NVIDIA GPUs (Graphics Processing Units) as specialized hardware accelerators to perform computational tasks faster than a traditional CPU (Central Processing Unit). The term "accelerator" in this context highlights the GPU's role in speeding up specific types of computations, particularly those that can be parallelized.  
  
*Why would you install OpenCV on the Jetson Nano, when your operating system has already a version pre-installed?* 
==> The main reason is that the **shipped version has no CUDA support**. And after all, wasn't the CUDA accelerator the main reason why we bought the Jetson Nano in the first place.  
  

This tutorial is about How to Install OpenCV on Jetson Nano with CUDA support. We've discussed..  
- **What is NVIDIA CUDA ?** - Basic Introduction. 
- **What is OpenCV ?** - Basic Information 
- **How to increase SWAP memory of Jetson Nano** - Demo
- **Demo of How to Install OpenCV on Jetson Nano with CUDA support** 


------------------------------------------------------------------------------------------------------

📕 **YouTube Video Links**  

▶️ [Tutorial] How to Install OpenCV on Jetson Nano with CUDA support - 🔗 https://youtu.be/6DBhDK_JCEY  

-------------------------------------------------------------------------------------------------------
📒 **Important Links**  
 
🌐 PyTorch for Jetson - 🔗https://forums.developer.nvidia.com/t/pytorch-for-jetson/72048  
📗 Jetpack 4.6.1 🔗 https://developer.nvidia.com/embedded/jetpack-sdk-461  
▶️ [Tutorial] Getting Started With Jetson Nano 🔗 https://youtu.be/IVw1cyanRi0  

------------------------------------------------------------------------------------------------------

📜 Source Code, Circuit Diagrams and Documentation : 

🌐 GitHub Repository - 🔗 https://github.com/make2explore/Tutorial-OpenCV-on-JetsonNano-with-CUDA-support    
  
🌐 Hackster Blog - 🔗 https://www.hackster.io/make2explore  
  
🌐 Instructable Blog - 🔗 https://www.instructables.com/make2explore  
  
------------------------------------------------------------------------------------------  

Shield: [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
