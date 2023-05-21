from sqlalchemy import create_engine,text


connector_string = 'mysql+mysqlconnector://e3jrja054vqsmjtwfcui:pscale_pw_4MHBCRnvvsw3nG1TQaNuAX7H46tkEKZsMwt28lbcoWz@aws.connect.psdb.cloud/test'

engine = create_engine(connector_string,echo=True)

def load_jobs():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM jobs"))
        jobs=[]
        for row in result.mappings():
            jobs.append(dict(row))
    return jobs