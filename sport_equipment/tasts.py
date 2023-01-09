import time
from .models import Category


def get_report_job():
    time.sleep(120)
    categories = Category.objects.all()
    with open('report.txt', 'w', encoding='utf-8') as f:
        for category in categories:
            f.write(f'{category.name}\n')
    print('Report has been saved')
    return 'Done'