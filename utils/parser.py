def parse_wos_file(file_path):
    articles = []
    article_data = {}

    read_empty_lines = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        key = None
        value = None
        while read_empty_lines < 20:
            line = file.readline()

            if line.startswith("   "):
                value = value + " " + line[3:].strip()
                continue

            line = line.strip()

            if not line:
                read_empty_lines += 1
                continue
            read_empty_lines = 0

            if key is not None and value:
                article_data[key] = value
            key = None
            value = ''

            # End of an article record
            if line.startswith('ER'):
                if article_data:  # Ensure there is data to add
                    articles.append(article_data)
                    article_data = {}  # Reset for next article
                continue

            # Parse lines and store data in the dictionary
            if line.startswith('AU '):  # Author
                key = 'Author'
            elif line.startswith('TI '):  # Title
                key = 'Title'
            elif line.startswith('CR '):  # Cited References
                key = 'CitedReferences'
            elif line.startswith('TC '):  # Total Citations
                value = 'TotalCitations'
            elif line.startswith('UT '):  # Unique WOS ID
                key = 'WOS_ID'

            if key is not None:
                value = line[3:].strip()

    return articles
