import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8050/")

welcome_msg = proxy.welcome_msg()
print(welcome_msg)
n1 = int(input('Enter the first number  :'))
n2 = int(input('Enter the Second number :'))


result = proxy.add(n1,n2)
print(f"Result of add({n1},{n2}) = {result}")