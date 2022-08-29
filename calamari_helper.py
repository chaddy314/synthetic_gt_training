import sys
import json
from train_calamari import train_calamari_model
from predict_calamari import predict_calamari
from eval_evalamari import eval_calamari


def main():
    json_path = sys.argv[1]
    calamari_args = {}



    with open(json_path) as f:
        json_file = json.load(f)
        calamari_args = json_file["calamari"]

    train_calamari_model(calamari_args["calamari-train"])

    for predict in calamari_args["calamari-predict"]:
        predict_calamari(predict)

    for evaluate in calamari_args["calamari-eval"]:
        eval_calamari(evaluate)


if __name__ == "__main__":
    main()