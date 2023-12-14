from faker import Faker
import json

fake = Faker()

data = []
for i in range(10):
    person = {
        "Ismi": fake.first_name(),
        "Familyasi": fake.last_name(),
        "Yoshi": fake.random_int(min=18, max=100),
        "Kasbi": fake.job(),
        "Yashash_manzili": fake.address()
    }
    data.append(person)

with open("data", "w") as f:
    json.dump(data, f)