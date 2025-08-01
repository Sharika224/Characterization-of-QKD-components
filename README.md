# Characterization of QKD Components

This repository contains simulation and analysis code for the **Characterization of Quantum Key Distribution (QKD) Components**, with a focus on the **Coherent One-Way (COW) protocol**, implemented as part of a research internship at **DRDO, Scientific Analysis Group (SAG)**.

## 🧠 Project Overview

The project aims to simulate and evaluate critical components of a QKD system using a combination of **Python-based modeling** and **OptiSystem-generated data**. The goal is to enhance the understanding of how quantum and classical signals behave across components and how these insights can be used to strengthen **quantum communication security**.

## 📌 Key Objectives

- Simulate the **Coherent One-Way (COW) QKD Protocol** using Python.
- Generate and analyze signal data for:
  - Intensity Modulator
  - Phase Modulator
  - Quantum Channel
  - Single Photon Detector
- Integrate **Quantum Random Number Generation (QRNG)** for secure key generation.
- Identify vulnerabilities (e.g., **Trojan Horse attacks**, **PNS attacks**) and propose countermeasures.
- Evaluate performance via **machine learning** and **data visualization**.
- Benchmark results against traditional QKD implementations.

## 🧪 Technologies & Tools

- **Python 3.10+**
- **Pandas**, **NumPy**, **Matplotlib**, **Scikit-learn**
- **OptiSystem** (for simulation circuit design and data generation)
- **Jupyter Notebook**

## 🗂️ Repository Structure
├── intensity_modulator.py # Analysis of intensity modulation output
├── phase_modulator.py # Phase modulator characterization
├── quantum_channel.py # Quantum channel transmission simulation
├── single_photon_detector.py # Performance analysis of SPD
├── qrng_generator.py # Quantum random number generation
├── utils/ # Helper functions and CSV parsers
├── data/ # OptiSystem-generated CSV files
└── visualization/ # Graph outputs and plots


## 📊 Sample Output

Graphs such as:
- Output Power vs Input Voltage (Intensity Modulator)
- Phase Shift vs Input Signal (Phase Modulator)
- Loss Characteristics of the Quantum Channel
- Detection Efficiency vs Signal Strength (SPD)

## 🛡️ Security Focus

The system was evaluated for robustness against:
- **Photon Number Splitting (PNS) attacks**
- **Trojan Horse attacks**
- **Quantum noise and signal degradation**

## 📄 Research Paper

A formal research paper was authored as part of this project. It includes:
- Theoretical foundation of QKD
- Component-level benchmarking
- Proposed enhancements for accuracy and security

(Contact for access if the paper is private.)










