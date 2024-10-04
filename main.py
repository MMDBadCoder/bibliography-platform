from config import DOWNLOADING_RECORDS_LIMIT
from utils.downloader import download_paged_files
from utils.files_aggregator import merge_files_content, aggregate_files_content
from utils.parser import read_articles_from_aggregated_file
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
merge_files_content(paged_files, 'raw.txt')
aggregated_file = 'aggregated.txt'
aggregate_files_content(paged_files, aggregated_file)

# Write articles in csv format
articles = read_articles_from_aggregated_file(aggregated_file)
