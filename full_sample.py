from utils.downloader import download_with_pagination
from utils.draw import draw_citation_graph
from utils.parser import parse_wos_file
from utils.query_id_maker import make_query

query = make_query()
query_id = query['query_id']
found_records_count = query['found_records_count']

output_file_path = download_with_pagination(query_id, 3000)
articles = parse_wos_file(output_file_path)
draw_citation_graph(articles)
