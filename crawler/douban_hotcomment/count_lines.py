
from proxies import Proxy

inst = Proxy("proxyfile.txt")
proxy = inst.get_proxy()

print(proxy)
