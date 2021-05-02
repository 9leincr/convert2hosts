from tinydb import TinyDB, Query

class DataManager:
    """DataManager"""

    __db = TinyDB('./db/db.json')
    __table = __db.table('hosts')

    def init(self):
        """Initialize DB"""
        self.__table.truncate()

    def appendAllow(self, list):
        """Append allowed hostname"""
        Host = Query()
        allowed = [rec['hostname'] for rec in self.__table.search(Host.action == 'allow')]
        # 差分を登録
        for h in (set(list) - set(allowed)):
            self.__table.insert({'hostname': h, 'action': 'allow'})

    def appendDeny(self, list):
        """Append denied hostname"""
        Host = Query()
        denied = [rec['hostname'] for rec in self.__table.search(Host.action == 'deny')]
        # 差分を登録
        for h in (set(list) - set(denied)):
            self.__table.insert({'hostname': h, 'action': 'deny'})

    def makeHosts(self):
        """Make hosts file from DB"""
        Host = Query()
        allows = [rec['hostname'] for rec in self.__table.search(Host.action == 'allow')]
        denies = [rec['hostname'] for rec in self.__table.search(Host.action == 'deny')]

        try:
            with open('./out/hosts.txt', 'w') as f:
                f.write('# Adfilter hosts\n\n')
                for h in sorted(set(denies) - set(allows)):
                    f.write('127.0.0.1 ' + h + '\n')
        except Exception as e:
            print(e)
