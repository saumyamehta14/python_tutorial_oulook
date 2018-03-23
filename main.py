from pyOutlook import OutlookAccount
from requests_oauthlib import OAuth2Session
from six.moves import input as inp

client_id = '4362cd09-acf6-4bee-91e2-c30516c2bebe'
client_secret = 'stbiybHFNQ466_~aHPK39|='
authorization_base_url = 'https://login.microsoftonline.com/common/oauth2/v2.0/authorize'
token_url = 'https://login.microsoftonline.com/common/oauth2/v2.0/token'
scope = ['https://outlook.office.com/Mail.ReadWrite']
redirect_uri = 'http://localhost:8000/tutorial/gettoken/'
outlook = OAuth2Session(client_id,scope=scope,redirect_uri=redirect_uri)
authorization_url, state = outlook.authorization_url(authorization_base_url)
print ('Please go here and authorize', authorization_url)
redirect_response = 'https://outlook.live.com/owa/'
token = outlook.fetch_token(token_url,client_secret=client_secret,authorization_response=redirect_response)
print(token)
