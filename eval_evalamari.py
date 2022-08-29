import subprocess

def eval_calamari(args):
    commands = ["calamari-eval"]

    commands.append("--gt PageXML")
    commands.append("--gt.xml_files")
    commands.append('"' + args["xml-files"] + '"')
    commands.append("--gt.pred_extension")
    commands.append('"' + args["pred-ext"] + '"')

    commands.append("--xlsx_output")
    commands.append('"' + args["xlsx-output"] + '"')

    commands.extend(args["options"])
    print(' '.join(commands))
    subprocess.run(' '.join(commands), shell=True)
