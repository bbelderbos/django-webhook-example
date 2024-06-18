import requests

url = "http://127.0.0.1:8000/webhook/"

# Replace with the actual rawRequest payload you captured from webhook.site
raw_request_payload = """
{
  "slug": "submit/241692120026345",
  "jsExecutionTracker": "build-date-1718700678061=>init-started:1718710188942=>validator-called:1718710188981=>validator-mounted-true:1718710188981=>init-complete:1718710188983=>onsubmit-fired:1718710204798=>submit-validation-passed:1718710204807",
  "submitSource": "form",
  "buildDate": "1718700678061",
  "q3_fullName": {"first": "bob", "last": "belderbos"},
  "q4_contactNumber": {"full": "(222) 333-4444"},
  "q5_emailAddress": "bob@pybit.es",
  "q13_whatDate13": {
    "implementation": "new",
    "date": "2024-06-19 10:00",
    "duration": "60",
    "timezone": "Europe/Madrid (GMT+02:00)"
  },
  "q12_anyOther": {
    "month": "06",
    "day": "18",
    "year": "2024",
    "timeInput": "01:29",
    "hour": "01",
    "min": "29",
    "ampm": "PM"
  },
  "q10_whatServices": "services",
  "event_id": "1718710188942_241692120026345_IMXUbBN",
  "timeToSubmit": "15",
  "path": "/submit/241692120026345"
}
""".strip()

payload = {
    'rawRequest': raw_request_payload,
    'submissionID': '5945194041717462825'
}

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}
response = requests.post(url, data=payload, headers=headers)
print(response.status_code)
print(response.json())
