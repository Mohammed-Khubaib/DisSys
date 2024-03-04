import socket

def perform_dns():
    host_name = input("Enter Host Name: ")
    try:
        ip_address = socket.gethostbyname(host_name)
        print(f"Host Name: {socket.gethostbyaddr(ip_address)[0]}")
        print(f"IP: {ip_address}")
    except socket.gaierror as e:
        print(f"Error: {e}")

def perform_reverse_dns():
    ip_address = input("Enter IP address: ")
    try:
        host_name, _, _ = socket.gethostbyaddr(ip_address)
        print(f"IP: {ip_address}")
        print(f"Host Name: {host_name}")
    except socket.herror as e:
        print(f"Error: {e}")

def main():
    while True:
        print("Select Option:")
        print("1. DNS")
        print("2. Reverse DNS")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == "1":
            perform_dns()
        elif choice == "2":
            perform_reverse_dns()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
