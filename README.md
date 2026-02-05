# AI Audio Stem Splitter 🎵

AI Audio Stem Splitter is a web-based tool for separating audio tracks into individual stems (vocals, drums, bass, guitar, piano, and others) using AI. Built with **Demucs** and **Gradio**, it runs online via **Hugging Face Spaces**, allowing users to upload songs, preview stems, and download them individually or as a zip.

## Features

- 4-Stem mode: vocals, drums, bass, other
- 6-Stem mode: vocals, drums, bass, guitar, piano, other
- MP3 conversion (44.1kHz, 320kbps)
- Audio previews
- Download individual stems or a zip file
- CPU-friendly (works on free Hugging Face tier)

## Usage

1. Upload an **MP3 or WAV** file.
2. Select **4-Stem** or **6-Stem** separation.
3. Click **Separate Audio**.
4. Preview separated stems.
5. Download individual MP3 files or the ZIP archive.

> ⚠️ **Note:** For CPU performance, recommended audio length ≤ 60 seconds on free Hugging Face Spaces.

## Installation (optional, for local testing)

```bash
git clone <repo-url>
cd AI-Audio-Stem-Splitter
pip install -r requirements.txt
