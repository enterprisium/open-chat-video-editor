from generator.video.retrieval.build import build_QueryTextVideoEmbedServer, build_VideoFiassKnnServer
from generator.video.video_generator import VideoGenByRetrieval
from generator.comm.meta_sever import VideoMetaServer
from comm.mylog import logger

def build_video_generator(cfg):
    video_generator = None
    visual_gen_type = cfg.video_editor.visual_gen.type
    logger.info(f'visual_gen_type: {visual_gen_type}')
    if visual_gen_type != "video_by_retrieval":
        raise ValueError(f'visual_gen_type: {visual_gen_type} not support')

    logger.info('start build_QueryTextEmbedServer')
    query_model = build_QueryTextVideoEmbedServer(cfg)

    # build faiss index 
    logger.info('start build_VideoFiassKnnServer')
    index_server = build_VideoFiassKnnServer(cfg)

    # build meta server 
    logger.info('start build_VideoMetaServer')

    meta_server = VideoMetaServer(cfg.video_editor.visual_gen.video_by_retrieval.meta_path)

    return VideoGenByRetrieval(cfg,query_model,index_server,meta_server)