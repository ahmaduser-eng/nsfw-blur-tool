# NSFW Video Blur Tool

This tool detects NSFW regions in a video and blurs them in real-time processing.
Single video at a time.

## How to Use with GitHub Actions
1. Create a new GitHub repo
2. Upload all these files
3. Enable Actions in your repo
4. Run the "Build EXE" workflow
5. Download the `.exe` from Releases

## Running locally
```bash
python prepare_model.py
python nsfw_video_blur.py path/to/video.mp4
```