# Metal Detection with Wi-Fi using Deep learning

![Intro](https://cdn.pbrd.co/images/HWwQCzh.png)

by Abdullah Aleem, Abuzar Ahmed and Saad Chugtai.

---

## Table of Contents

- [Introduction](#introduction)
- [Related Work](#related-work)
- [Hardware Design and Experimental Setup](#hardware-design-and-experimental-setup)
- [Data Collection](#data-collection)
- [Data Preprocessing](#data-preprocessing)
- [Model Used](#model-used)
- [Experimental Results](#experimental-results)
- [Conclusion and Limitations](#conclusion-and-limitations)


## Introduction
Present metal detection systems for security purposes work on the principle of electromagnetic induction. They have a small coverage area and require dedicated expensive hardware. Also, ionizing radiations of X-Ray are harmful for the skin. Hence, there is a need for a non-obtrusive metal detector which large coverage area.

The basic idea behind the detection of metallic objects using Wi-Fi is that the presence of metal produces changes in the received signal. These changes can then be detected as well as differentiated from non-metal cases. In order to detect the changes in received signal, fine-grained CSI information can be utilized. A custom hardware was designed to collect CSI information which was then processed and classifed used Deep learning.

## Related Work
A similar approach to Wi-Fi based metal detection has been proposed in Wi-Metal. However, the system in Wi-Metal requires that the target of interest is not moving. Thus, the robustness of the system while the subject is moving was not tested. As opposed to Wi-Metal, our proposed system has extended work where the targets are moving.

## Hardware Design and Experimental Setup

![design](https://cdn.pbrd.co/images/HWwIlJf.png)

Transmitter is configured to send Wi-Fi packets with 1 ms inter-packet delay.It is connected to a pyramidal horn antenna having 9 dBi gain and each receiver node is connected to three omni-directional antennas. Packets are received at receiving nodes after reflecting off the moving subject. At the receiver nodes, CSI is estimated and extracted for preprocessing. 

![setup](https://userscontent2.emaze.com/images/694313c7-4a1b-4238-afea-b3d7418ecc2d/316ece7fbf0d0e35baad1f07800c0903.jpg)


## Data Collection

- We conducted 460 experiments with minimal differences in experimental setup for four people, having different heights and body masses, with and without metal sheet. The walking pace and angles for all subjects were kept almost the same with natural variations only.
- Experiments were conducted in a basement (42 x 39 ft) and the receiver nodes are put 11.5 ft from the transmitter node.
- Duration of each experiment was 10 seconds involving a person approaching the transmitter node starting from a fixed position and stopping at another fixed position, 17 ft away.


**CSI Extraction** was done using a tool built by Asif Hanif on the Intel Wi-Fi Wireless Link 5300 802.11n MIMO radios, using a custom modified firmware and open source Linux wireless drivers. It provides channel state information for 30 sub-carrier groups. Each channel matrix entry is a complex number, with signed 8-bit resolution each for the real and imaginary parts. It specifies the gain and phase of the signal path between a single transmit-receive antenna pair.

**CSI with Static Target**

![statictargetCSI](https://res.cloudinary.com/emazecom/image/fetch/c_limit,a_ignore,w_440,h_280/https%3A%2F%2Fuserscontent2.emaze.com%2Fimages%2F694313c7-4a1b-4238-afea-b3d7418ecc2d%2F72fd1edee58e624798969bd18a8a63c9.jpg)

**CSI with moving Target**

![movingtargetCSI](https://cdn.pbrd.co/images/HWx61Qt.png)

Contrary to the static cases, target motion along a predefined trajectory also induces motion artifacts in received CSI. As a result, the previously differnce in CSI no longer remains.

## Data Preprocessing

- The CSI stream corresponding to each of the 6 antennas is truncated to accommodate for target motion by removing initial and final transients, choosing the middle 5000 recordings. 
- A Gaussian moving average filter removes high frequency noise.
- A non-overlapping window averages adjacent CSI recordings reducing 5000 recordings down to  250 for each CSI stream.
- After concatenating CSI data from all antennae, we obtain a CSI matrix of size 250x180 which serves as an input for feature extraction.

![preprocessing](https://res.cloudinary.com/emazecom/image/fetch/c_limit,a_ignore,w_400,h_320/https%3A%2F%2Fuserscontent2.emaze.com%2Fimages%2F694313c7-4a1b-4238-afea-b3d7418ecc2d%2Fdcec83954c9e0b035fd2bd323684f6f8.JPG)


## Model Used

Instead of manually identifying a better set of features, we resort to utilizing a convolutional neural network (given below) for classification purposes.

![model](https://res.cloudinary.com/emazecom/image/fetch/c_limit,a_ignore,w_720,h_200/https%3A%2F%2Fuserscontent2.emaze.com%2Fimages%2F694313c7-4a1b-4238-afea-b3d7418ecc2d%2Fb2d42aefe6b8261b77729da892905895.jpg)

![parameters](https://cdn.pbrd.co/images/HWx6SJC.png)


## Experimental Results

**Confusion Matrix and Comparison**
![confusionmatrix](https://cdn.pbrd.co/images/HWxdkSx.png)

**K-fold Cross Validation**
![kfoldresults](https://cdn.pbrd.co/images/HWxe1jK.png)

**Model Accuracy and Loss**
![accuracyandloss](https://cdn.pbrd.co/images/HWxeC6W.png)


## Conclusion and Limitations

**Conclusion**

- We have explored the use of commodity WiFi radios for developing a non-obtrusive system for concealed metallic object detection.
- By collecting data in an experimental setup, we have demonstrated the effectiveness of the framework with a deep CNN classifier achieving an average accuracy of **86.44%**. 
- The robustness of the proposed system has been increased by deploying a number of receivers which simultaneously collect the reflected energy from the metallic object. 
- Our system has the potential to significantly increase the coverage area without requiring subjects to pass through a narrowly localized path.


**Limitations**

- All the experiments have been conducted with a single metal sheet. Also, during each experiment, there was only one target human either static or in motion. We intend to expand this to work for multiple persons.
- The system still needs to be tested and validated against variations and uncertainties such as walking speed and angle before a working deployable prototype is ready. 
- Nevertheless, the preliminary results reported above, point to the promise of using Wi-Fi radios for non-obtrusive metal detection systems.



## Our work has resulted in the submission of a research paper to 2018 IEEE Global Communications Conference.

