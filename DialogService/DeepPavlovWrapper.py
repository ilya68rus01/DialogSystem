import os
from deeppavlov.core.common.file import read_json
from deeppavlov import configs, train_model
from deeppavlov import build_model
import spacy

nlp = spacy.load('en')

model_config = read_json(configs.doc_retrieval.en_ranker_tfidf_wiki)
model_config["dataset_reader"]["data_path"] = os.path.abspath(os.getcwd()) + "\\Resourses"
model_config["dataset_reader"]["dataset_format"] = "txt"
model_config["train"]["batch_size"] = 1000
doc_retrieval = train_model(model_config)
res = doc_retrieval(['TSTU'])
print(res)
