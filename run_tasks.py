from datetime import timedelta

from redis import Redis
from rq import Queue
from tasks import get_report

q = Queue(connection=Redis())


if __name__ == '__main__':
    print('start')
    # get_report()
    # result = q.enqueue(get_report, '\n')
    result = q.enqueue_in(timedelta(seconds=10), get_report)
    print(result)
    print(type(result))
    print(result.result)
    print('end')