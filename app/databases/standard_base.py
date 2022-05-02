class BaseDB:

    def __init__(self, collection, model):
        self.collection = collection
        self.model = model

    async def create_one(self, cpu):
        document = cpu
        result = await self.collection.insert_one(document)
        return result

    async def fetch_all(self, limit, skip):
        cpus = []
        cursor = self.collection.find({}).limit(limit).skip(skip)
        amount = await self.collection.count_documents({})
        async for document in cursor:
            document['specifications'] = [{"key": key, "value": value} for key, value in document['specifications'].items()]
            cpus.append(self.model(**document))
        return amount, cpus

    async def fetch_one(self, name):
        cpus = []
        find_string = {"name": name}
        cursor = self.collection.find(find_string)
        async for document in cursor:
            cpus.append(self.model(**document))
        return cpus

    async def fetch_by_params(self, *args):
        return None

