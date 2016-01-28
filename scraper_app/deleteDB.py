from sqlalchemy.orm import sessionmaker
from models import db_connect
 
engine = db_connect()
databases=["flipkartdata","jabongdata","polyvoredata"]
for database in databases:
	engine.execute("DROP TABLE "+database);

