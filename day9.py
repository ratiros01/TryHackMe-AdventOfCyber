import requests

path = ''
host = 'http://10.10.169.100:3000/'

value = ''

while(path is not 'end'):
	response = requests.get(host + path)
	print(response)
	#status_code = response.status_code
	#print(status_code)

	json_response = response.json()

	value += json_response['value']
	path = json_response['next']
	
	#converted_response = json_response.encode('ascii')
	#print(converted_response)

	#text = response.text
	#print(text)
	#path = ''
	#break
	print path + " "
	print value

print value
