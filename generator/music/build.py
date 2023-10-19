from generator.music.toy import ToyBgmGenerator
from comm.mylog import logger

def build_bgm_generator(cfg):
    bgm_gen_type = cfg.video_editor.bgm_gen.type
    logger.info(f'bgm_gen_type: {bgm_gen_type}')
    return ToyBgmGenerator() if bgm_gen_type == "toy" else None

