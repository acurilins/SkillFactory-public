from ewallet import Customer

cust1 = Customer('"Иван Петров".', 50)
cust2 = Customer('"Алексей Попович".', 2000)

print("Клиент", cust1.getName(),'Баланс:', cust1.getBalance(), "руб")
print("Клиент", cust2.getName(),'Баланс:', cust2.getBalance(), "руб")
