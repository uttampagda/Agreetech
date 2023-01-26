import os,datetime
import dropbox
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agritech.settings')

file_name = str(datetime.datetime.now().date())+"--db_dump.sql"

os.system(f"sqlite3 {settings.DATABASES['default']['NAME']} .dump > {file_name}")

dbx = dropbox.Dropbox("sl.BXmQVuic7SJp92-M16NDJzXwynnAO4tgE4Vj1IO_GZ5VAMOMr3TCmDPXoTMjP1vHDNQemdimGBKVmiD3gdCkyqhW85Kq9E55bTtuUxgftE1VWps821tyxa6dOCcZdIXwDVa7ZKJR9tA")

destination_path = "/"+file_name

with open(file_name, "rb") as f:
    dbx.files_upload(f.read(), destination_path)

os.remove(file_name)
print("Dump file created and uploaded successfully.")
