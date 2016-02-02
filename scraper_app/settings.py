
SPIDER_MODULES = ['scraper_app.spiders']

DATABASE = {
    'drivername': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'username': 'fashion',
    'password': 'fashion',
    'database': 'fashion'
}

DOWNLOAD_HANDLERS = {'s3': None,}


DATABASE_NAMES=["flipkartdata","jabongdata","polyvoredata",'flipkartpagedata','jabongpagedata']

LOG_LEVEL = 'INFO'