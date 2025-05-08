#!/bin/python3

import os
import sys
import toml

PWD = sys.path[0]
os.chdir(f"{PWD}/../../")

CARGO_TOML = "Cargo.toml"

binaries = [i["name"] for i in toml.load(CARGO_TOML)["bin"]]

def test_bin(bin_name: str) -> bool:
    result = os.system(f"rustlings run {bin_name}")
    return result == 0

def count_pass() -> int:
    cnt = 0
    for bin_name in binaries:
        if test_bin(bin_name):
            cnt += 1
    return cnt

def count_total() -> int:
    return len(binaries)

def main() -> None:
    print(f"{count_pass()} {count_total()}")   

if __name__ == "__main__":
    main()
