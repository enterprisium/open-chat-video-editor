import random
class ToyBgmGenerator(object):
    def __init__(self) -> None:
        self.bgms = [
            "generator/music/12Mornings.mp3",
            "generator/music/AcousticBlues.mp3",
            "generator/music/AllGoodInTheWood.mp3",
            "generator/music/ClapAlong.mp3",
        ]
    
    def run(self,):
        local_file = random.choice(self.bgms)
        return {
            'bgm_local_file': local_file,
        }