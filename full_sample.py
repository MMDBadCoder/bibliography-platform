from config import DOWNLOADING_RECORDS_LIMIT
from utils.downloader import download_paged_files, merge_files_content
from utils.draw import draw_citation_graph
from utils.parser import read_articles_from_file
from utils.query_id_maker import make_query

# Create a query in wos
query = make_query()
query_id = query['query_id']
found_records_count = query['found_records_count']

# Determine count of downloading records
downloading_records_count = min(DOWNLOADING_RECORDS_LIMIT, found_records_count)

# Download files with pagination
paged_files = download_paged_files(query_id, downloading_records_count)

# Aggregate small files and aggregate them with a more readable format
output_file = 'aggregated.txt'
aggregated_output_file_path = merge_files_content(paged_files, output_file)

# Write articles in csv format
articles = read_articles_from_file(aggregated_output_file_path)
draw_citation_graph(articles)
