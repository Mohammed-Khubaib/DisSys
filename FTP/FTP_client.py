import streamlit as st
from ftplib import FTP

def download_file(ftp, filename):
    with open(filename, 'wb') as file:
        ftp.retrbinary(f'RETR {filename}', file.write)
    st.success(f"File '{filename}' downloaded successfully")

def upload_file(ftp, filename):
    with open(filename, 'rb') as file:
        ftp.storbinary(f'STOR {filename}', file)
    st.success(f"File '{filename}' uploaded successfully")

def main():
    st.title("FTP Client")
    ftp = FTP('localhost')
    ftp.login(user='user', passwd='password')
    
    # List files on the server
    files = ftp.nlst()
    st.write("Files on the server:")
    st.write(files)

    choice = st.selectbox("Select Operation:", ["Download", "Upload", "Exit"])
    if choice == "Download":
        filename = st.text_input("Enter file name to download:")
        if st.button("Download"):
            download_file(ftp, filename)
    elif choice == "Upload":
        uploaded_file = st.file_uploader("Choose a file to upload:")
        if uploaded_file is not None:
            filename = uploaded_file.name
            if st.button("Upload"):
                upload_file(ftp, filename)

    ftp.quit()

if __name__ == "__main__":
    main()