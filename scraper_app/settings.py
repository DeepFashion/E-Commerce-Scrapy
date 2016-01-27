SITE_NAME='Flipkart'

BOT_NAME = SITE_NAME+'Bot'

SPIDER_MODULES = ['scraper_app.spiders']

DATABASE = {
    'drivername': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'username': 'postgres',
    'password': 'qwerty',
    'database': 'test'
}

ITEM_PIPELINES = ['scraper_app.pipelines.'+SITE_NAME+'Pipeline']