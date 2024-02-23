from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('localhost', 27017)  # Connect to MongoDB running locally on default port

# Select the database
db = client.pritydb # Replace 'another' with your database name

# Select the collection
collection = db.emp  # Replace 'new' with your collection name

# Find all documents in the collection
cursor = collection.find({})  # Query to find all documents, you can pass filter criteria here

# Print the documents
for document in cursor:
    print(document)

# Close the MongoDB connection
client.close()