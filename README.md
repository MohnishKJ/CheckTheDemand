# CheckTheDemand 📊

ML-based tourism demand prediction system that forecasts travel demand from booking and customer-related features.

## 🚀 What it does
- Takes booking-related travel details as input through a web interface
- Predicts tourism demand as High or Low
- Built for travel agencies, tourism planners, and hospitality services to plan resources based on demand trends

## ⚙️ How it works
- Preprocesses and engineers features from booking data
- Trains a Scikit-learn model and serializes it as a .pkl file
- Flask backend serves the model and handles predictions
- Application packaged with Docker for consistent deployment
- Deployed as a cloud web service on Render
- GitHub Actions enables automatic redeployment on every push

## 🏗 System Architecture
Dataset → Data Preprocessing → Feature Engineering → Model Training → Model Serialization (.pkl) → Flask Web App → Docker Container → Render Cloud Deployment → Automated CI/CD via GitHub Actions

## 🛠️ Tech Stack
**Frontend**
- HTML
- CSS
- JavaScript

**Backend**
- Python
- Flask

**Machine Learning**
- Scikit-learn
- Pandas
- NumPy
- Matplotlib

**Deployment**
- Render

**DevOps & MLOps**
- Docker
- GitHub Actions (CI/CD)

**Version Control**
- Git
- GitHub

## 👤 Owner & Author
Mohnish KJ
Final Year B.E CSE (AI & ML) Student | AI & ML Enthusiast
- LinkedIn: [www.linkedin.com/in/mohnishkj](https://www.linkedin.com/in/mohnishkj)
- Project: CheckTheDemand – Tourism Demand Prediction System

Built as an end-to-end ML application with a focus on real-world deployment, automation, and modern MLOps practices.
