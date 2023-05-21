from sqlalchemy import create_engine,text
import os

connector_string = os.environ["DB_CRED"]

engine = create_engine(connector_string,echo=True)

def load_jobs():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM jobs"))
        jobs=[]
        for row in result.mappings():
            jobs.append(dict(row))
    return jobs