import gradio as gr
import os
from separator import separate_audio

# Ensure temp folder exists
os.makedirs("uploads", exist_ok=True)

def process_audio(file, stem_mode):
    """
    Handles uploaded audio file, runs Demucs separation, and returns MP3 stems + zip.
    """
    if file is None:
        return "No file uploaded.", []

    # Save uploaded file locally
    file_path = os.path.join("uploads", file.name)
    with open(file_path, "wb") as f:
        f.write(file.read())

    # Run separation (4-Stem or 6-Stem)
    try:
        output_paths = separate_audio(file_path, stem_mode)
    except Exception as e:
        return f"Error during separation: {e}", []

    # Prepare Gradio audio previews
    audio_previews = [path for path in output_paths if path.endswith(".mp3")]

    # Return message + previews + zip (zip is last element in output_paths)
    return "Separation complete!", audio_previews + [output_paths[-1]]

# -----------------------------
# Gradio UI
# -----------------------------
with gr.Blocks() as demo:
    gr.Markdown("## 🎵 AI Audio Stem Splitter")
    gr.Markdown(
        "Upload an audio file (MP3/WAV), choose **4-Stem** or **6-Stem** separation, "
        "preview the separated stems, and download individual MP3s or a zip."
    )

    # File upload
    audio_file = gr.File(label="Upload Audio (MP3/WAV)", file_types=[".mp3", ".wav"])

    # Stem mode selection
    stem_option = gr.Radio(
        choices=["4-Stem (vocals, drums, bass, other)", 
                 "6-Stem (vocals, drums, bass, guitar, piano, other)"],
        value="4-Stem (vocals, drums, bass, other)",
        label="Choose Stem Mode"
    )

    # Status / info
    status_text = gr.Textbox(label="Status", interactive=False)

    # Audio previews & downloads
    output_files = gr.File(label="Separated Audio Stems", file_types=[".mp3", ".zip"], interactive=True, file_types_mode="multiple")

    # Button
    separate_btn = gr.Button("Separate Audio")
    separate_btn.click(fn=process_audio, inputs=[audio_file, stem_option], outputs=[status_text, output_files])

demo.launch()
