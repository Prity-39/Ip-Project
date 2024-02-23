from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('localhost', 27017)  # Connect to MongoDB running locally on default port

# Select the database
db = client.pritydb  # Replace 'another' with your database name

# Select the collection
collection = db.emp  # Replace 'new' with your collection name

# List of documents (each representing a person)
people = [
    {"empname": "Alice", "mpage": 30},
    {"empname": "Bob", "mpage": 27},
    {"empname": "Charlie", "mpage": 35}
]

# Insert multiple documents into the collection
insert_result = collection.insert_many(people)

# Print the IDs of the inserted documents
for id in insert_result.inserted_ids:
    print("Inserted document ID:", id)

# Close the MongoDB connection
client.close()