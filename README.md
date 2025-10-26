# yt-cc-capture

**YouTube Closed Captions Capture** — a CLI tool to download YouTube video transcripts (closed captions) as plain `.txt` files.

## Features

- Fetches captions via the YouTube Transcript API
- Saves the transcript as `<video_id>.txt` in your chosen output directory
- Graceful handling of missing or malformed input

## Installation

```bash
poetry install
```

## Usage

```bash
poetry run yt-cc-capture --video-id <VIDEO_ID> [--out-dir <OUTPUT_DIR>]
```

### Arguments

- `--video-id` (required): YouTube video ID (e.g. `dQw4w9WgXcQ`)
- `--out-dir` (optional): Output directory (defaults to `./transcripts`). Must already exist.

### Example

```bash
poetry run yt-cc-capture --video-id CH3ji8u3hfs --out-dir ./my_transcripts
```

## Project Structure

```
yt-cc-capture/
├── pyproject.toml
├── README.md
└── src/
    └── yt_cc_capture/
        └── main.py
```

## License
MIT © Eugene Odeluga
