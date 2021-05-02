import re
from data_manager import DataManager

class Converter:
    """Converter"""

    def convert(self, data, type):
        """Get hostname data"""
        if (type == 'adguard'):
            self.extractAdgHosts(data)

    def extractAdgHosts(self, data):
        """Extract hostname from adguard format"""
        allows = re.findall(r'(?<=\n)@@\|\|.+\n', data)
        denies = re.findall(r'(?<=\n)\|\|.+\n', data)

        allows = [re.sub(r'@@\|\|\s*([^\r\n]+)[\r\n]*', r'\1', s) for s in allows]
        denies = [re.sub(r'\|\|\s*([^\r\n]+)[\r\n]*', r'\1', s) for s in denies]

        allows = [re.sub(r'([^\^]+)\^', r'\1', s) for s in allows]
        denies = [re.sub(r'([^\^]+)\^', r'\1', s) for s in denies]

        dmgr = DataManager()
        dmgr.appendAllow(allows)
        dmgr.appendDeny(denies)
