from generator.tts.tts_generator import TTSGenerator
from generator.tts.paddlespeech_model import PaddleSpeechTTS
from comm.mylog import logger
def build_tts_generator(cfg):
    tts_model = cfg.video_editor.tts_gen.model
    logger.info(f'tts_model: {tts_model}')
    tts_generator = None
    if tts_model != "PaddleSpeechTTS":
        raise ValueError(f'tts_model: {tts_model} not support')
    model = PaddleSpeechTTS(
                            lang=cfg.video_editor.tts_gen.lang,
                            am=cfg.video_editor.tts_gen.am,
                            )
    return TTSGenerator(cfg,model)

    