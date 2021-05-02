#!/usr/bin/env python3

from controller import Controller

def update(url, style):
    """Update hosts"""
    ctl = Controller()
    ctl.setData(url, style)

def reset():
    """Clear hosts"""
    ctl = Controller()
    ctl.reset()

def export():
    """Export hosts file"""
    ctl = Controller()
    ctl.make()

if __name__ == '__main__':
    targets = {'https://280blocker.net/files/280blocker_domain_ag_[[yyyyMM]].txt': 'adguard'}
    for url, style in targets.items():
        update(url, style)

    export()
