import xmlrpc.client

proxy = xmlrpc.client.ServerProxy('http://localhost:5555')
num1 = 5
num2 = 20

s = input("Enter the text: ")

print(proxy.add(num1, num2))
print(proxy.findLen(s))