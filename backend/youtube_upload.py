```python
import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from googleapiclient.http import MediaFileUpload
from backend.error_handling_feedback import handle_error, show_success_message

def authenticate_youtube_api():
    scopes = ["https://www.googleapis.com/auth/youtube.upload"]
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret.json"

    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)

    return youtube

def upload_video(youtube, video_file_path, video_title, video_description, video_category, video_privacy_status):
    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "categoryId": video_category,
                "description": video_description,
                "title": video_title
            },
            "status": {
                "privacyStatus": video_privacy_status
            }
        },
        media_body=MediaFileUpload(video_file_path)
    )
    try:
        response = request.execute()
        show_success_message(f"Video uploaded successfully with ID: {response['id']}")
        return response['id']
    except Exception as e:
        handle_error(f"Failed to upload video: {e}")
        return None

def add_video_to_playlist(youtube, video_id, playlist_id):
    request = youtube.playlistItems().insert(
        part="snippet",
        body={
            "snippet": {
                "playlistId": playlist_id,
                "resourceId": {
                    "kind": "youtube#video",
                    "videoId": video_id
                }
            }
        }
    )
    try:
        response = request.execute()
        show_success_message(f"Video added to playlist successfully with ID: {response['id']}")
    except Exception as e:
        handle_error(f"Failed to add video to playlist: {e}")
```
