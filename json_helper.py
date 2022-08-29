import os
import sys
import json


def main():
    json_path = sys.argv[1]
    get_var = sys.argv[2]
    general = "general"
    if len(sys.argv) > 3:
        general = sys.argv[3]

    with open(json_path) as f:
        json_file = json.load(f)
        print(json_file[general][get_var])


if __name__ == "__main__":
    main()
