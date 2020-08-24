import sys
import redis
import config

r = redis.Redis(config.HOST)

key = "masuk:%s#%s#" % (sys.argv[1], sys.argv[2])
key_on = key + "on"
key_off = key + "off"

try:
    r.rename(key_on, key_off)
except redis.exceptions.ResponseError:
    print("Key not found")
