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

## Data Preprocessing
 
**CSI Extraction**
CSI is extracted from CSI tool built on the Intel Wi-Fi Wireless Link 5300 802.11n MIMO radios, using a custom modified firmware and open source Linux wireless drivers. It provides channel state information for 30 sub-carrier groups.Each channel matrix entry is a complex number, with signed 8-bit resolution each for the real and imaginary parts. It specifies the gain and phase of the signal path between a single transmit-receive antenna pair.

an example of CSI with static target.

![statictargetCSI](https://res.cloudinary.com/emazecom/image/fetch/c_limit,a_ignore,w_440,h_280/https%3A%2F%2Fuserscontent2.emaze.com%2Fimages%2F694313c7-4a1b-4238-afea-b3d7418ecc2d%2F72fd1edee58e624798969bd18a8a63c9.jpg)

