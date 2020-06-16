import os
from deeppavlov import configs, train_model
from deeppavlov.core.common.file import read_json
from deeppavlov import build_model
import numpy as np

class DeepPavlovWrapper:
    def __init__(self):
        self.model_qa = build_model(configs.squad.squad_ru_bert, download= True)
        self.directory = os.path.abspath(os.getcwd()) + "\\Resourses"
        self.files = os.listdir(self.directory)
        self.data = ''
        for i in range(np.size(self.files)):
            file = open(self.directory + '\\' + self.files[i], 'r',encoding='utf-8')
            self.data += file.read()

    def get_answer_on_question(self,question):
        answer = self.model_qa([self.data], [question])
        return answer


# model_config = read_json(configs.doc_retrieval.ru_ranker_tfidf_wiki)
# model_config["dataset_reader"]["data_path"] = os.path.abspath(os.getcwd())+"/Resourses"
# model_config["dataset_reader"]["dataset_format"] = "txt"
# model_config["train"]["batch_size"] = 100
# print("work!")
# doc_retrieval = train_model(model_config)
# print(doc_retrieval(['Тамбов']))
# # Download all the SQuAD models
# print("Тут еще работает")
# squad = build_model(configs.squad.squad_ru_rubert_infer, download=True)
# print("Тут не работает")
# # Do not download the ODQA models, we've just trained it
# odqa = build_model(configs.odqa.ru_odqa_infer_wiki_rubert, download=False)
# print("Или тут")
# answers = odqa(["В каком году был образован ТГТУ?"])
# print("Ну может тут")
# print(answers)
