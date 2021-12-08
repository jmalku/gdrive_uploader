from googleapiclient.http import MediaFileUpload
from Google import Create_Service

CLIENT_SECRET_FILE = 'client_secrets.json' 
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

folder_id = '1enPCVeZmcxWABJ36qnUebF9IuBzu2F9M'
file_names = f'target_{cnt}.jpg'
mime_types = ['image/jpeg']
for file_name, mime_type in zip(file_names, mime_types):
    file_metadata = {
        'name': file_name,
        'parents': [folder_id]
    }
    media = MediaFileUpload(f'tmp/{file_names}', mimetype=mime_type)
    create_response = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()

    file_id = create_response.get('id')
    print(file_id)
    # time.sleep(25)
    # delete_file(file_id)

    request_body = {
        'role': 'reader',
        'type': 'anyone'
    }

    response_permission = service.permissions().create(
        fileId=file_id,
        body=request_body
    ).execute()

    # print(response_permission)

    # Print Sharing URL
    response_share_link = service.files().get(
        fileId=file_id,
        fields='webViewLink'
    ).execute()

    print(response_share_link)

    # Remove Sharing Permission
    # service.permissions().delete(
    #     fileId=file_id,
    #     permissionId='anyoneWithLink'
    # ).execute()

def delete_file(file_id):
    del_response = service.files().delete(fileId=file_id).execute()
    print('del_response.body:')
    print(del_response)
    # print('I will try to emptyTrash:')
    # trash_response = service.files().emptyTrash().execute()
    # print('trash_response.body:')
    # print(trash_response)


image_2 = f'https://docs.google.com/uc?id={file_id}'
