
import openai 
import os
import re
from comm.mylog import logger
from comm.url_parser import get_paragraph_texts

# openai.organization = os.getenv("OPENAI_ORG_ID")
# openai.api_key = os.getenv("OPENAI_API_KEY")
def is_all_chinese(strs):
    return all('\u4e00' <= _char <= '\u9fa5' for _char in strs)

def is_contains_chinese(strs):
    return any('\u4e00' <= _char <= '\u9fa5' for _char in strs)
class ChatGPTModel(object):
    def __init__(self,cfg,
                 organization,
                 api_key,
                 ) -> None:
        self.cfg = cfg
        openai.organization = organization
        openai.api_key = api_key
        # ch_prompt = ''
    def run(self, input_text):
        contain_ch = False
        if is_contains_chinese(input_text):
            prompt = f"请以{input_text}为内容，生成100字的短视频文案"
            contain_ch = True
        else:
            prompt = f"Please use {input_text} as the content to generate a 50-word short video copy"

        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=400,
        stream=False,
        echo=False,)
        text = response.choices[0].text
        logger.info(f"chatgpt response: {text}")
        text = text.replace('\n','')

        # split text 
        sentences = re.split("[,|，|！|.|?|!|。]",text)
        sentences = [s for s in sentences if len(s) > 0]
        logger.info(f'sentences: {sentences}')
        out_info = []
        resp = {}
        # 生成的文案是中文文案
        if contain_ch:
            resp['lang'] = 'zh'
            for s in sentences:
                en_s = self._translate(s)
                info = {
                    'zh':s,
                    'en':en_s,
                }
                out_info.append(info)
        # 生成的文案是英文文案
        else:
            resp["lang"] = 'en'
            for s in sentences:
                info = {
                    'en':s,
                }
                out_info.append(info)
        resp["out_text"] = out_info
        return resp
            
    
    def _translate(self,text):
        prompt = "将以下句子翻译成英文:\n\n" + text +'\n\n1'
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=400,
        stream=False,
        echo=False,)
        out_text = response.choices[0].text
        logger.info(f'_translate out_text: {out_text}')

        return out_text.replace('\n','').replace('. ','')


class URL2TextChatGPTModel(object):
    
    def __init__(self,cfg,
                 organization,
                 api_key,
                 ) -> None:
        self.cfg = cfg
        openai.organization = organization
        openai.api_key = api_key
    
    def _ask(self,question):
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=question,
        max_tokens=400,
        stream=False,
        echo=False,)
        return response.choices[0].text

    def _translate(self,text):
        prompt = "将以下句子翻译成英文:\n\n" + text +'\n\n1'
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=400,
        stream=False,
        echo=False,)
        out_text = response.choices[0].text
        logger.info(f'_translate out_text: {out_text}')

        return out_text.replace('\n','').replace('. ','')
    def run(self, url):
        texts = get_paragraph_texts(url)
        logger.info(f'url out texts: {texts}')
        resp = dict()
        # resp['']
        out_texts = []
        out_info = []
        for s in texts:
            # info = {}
            if len(s) >= 100:
                prompt = f"请将以下内容：{s}\n 摘要出30字的短视频文案"
                response_text = self._ask(prompt)
                logger.info(f'response_text: {response_text}')
                out_texts.append(response_text)
                        
                        # final_text.append(response_text)
            else:
                out_texts.append(s)

        out_texts = "".join(out_texts)
        logger.info(f'tmp out_texts: {out_texts}')
        prompt = f'请根据一下内容{out_texts}\n，生成一个100字左右的不含英文的短视频文案'

        final_text = self._ask(prompt)
        logger.info(f'final_text: {final_text}')

        sentences = re.split("[,|，|！|.|?|!|。]",final_text)
        sentences = [s for s in sentences if len(s) > 0]
        logger.info(f'sentences: {sentences}')
        out_info = []
        for s in sentences:
            en_s = self._translate(s)
            info = {
                'zh':s,
                'en':en_s,
            }
            out_info.append(info)

        resp['lang'] = 'zh'
        resp["out_text"] = out_info
        return resp
               
 
        
    
    
    
        
            
        
    