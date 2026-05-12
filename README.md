# 🍽️ AI Restaurant Data Manager

> **A command-line data management system powered by IBM WatsonX AI to structure, browse, and manage restaurant records stored in JSON format.**

---

## 📌 Overview

The AI Restaurant Data Manager is a Python-based CLI tool that automates the management of structured restaurant data. It leverages **IBM WatsonX AI** to parse unstructured restaurant descriptions into a standardized JSON knowledge base — enabling consistent, machine-readable records that can be used in downstream AI and recommendation applications.

This project is part of the **IBM Generative AI / Agentic AI Professional Certificate** curriculum on Coursera (IBM Skills Network).

---

## 🎯 Key Features

- 📋 **Browse** all restaurant records in the dataset
- 🔍 **View** detailed restaurant cards by index
- ➕ **Add** new restaurants via natural language description (auto-structured via LLM)
- ✏️ **Edit** any field of an existing restaurant record
- 🗑️ **Delete** records with confirmation prompts
- 💾 **Auto-backup** — saves a `.bak` copy before every write operation
- 🔄 **Persistent storage** — all changes saved to JSON in real time

---

## 🗂️ Project Structure

```
ai-restaurant-data-manager/
│
├── restaurant_data_management.py       # Main CLI application
├── structured_restaurant_data.json     # Active restaurant dataset (JSON)
├── structured_restaurant_data.json.bak # Auto-generated backup file
├── requirements.txt                    # Python dependencies
└── README.md                           # Project documentation
```

---

## 📊 Data Schema

Each restaurant record in `structured_restaurant_data.json` follows this structure:

```json
{
    "name": "Mar de Cortez",
    "location": "Santa Monica",
    "cuisine": "Baja-style seafood",
    "rating": 4.2,
    "description": "A casual taqueria offering seafood dishes like snapper tacos and octopus ceviche.",
    "id": 1
}
```

| Field | Type | Description |
|---|---|---|
| `name` | string | Restaurant name |
| `location` | string | City or neighborhood |
| `cuisine` | string | Cuisine type or style |
| `rating` | float | Star rating (out of 5) |
| `description` | string | Short description of the restaurant |
| `id` | integer | Unique restaurant identifier |

---

## 🧠 Tech Stack

| Tool / Library | Purpose |
|---|---|
| **Python 3** | Core programming language |
| **IBM WatsonX AI** (`ibm_watsonx_ai==1.4.7`) | LLM-powered data structuring |
| **JSON** | Persistent data storage format |
| **Pandas** (`2.2.3`) | Data analysis and tabular operations |
| **NumPy** (`2.4.4`) | Numerical operations |
| **Tabulate** (`0.10.0`) | Clean terminal table formatting |
| **shutil / os** | File handling and backup management |

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.8+
- IBM WatsonX AI account with API credentials

### Install Dependencies

```bash
pip install -r requirements.txt
```

Or install the key packages directly:

```bash
pip install ibm_watsonx_ai==1.4.7 pandas==2.2.3 tabulate==0.10.0
```

### IBM WatsonX Credentials

Configure your credentials before running:

```python
from ibm_watsonx_ai import Credentials

credentials = Credentials(
    url="https://us-south.ml.cloud.ibm.com",
    api_key="YOUR_IBM_API_KEY"
)
```

---

## 🚀 How to Run

```bash
python restaurant_data_management.py
```

You will be presented with an interactive menu:

```
Records: 5
1. Browse
2. View
3. Add
4. Edit
5. Delete
6. Exit

Enter choice:
```

---

## 🖥️ Menu Options

### 1. Browse
Lists all restaurant names with their index numbers.

### 2. View
Enter an index number to display the full restaurant card:
```
--- Restaurant #0 ---
name: Mar de Cortez
location: Santa Monica
cuisine: Baja-style seafood
rating: 4.2
description: A casual taqueria offering seafood dishes...
id: 1
```

### 3. Add
Type `yes` to confirm, then enter a free-text description of the restaurant. The system creates a new structured record and assigns an auto-incremented ID (`100000 + current count`).

### 4. Edit
Type `yes` to confirm, then enter the index. You can update any field — leave blank to keep the existing value.

### 5. Delete
Type `yes` to confirm, then enter the index. The record is removed and the file is saved. A backup is created automatically before deletion.

### 6. Exit
Quits the application.

---

## 💾 Backup Mechanism

Every time data is saved (Add / Edit / Delete), the system automatically:
1. Copies the current `structured_restaurant_data.json` → `structured_restaurant_data.json.bak`
2. Writes the updated data to `structured_restaurant_data.json`

This ensures you can always recover the previous state if needed.

---

## 📚 Course Context

This project is a hands-on exercise from:
- **Course:** IBM Generative AI / Agentic AI Professional Certificate
- **Topic:** Structuring unstructured data with LLMs for AI-powered applications
- **Platform:** Coursera / IBM Skills Network

---

## 👤 Author

**Leela Issak Attota**
- 📍 Bengaluru, India
- 💼 AI/ML Enthusiast | Generative AI | Data Science
- 🔗 [GitHub](https://github.com/Leelaissakattaota)
- 🎓 IBM Data Science Professional Certificate | IBM Generative AI Professional Certificate | IBM RAG and Agentic AI Professional Certificate

---

## 📄 License

This project is built on IBM Skills Network lab materials © IBM Corporation. All rights reserved.
The implementation code is shared for educational and portfolio purposes.

---

*⭐ If you found this project helpful, consider giving it a star!*
