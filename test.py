import json
import requests
import numpy as np 

def test_predict_tfserving(text, endpoint):
    text_processed = text_preprocessing(text, dict_word=word_dict)

    json_data = json.dumps({"instances": text_processed})

    response = requests.post(endpoint, data=json_data)
    prediction = response.json()["predictions"][0]
    print(f"Prediction from TFServing: {prediction}")

    list_class_name = ["negative", "neutral", "positive "]

    index_class_predicted = np.argmax(prediction)
    print(f"Index class predicted : {index_class_predicted}")
    print(f"Class name predicted : {index_class_name[index_class_predicted]}")

test_predict_tfserving(
    text="enak sekali bikin mau beli satu truk",
    endpoint=" "
)
