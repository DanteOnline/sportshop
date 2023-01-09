import redis

# Connect to Redis
redis_conn = redis.Redis(host='localhost', port=6379)

# Set a key
redis_conn.set('key', 'test value')

# Get a key
value = redis_conn.get('key')
print(value)  # b'value'
