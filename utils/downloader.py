import os
from pathlib import Path
from time import sleep

import requests

from config import COOKIE, SORTED_BY, TIME_TO_SLEEP_BETWEEN_DOWNLOADS, PAGE_SIZE


def download_page(query_id, from_index, to_index):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
        'content-type': 'application/json',
        'origin': 'https://https-www--webofscience--com.daccess.ir',
        'priority': 'u=1, i',
        'referer': f'https://https-www--webofscience--com.daccess.ir/wos/woscc/summary/68d37720-1362-4892-a4c4-52a2c19bd4a5-010d65a2a9/{SORTED_BY}/1(overlay:export/exp)',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'x-1p-wos-sid': 'EUW1ED0B991PDR06qbl8WLwZ2GtRj',
    }

    json_data = {
        'parentQid': query_id,
        'sortBy': SORTED_BY,
        'displayTimesCited': 'true',
        'displayCitedRefs': 'true',
        'product': 'UA',
        'colName': 'WOS',
        'displayUsageInfo': 'true',
        'fileOpt': 'othersoftware',
        'action': 'saveToFieldTagged',
        'markFrom': str(from_index),
        'markTo': str(to_index),
        'view': 'summary',
        'isRefQuery': 'false',
        'locale': 'en_US',
        'filters': 'fullRecordPlus',
    }

    response = requests.post(
        'https://https-www--webofscience--com.daccess.ir/api/wosnx/indic/export/saveToFile',
        cookies=COOKIE,
        headers=headers,
        json=json_data,
    )

    file_path = f'downloaded/{str(from_index)}-{str(to_index)}.txt'
    with open(file_path, 'w') as output:
        content = str(response.content)
        content = content.replace('\\n', '\n')
        content = content[52:]  # remove first line that is header of wos
        content = content[:-4]  # remove EF at end of file
        output.write(content)
    print(f"File {file_path} was created")
    return file_path


def merge_files_content(file_paths, output_file_path):
    try:
        with open(output_file_path, 'w') as output_file:
            for file_path in file_paths:
                # Check if the file exists
                if os.path.exists(file_path):
                    with open(file_path, 'r') as input_file:
                        content = input_file.read()
                        output_file.write(content + '\n')  # Add a newline between files
                else:
                    print(f"File not found: {file_path}")
        print(f"Successfully merged files into: {output_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


def download_paged_files(query_id, records_count):
    Path("downloaded").mkdir(parents=True, exist_ok=True)

    downloaded_files = []
    current_index = 1
    while current_index <= records_count:
        to_index = min(current_index + PAGE_SIZE - 1, records_count)
        file_path = download_page(query_id, current_index, to_index)
        downloaded_files.append(file_path)
        current_index = to_index + 1
        sleep(TIME_TO_SLEEP_BETWEEN_DOWNLOADS)

    output_file_path = 'merge.txt'
    merge_files_content(downloaded_files, output_file_path)
    return output_file_path
