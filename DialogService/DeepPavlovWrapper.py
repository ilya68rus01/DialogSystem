from deeppavlov import build_model, configs
from deeppavlov import configs
from deeppavlov.core.common.file import read_json
from deeppavlov import configs, train_model
from deeppavlov import configs
from deeppavlov.core.commands.train import train_evaluate_model_from_config


model_config = read_json(configs.doc_retrieval.ru_ranker_tfidf_wiki)
model_config["dataset_reader"]["data_path"] = "/Users/Ilya/PycharmProjects/DialogSystem/Resourses/"
model_config["dataset_reader"]["dataset_format"] = "txt"
doc_retrieval = train_model(model_config)
#print(doc_retrieval(['В каком году образован ТГТУ?']))


#models = BertSQuADModel(bert_config_file=configs.squad.squad_bert, keep_prob=0.1)
#
# models.fit(["Тамбовский государственный технический университет (ТГТУ) образован в 1958 году как филиал\
#  Московского института химического машиностроения в связи с интенсивным развитием в нашей стране химической\
# промышленности и предприятий химического машиностроения. Его возглавил Федор Семенович Полянский.\
# Открытие в 1958 году Тамбовского филиала Московского института химического машиностроения было важным шагом\
# в решении задач обеспечения народного хозяйства страны кадрами в области создания, эксплуатации и ремонта\
# химической техники. По мере развития химической промышленности и химического машиностроения в СССР росла\
# и потребность в кадрах. Вузом, тогда полностью специализированным на подготовке инженеров для химического\
# машиностроения, оставался только МИХМ. К концу 1950-х годов проблема открытия еще одного высшего учебного\
# заведения такого типа назрела окончательно.Выбор Тамбова для размещения нового института не был случайным,\
# поскольку в 1940–1950-е годы в нашем регионе быстрыми темпами развивалось промышленное производство, в том числе и химическое машиностроение."])
