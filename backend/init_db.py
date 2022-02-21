import asyncio
from databases import Database

async def main() -> None:
    database = Database("sqlite:///vectorai.db")
    await database.connect()

    query = """
        CREATE TABLE bank (
            _id INTEGER PRIMARY KEY, 
            bank_type VARCHAR(100), 
            title VARCHAR(100), 
            position INTEGER,
            image VARCHAR(200)
        )
    """
    await database.execute(query=query)

    query = """
        INSERT INTO bank(bank_type, title, position, image) 
        VALUES (:bank_type, :title, :position, :image)
    """
    values = [
        { "bank_type": "bank-draft", "title": "Bank Draft", "position": 0, "image": "https://source.unsplash.com/2ShvY8Lf6l0/800x599" },
        { "bank_type": "bill-of-lading", "title": "Bill of Lading", "position": 1, "image": "https://source.unsplash.com/Dm-qxdynoEc/800x799" },
        { "bank_type": "invoice", "title": "Invoice", "position": 2, "image": "https://source.unsplash.com/qDkso9nvCg0/600x799"},
        { "bank_type": "bank-draft-2", "title": "Bank Draft 2", "position": 3, "image": "https://source.unsplash.com/iecJiKe_RNg/600x799"},
        { "bank_type": "bill-of-lading-2", "title": "Bill of Lading 2", "position": 4, "image": "https://source.unsplash.com/NQSWvyVRIJk/800x599"},
    ]
    await database.execute_many(query=query, values=values)
    await database.disconnect()

if __name__ == "__main__":
    asyncio.run(main())