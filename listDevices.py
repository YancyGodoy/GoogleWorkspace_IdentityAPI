/**
 * Lists devices in a Google Workspace domain.
 * @see https://cloud.google.com/identity/docs/how-to/setup-devices
 */
 
from google.oauth2 import service_account
import googleapiclient.discovery
from pprint import pprint

# Scopes required by this endpoint -> https://cloud.google.com/identity/docs/reference/rest/v1/devices/list
SCOPES = ['https://www.googleapis.com/auth/cloud-identity.devices',
          'https://www.googleapis.com/auth/cloud-identity',
          'https://www.googleapis.com/auth/cloud-identity.devices.readonly']

# Service Account Credentials to be used. How to create at https://developers.google.com/workspace/guides/create-credentials#service-account
SERVICE_ACCOUNT_FILE = 'deviceskey.json'


def create_service():
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

#Google Workspace Super Admin user account to be impersonated to retrieve the list of devices
    delegated_credentials = credentials.with_subject('yyyy@aaaaaaa.info')

    service_name = 'cloudidentity'
    api_version = 'v1'
   
    service = googleapiclient.discovery.build(
        service_name,
        api_version,
        credentials=delegated_credentials)

    return service

results = create_service().devices().list().execute()

pprint(results)
