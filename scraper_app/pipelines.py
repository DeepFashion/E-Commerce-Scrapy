from sqlalchemy.orm import sessionmaker
from models import FlipkartProducts, db_connect, create_deals_table, JabongProducts,PolyvoreProducts,FlipkartPageProducts,JabongPageProducts


class FlipkartPipeline(object):
    """Flipkart pipeline for storing scraped items in the database"""
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_deals_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save deals in the database.

        This method is called for every item pipeline component.

        """
        session = self.Session()
        deal = FlipkartProducts(**item)

        try:
            session.add(deal)
            session.commit()
            print "success",
        except:
            print "rollback",
            session.rollback()
            raise
        finally:
            session.close()

        return item


class JabongPipeline(object):
    """JabongData pipeline for storing scraped items in the database"""
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_deals_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save deals in the database.

        This method is called for every item pipeline component.

        """
        session = self.Session()
        deal = JabongProducts(**item)

        try:
            session.add(deal)
            session.commit()
            print "success",
        except:
            print "rollback",
            session.rollback()
            raise
        finally:
            session.close()

        return item

class PolyvorePipeline(object):
    """PolyvoreData pipeline for storing scraped items in the database"""
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_deals_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save deals in the database.

        This method is called for every item pipeline component.

        """
        session = self.Session()
        deal = PolyvoreProducts(**item)

        try:
            session.add(deal)
            session.commit()
            print "success",
        except:
            print "rollback",
            session.rollback()
            raise
        finally:
            session.close()

        return item

class FlipkartPagePipeline(object):
    """FlipkartPagePipeline for storing scraped items in the database"""
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_deals_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save deals in the database.

        This method is called for every item pipeline component.

        """
        session = self.Session()
        deal = FlipkartPageProducts(**item)

        try:
            session.add(deal)
            session.commit()
            print "success",
        except:
            print "rollback",
            session.rollback()
            raise
        finally:
            session.close()

        return item


class JabongPagePipeline(object):
    """JabongPagePipeline for storing scraped items in the database"""
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_deals_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save deals in the database.

        This method is called for every item pipeline component.

        """
        session = self.Session()
        deal = JabongPageProducts(**item)

        try:
            session.add(deal)
            session.commit()
            print "success",
        except:
            print "rollback",
            session.rollback()
            raise
        finally:
            session.close()

        return item