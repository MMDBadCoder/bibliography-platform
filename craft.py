from utils.files_aggregator import aggregate_files_content


def filter_article(article: dict):
    if article.__contains__('TotalCitations'):
        return int(article['TotalCitations']) > 50
    return False


files = [
    'downloaded/1-500.txt',
    'downloaded/501-1000.txt',
    'downloaded/1001-1500.txt',
    'downloaded/1501-2000.txt',
    'downloaded/2001-2500.txt',
    'downloaded/2501-3000.txt',
]

aggregate_files_content(files, 'test.txt')
