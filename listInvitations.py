from pprint import pprint
from google.oauth2 import service_account
import googleapiclient.discovery
import pprint

SCOPES = ['https://www.googleapis.com/auth/cloud-identity.userinvitations, https://www.googleapis.com/auth/cloud-identity.userinvitations.readonly, https://www.googleapis.com/auth/cloud-identity.userinvitations, https://www.googleapis.com/auth/cloud-identity']

SERVICE_ACCOUNT_FILE = 'identity.json'


def create_service():
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    delegated_credentials = credentials.with_subject(
        'yancymelany@support-domain29.xyz')

    service_name = 'cloudidentity'
    api_version = 'v1beta1'
    service = googleapiclient.discovery.build(
        service_name,
        api_version,
        credentials=delegated_credentials)
    customer = 'C00pi502y'
    
    #customers.userinvitations.list()
    results = service.customers.userinvitations.list()

    pprint(results)
 
