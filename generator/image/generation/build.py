from generator.image.generation.stable_diffusion import StableDiffusionImgModel,StableDiffusionImg2ImgModel

def build_img_gen_model(cfg):
    
    model_id = cfg.video_editor.visual_gen.image_by_diffusion.model_id
    return StableDiffusionImgModel(model_id)

def build_img2img_gen_model(cfg):
    model_id = cfg.video_editor.visual_gen.image_by_retrieval_then_diffusion.model_id
    return StableDiffusionImg2ImgModel(model_id)