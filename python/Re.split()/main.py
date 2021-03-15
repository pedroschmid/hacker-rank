import re

if __name__ == "main":
    regex_pattern = r"[,.]"

    print("\n".join(re.split(regex_pattern, input())))