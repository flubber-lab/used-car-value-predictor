# 🚗 AI-Powered Car Recommendation & Valuation App

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Podman](https://img.shields.io/badge/Podman-892CA0?style=for-the-badge&logo=podman&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white)
![Weights & Biases](https://img.shields.io/badge/Weights%20%26%20Biases-FFCC33?style=for-the-badge&logo=weightsandbiases&logoColor=black)

An **AI-powered Streamlit app** that predicts **used car prices** and recommends **cars based on your budget**. It uses **Machine Learning (ML)** for price prediction and an interactive chatbot for car recommendations.

---

## 🚀 **Features**
✅ **Predict Used Car Prices** based on specifications  
✅ **Find the Best Car** within your budget  
✅ **Interactive Chatbot** for personalized recommendations  
✅ **Deployed using Podman on AWS EC2**  
✅ **Weights & Biases for Experiment Tracking**  
✅ **Elegant UI** with a modern design  

---

## 💂️ **Project Structure**
```
/car-app
│── app.py               # Main Streamlit app
│── chatbot.py           # Chatbot logic
│── model.pkl            # Trained ML model
│── requirements.txt     # Python dependencies
│── Dockerfile           # Container setup
│── cars_data.csv        # Car dataset
│── wandb_integration.py # Weights & Biases tracking
│── README.md            # Project documentation
```

---

## 🛠 **Installation**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/car-app.git
cd car-app
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ Set Up Weights & Biases**
```bash
wandb login
```

### **4️⃣ Run the Streamlit App**
```bash
streamlit run app.py
```

---

## 🎯 **Docker & Podman Deployment**
### **1️⃣ Build the Image**
```bash
podman build -t streamlit-car-app .
```

### **2️⃣ Run the Container**
```bash
podman run -d -p 8501:8501 --name car-app streamlit-car-app
```

Now, open **`http://localhost:8501`** in your browser! 🎉  

---

## ☁️ **Deploy on AWS EC2**
### **1️⃣ Launch an AWS EC2 Instance**
- Choose **Ubuntu 22.04** as OS  
- Allow **ports 22 (SSH) and 8501 (Streamlit)**  

### **2️⃣ Install Podman**
```bash
sudo apt update -y
sudo apt install -y podman
```

### **3️⃣ Transfer Files to EC2**
```bash
scp -i your-key.pem -r car-app ubuntu@your-ec2-ip:~
ssh -i your-key.pem ubuntu@your-ec2-ip
```

### **4️⃣ Build & Run the Container on EC2**
```bash
cd car-app
podman build -t streamlit-car-app .
podman run -d -p 8501:8501 --name car-app streamlit-car-app
```

### **5️⃣ Access the App**
Open:
```
http://your-ec2-ip:8501
```

---

## 🤖 **Tech Stack**
- **Frontend**: Streamlit 🎨  
- **Machine Learning**: Scikit-Learn, Transformers 🤖  
- **Backend**: Python, Pandas, NumPy 🐖  
- **Experiment Tracking**: Weights & Biases 📊  
- **Deployment**: Podman, AWS EC2 ☁️  

---

## 📝 **License**
This project is **open-source** and available under the **MIT License**.

---

## 💬 **Contributing**
1. **Fork** the repository 🍔  
2. **Clone** your forked repo:  
   ```bash
   git clone https://github.com/flubber-lab/used-car-value-predictor.git
   ```
3. **Create a feature branch**:  
   ```bash
   git checkout -b new-feature
   ```
4. **Commit your changes** ✨  
   ```bash
   git commit -m "Added new feature"
   ```
5. **Push changes** 🚀  
   ```bash
   git push origin new-feature
   ```
6. **Create a Pull Request** ✔️  

---

## 🔥 **Star this repository** ⭐ if you found it useful!

