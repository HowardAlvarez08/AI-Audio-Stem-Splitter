import os
from pydub import AudioSegment
import shutil

def convert_and_zip(demucs_out_dir, stems, input_name):
    """
    Converts WAV stems to MP3 and zips them.

    Args:
        demucs_out_dir (str): Path where Demucs saved WAV stems
        stems (list): List of stem names (e.g., ["vocals","drums","bass","other"])
        input_name (str): Original audio file name (without extension)

    Returns:
        List[str]: Paths to MP3 files + zip
    """
    # Create output folder for MP3s
    output_dir = f"converted_mp3_{input_name}"
    os.makedirs(output_dir, exist_ok=True)

    mp3_paths = []

    for stem in stems:
        wav_path = os.path.join(demucs_out_dir, f"{stem}.wav")
        mp3_path = os.path.join(output_dir, f"{input_name} ({stem}).mp3")

        if os.path.exists(wav_path):
            # Convert WAV to MP3
            audio = AudioSegment.from_wav(wav_path)
            audio = audio.set_frame_rate(44100).set_channels(2)
            audio.export(mp3_path, format="mp3", bitrate="320k")
            mp3_paths.append(mp3_path)
        else:
            print(f"[Warning] WAV file not found: {wav_path}")

    # Create ZIP archive
    zip_name = f"{input_name}_stems"
    shutil.make_archive(zip_name, 'zip', output_dir)

    # Add zip path to output list
    mp3_paths.append(zip_name + ".zip")

    return mp3_paths
