# 🛠️ Steps to Back Up Media Files and Store in MongoDB
# Back Up Media Files:
# Use the mediabackup command from the django-dbbackup package to create a backup of your media files:
# python manage.py mediabackup --output-filename=media_backup.tar
#
# This will generate a tarball (media_backup.tar) containing your media files.
#
# Store Backup in MongoDB:
# To store the backup in MongoDB, you can use GridFS, which is designed for storing and retrieving large files:
# from pymongo import MongoClient
# import gridfs
#
# client = MongoClient("mongodb://localhost:27017/")
# db = client["your_database"]
# fs = gridfs.GridFS(db)
#
# with open("media_backup.tar", "rb") as f:
#     fs.put(f, filename="media_backup.tar")
#
# This code reads the tarball and stores it in MongoDB using GridFS.
#
# Retrieve and Restore Backup:
# To retrieve the backup from MongoDB and restore your media files:
# file = fs.find_one({"filename": "media_backup.tar"})
# with open("media_backup.tar", "wb") as f:
#     f.write(file.read())
#
# Then, extract the tarball to restore your media files:
#
# tar -xvf media_backup.tar -C /path/to/media/