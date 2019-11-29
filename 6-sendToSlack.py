import requests
import json

def sendToSlack(msg):
	slack_url = "https://hooks.slack.com/services/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"
	payload = json.dumps({
            'username': 'Historic Computation Alert',
            'attachments': [
                {
                    'fallback': msg,
                    'color': '#36a64f',
                    'fields': [
                        {
                            'title': '',
                     							'value': msg
                        }
                    ]
                }
            ]})
	try:
		requests.post(slack_url, data=payload, timeout=10)
	except:
		pass
	return


sendToSlack('check')