#!/usr/bin/env python
import asyncio_redis

from owllook.config import CONFIG


# Token from https://github.com/subyraman/sanic_session
class RedisSession:
    """
    A simple wrapper class that allows you to share a connection
    pool across your application.
    """
    _pool = None

    async def get_redis_pool(self):
        if not self._pool:
            REDIS_DICT = CONFIG.REDIS_DICT
            self._pool = await asyncio_redis.Pool.create(
                host=REDIS_DICT.get('REDIS_ENDPOINT', None), port=REDIS_DICT.get('REDIS_PORT', None),
                poolsize=REDIS_DICT.get('POOLSIZE', None), password=REDIS_DICT.get('PASSWORD', None),
                db=REDIS_DICT.get('SESSION_DB', None)
            )

        return self._pool
