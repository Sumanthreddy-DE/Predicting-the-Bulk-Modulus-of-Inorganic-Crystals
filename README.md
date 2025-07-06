
# Predicting the Bulk Modulus of Inorganic Crystals

This repository focuses on predicting the bulk modulus of inorganic crystals using a variety of machine learning techniques. The project leverages a dataset sourced from Matminer, enhanced with the Magpie feature generator, and explores several regression and feature selection methods to identify the optimal predictive model.

## Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Features](#features)
- [Methods](#methods)
- [Usage](#usage)
- [Results](#results)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [References](#references)
- [License](#license)

---

## Overview

The goal of this project is to accurately predict the bulk modulus (a measure of material stiffness) of inorganic crystals. This is achieved by applying and comparing various machine learning models and feature selection techniques on a comprehensive dataset of material properties.

## Dataset

- **Source:** [Matminer](https://hackingmaterials.lbl.gov/matminer/)
- **Feature Generation:** [Magpie](https://github.com/hackingmaterials/magpie)
- **Files:**
  - `features-bulknew.csv`: Contains the generated features for each material.
  - `target-bulknew.csv`: Contains the target bulk modulus values.

## Features

- Principal Component Analysis (PCA) for dimensionality reduction
- Linear regression models: Least Squares, Ridge, Lasso
- Polynomial feature expansion
- Decision Tree Regressor
- Kernel Ridge Regression
- Feature selection: LARS, Recursive Feature Elimination (RFE)
- Model evaluation using standard performance metrics

## Methods

The following steps are implemented in the project:

1. **Data Preprocessing:** Loading, cleaning, and normalizing the dataset.
2. **Feature Engineering:** Applying PCA and polynomial expansion.
3. **Model Training:** Training various regression models.
4. **Feature Selection:** Using LARS and RFE to select the most relevant features.
5. **Model Evaluation:** Comparing models using metrics such as RMSE, MAE, and R².

## Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Sumanthreddy-DE/Predicting-the-Bulk-Modulus-of-Inorganic-Crystals.git
   cd Predicting-the-Bulk-Modulus-of-Inorganic-Crystals
   ```

2. **Install dependencies:**
   - Recommended: Use a virtual environment.
   - Install required packages (see [Requirements](#requirements)).

3. **Run the analysis:**
   - For PCA analysis:
     ```bash
     python pca.py
     ```
   - For model training and evaluation:
     ```bash
     python task2.py
     python task3.py
     ```
   - For plotting PCA spectrum:
     ```bash
     python pca_plot_spectrum.py
     ```

4. **Jupyter Notebook:**
   - Open `PCA.ipynb` for an interactive exploration.

## Results

The project compares multiple regression models and feature selection techniques to determine the best approach for predicting the bulk modulus. Results and plots are generated and saved during script execution. For detailed results, refer to the output files and notebook.

## Project Structure

```
.
├── Exercise-Instructions.pdf
├── features-bulknew.csv
├── target-bulknew.csv
├── get_data.py
├── pca.py
├── pca_plot_spectrum.py
├── PCA.ipynb
├── task2.py
├── task3.py
├── Task3-finished
└── README.md
```

## Requirements

- Python 3.7+
- numpy
- pandas
- scikit-learn
- matplotlib
- (Optional) jupyter

Install all dependencies using:
```bash
pip install -r requirements.txt
```
or install individually as needed.

## References

- [Matminer: Open-source toolkit for materials data mining](https://hackingmaterials.lbl.gov/matminer/)
- [Magpie: Materials-Agnostic Platform for Informatics and Exploration](https://github.com/hackingmaterials/magpie)
- [scikit-learn documentation](https://scikit-learn.org/)

## License

This project is for educational and research purposes. See [LICENSE](LICENSE) if provided.

---

Feel free to modify this README to better fit your specific workflow or to add more details about your results and findings!
