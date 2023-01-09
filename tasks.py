import time


def get_report(separator='\n'):
    time.sleep(10)
    data = [
    'Теннис',
    'Зимние виды спорта',
    'Плавание'
        ]
    with open('report.txt', 'w', encoding='utf-8') as f:
        for category in data:
            f.write(f'{category}{separator}')
    print("Report has been saved")
    return 'Saved'