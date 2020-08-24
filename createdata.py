import redis
import config

r = redis.Redis(config.HOST)

with r.pipeline() as pipe:
    for a in range(100):
        for b in range(100):
            key = "masuk:%s#%s#on" % (a,b)
            pipe.hmset(key, {"title":"Anu", "create_date": "ewe"})
    pipe.execute()

r.bgsave()
