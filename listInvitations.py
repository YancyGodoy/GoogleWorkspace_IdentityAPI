from pprint import pprint
from google.oauth2 import service_account
import googleapiclient.discovery

SCOPES = [
    'https://www.googleapis.com/auth/cloud-identity.userinvitations.readonly',
    'https://www.googleapis.com/auth/cloud-identity.userinvitations',
    'https://www.googleapis.com/auth/cloud-identity']

SERVICE_ACCOUNT_FILE = 'identity.json' #Your Json Key created for Service Account used.

def create_service():
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    delegated_credentials = credentials.with_subject(
        'SuperAdminAccount@domain.xyz') #Super Admin account to be impersonated to execute this list. This won't work with Non Super Admin Accounts

    service_name = 'cloudidentity'
    api_version = 'v1beta1'
    
    service = googleapiclient.discovery.build(
        service_name,
        api_version,
        credentials=delegated_credentials
        )
   
    #parent='customers/ = Google Workspace Customer ID -> https://support.google.com/a/answer/10070793
    results = service.customers().userinvitations().list(parent='customers/C0xxxxx').execute()
    
    #Other Methods as documented at https://cloud.google.com/identity/docs/how-to/manage-user-invitations
        #service.customers().userinvitations().get(parent='customers/C0xxxxx').execute()
        #service.customers().userinvitations().send(parent='customers/C0xxxxx').execute()

    pprint(results)
 
if __name__ == '__main__':
    create_service()
