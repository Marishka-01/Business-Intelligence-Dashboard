import numpy as np
import pandas as pd
import random
import faker

fake = faker.Faker()
np.random.seed(42)
random.seed(42)

n = 10000  # Number of rows in the dataset
data = []

for i in range(n):
    transaction_id = f"TXN_{i:05d}"
    invoice_id = random.randint(100000, 999999)
    date = fake.date_between(start_date='-2y', end_date='today')
    customer = fake.name()
    supplier = fake.company()
    category = random.choice(['Software', 'Office', 'Travel'])
    country = random.choice(['USA', 'Canada', 'UK', 'Germany', 'France'])
    amount = round(random.uniform(0, 1000), 2)
    payment_method = random.choice(['Credit Card', 'Debit Card', 'PayPal', 'Bank Transfer'])
    status = random.choice(['Completed', 'Pending', 'Cancelled'])
    employee = fake.name()
    department = random.choice(['Sales', 'Marketing', 'IT', 'HR', 'Finance'])


    data.append({transaction_id,
                invoice_id,
                date,
                customer,
                supplier,
                category,
                country,
                amount,
                payment_method,
                status,
                employee,
                department})
    

df = pd.DataFrame(data, columns=['Transaction ID', 
                                 'Invoice ID', 
                                 'Date', 
                                 'Customer', 
                                 'Supplier', 
                                 'Category', 
                                 'Country', 
                                 'Amount', 
                                 'Payment Method', 
                                 'Status', 
                                 'Employee', 
                                 'Department'])

df.to_csv("data/raw/transactions.csv", index=False)
print("Dataset generated and saved to data/raw/transactions.csv")

