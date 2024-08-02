import csv
import random
import faker

# Initialize the Faker library
fake = faker.Faker()

# Generate random grades
grades = ['A', 'B', 'C', 'D', 'E', 'F']

# Function to create a single record
def create_record(id):
    return {
        'id': id,
        'name': fake.name(),
        'age': random.randint(18, 30),
        'grade': random.choice(grades),
        'email': fake.email()
    }

# Generate 1000 records
records = [create_record(i) for i in range(1, 2001)]

# Define CSV file name
csv_file = 'students.csv'

# Write records to CSV
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['id', 'name', 'age', 'grade', 'email'])
    writer.writeheader()
    writer.writerows(records)

print(f"CSV file '{csv_file}' created successfully.")
