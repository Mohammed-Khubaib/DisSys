from ftplib import FTP

def download_file(ftp, filename):
    with open(filename, 'wb') as file:
        ftp.retrbinary(f'RETR {filename}', file.write)
    print(f"File '{filename}' downloaded successfully")

def upload_file(ftp, filename):
    with open(filename, 'rb') as file:
        ftp.storbinary(f'STOR {filename}', file)
    print(f"File '{filename}' uploaded successfully")

def main():
    ftp = FTP('localhost')
    ftp.login(user='user', passwd='password')
    # List files on the server
    ftp.retrlines('LIST')
    while True:
        print("Select Operation:")
        print("1. Download")
        print("2. Upload")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            filename = input("Enter file name to download: ")
            download_file(ftp, filename)
        elif choice == "2":
            filename = input("Enter file name to upload: ")
            upload_file(ftp, filename)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    ftp.quit()

if __name__ == "__main__":
    main()
