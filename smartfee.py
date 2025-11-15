import time
import pyautogui
import pywhatkit as kit
import streamlit as st
import pandas as pd
st.set_page_config(page_title="Smart fee-Smart Simple Seamless")
st.title("Smart fee-Smart Simple Seamless")
upload=st.file_uploader("UPLOAD AN EXCEL FILE",type=["xlsx"])
if upload is not None:
    df=pd.read_excel(upload)
    st.success("File Successfully Uploaded")
    st.dataframe(df)
    if st.button("send message"):
        for i,row in df.iterrows():
            phone=f"+{row['phone']}"
            Fees_status=str(row["fee_status"])
            if Fees_status.strip().upper() == "PAID":
                message=("Dear Parents,\n\nThis is to confirm the payment of your child’s school fee. We sincerely appreciate your timely payment and continued support towards the school’s educational objectives.\n\nwarm regards,\nAccount Department ")
                kit.sendwhatmsg_instantly(phone,message,wait_time=35)
                time.sleep(8)
                pyautogui.press("enter")
                print("send")
            else:
                message=("Dear Parents,\n\nThis is a courteous reminder to kindly clear your child’s pending school dues at your earliest convenience.Timely payment ensures the smooth continuation of academic and administrative activities.\n\nSincerely,\nAccount Department")
                kit.sendwhatmsg_instantly(phone,message,wait_time=35)
                time.sleep(8)
                pyautogui.press("enter")
                print("send")
        st.success("All Message Successfully Send")
st.info("Deveolped by Adeeba Yameen Sheikh")


