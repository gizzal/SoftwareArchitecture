from pyowm.webapi25.configuration25 import *
from pyowm.caches.lrucache import LRUCache

# Cache provider to be used
cache = LRUCache()

# Default API subscription type ('free' or 'pro')
API_SUBSCRIPTION_TYPE = 'free'
