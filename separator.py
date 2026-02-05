import os
import subprocess
from utils import convert_and_zip  # We'll create this in utils.py

# CPU-safe Demucs separation
def separate_audio(file_path, stem_mode="4-Stem"):
    """
    Separates an audio file into stems using Demucs.
    
    Args:
        file_path (str): Path to uploaded audio file (MP3/WAV)
        stem_mode (str): "4-Stem" or "6-Stem"
    
    Returns:
        List[str]: List of output file paths (MP3 stems + zip)
    """
    # Choose Demucs model
    if stem_mode.startswith("4-Stem"):
        model = "htdemucs_ft"   # CPU-friendly 4-stem
        stems = ["vocals", "drums", "bass", "other"]
    else:
        model = "htdemucs_6s"   # 6-stem (includes guitar + piano)
        stems = ["vocals", "drums", "bass", "guitar", "piano", "other"]

    # Run Demucs
    subprocess.run(["demucs", "-n", model, file_path], check=True)

    # Determine Demucs output directory
    input_name = os.path.splitext(os.path.basename(file_path))[0]
    demucs_out_dir = os.path.join("separated", model, input_name)

    # Convert WAV stems to MP3 + create zip
    output_paths = convert_and_zip(demucs_out_dir, stems, input_name)

    return output_paths
