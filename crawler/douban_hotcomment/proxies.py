class Proxy(object):
   _instance = None
   def __new__(cls, proxyfile):
       if not isinstance(cls._instance, cls):
           cls._instance = super(Proxy, cls).__new__(cls)
           with open(proxyfile) as f:
               content = f.read()
               lines = content.split("\n")
               cls._instance._proxies = lines[:-1]
               cls._instance._curr = 0
       return cls._instance
   
   def get_proxy(self):
       idx = self._curr % len(self._proxies)
       proxy = self._proxies[idx]
       self._curr += 1
       return proxy
