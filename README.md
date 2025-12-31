# 🎬 Universal Video Downloader

A powerful, flexible command-line tool for downloading videos from YouTube, Facebook, Instagram, Twitter, and 1000+ other platforms. Built with Python and yt-dlp.

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ✨ Features

- 📹 **Multi-Platform Support** - Download from YouTube, Facebook, Instagram, TikTok, Twitter, and [1000+ sites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)
- 🎵 **Audio Extraction** - Convert videos to MP3 format
- 📋 **Playlist Support** - Download entire playlists with resume capability
- 🎯 **Quality Selection** - Choose specific resolutions (720p, 1080p, 4K, etc.)
- 📝 **Subtitle Download** - Automatic subtitle fetching
- 🔄 **Robust Error Handling** - Auto-retry on failures (5 attempts)
- ⚡ **Fast & Efficient** - Direct yt-dlp library integration
- 🎨 **Clean CLI** - Intuitive command-line interface with helpful messages

## 📋 Requirements

- Python 3.7 or higher
- yt-dlp
- FFmpeg (for audio extraction and format conversion)

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/n-cognto/video-downloader.git
   cd video-downloader
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install yt-dlp
   ```

4. **Install FFmpeg:**
   
   **Ubuntu/Debian:**
   ```bash
   sudo apt update
   sudo apt install ffmpeg
   ```
   
   **macOS:**
   ```bash
   brew install ffmpeg
   ```
   
   **Fedora:**
   ```bash
   sudo dnf install ffmpeg
   ```
   
   **Windows:**
   Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH

5. **Make script executable (optional):**
   ```bash
   chmod +x video_downloader.py
   ```

## 📖 Usage

### Basic Syntax

```bash
python video_downloader.py [command] [url] [options]
```

### Commands

- `download` - Download video(s)
- `list` - List all available formats for a video

### Common Examples

#### Download a single video (best quality)
```bash
python video_downloader.py download "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

#### Download with specific quality
```bash
python video_downloader.py download "VIDEO_URL" -q 720
python video_downloader.py download "VIDEO_URL" -q 1080
```

#### Download audio only (MP3)
```bash
python video_downloader.py download "VIDEO_URL" --audio
```

#### Download to specific directory
```bash
python video_downloader.py download "VIDEO_URL" -o ~/Downloads
```

#### Download with subtitles
```bash
python video_downloader.py download "VIDEO_URL" -s
```

#### Download entire playlist
```bash
python video_downloader.py download "PLAYLIST_URL"
```

#### Resume playlist from specific video
```bash
python video_downloader.py download "PLAYLIST_URL" --start 5
```

#### Download single video from playlist
```bash
python video_downloader.py download "PLAYLIST_VIDEO_URL" --no-playlist
```

#### List available formats
```bash
python video_downloader.py list "VIDEO_URL"
```

#### Download specific format
```bash
python video_downloader.py download "VIDEO_URL" -f "137+140"
```

### All Options

```
positional arguments:
  command               Command: download video or list available formats
  url                   Video or playlist URL

optional arguments:
  -h, --help            Show help message and exit
  -o, --output DIR      Output directory (default: downloads)
  -q, --quality QUALITY Video quality: best, worst, or height (720, 1080, etc.)
  -a, --audio           Download audio only (MP3 format)
  -f, --format FORMAT   Specific format code (use "list" command to see options)
  -s, --subtitle        Download subtitles
  --start INDEX         Playlist start index (default: 1)
  --no-playlist         Download only the video, not the playlist
```

## 🌐 Supported Platforms

This tool supports 1000+ websites including:

- **Video Platforms:** YouTube, Vimeo, Dailymotion, Twitch
- **Social Media:** Facebook, Instagram, Twitter/X, TikTok, Reddit
- **Educational:** Coursera, Udemy, Khan Academy
- **News:** CNN, BBC, NBC
- **And many more...**

[See full list of supported sites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)

## 💡 Tips & Tricks

### Quality Selection
- `best` - Highest available quality (default)
- `worst` - Lowest quality (faster downloads, smaller files)
- `720`, `1080`, `1440`, `2160` - Specific resolutions

### Format Codes
Use the `list` command to see all available formats, then download specific ones:
```bash
python video_downloader.py list "VIDEO_URL"
python video_downloader.py download "VIDEO_URL" -f "137+140"
```

### Playlist Management
If a large playlist download fails, resume from where it stopped:
```bash
# Original playlist had 50 videos, stopped at video 23
python video_downloader.py download "PLAYLIST_URL" --start 23
```

### Audio Quality
The default audio extraction uses 192kbps MP3, which provides good quality while keeping file sizes reasonable.

## 🐛 Troubleshooting

### "FFmpeg not found" warning
Install FFmpeg using the instructions in the Installation section. Audio extraction won't work without it.

### "Download failed" errors
- Check your internet connection
- Verify the URL is correct and the video is publicly accessible
- Some videos may be geo-restricted or require authentication
- Try updating yt-dlp: `pip install --upgrade yt-dlp`

### Slow downloads
- Try a lower quality with `-q 480` or `-q 720`
- Check your internet speed
- Some platforms rate-limit downloads

### "Unable to extract" errors
- The platform may have changed its structure
- Update yt-dlp to the latest version: `pip install --upgrade yt-dlp`

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚖️ Legal Notice

This tool is for personal use only. Please respect copyright laws and the terms of service of the platforms you download from. The developers are not responsible for any misuse of this software.

- Only download videos you have permission to download
- Respect copyright and intellectual property rights
- Follow the terms of service of each platform

## 🙏 Acknowledgments

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - The powerful engine behind this tool
- [FFmpeg](https://ffmpeg.org/) - For audio/video processing
- All contributors who help improve this project

## 📬 Contact

If you have questions or suggestions, please open an issue on GitHub.

---

**⭐ If you find this tool useful, please consider giving it a star on GitHub!**
