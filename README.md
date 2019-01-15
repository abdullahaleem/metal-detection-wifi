# metal-detection-using-wifi

![Intro](https://cdn.pbrd.co/images/HWwE1cM5.jpg)

by Abdullah Aleem, Abuzar Ahmed and Saad Chugtai.

---

## Table of Contents

- [Introduction](#introduction)
- [Related Work](#related-work)
- [Hardware Design and Experimental Setup](#hardware-design)
- [Data Collection and Preprocessing](#data-collection)
- [Deep Learning Model](#deep-learning-model)
- [Experimental Results](#experimental-results)
- [Conclusion and Limitations](#conclusion)


## Introduction
Present metal detection systems for security purposes work on the principle of electromagnetic induction. They have a small coverage area and require dedicated expensive hardware. Also, ionizing radiations of X-Ray are harmful for the skin. Hence, there is a great need to having non-obtrusive metal detector which large coverage area.

The main idea is to detect metallic object on human by recording and processing the changes in CSI amplitude (Wi-Fi Signal). The setup was designed with transmitter node and two receiver nodes. The signal after processing was classifed used Deep learning.

## Related Work
A similar approach to Wi-Fi based metal detection has been proposed in Wi-Metal. However, the system in Wi-Metal requires that the target of interest is not moving. Thus, the robustness of the system while the subject is moving was not tested. As opposed to Wi-Metal, our proposed system has extended work where the targets are moving.

