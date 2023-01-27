import os,datetime
import dropbox
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agritech.settings')

file_name = str(datetime.datetime.now().date())+"--db_dump.sql"

os.system(f"sqlite3 {settings.DATABASES['default']['NAME']} .dump > {file_name}")

key = 'mpufrgbq3iq6x4j'
secret = 'smze5cm9v1746r4'
dbx = dropbox.Dropbox("sl.BXofc1u4QfDvM5LWmyzXg_HP03zJKzsLgp1E47cTOQCMg3g2tHMfW9NgLbmRsh2nGKTyOhY3eg7pffh80AMf9iSAXUVJDeaafAiBh3UtvJ7FwUkJtJqng2PHlrg6H4JKq2LbgiEZDuo")

destination_path = "/"+file_name

with open(file_name, "rb") as f:
    dbx.files_upload(f.read(), destination_path)

os.remove(file_name)
print("Dump file created and uploaded successfully.")
