import subprocess

def predict_calamari(args):
    commands = ["calamari-predict"]

    commands.append("--checkpoint")

    for model in args["models"]:
        commands.append('"' + model + "best.ckpt.json" + '"')
    commands.append("--data PageXML")
    commands.append("--data.gt_extension")
    commands.append('"' + args["gt-ext"] + '"')
    commands.append("--data.pred_extension")
    commands.append('"' + args["pred-ext"] + '"')

    commands.append("--data.images")
    commands.append('"' + args["images"] + '*.png"')

    commands.append('--data.text_index=' + str(args["text-index"]))

    commands.extend(args["options"])
    print(' '.join(commands))
    subprocess.run(' '.join(commands), shell=True)
