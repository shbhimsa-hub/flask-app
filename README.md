
# 🛠️ Infrastructure Engineer Take-Home Assignment

## **Flask App – Infrastructure Engineer Task**

This project is a simple Flask + PostgreSQL API that supports:

- ✅ **Insert/update** records via `/data`
- ✅ **Query** records via `/data`
- ✅ **Local development** with Docker Compose
- ✅ **AWS ECS deployment** using Terraform

---

## 🚀 **Getting Started (Locally)**

### **1. Clone the Repo**

```bash
git clone https://github.com/shbhimsa-hub/flask-app-template.git
cd flask-app-template
```

### **2. Run with Docker Compose**

```bash
docker-compose up --build
```

Once up, access:

- **Health Check:** http://localhost:5050/
- **API Endpoint:** http://localhost:5050/data

---

## 📦 **API Usage**

### **POST /data**

Insert or update a record:

```bash
curl -X POST http://localhost:5050/data \
  -H "Content-Type: application/json" \
  -d '{"key": "HomeTask", "value": "Shubham"}'
```

### **GET /data**

Returns all records:

```bash
curl http://localhost:5050/data
```

---

## ☁️ **Deployment to AWS**

> You must have **AWS CLI + Terraform installed** and an AWS account.
> ECS deployment pulls your app image from docker hub.
> Before deploying, make sure you are logged into Docker Hub — the ECS task will pull the image from there.

### **login to docker hub**
docker login

### **1. Set AWS Credentials**

```bash
aws configure
```

### **2. Deploy with Terraform**

```bash
cd terraform/
terraform init
terraform apply
```

---

## 🌐 **Access the Flask App (Public IP)**

If you're not using a Load Balancer, you can access the app via **ECS task public IP**:

### **Steps:**

1. Go to **AWS Console → ECS → Clusters → flask-cluster**
2. Click on the **“Tasks”** tab
3. Click the running **task ID**
4. Scroll to the **“Network”** section
5. Look for the **Public IPv4 address**

### **Test with curl:**

```bash
curl http://<public-ip>:5000/
```

```bash
curl -X POST http://<public-ip>:5000/data \
  -H "Content-Type: application/json" \
  -d '{"key": "deployed", "value": "true"}'
```

---

## 🧠 **Design Choices & Trade-offs**

### **1. Flask + SQLAlchemy**
- **Why:** Flask is lightweight and well-suited for simple REST APIs. SQLAlchemy provides clean model definitions and easy integration with PostgreSQL.
- **Trade-off:** Flask doesn’t enforce strong structure, so it’s up to the developer to maintain modularity and clarity.

---

### **2. Key-Value Upsert Model**
- **Why:** The `/data` endpoint uses a simple key–value structure with upsert logic for clarity and performance.
- **Trade-off:** Minimal schema validation; this assumes trusted input or upstream validation.

---

### **3. Docker & Docker Compose**
- **Why:** Local development should be fast, repeatable, and isolated. Docker Compose ensures the database and app run together easily.
- **Trade-off:** For multi-service or scaled setups, Kubernetes or ECS would be better—but for this task, Compose is sufficient.

---

### **4. AWS ECS with Fargate (via Terraform)**
- **Why:** ECS with Fargate allows fully serverless container deployment, and Terraform makes infrastructure reproducible and declarative.
- **Trade-off:** No Load Balancer was included by default to keep Terraform simpler. Public IP + port access was used instead. This works for testing but isn’t production-grade.

---
