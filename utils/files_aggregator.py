import os
import re

# Creating a Python dictionary based on the provided mapping

field_mapping = {
    "VR": "Version",
    "PT": "Publication Type",
    "AU": "Author",
    "AF": "Author Full Name",
    "BE": "Book Editor",
    "TI": "Title",
    "SO": "Source",
    "SE": "Series Title",
    "LA": "Language",
    "DT": "Document Type",
    "DE": "Keywords",
    "AB": "Abstract",
    "C1": "Address",
    "RP": "Corresponding Author",
    "CR": "Cited References",
    "NR": "Number of References",
    "TC": "Total Citations",
    "Z9": "Not Used",
    "U1": "Not Used",
    "U2": "Not Used",
    "PU": "Publisher",
    "PI": "Place of Publication",
    "PA": "Publisher Address",
    "SN": "ISSN",
    "EI": "e-ISSN",
    "BN": "ISBN",
    "J9": "Journal Abbreviation",
    "JI": "Journal Title",
    "PY": "Publication Year",
    "VL": "Volume",
    "BP": "Beginning Page",
    "EP": "Ending Page",
    "DI": "Digital Object Identifier",
    "D2": "Alternative DOI",
    "PG": "Page Count",
    "WC": "Web of Science Categories",
    "WE": "Indexing Source",
    "SC": "Research Areas",
    "GA": "Accession Number",
    "UT": "Unique WOS ID",
    "PM": "PubMed ID",
    "DA": "Date of Addition to WoS",
    "ER": "End of Record"
}


def aggregate_files_content(file_paths, output_file_path):
    try:
        with open(output_file_path, 'w') as output_file:
            index = [0]
            for file_path in file_paths:
                # Check if the file exists
                if os.path.exists(file_path):
                    with open(file_path, 'r') as input_file:
                        lines = input_file.readlines()
                        convert_and_write_lines_to_output(lines, output_file, index)
                else:
                    print(f"File not found: {file_path}")
        print(f"Successfully merged files into: {output_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


def starts_with_field_key(line: str) -> bool:
    pattern = r'^[A-Z]{2} '
    return bool(re.match(pattern, line))


def convert_and_write_lines_to_output(lines, output_file, index):
    field_key = None
    field_value_lines = []
    for line in lines:
        line = line.strip()

        if line == 'ER':
            index[0] = index[0] + 1
            output_file.write('-----\n')

        if starts_with_field_key(line):
            if field_key is not None:
                output_file.write('--\n')
                output_file.write(f'record index: {str(index[0])}\n')
                output_file.write(f'key: {field_key}\n')
                field_name = 'None'
                if field_mapping.__contains__(field_key):
                    field_name = field_mapping[field_key]
                output_file.write(f'name: {field_name}\n')
                output_file.write(f'value:\n')
                field_value = '\n'.join(field_value_lines)
                output_file.write(field_value + '\n')
            field_key = line[:2]
            field_value_lines = [line[3:]]
        elif line:
            field_value_lines.append(line)
