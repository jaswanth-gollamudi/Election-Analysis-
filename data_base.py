import sqlite3
import requests

class DataBase:
    def __init__(self , base_url):
        self.conn = self.create_db()
        self.start_url = base_url
        self.add_link(self.start_url)
    
    def get_status(self , url):
        try:
            status = requests.get(url)
            return status.status_code
        except:
            return False
        
    def create_db(self):
        self.conn = sqlite3.connect('kumarrr.db')
        self.conn.execute("create table links_html (url TEXT primary key , html TEXT , status TEXT, crawled TEXT)")
        self.conn.commit()
        return self.conn
    
    def execute_query(self , query):
        data = self.conn.execute(query)
        return data
    
    def get_data_from_db(self):
        data = self.conn.execute("SELECT * FROM links_html")
        return data
    
    def link_count(self):
        count = list(self.conn.execute('select count(*) from links_html'))[0][0]
        return count
    
    def get_uncrawled_links(self):
        data = self.conn.execute("select url from links_html where crawled = 'no'")
        return data
    
    def set_link_to_crawled(self , url):
        self.conn.execute("update links_html set crawled = 'yes' where url = (?)", (str(url),))
        self.conn.commit()
    
    def add_link(self , link):
        try:
            self.conn.execute("INSERT INTO links_html (url , status , crawled) VALUES (? , ? , ?)" , (str(link) , str('unscrapped') , str('no')))
            self.conn.commit()
        except:
            pass
        return True
    
    def get_link_from_db(self):
        data = self.conn.execute("select url from links_html where status = 'unscrapped'")
        for i in data:
            link = i[0]
            break
        return link
    
    def add_html_db(self ,html , url , status):
        if status == 200:
            self.conn.execute("update links_html set html = (?) where url = (?);" , (str(html) , str(url)))
            self.conn.commit()
            self.conn.execute("update links_html set status = 'scraped' where url = (?)", (str(url),))
            self.conn.commit()
            return True
        else:
            self.conn.execute("update links_html set status = 'couldnt be crawled' where url = (?)" , (str(url),))
            return True

    def add_html_to_db(self , links):
        for url in links:
            self.add_html(url)
        return True
    
    def get_number_of_pending_links(self):
        l = self.conn.execute("select count(*) from links_html where status = 'unscrapped'")
        for i in l:
            x = i[0]
            break
        return x
    
    def final_function(self):
        x = self.get_number_of_pending_links()
        while x > 0:
            link = self.get_link_from_db()
            self.add_html(link)
            x = self.get_number_of_pending_links()
        return True
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
 