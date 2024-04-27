import requests
import urllib3

urllib3.disable_warnings()

url = "https://la-service.siemens.com.cn/lapoc/uim/uimanon/getUserLeaveByDateAndGid"

# umi_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOiIyMDI0LTAyLTA1IDEwOjQ4OjU2IiwiZXhwIjoiMjAyNC0wMi0wNiAxMDo0ODo1NiIsImV4cFJlYXNvbiI6bnVsbCwic3ViIjoidWltIiwidWltIjp7ImFwcElkIjoiMjAyMzExMTUiLCJhcHBTZWNyZXQiOiJ0cEhQNWZ0VGpwSlBjQkp6In0sImV4cGlyZWQiOmZhbHNlLCJkdXJhdGlvbiI6Ijg2NDAwIiwiZXhwaXJlZEhhbGYiOmZhbHNlfQ.5210wD5wBTfZ2uWf2r8SekLflKCQg8i3vg7IbQ6kC9Q'


headers = {
    'uimToken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOiIyMDI0LTAyLTA1IDEwOjQ4OjU2IiwiZXhwIjoiMjAyNC0wMi0wNiAxMDo0ODo1NiIsImV4cFJlYXNvbiI6bnVsbCwic3ViIjoidWltIiwidWltIjp7ImFwcElkIjoiMjAyMzExMTUiLCJhcHBTZWNyZXQiOiJ0cEhQNWZ0VGpwSlBjQkp6In0sImV4cGlyZWQiOmZhbHNlLCJkdXJhdGlvbiI6Ijg2NDAwIiwiZXhwaXJlZEhhbGYiOmZhbHNlfQ.5210wD5wBTfZ2uWf2r8SekLflKCQg8i3vg7IbQ6kC9Q',
    'Content-Type': 'application/json',
}


json_data = {
    "gid": "Z0031WYD",
    "startDate": "2024-03-01",
    "endDate": "2024-03-31"
}


get_request = requests.post(url, headers=headers, json=json_data, verify=False)
# current_version = dict(get_request.json().get('data')[0]).get('dictKey')
# print(current_version)
response = get_request.json()

print(response)

