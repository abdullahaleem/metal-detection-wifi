# metal-detection-using-wifi

![Intro](https://cdn.pbrd.co/images/HWwQCzh.png)

by Abdullah Aleem, Abuzar Ahmed and Saad Chugtai.

---

## Table of Contents

- [Introduction](#introduction)
- [Related Work](#related-work)
- [Hardware Design and Experimental Setup](#hardware-design)
- [Data Collection](#data-collection)
- [Data Preprocessing](#data-preprocessing)
- [Deep Learning Model](#deep-learning-model)
- [Experimental Results](#experimental-results)
- [Conclusion and Limitations](#conclusion)


## Introduction
Present metal detection systems for security purposes work on the principle of electromagnetic induction. They have a small coverage area and require dedicated expensive hardware. Also, ionizing radiations of X-Ray are harmful for the skin. Hence, there is a great need to having non-obtrusive metal detector which large coverage area.

The basic idea behind the detection of metallic objects using Wi-Fi is that the presence of metal produces changes in the received signal. These changes can then be detected as well as differentiated from non-metal cases. In order to detect the changes in received signal, fine-grained CSI information can be utilized. A custom hardware was designed to collect CSI informatiion which after processing was classifed used Deep learning.

## Related Work
A similar approach to Wi-Fi based metal detection has been proposed in Wi-Metal. However, the system in Wi-Metal requires that the target of interest is not moving. Thus, the robustness of the system while the subject is moving was not tested. As opposed to Wi-Metal, our proposed system has extended work where the targets are moving.

## Hardware Design and Experimental Setup

![design](https://cdn.pbrd.co/images/HWwIlJf.png)

Transmitter is configured to Wi-Fi packets with 1 ms inter-packet delay.It is connected to a pyramidal horn antenna having 9 dBi gain and each receiver node is connected to three omni-directional antennas. Packets are received at receiving nodes after reflecting off the moving subject. At the receiver nodes, CSI is estimated and extracted for preprocessing. 

![setup](https://userscontent2.emaze.com/images/694313c7-4a1b-4238-afea-b3d7418ecc2d/316ece7fbf0d0e35baad1f07800c0903.jpg)


## Data Collection

Experiments were conducted in a basement (42 x 39 ft) and the receiver nodes are put 11.5 ft from the transmitter node. 
Duration of each experiment was 10 seconds involving a person approaching the transmitter node starting from a fixed position and stopping at another fixed position, 17 ft away.
In the first case, subjects approach the transmitter without holding any metallic sheet. In the second case, they carry a metallic aluminum sheet.
Data is collected over multiple days and four people with different heights and body masses performed the experiment.


**CSI Extraction** is done using a tool built by Asif Hanif on the Intel Wi-Fi Wireless Link 5300 802.11n MIMO radios, using a custom modified firmware and open source Linux wireless drivers. It provides channel state information for 30 sub-carrier groups. Each channel matrix entry is a complex number, with signed 8-bit resolution each for the real and imaginary parts. It specifies the gain and phase of the signal path between a single transmit-receive antenna pair.

** CSI with Static Target**

![statictargetCSI](https://res.cloudinary.com/emazecom/image/fetch/c_limit,a_ignore,w_440,h_280/https%3A%2F%2Fuserscontent2.emaze.com%2Fimages%2F694313c7-4a1b-4238-afea-b3d7418ecc2d%2F72fd1edee58e624798969bd18a8a63c9.jpg)

** CSI with moving Target**
Contrary to the static cases, target motion along a predefined trajectory also induces motion artifacts in received CSI. As a result, the previously differnce in CSI no longer remains.

![movingtargetCSI](https://res.cloudinary.com/emazecom/image/fetch/c_limit,a_ignore,w_360,h_240/https%3A%2F%2Fuserscontent2.emaze.com%2Fimages%2F694313c7-4a1b-4238-afea-b3d7418ecc2d%2Ff2a1ddbd0b954c29b647067e2b7d223a.jpg)

## Data Preprocessing

The CSI stream corresponding to each of the 6 antennas is truncated to accommodate for target motion by removing initial and final transients, choosing the middle 5000 recordings. 

A Gaussian moving average filter removes high frequency noise.

A non-overlapping window averages adjacent CSI recordings reducing 5000 recordings down to  250 for each CSI stream.

After concatenating CSI data from all antennae, we obtain a CSI matrix of size 250x180 which serves as an input for feature extraction.

![preprocessing](https://res.cloudinary.com/emazecom/image/fetch/c_limit,a_ignore,w_400,h_320/https%3A%2F%2Fuserscontent2.emaze.com%2Fimages%2F694313c7-4a1b-4238-afea-b3d7418ecc2d%2Fdcec83954c9e0b035fd2bd323684f6f8.JPG)



