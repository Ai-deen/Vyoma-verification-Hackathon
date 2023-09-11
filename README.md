# Design Verification Hackathon

## Overview

This repository documents my participation in the Design Verification Hackathon, mentored by IIT Madras and IEEE Robotics. The hackathon provided a platform to work on real-world design verification challenges and collaborate with peers.
To provide a basic hands-on for design verification, which enhances practical verification knowledge. The verification challenge helps to understand the verification intent to detect bugs in designs, understand debugging and fix the buggy designs. It provides a practical exposure to real world design verification activities

The Hackathon aims to generate skilled manpower in the domain of Design Verification, which will strengthen the quality of designs being manufactured.


## Problem Statement
The Design Verification Hackathon consists of three levels, each with a unique challenge. In the first two levels, participants are tasked with finding bugs in provided code and writing test cases to filter out these bugs. The third level presents a different challenge - participants are required to intentionally introduce bugs into the code and then write test cases to identify and filter out these newly introduced bugs.

For the third level of the hackathon, I chose to work on a problem involving the PRESENT cipher. I encrypted a message using the cipher and intentionally made the code buggy. The challenge was to write test cases that could detect and filter out these bugs. The encrypted result of the buggy code could not be decrypted back to the original message.
## Tools Used

- [Vyoma's UpTickPro](https://vyomasystems.com)
- [CoCoTb](https://www.cocotb.org/)

## Test Scenarios

I successfully introduced two critical design bugs in the verification process:

Design Bug - 1: XOR symbols (^) were replaced with AND symbols (&), causing incorrect behavior.
Design Bug - 2: Similar XOR symbol replacement led to another issue.

## Verification Strategy

This repository captures my journey during the Design Verification Hackathon, highlighting the challenges faced and the steps taken to address them.

## Conclusion

Participating in this hackathon was a valuable experience, allowing me to enhance my verification skills and collaborate on a real-world design challenge.


