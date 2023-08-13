import requests
""""Python module for fetching requests"""


r = requests.get('https://alu-intranet.hbtn.io/status')

print('Body response:\n\t- {}'.format(r))

