# 🏅 Olympic Athletes Data Analysis

### 📊 Big Data Assignment | MongoDB, PyMongo & MapReduce (1980–2020)

---

## 📘 Overview

This repository contains source code, output files, and documentation for a **Big Data analysis assignment** focused on **medal-winning Olympic athletes** from the **Summer Olympics (1980–2020)**.

Key technologies used:

* 🐍 **Python (mrjob for MapReduce)**
* 🍃 **MongoDB + PyMongo**
* 📈 **MapReduce processing**
* 📂 Dataset: *Olympic historical dataset* (not included)

The goal is to extract, transform, and analyze athlete, country, and event data to generate insightful summaries.

---

## 🗂️ Project Structure

### 🧠 **Source Code**

| Script       | Description                                                                                                   |
| ------------ | ------------------------------------------------------------------------------------------------------------- |
| `task1_1.py` | Extracts medal-winning athlete data from MongoDB and writes to `athletes.txt`                                 |
| `task1_2.py` | MapReduce job to sort `athletes.txt` by **Athlete ID** → Output: `output1_2.txt`                              |
| `task2_1.py` | MapReduce job to count medals by **athlete and type**, identifying top 3 athletes per medal → `output2_1.txt` |
| `task2_2.py` | MapReduce job to count **medals by country**, identifying top 3 by **Gold medals** → `output2_2.txt`          |
| `task2_3.py` | MapReduce job to group data by **decade, country, event**, finding top 3 events per decade → `output2_3.txt`  |

---

### 📄 **Output Files**

| File            | Description                                                                   |
| --------------- | ----------------------------------------------------------------------------- |
| `athletes.txt`  | Raw extracted data: `athlete ID, country, year, event, medal`                 |
| `output1_2.txt` | Sorted athletes by athlete ID                                                 |
| `output2_1.txt` | 🥇🥈🥉 Top 3 athletes per medal type                                          |
| `output2_2.txt` | 🌍 Top 3 countries by **Gold medals** (e.g., USA: 1324, CHN: 402, GER: 358)   |
| `output2_3.txt` | 📆 Top 3 events per decade (e.g., 2000–2009: CUB Baseball Men with 72 medals) |

---

### 📊 **Documentation**

* `FlowChart_Task3.pdf`: Visual flowcharts outlining the MapReduce logic for:

  * Task 2.1 (Athlete Medal Count)
  * Task 2.2 (Country Medal Count)
  * Task 2.3 (Top Events per Decade)

---

## ⚙️ Prerequisites

Ensure the following tools and libraries are installed:

```bash
pip install pymongo mrjob
```

**Other requirements:**

* MongoDB (running locally or in cloud)
* Olympic dataset loaded in MongoDB
* Optional: [Studio 3T](https://studio3t.com/) for MongoDB UI access

---

## ▶️ How to Run the Project

### 1. 🔧 Setup MongoDB

* Import the dataset (`Olympie_Athletes.zip`) into a MongoDB collection
* Adjust the **MongoDB connection string** in `task1_1.py` if needed

---

### 2. 🛠️ Execute Tasks

#### Task 1.1: Extract Athlete Data

```bash
python task1_1.py
```

→ Generates `athletes.txt`

---

#### Task 1.2: Sort by Athlete ID

```bash
python task1_2.py athletes.txt > output1_2.txt
```

---

#### Task 2.1: Top Athletes per Medal Type

```bash
python task2_1.py athletes.txt > output2_1.txt
```

---

#### Task 2.2: Top Countries by Gold Medals

```bash
python task2_2.py athletes.txt > output2_2.txt
```

---

#### Task 2.3: Top Events per Decade

```bash
python task2_3.py athletes.txt > output2_3.txt
```

---

### 3. 📄 View Flowcharts

Open `FlowChart_Task3.pdf` to visualize MapReduce processes for tasks 2.1–2.3.

---

## 📌 Notes

* The dataset includes **Summer Olympics** data from **1980 to 2020**
* Output files are formatted as **comma-separated values (CSV-style)**
* All outputs reflect only **medal-winning athletes**
* Dataset file is assumed to be provided by your instructor or authorized source

---

## 🧾 License

This project is for **educational purposes only**.
It is **not licensed for commercial use**.
All Olympic data rights remain with the original data source or course provider.

---

## 📬 Contact

**Hassan Mohammad**
📧 [hassan\_md@live.com](mailto:hassan_md@live.com)
🔗 [LinkedIn: hassan1207](https://www.linkedin.com/in/hassan1207/)

