from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('localhost', 27017)  # assuming MongoDB is running locally on default port 27017

# Select the database
db = client.another  # replace 'pritydb' with your database name

# Select the collection
collection = db.new  # replace 'emp' with your collection name

# Insert a document (string) into the collection
document = {"empname": "Prity", "mpage": 26}  # replace with your document
insert_result = collection.insert_one(document)

# Print the inserted document's ID
print("Inserted document ID:", insert_result.inserted_id)

# Close the MongoDB connection
client.close()
