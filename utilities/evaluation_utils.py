from typing import List, Dict
#import torch
#from transquest.algo.sentence_level.siamesetransquest.run_model import SiameseTransQuestModel
import sacrebleu
from typing import List, Dict
from unittest import result

#from matplotlib.font_manager import json_load
import json

def calculate_bleu(results: List[Dict[str, str]]) -> float:
    """
    Calculate the BLEU score for a collection of results.

    :param results: collection of dictionary with entries containing target sequences and generated sequences
    :return: BLEU score
    """
    '''model = SiameseTransQuestModel("TransQuest/siamesetransquest-da-en_zh-wiki")
    #model = SiameseTransQuestModel("xlmroberta","TransQuest/siamesetransquest-da-en_zh-wiki",labels=["OK", "BAD"], use_cuda=torch.cuda.is_available())
    #model = MicroTransQuestModel("xlmroberta", "TransQuest/microtransquest-en_lv-pharmaceutical-nmt", labels=["OK", "BAD"], use_cuda=torch.cuda.is_available())'''
    candidates = [dct['decoded_sequence'] for dct in results]
    #print(candidates)
    references = [[dct['target_sequence'] for dct in results]]
    #predictions = model.predict([[candidates, references]])
    #print("TransQuest Result:"+predictions)
    bleu = sacrebleu.corpus_bleu(candidates, references)
    #data = json.load(results)
    with open('QEdata.json', 'w') as f:
        json.dump(results, f)
    f.close()
    return bleu.score