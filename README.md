# 📄 README - DOCX Grep-Like Search Tool (grep-docx.py)

## 📌 Overview
A powerful and user-friendly Python script that recursively searches all `.docx` files in your project directory (and subdirectories), looking for a specific keyword or phrase. Inspired by Linux's `grep` command, but tailored for Microsoft Word documents and enhanced with colored, structured terminal output.

---

## ⚙️ Features
- ✅ Recursive search in all subfolders.
- ✅ Matches partial words (e.g., "tation" matches "Presentation").
- ✅ Supports both **Arabic** and **English** content.
- ✅ Color-coded, structured, and readable terminal output using `colorama`.
- ✅ Shows line numbers and highlights the matched text.
- ✅ Prints full and relative paths for clarity.
- ✅ Stays in interactive mode until `\Exit` is typed.

---

## 🗂️ Folder Structure
Make sure to keep this script in a root folder. It automatically ignores:
- `grep-docx.py` itself
- `requirements.txt`
- Any environment folder like `myenv`

Your folder may look like:
```
project_root/
├── grep-docx.py
├── requirements.txt
├── myenv/           # Ignored
├── 06.16/
│   ├── Example.docx
│   └── Folder/
│       └── Example.docx
└── Folder/
    └── Candidate/Example.docx
```

---

## 🚀 How to Run
1. Activate your environment (optional but recommended).
2. Run the script in your terminal:
   ```bash
   python grep-docx.py
   ```
3. Type the word/phrase you want to search for. Use `\Exit` or `\exit` to quit.

---

## 🎨 Sample Output
```
📄 DOCX GREP-LIKE SEARCH TOOL
Type \Exit to quit at any time.

🔎 Enter search term (or \Exit to quit): Summary

====================================================================================================
🔍  FILE: Example.docx
📁  FULL PATH: /your/path/to/Example.docx
📂  RELATIVE PATH: resumes/Candidate/Example.docx
====================================================================================================
  • Line   5: Professional [31mSummary[0m:
----------------------------------------------------------------------------------------------------
```

---

## 📦 Requirements
Install dependencies using:
```bash
pip install -r requirements.txt
```

**requirements.txt**
```
python-docx
colorama
```

---

## 🧠 Tips
- For best Arabic support, use properly encoded `.docx` files.
- Works well on both Windows and Linux terminals.
- Avoid running inside extremely large directories unless needed.

---

## 📞 Support
If you encounter issues or need enhancements, feel free to fork or modify the script for your needs.

---

## 📜 License: >MIT<
This script is free to use, modify, and distribute.

Enjoy lightning-fast Word document searches! ⚡
