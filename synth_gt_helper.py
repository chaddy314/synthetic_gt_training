import os
import sys
import json
from create_synth_gt import create_lines
from pathlib import Path


def main():
    json_path = sys.argv[1]
    source_text_file = ""
    source_eval_text_file = ""
    output_dir = ""
    font_dir = ""
    line_size = ""
    eval_size = ""
    output_fonts = False
    filter_common_confusions = False
    check_for_caps = False
    trdg_params = {}
    use_eval_text_file = False


    with open(json_path) as f:
        json_file = json.load(f)
        source_text_file = json_file["synthgt"]["source-text-file"]
        source_eval_text_file = json_file["synthgt"]["source-eval-text-file"]
        output_dir = json_file["synthgt"]["output_dir"]
        font_dir = json_file["synthgt"]["font_dir"]
        line_size = json_file["synthgt"]["line-size"]
        eval_size = json_file["synthgt"]["eval-size"]
        output_fonts = json_file["synthgt"]["output-fonts"]
        filter_common_confusions = json_file["synthgt"]["filter-common-confusions"]
        check_for_caps = json_file["synthgt"]["check-for-caps"]
        trdg_params = json_file["synthgt"]["trdg"]

        use_eval_text_file = json_file["general"]
    if use_eval_text_file:
        num_lines = sum(1 for line in open(source_text_file))
        if num_lines < line_size + eval_size:
            print("WARNING: Training overlaps with Eval Data")

    if os.path.isfile(source_text_file):
        Path(output_dir + "train/").mkdir(parents=True, exist_ok=True)
        create_lines(source_text_file, line_size, font_dir, output_dir + "train/", output_fonts,
                     filter_common_confusions, check_for_caps, trdg_params)
        Path(output_dir + "val/").mkdir(parents=True, exist_ok=True)
        if use_eval_text_file and os.path.isfile(source_eval_text_file):
            create_lines(source_eval_text_file, eval_size, font_dir, output_dir + "val/", output_fonts,
                         filter_common_confusions, check_for_caps, trdg_params)
        else:
            create_lines(source_text_file, line_size, font_dir, output_dir + "val/", output_fonts,
                         filter_common_confusions, check_for_caps, trdg_params, reverse_lines=True)

if __name__ == "__main__":
    main()