# File: mongodb_view.py
#
# Copyright (c) 2018-2021 Splunk Inc.
#
# SPLUNK CONFIDENTIAL - Use or disclosure of this material in whole or in part
# without a valid written license from Splunk Inc. is PROHIBITED.
#


def display_query_results(provides, all_results, context):

    headers = []
    context['results'] = results = []

    headers_set = set()
    for summary, action_results in all_results:
        for result in action_results:
            for record in result.get_data():
                headers_set.update(record.keys())

    if not headers_set:
        headers_set.update(headers)
    headers.extend(headers_set)
    headers.sort(key=str.lower)
    final_result = {'headers': headers, 'data': []}

    for summary, action_results in all_results:
        for result in action_results:
            data = result.get_data()
            for item in data:
                row = []
                for header in headers:
                    row.append(item.get(header, ''))
                final_result['data'].append(row)

    results.append(final_result)
    return 'display_results.html'
