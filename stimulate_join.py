from mongita import MongitaClientDisk

# Initialize Mongita client
client = MongitaClientDisk()
db = client['class_database']

# Sample data for 'pets' and 'kinds'
sample_pets = [
    {"name": "Akshara", "kind_id": "1"},
    {"name": "Nookala", "kind_id": "2"},
    {"name": "Tomy", "kind_id": "3"},
    {"name": "Patil", "kind_id": "1"},
    {"name": "Sharika", "kind_id": "4"},
    {"name": "Ramana", "kind_id": "5"}
]

sample_kinds = [
    {"_id": "1", "kind": "Dog"},
    {"_id": "2", "kind": "Cat"},
    {"_id": "3", "kind": "Rabbit"},
    {"_id": "4", "kind": "Parrot"},
    {"_id": "5", "kind": "Fish"},
    {"_id": "6", "kind": "Hamster"}
]

# Clear existing data in the collections
db.pets.delete_many({})
db.kinds.delete_many({})

# Insert sample data
db.pets.insert_many(sample_pets)
db.kinds.insert_many(sample_kinds)

print("Inserted sample data into 'pets' and 'kinds' collections.")

# Display the data to confirm insertion
print("\nPets Collection:")
for pet in db.pets.find():
    print(pet)

print("\nKinds Collection:")
for kind in db.kinds.find():
    print(kind)

# Simulate join between 'pets' and 'kinds' collections
pets = db.pets.find()
combined_results = []

for pet in pets:
    kind = db.kinds.find_one({"_id": pet["kind_id"]})
    if kind:
        combined_pet = {**pet, "kind": kind["kind"]}
        combined_results.append(combined_pet)

# Print results of the simulated join
print("\nSimulated Join Results:")
for result in combined_results:
    print(result)
