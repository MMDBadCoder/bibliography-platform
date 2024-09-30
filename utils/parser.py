def parse_wos_file(file_path):
    articles = []
    article_data = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()

            # End of an article record
            if line.startswith('ER'):
                if article_data:  # Ensure there is data to add
                    articles.append(article_data)
                    article_data = {}  # Reset for next article
                continue

            # Parse lines and store data in the dictionary
            if line.startswith('AU '):  # Author
                authors = line[3:].split('; ')
                article_data['Authors'] = [author.strip() for author in authors if author]
            elif line.startswith('TI '):  # Title
                article_data['Title'] = line[3:].strip()
            elif line.startswith('SO '):  # Source
                article_data['Source'] = line[3:].strip()
            elif line.startswith('PY '):  # Publication Year
                article_data['Year'] = line[3:].strip()
            elif line.startswith('AB '):  # Abstract
                article_data['Abstract'] = line[3:].strip()
            elif line.startswith('CR '):  # Cited References
                if 'CitedReferences' not in article_data:
                    article_data['CitedReferences'] = []
                cited_reference = line[3:].strip()
                if cited_reference:
                    article_data['CitedReferences'].append(cited_reference)
            elif line.startswith('TC '):  # Total Citations
                article_data['TotalCitations'] = line[3:].strip()
            elif line.startswith('UT '):  # Unique WOS ID
                article_data['WOS_ID'] = line[3:].strip()
            # Add other fields as needed

    return articles
