from utils.draw import draw_citation_graph
from utils.parser import parse_wos_file


def filter_article(article: dict):
    if article.__contains__('TotalCitations'):
        return int(article['TotalCitations']) > 50
    return False


articles = parse_wos_file('repo/full.txt')
articles = [article for article in articles if filter_article(article)]
draw_citation_graph(articles)
