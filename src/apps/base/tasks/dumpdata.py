import os
import json
import certifi
from io import StringIO
from celery import shared_task
from pymongo import MongoClient
from dotenv import  load_dotenv
from django.core.management import call_command


load_dotenv(verbose=True)

# === MongoDB Configurations ===
MONGODB_URI = os.getenv("MONGO_CLIENT")
DATABASE_NAME = os.getenv("DATABASE_NAME")
COLLECTION_NAME = os.getenv("RAW_COLLECTION_NAME")


@shared_task()
def dumpdata():
    """
    Celery task to dump data from the database and send it to MongoDB to store it.
    Every time this task is called, the previous MongoDB data is deleted and replaced with the new one.
    """
    # === MongoDb Connect ===
    ca_cert_path = certifi.where()
    client = MongoClient(MONGODB_URI, tlsCAFile=ca_cert_path)
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]

    # === Get Data from Database ===
    out = StringIO()
    call_command('dumpdata', stdout=out)
    json_data = out.getvalue()
    docs = json.loads(json_data)

    # === Delete Previous Data ===
    collection.delete_many({})

    # === Save current Data ===
    collection.insert_many(docs)






