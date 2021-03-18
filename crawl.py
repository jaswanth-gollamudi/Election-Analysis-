from urllib.request import urlopen, urlparse
from bs4 import BeautifulSoup
from link_finder import LinkFinder
from data_base import DataBase
import requests
import copy

class Spider:
    
    def __init__(self , base_url , start_url , domain_name):
        self.base_url = base_url
        self.start_url = start_url
        self.domain_name = domain_name
        self.max_count = 10
        self.crawled = set()
        self.db = DataBase(self.start_url)
    
    def get_response(self , url):
        try:
            response = requests.get(url)
            return response.status_code
        except:
            return False
            
    def get_html(self , url):
        try:
            html_body = requests.get(url)
            soup = BeautifulSoup(html_body.text , features="lxml")
            html = soup.prettify()
            return html
        except:
            return ''
    
    def gather_links(self , page_url):
        html_string = ''
        #import pdb; pdb.set_trace()
        try:
            response = urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                soup = BeautifulSoup(response)
                html_string = soup.prettify()
            finder = LinkFinder(self.base_url, page_url)
            finder.feed(html_string)
        except Exception as e:
            print(str(e))
            return set()
        #import pdb; pdb.set_trace()
        urls =  finder.page_links()
        result = set()
        for i in urls:
            if self.domain_name in i:
                result.add(i)
        return result
    
    def get_domain_name(self , url):
        try:
            domain = urlparse(url).netloc.split('.')
            if len(domain) < 2:
                return domain[-1]
            else:
                return domain.split('.')[-2] + '.' + domain.split('.')[-1]
        except:
            return ''
        
        
    def remove_other_links(self , links):
        result = copy.deepcopy(links)
        for url in links:
            domain = self.get_domain_name(url)
            if self.domain_name not in domain:
                result.remove(url)
        return result
    
    def get_link_from_db_for_crawling(self):
        data = self.db.get_uncrawled_links()
        for i in data:
            return i[0]
        else:
            pass
    
    def add_links_to_db(self):
        c = self.db.link_count()
        if c < self.max_count:
            url = self.get_link_from_db_for_crawling()
            #import pdb; pdb.set_trace()
            links = self.gather_links(url)
            self.db.set_link_to_crawled(url)
            for link in links:
                self.db.add_link(link)
                if self.db.link_count() >= self.max_count:
                    return True
                else:
                    pass
        new_c = self.db.link_count()
        if new_c < self.max_count:
            crawled_cursor = self.db.execute_query("select count(*) from links_html where crawled = 'no'")
            for i in crawled_cursor:
                crawled_links = i[0]
            print(crawled_links)
            if crawled_links > 0:
                return self.add_links_to_db()
            else:
                print('no more links to crawl')
            return True
        else:
            return True
        
    def add_html(self , link):
        status = self.get_response(link)
        html = str(self.get_html(link))
        self.db.add_html_db(html , link , status)
        return True
        
    def crawl_and_store(self):
        self.add_links_to_db()
        pending_count = self.db.get_number_of_pending_links()
        while pending_count > 0:
            link = self.db.get_link_from_db()
            print("crawling link : "+ str(link))
            print('pending links:'+ str(pending_count - 1))
            self.add_html(link)
            pending_count = self.db.get_number_of_pending_links()
        return True
    

if __name__ == '__main__' :
    obj = Spider('https://thewire.in/politics/elections-2019-bjp' , 'https://thewire.in/politics/elections-2019-live-latest-news' , 'thewire')
    obj.crawl_and_store()




