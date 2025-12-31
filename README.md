# Smart Fee – Smart, Simple, Seamless
<img width="1024" height="1024" alt="whatsapp" src="https://github.com/user-attachments/assets/2145abbf-9376-4189-80d9-59729ad309a6" />

**Smart Fee** is a professional, automated communication system designed for educational institutions to manage fee-related notifications via WhatsApp.  
Developed with **Python** and **Streamlit**, it provides a user-friendly interface for sending personalized reminders and acknowledgments to parents, helping schools maintain efficient and transparent communication.

---

## Project Overview

Smart Fee allows school administrators to upload a structured Excel sheet containing student contact details and fee status.  
The system automatically sends personalized WhatsApp messages for paid and pending fees, reducing manual workload and ensuring timely communication.

---

## Key Features

- Upload Excel files with student phone numbers and fee status  
- Automatically send WhatsApp messages for fee confirmations or reminders  
- Detect *PAID* vs *UNPAID* status and send appropriate messages  
- Clean, intuitive web interface powered by **Streamlit**  
- Operates entirely locally to ensure data privacy  

---

## Technology Stack

| Component       | Purpose                          |
|-----------------|---------------------------------|
| Python 3.8+     | Core programming language       |
| Streamlit       | Web application interface       |
| PyWhatKit       | WhatsApp message automation     |
| PyAutoGUI       | Keyboard automation for sending messages |
| Pandas          | Excel data handling and processing |

---

## Excel Data Format

Your Excel file (`.xlsx`) should include the following columns:

| phone            | fee_status         |
|------------------|------------------|
| `<parent_phone>` | `<PAID or UNPAID>` |
| `<parent_phone>` | `<PAID or UNPAID>` |

> **Note:** Phone numbers must include the **country code** (e.g., `92` for Pakistan) and contain no spaces or special characters.

---

## Message Templates

**For Paid Fees:**  

Dear Parents,

This is to confirm the payment of your child’s school fee.
We sincerely appreciate your timely payment and continued support towards the school’s educational objectives.

Warm regards,
Accounts Department


---
**For Unpaid Fees:**  


Dear Parents,

This is a courteous reminder to kindly clear your child’s pending school dues at your earliest convenience.
Timely payment ensures the smooth continuation of academic and administrative activities.

Sincerely,
Accounts Department

---

# Deployment Instructions

Clone the repository and install dependencies:

bash
git clone https://github.com/adibayameen/Smart-Fee-Automated-WhatsApp-Fee-Reminder-App.git
cd Smart-Fee-Automated-WhatsApp-Fee-Reminder-App
pip install -r requirement.txt


Run the application:

bash
streamlit run smartfee.py


Upload your Excel file through the Streamlit interface, then click **“Send Message”** to initiate WhatsApp notifications.

---

## Data Privacy

Smart Fee operates entirely on your local machine. No external storage or transmission of your data occurs.
All messaging is executed from your system, ensuring complete privacy and control over sensitive information.


https://github.com/user-attachments/assets/0af2ee96-1916-4ee6-ac9f-dd6ed7bd05d5



---

## Developer

**Adeeba Yameen Sheikh**
*Developer & Creator of Smart Fee – Smart, Simple, Seamless*



---

## Acknowledgments

Thanks to the open-source communities and developers of **Streamlit**, **PyWhatKit**, **PyAutoGUI**, and **Pandas** for enabling this automated workflow.

