```python
import frontend.oauth2_integration as oauth2
import frontend.error_handling_feedback as feh
import backend.spectrogram_generation as spectrogram
import backend.video_creation as video
import backend.youtube_upload as youtube
import backend.error_handling_feedback as beh

def main():
    try:
        # OAuth2 Integration
        oauth2.authorize_access()

        # Spectrogram Generation
        audio_file_data = spectrogram.generate_spectrogram()

        # Video Creation
        video_data = video.create_video(audio_file_data)

        # YouTube Upload
        youtube.upload_video(video_data)

        # Success Notification
        feh.success_notification("Upload Successful")

    except Exception as e:
        # Error Handling & Feedback
        feh.error_message(str(e))
        beh.error_message(str(e))

if __name__ == "__main__":
    main()
```