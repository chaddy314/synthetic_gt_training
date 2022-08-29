import sys
import json
import subprocess
from pathlib import Path

def train_calamari_model(args, warmstart_path=""):
    commands = ["calamari-train"]

    if args["rel-fold-data-path"]and args["training-data"] != "skip-training":
        for fold_dir in args["rel-fold-data-path"]:
            if args["training-data"] == "lines":
                if args["split-train"] == "":
                    commands.append("--train.images")
                    commands.append('"' + args["dataset-path"] + "train/" + fold_dir + "*.png" + '"')
                    commands.append("--val.images")
                    commands.append('"' + args["dataset-path"] + "val/" + fold_dir + "*.png" + '"')
                else:
                    commands.append(args["split-train"])
                    commands.append("--train.images")
                    commands.append('"' + args["dataset-path"] + "train/" + fold_dir + "*.png" + '"')
            elif args["training-data"] == "page":
                commands.append("--train PageXML")
                if args["split-train"] == "":
                    commands.append("--train.images")
                    commands.append('"' + args["dataset-path"] + "train/" + fold_dir + "*.png" + '"')
                    commands.append("-val PageXML")
                    commands.append("--val.images")
                    commands.append('"' + args["dataset-path"] + "val/" + fold_dir + "*.png" + '"')
                else:
                    commands.append(args["split-train"])
                    commands.append("--train.images")
                    commands.append('"' + args["dataset-path"] + "train/" + fold_dir + "*.png" + '"')
            commands.append("--trainer.output_dir")
            commands.append('"' + args["model-path"] + fold_dir + '"')
            Path(args["model-path"]).mkdir(parents=True, exist_ok=True)
            commands.append("--n_augmentations")
            commands.append(str(args["augmentations"]))
            commands.append("--early_stopping.n_to_go")
            commands.append(str(args["early-stopping"]))
            commands.extend(args["options"])
            if warmstart_path != "":
                commands.append("--warmstart.model")
                commands.append(warmstart_path)
            print(' '.join(commands))
            subprocess.run(' '.join(commands), shell=True)
    elif args["training-data"] in ["lines", "page"]:
        if args["training-data"] == "lines":
            if args["split-train"] == "":
                commands.append("--train.images")
                commands.append('"' + args["dataset-path"]+ "train/*.png" + '"')
                commands.append("--val.images")
                commands.append('"' + args["dataset-path"] + "val/*.png" + '"')
            else:
                commands.append(args["split-train"])
                commands.append("--train.images")
                commands.append('"' + args["dataset-path"] + "train/*.png" + '"')
        elif args["training-data"] == "page":
            commands.append("--train PageXML")
            if args["split-train"] == "":
                commands.append("--train.images")
                commands.append('"' + args["dataset-path"] + "train/*.png" + '"')
                commands.append("-val PageXML")
                commands.append("--val.images")
                commands.append('"' + args["dataset-path"] + "val/*.png" + '"')
            else:
                commands.append(args["split-train"])
                commands.append("--train.images")
                commands.append('"' + args["dataset-path"] + "train/*.png" + '"')
        commands.append("--trainer.output_dir")
        commands.append('"' + args["model-path"] + '"')
        Path(args["model-path"]).mkdir(parents=True, exist_ok=True)
        commands.append("--n_augmentations")
        commands.append(str(args["augmentations"]))
        commands.append("--early_stopping.n_to_go")
        commands.append(str(args["early-stopping"]))
        commands.extend(args["options"])
        if warmstart_path != "":
            commands.append("--warmstart.model")
            commands.append(warmstart_path)
        print(' '.join(commands))
        subprocess.run(' '.join(commands), shell=True)




        if args["training-data"] != "skip-training" and args["warmstart"] and not args["rel-fold-data-path"]:
            train_calamari_model(args["warmstart"]["calamari-train"], args["model-path"] + "best.ckpt.json")


