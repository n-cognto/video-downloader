#!/usr/bin/env python3
"""
Downloads videos from YouTube, Facebook, and other platforms using yt-dlp
Combines direct library usage with powerful CLI features
"""

import sys
import os
import argparse
from pathlib import Path
from yt_dlp import YoutubeDL

def check_dependencies():
    """Check if FFmpeg is available for post-processing"""
    import shutil
    if not shutil.which('ffmpeg'):
        print("⚠️  Warning: FFmpeg is not installed")
        print("   Some features (audio extraction, format conversion) may not work")
        print("   Install: sudo apt install ffmpeg  (or brew install ffmpeg on macOS)")
        return False
    return True

def download_video(url, audio_only=False, output_dir="downloads", start=1, 
                   quality="best", format_code=None, subtitle=False, 
                   no_playlist=False):
    """
    Download video(s) with flexible options
    
    Args:
        url: Video or playlist URL
        audio_only: Extract audio only (MP3)
        output_dir: Output directory path
        start: Playlist start index (1-based)
        quality: Video quality (best, worst, or height like 720, 1080)
        format_code: Custom format code for advanced users
        subtitle: Download subtitles
        no_playlist: Download single video even if URL is a playlist
    """
    
    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Base options
    ydl_opts = {
        "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
        "ignoreerrors": True,
        "playliststart": start,
        "noplaylist": no_playlist,
        "retries": 5,
        "fragment_retries": 5,
        "progress_hooks": [progress_hook],
    }
    
    # Audio extraction
    if audio_only:
        ydl_opts.update({
            "format": "bestaudio/best",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
        })
        print("🎵 Mode: Audio only (MP3)")
    
    # Video format selection
    else:
        if format_code:
            ydl_opts["format"] = format_code
            print(f"🎬 Mode: Custom format ({format_code})")
        elif quality == "best":
            ydl_opts["format"] = "bestvideo+bestaudio/best"
            print("🎬 Mode: Best quality")
        elif quality == "worst":
            ydl_opts["format"] = "worst"
            print("🎬 Mode: Lowest quality")
        else:
            ydl_opts["format"] = f"bestvideo[height<={quality}]+bestaudio/best[height<={quality}]"
            print(f"🎬 Mode: Up to {quality}p quality")
    
    # Subtitle options
    if subtitle:
        ydl_opts.update({
            "writesubtitles": True,
            "writeautomaticsub": True,
            "subtitleslangs": ["en"],
        })
        print("📝 Subtitles: Enabled")
    
    print(f"📁 Output: {output_path.absolute()}")
    print(f"🔗 URL: {url}\n")
    
    try:
        with YoutubeDL(ydl_opts) as ydl:
            # Extract info first to show what we're downloading
            info = ydl.extract_info(url, download=False)
            
            if 'entries' in info:
                total = len(info['entries'])
                print(f"📋 Playlist detected: {info.get('title', 'Unknown')} ({total} videos)")
                if start > 1:
                    print(f"⏩ Starting from video #{start}\n")
            else:
                print(f"📹 Single video: {info.get('title', 'Unknown')}\n")
            
            # Download
            ydl.download([url])
            print("\n✅ Download completed successfully!")
            return True
            
    except KeyboardInterrupt:
        print("\n\n⚠️  Download cancelled by user")
        return False
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return False

def progress_hook(d):
    """Custom progress display"""
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', 'N/A')
        speed = d.get('_speed_str', 'N/A')
        eta = d.get('_eta_str', 'N/A')
        print(f"\r⬇️  {percent} at {speed} (ETA: {eta})   ", end='', flush=True)
    elif d['status'] == 'finished':
        print("\r✓ Download finished, processing...             ", flush=True)

def list_formats(url):
    """List all available formats for a video"""
    print(f"📋 Available formats for: {url}\n")
    
    ydl_opts = {
        "quiet": False,
        "no_warnings": False,
    }
    
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            
            if 'formats' in info:
                print("\n{:<10} {:<15} {:<10} {:<15} {:<10}".format(
                    "FORMAT", "EXTENSION", "RESOLUTION", "FILESIZE", "NOTE"
                ))
                print("-" * 70)
                
                for f in info['formats']:
                    format_id = f.get('format_id', 'N/A')
                    ext = f.get('ext', 'N/A')
                    resolution = f.get('resolution', 'audio only' if f.get('vcodec') == 'none' else 'N/A')
                    filesize = f.get('filesize_approx', f.get('filesize', 0))
                    filesize_str = f"{filesize / 1024 / 1024:.1f}MB" if filesize else "N/A"
                    note = f.get('format_note', '')
                    
                    print("{:<10} {:<15} {:<10} {:<15} {:<10}".format(
                        format_id, ext, resolution, filesize_str, note
                    ))
                
                print("\n💡 Use -f FORMAT_ID to download a specific format")
                print("   Example: python script.py download URL -f 137+140")
            else:
                print("❌ No format information available")
                
    except Exception as e:
        print(f"❌ Error listing formats: {e}")

def main():
    parser = argparse.ArgumentParser(
        description='Download videos from YouTube, Facebook, and 1000+ other sites',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s download "https://www.youtube.com/watch?v=VIDEO_ID"
  %(prog)s download "PLAYLIST_URL" --start 5
  %(prog)s download "VIDEO_URL" -o ~/Downloads -q 720
  %(prog)s download "VIDEO_URL" --audio
  %(prog)s download "VIDEO_URL" -s
  %(prog)s list "VIDEO_URL"
  %(prog)s download "VIDEO_URL" -f "137+140"
  %(prog)s download "VIDEO_URL" --no-playlist
        """
    )
    
    parser.add_argument('command', choices=['download', 'list'],
                       help='Command: download video or list available formats')
    parser.add_argument('url', help='Video or playlist URL')
    parser.add_argument('-o', '--output', default='downloads',
                       help='Output directory (default: downloads)')
    parser.add_argument('-q', '--quality', default='best',
                       help='Video quality: best, worst, or height (720, 1080, etc.)')
    parser.add_argument('-a', '--audio', action='store_true',
                       help='Download audio only (MP3 format)')
    parser.add_argument('-f', '--format',
                       help='Specific format code (use "list" command to see options)')
    parser.add_argument('-s', '--subtitle', action='store_true',
                       help='Download subtitles')
    parser.add_argument('--start', type=int, default=1,
                       help='Playlist start index (default: 1)')
    parser.add_argument('--no-playlist', action='store_true',
                       help='Download only the video, not the playlist')
    
    args = parser.parse_args()
    
    # Check dependencies
    check_dependencies()
    print()
    
    if args.command == 'list':
        list_formats(args.url)
    elif args.command == 'download':
        download_video(
            url=args.url,
            audio_only=args.audio,
            output_dir=args.output,
            start=args.start,
            quality=args.quality,
            format_code=args.format,
            subtitle=args.subtitle,
            no_playlist=args.no_playlist
        )
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
