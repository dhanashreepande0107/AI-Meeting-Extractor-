# 🤖 AI Meeting Action-Item Extractor

## 📌 Project Overview
AI Meeting Action-Item Extractor is a simple AI-powered web application that converts meeting transcripts into structured action items. The system automatically identifies tasks, owners, deadlines, status, and confidence scores from meeting discussions.

## 🚀 Features
- Upload meeting transcript (.txt file)
- Paste transcript manually
- Extract action items automatically
- Identify task owner
- Detect deadlines
- Assign confidence score
- Display results in a table
- Download results as CSV file
- Simple and user-friendly interface

## 🛠️ Technologies Used
- Python
- Streamlit
- Pandas
- Regular Expressions (Regex)

## 📂 Project Structure

AI-Meeting-Extractor/
│
├── app.py
├── extractor.py
├── requirements.txt
└── README.md

## ⚙️ Installation

1. Clone the repository

```bash
git clone https://github.com/your-username/AI-Meeting-Extractor.git
```

2. Move into the project folder

```bash
cd AI-Meeting-Extractor
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Project

```bash
py -m streamlit run app.py
```

## 📝 Sample Input

Manager: Rahul will submit project report by 10/10/2026.

Team Lead: Priya will prepare presentation by 12/10/2026.

Developer: Amit should fix login bug by 15/10/2026.

## 📊 Sample Output

| Task | Owner | Deadline | Status | Confidence |
|------|--------|----------|----------|------------|
| submit project report | Rahul | 10/10/2026 | Pending | 90% |
| prepare presentation | Priya | 12/10/2026 | Pending | 90% |
| fix login bug | Amit | 15/10/2026 | Pending | 90% |

## 🎯 Future Enhancements
- NLP-based extraction using Transformers
- Support for PDF and DOCX files
- Real-time meeting transcription
- Dashboard analytics
- Email notifications for pending tasks

## 👨‍💻 Author

Dhanashree Vijay Pande

BCA Student | AI & Web Development Enthusiast