import sys
import argparse
from youtube_transcript_api import YouTubeTranscriptApi
from pathlib import Path

def main():
  parser = argparse.ArgumentParser(description='Downloads closed captions from YouTube videos as transcripts')
  parser.add_argument('--video-id', type=str, required=True, help='YouTube video id')
  parser.add_argument('--out-dir', type=str, required=False, help='Transcript text file output directory')
  args = parser.parse_args()
  
  # Normalise input
  video_id = args.video_id.strip()
  out_dir = (args.out_dir.strip().rstrip('/') if args.out_dir else './transcripts')
  print (f'video_id: {video_id}\nout_dir: {out_dir}\n')
  
  # Check output location exists
  file_path = Path(out_dir)  
  if not file_path.exists():
    print(f'location: {out_dir} cannot be found')
    sys.exit(1)
    
  output_file = file_path / f'{video_id}.txt'

  try:    
    ytt_api = YouTubeTranscriptApi()
    print('Fetching captions...')
    transcript = ytt_api.fetch(video_id)
    full_text = '\n'.join(item.text for item in transcript)
    
    # Save the transcript to a text file
    with open(output_file, 'w', encoding='utf-8') as f:
      f.write(full_text)
  except Exception as e:
    print(f'Error: {e}')

