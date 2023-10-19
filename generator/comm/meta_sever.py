import dbm 
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


class MetaServerBase(object):
    def get_meta(self,ids):
        raise NotImplementedError


class ImgMetaServer(MetaServerBase):
    def __init__(self,db_path) -> None:
        
        logging.info(f'db_path: {db_path}')
        self.db_path = db_path
        self.db = dbm.open(self.db_path,'r')
        
    def get_meta(self,ids):
        ids = str(ids)
        return self.db[ids].decode('utf-8')
    
    def batch_get_meta(self,ids_list):
        
        return [self.db[str(idx)].decode('utf-8') for idx in ids_list] 

    
class VideoMetaServer(MetaServerBase):
    def __init__(self,db_path) -> None:
        
        logging.info(f'db_path: {db_path}')
        self.db_path = db_path
        self.db = dbm.open(self.db_path,'r')
        
    def get_meta(self,ids):
        ids = str(ids)
        return self.db[ids].decode('utf-8')
    
    def batch_get_meta(self,ids_list):
        
        return [self.db[str(idx)].decode('utf-8') for idx in ids_list] 

        
        
    