class BaseDB:

    def __init__(self, collection, model):
        self.collection = collection
        self.model = model

    async def create_one(self, cpu):
        document = cpu
        result = await self.collection.insert_one(document)
        check = await self.collection.find_one({"_id": result.inserted_id})
        del check["_id"]
        return check

    async def fetch_all(self, limit, skip, sort, sort_direction):
        cpus = []
        sorter = "_id"
        direction = 1
        if sort in ["name", "rating", "_id"]:
            sorter = sort
        if sort_direction == -1:
            direction = sort_direction

        cursor = self.collection.find({}).limit(limit).skip(skip).sort(sorter, direction)
        amount = await self.collection.count_documents({})
        async for document in cursor:
            document['specifications'] = [{"key": key, "value": value} for key, value in
                                          document['specifications'].items()]
            cpus.append(self.model(**document))
        return amount, cpus

    async def fetch_one(self, name):
        find_string = {"link_name": name}
        document = False
        cursor = self.collection.find(find_string)
        async for document in cursor:
            document['specifications'] = [{"key": key, "value": value} for key, value in
                                          document['specifications'].items()]
            document = self.model(**document)
        return document

    # TODO сделай кароче 1 таблицу со всеми и тобавь туда категории
    async def find_by_name(self, name):
        return None

    async def fetch_by_params(self, *args):
        return None

