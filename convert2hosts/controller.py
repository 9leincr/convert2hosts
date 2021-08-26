import urllib.request
import re
from datetime import datetime, timezone, timedelta

from converter import Converter
from data_manager import DataManager

class Controller:
    """Controller"""

    def setData(self, url, style):
        """Get the data & Set it"""
        url = self.translate(url)
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'
        headers = {'User-Agent': user_agent}
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req) as res:
                print(url)
                print(res.status)
                body = res.read().decode()
                Converter().convert(body, style)
        except urllib.error.URLError as e:
            print(url)
            print(e.reason)
        except urllib.error.HTTPError as e:
            print(url)
            print('Error code: ', e.code)
            #print(e.read())

    def make(self):
        """Make hosts file"""
        DataManager().makeHosts()

    def reset(self):
        """Reset host data"""
        DataManager().init()

    def translate(self, url):
        """Change particular string"""
        url = re.sub(r'\[\[yyyyMM\]\]', datetime.now(timezone(timedelta(hours=9))).strftime('%Y%m'), url)
        return url
