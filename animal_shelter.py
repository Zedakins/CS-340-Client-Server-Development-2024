from pymongo import MongoClient

class AnimalShelter:
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, mongo_user, mongo_pass, mongo_host, mongo_port):
        """
        Initialize the MongoDB connection using credentials passed to the constructor.
        """
        try:
            # Construct the MongoDB connection URI
            connection_uri = f"mongodb://{mongo_user}:{mongo_pass}@{mongo_host}:{mongo_port}/?authSource=admin"
            
            # Establish connection
            self.client = MongoClient(connection_uri)
            self.db = self.client['AAC']  # Connect to the 'AAC' database
            print("Connection to MongoDB successful.")
        except Exception as e:
            print(f"Failed to connect: {e}")

    def create(self, data):
        """
        Inserts a document into the 'animals' collection.
        
        Args:
        - data: A dictionary representing the document to be inserted.
        
        Returns:
        - True if insert is successful, otherwise False.
        """
        if data:
            try:
                result = self.db.animals.insert_one(data)
                if result.acknowledged:
                    print(f"Document inserted with ID: {result.inserted_id}")
                    return True
                else:
                    print("Document insertion failed.")
                    return False
            except Exception as e:
                print(f"An error occurred during insertion: {e}")
                return False
        else:
            print("Data is None or empty.")
            return False

    def read(self, query):
        """
        Queries documents from the 'animals' collection.

        Args:
        - query: A dictionary representing the query for MongoDB.

        Returns:
        - A list of documents that match the query, or an empty list if none are found.
        """
        try:
            # If query is empty or None, retrieve all documents
            query = query or {}  # If query is None or empty, set it to {}
            cursor = self.db.animals.find(query)
            results = [document for document in cursor]
            return results if results else []
        except Exception as e:
            print(f"An error occurred during the query: {e}")
            return []


    def update(self, query, update_data):
        """
        Updates document(s) in the 'animals' collection based on a query.

        Args:
        - query: A dictionary representing the query to find documents.
        - update_data: A dictionary containing the key-value pairs to update.
        
        Returns:
        - The number of documents updated.
        """
        if query and update_data:
            try:
                result = self.db.animals.update_many(query, {'$set': update_data})
                print(f"Number of documents modified: {result.modified_count}")
                return result.modified_count
            except Exception as e:
                print(f"An error occurred during update: {e}")
                return 0
        else:
            print("Query or update data is None or empty.")
            return 0

    def delete(self, query):
        """
        Deletes document(s) from the 'animals' collection based on a query.

        Args:
        - query: A dictionary representing the query to find documents.
        
        Returns:
        - The number of documents removed.
        """
        if query:
            try:
                result = self.db.animals.delete_many(query)
                print(f"Number of documents removed: {result.deleted_count}")
                return result.deleted_count
            except Exception as e:
                print(f"An error occurred during deletion: {e}")
                return 0
        else:
            print("Query is None or empty.")
            return 0

