from TTS.api import TTS

tts = TTS("tts_models/zh-CN/baker/tacotron2-DDC-GST")

tts.tts_to_file(text="你好，吴女士",
                file_path="/Users/chensen/Downloads/output.wav")
