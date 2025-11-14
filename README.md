# CIS-260

### The Insurance Command Line AI Helper

This is a README file for the command line chatbot designed to assist **insurance professionals** with policy inquires, claims guidance and general insurance information. This is all powered by the OpenAI API.

## 10/15/2025 Comments

To run help.py:


### Install Dependencies: 
`pip install openai python-dotenv datetime`

### Create a .env file (in the same folder)
`OPENAI_API_KEY=sk-yourkeyhere`
Note: *(Never share your API key publicly!)*

### Running from command line

Windows: `python help.py`
Linux/MacOS: `python3 help.py`

## 10/28/2025 Comments

### You'll see:


========================================

       Your Insurance AI Helper
       
========================================


OPENAI_API_KEY loaded: True
Enter your role (e.g., 'claims adjuster', 'agent', 'customer support'):

### Ask an Insurance Question!
Ask the Insurance Bot (or type 'exit' to quit): What does liability insurance cover?

Bot: Liability insurance is designed to protect you financially in the event that you are held responsible for causing injury to someone else or damaging their property...

### Quick Commands: 

| Command          | Description                         |
| ---------------- | ----------------------------------- |
| `help`           | Show available quick commands       |
| `policies`       | List common insurance policy types  |
| `claims`         | Outline standard claim filing steps |
| `coverage`       | Summarize standard coverage         |
| `exit` or `quit` | End the session                     |

### Role Validation & Insurance-Only Guardrails:
To maintain accuracy and compliance, the help.py assistant now includes two layers of safety logic.

### Role Validation System
Before the chatbot starts, users must now identify themselves with a valid insurance role.

### [x] Accepted Examples 
The include but are not limited to:
-Agent
-Broker
-Underwriter
-Policy Administrator
-Risk Assesor


