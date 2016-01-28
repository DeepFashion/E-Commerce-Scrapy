from sqlalchemy.orm import sessionmaker
from models import db_connect
import optparse
import settings

def parse_args():

	usage="""
		use flag --all with arguement 1 to delete all databases 
		use flag --db with arguement dbName to delete specific dataabse

	"""
	parser = optparse.OptionParser(usage)

	help = "Delete all databases, default None"
	parser.add_option('--all', default=None,help=help)

	help = "Delete particular databases, default None"
	parser.add_option('--db', help=help, default=None)

	options, args = parser.parse_args()

	if not options.db and not options.all:
	    parser.error('Provide atleast single flag')
	elif options.db and options.all:
		parser.error('Provide only single flag')

	return options

if __name__ == '__main__':
	options=parse_args()
	engine = db_connect()
	databases=settings.DATABASE_NAMES
	if options.all:
		for database in databases:
			try:
				engine.execute("DROP TABLE "+database);
			except Exception, e:
				print "Database does not exist: "+database+""
	elif options.db:
		try:
				engine.execute("DROP TABLE "+options.db);
		except Exception, e:
			print "Database does not exist "+options.db+""
	else:
		print "unknown flag or value"

			

