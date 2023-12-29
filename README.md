## Requirement

Some python modules have to be installed :

```bash
pip install discord.py
pip install mysql-connector-python
```

## Prerequisite

You have to create a config.py file containing your Token bot and your database info connection :

```bash
import mysql.connector

TOKEN = 'YOUR_TOKEN'

db = mysql.connector.connect(
    host="HOSTNAME TO YOUR DB",
    user="DB USER",
    passwd="DB PASSWORD",
    database="DB NAME"
```
