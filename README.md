#  Concrete Strength Predictor

A machine learning-powered web app to predict the **compressive strength of concrete** based on its ingredient composition — built with Flask, scikit-learn, and Bootstrap.

---

##  Project Overview

This project is part of a data science capstone where the goal is to assist civil engineers in estimating concrete strength **before physical testing**. By using this tool, users can input quantities of cement, water, slag, aggregates, and more, and receive a strength prediction in **megapascals (MPa)**.

---

##  Tech Stack

- **Python** (3.x)  
- **Flask** – lightweight backend web framework  
- **scikit-learn** – for building the Random Forest regression model  
- **joblib** – for model saving/loading  
- **HTML/CSS** with **Bootstrap 5.3** – for responsive UI  
- **pandas & numpy** – for data manipulation  

---

##  Features

-  Predict concrete compressive strength in real time  
-  Input key concrete mix ingredients (cement, slag, water, etc.)  
-  Responsive, mobile-friendly Bootstrap form UI  
-  Machine learning model trained on real construction data  
-  Clean structure, input validation, and error handling  

---

##  Folder Structure

```
concrete_strength_app/
├── app.py               # Flask app backend
├── model.pkl            # Trained machine learning model
├── train_model.py       # Script to train and save model
├── requirements.txt     # Dependencies list
├── .gitignore           # Files to exclude from Git
└── templates/
    └── index.html       # HTML frontend
```

---

##  How to Run the App Locally

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/concrete_strength_app.git
cd concrete_strength_app
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
venv\\Scripts\\activate     # For Windows
# Or: source venv/bin/activate for Linux/macOS
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Train the Model

Make sure you have `Concrete_Data.xls` in the root folder.

```bash
python train_model.py
```

### 5. Run the Flask App

```bash
python app.py
```

Then open your browser and visit:  
[http://localhost:5000](http://localhost:5000)

---

##  Sample Test Input

| Feature           | Value   |
|-------------------|---------|
| Cement            | 540     |
| Slag              | 0       |
| Fly Ash           | 0       |
| Water             | 162     |
| Superplasticizer  | 2.5     |
| Coarse Aggregate  | 1040    |
| Fine Aggregate    | 676     |
| Age               | 28      |

**Expected output:** ~72–82 MPa

---


---

##  Dataset Source

- [UCI Concrete Compressive Strength Dataset](https://archive.ics.uci.edu/ml/datasets/concrete+compressive+strength)  
- Provided by **Prof. I-Cheng Yeh**

---

##  Acknowledgments

- Built as a capstone project for **Moringa School**  
- Special thanks to teammates and reviewers  
- Developed and led by **Group 7 Dev Team** 

---

## 🪪 License

This project is intended for **educational** and **demonstration** purposes.  
You're welcome to fork, contribute, and expand it further!
