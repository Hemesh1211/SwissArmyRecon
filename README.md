# 🛠️ Swiss Army Recon Tool 🛡️

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Security-Pentesting-red?style=for-the-badge" alt="Security">
  <img src="https://img.shields.io/badge/Academic-Project-green?style=for-the-badge" alt="Academic">
</p>

---

## 📖 What is this tool? (The Simple Version)
Imagine you are a digital detective. Before a detective enters a building, they don't just run inside; they look at the map, check which windows are open, and see who is guarding the doors. 

**Swiss Army Recon Tool** does exactly that for websites! It's like a "Digital Binocular" that helps a security expert see how a website is set up so they can find and fix the "open windows" (vulnerabilities) before a bad hacker finds them.

### 🚀 What does it actually do?
1. **DNS Enumeration:** Like finding all the secret side-entrances to a building (Subdomains).
2. **Port Scanning:** Like walking around a house and checking every single door and window to see if any are unlocked (Open Ports).
3. **Banner Grabbing:** Like peeking through a window to see what brand of lock is on the door so you know how to open it (Service Versions).
4. **HTTP Audit:** Like checking if the building has a security alarm and a fence (Security Headers).

---

## 🛠️ How to Use This Tool (Step-by-Step)

If you have never used a tool like this before, don't worry! Just follow these simple steps:

### Step 1: Install Python 🐍
This tool is written in a language called **Python**. If you don't have it:
1. Go to [python.org](https://www.python.org/downloads/).
2. Download and install it. 
3. **IMPORTANT:** When installing, check the box that says **"Add Python to PATH"**.

### Step 2: Open your Terminal (The Black Box) 💻
You don't run this tool by double-clicking an icon. You use the "Command Line":
- **Windows:** Open "PowerShell" or "Command Prompt".
- **Mac/Linux:** Open "Terminal".

### Step 3: Go to the Project Folder 📁
Type this command to enter the folder where the tool is saved:
\\\ash
cd C:\Users\HP\SwissArmyRecon
\\\

### Step 4: Install the "Helper" Libraries 📦
The tool needs a few extra pieces of code (called libraries) to work. Run this command to download them automatically:
\\\ash
pip install -r requirements.txt
\\\

### Step 5: Start the Detective Work! 🔍
Now, run the tool and tell it which website to analyze using the -t (target) flag. 

**Example (using a safe testing site):**
\\\ash
python recon_tool.py -t scanme.nmap.org
\\\

---

## 🚦 Understanding the Results
- <span style="color:green">**Green [+]**</span> $\rightarrow$ **Success!** We found something (like an open door).
- <span style="color:red">**Red [-]**</span> $\rightarrow$ **Missing!** Something is missing (like a missing security lock).
- <span style="color:blue">**Blue [INFO]**</span> $\rightarrow$ Just a message telling you what the tool is doing.

---

## ⚠️ THE GOLDEN RULE (Read This!)
**Hacking without permission is illegal.** 🛑
This tool is like a powerful flashlight. Use it to learn and to help people, but **NEVER** use it on a website or server that you do not own. Only use it on "legal" testing sites or your own home network.

---
<p align="center">Developed as a 3rd Year Engineering Academic Project</p>
