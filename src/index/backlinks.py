class BacklinkIndex:
    def __init__(self):
        self.links = {}
    def add_link(self, src, dst):
        self.links.setdefault(dst, set()).add(src)
