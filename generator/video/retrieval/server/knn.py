import numpy as np
import os
import faiss
import logging

class VideoFiassKnnServer(object):
    def __init__(self,
                 index_path,
                 ):
        # loading faiss index
        # self.top_k = 10
        self.nprobe = 2048
        self.index_path = index_path

        self.index = faiss.read_index(index_path)
        if isinstance(self.index,faiss.swigfaiss.IndexPreTransform):
            faiss.ParameterSpace().set_index_parameter(self.index, "nprobe", self.nprobe)
        else:
            logging.info(f'set nprobe: {self.nprobe}')
            self.index.nprobe = self.nprobe

        
    def search(self,query_emebed,top_k=50):
        '''
        query_emebed: numpy array
        '''
        query_emebed = query_emebed.astype('float32')
        distances, indices = self.index.search(query_emebed, top_k)
        return  distances, indices

    def batch_search(self,query_list):
        pass