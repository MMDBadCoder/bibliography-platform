def read_articles_from_aggregated_file(file_path):
    articles = []

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        article_data = {}
        line_number = 0
        while line_number != len(lines):
            line = lines[line_number].strip()
            if line == '--':
                key = lines[line_number + 2].strip()[5:]

                end_line_number = line_number + 5
                while not lines[end_line_number].startswith('--'):
                    end_line_number += 1

                value = ' '.join([l.strip() for l in lines[line_number + 5: end_line_number]])
                article_data[key] = value
                line_number = end_line_number
            elif line == '-----':
                articles.append(article_data)
                article_data = {}
                line_number += 1
            else:
                break

    return articles
