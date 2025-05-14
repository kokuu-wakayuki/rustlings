#!/bin/python3

import os
import sys
import toml

PWD = sys.path[0]
os.chdir(f"{PWD}/../../")

STATE_TXT = ".rustlings-state.txt"
CARGO_TOML = "Cargo.toml"

binaries = [i["name"] for i in toml.load(CARGO_TOML)["bin"] if not str(i["name"]).endswith("_sol")]

def count_pass() -> int:
    unused_len_num = 4
    with open(STATE_TXT, "r") as f:
        return len(f.readlines()) - unused_len_num

def count_total() -> int:
    return len(binaries)

def main() -> None:
    print(f"{count_pass()}/{count_total()}")   

if __name__ == "__main__":
    main()
