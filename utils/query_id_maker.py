import requests

from config_loader import COOKIE, SID


def read_search_string():
    with open('./search_string.txt', 'r', encoding='utf-8') as search_string_file:
        return "\n".join(search_string_file.readlines()).replace("\n", " ").replace('"', '\\"')


def make_query():
    headers = {
        'accept': 'application/x-ndjson',
        'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
        'content-type': 'text/plain;charset=UTF-8',
        'origin': 'https://https-www--webofscience--com.daccess.ir',
        'priority': 'u=1, i',
        'referer': 'https://https-www--webofscience--com.daccess.ir/wos/woscc/advanced-search',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    }

    params = {
        'SID': SID,
    }

    data = '{"product":"WOSCC","searchMode":"general","viewType":"search","serviceMode":"summary","search":{"mode":"general","database":"WOSCC","query":[{"rowText":"' \
           '' + read_search_string() + \
           '"}],"sets":[],"options":{"lemmatize":"On"}},"retrieve":{"count":50,"history":true,"jcr":true,"sort":"relevance","analyzes":["TP.Value.6","REVIEW.Value.6","EARLY ACCESS.Value.6","OA.Value.6","DR.Value.6","ECR.Value.6","PY.Field_D.6","DT.Value.6","AU.Value.6","DX2NG.Value.6","PEERREVIEW.Value.6"],"locale":"en_US"},"eventMode":null}'

    response = requests.post(
        'https://https-www--webofscience--com.daccess.ir/api/wosnx/core/runQuerySearch',
        params=params,
        cookies=COOKIE,
        headers=headers,
        data=data,
    )

    query_id = str(response.content).split('"QueryID":"')[1].split('"')[0]
    found_records_count = int(str(response.content).split('"RecordsFound":')[1].split(",")[0])

    print(f"Query was created: {query_id}")
    print(f"Found records count: {str(found_records_count)}")

    return {
        'query_id': query_id,
        'found_records_count': found_records_count
    }
