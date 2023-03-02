from .sites import *
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Available Options")
    for key in SITES:
        parser.add_argument(f"-{key[0]}", f"--{key}", dest=key, action="store_true")
    parser.add_argument("-s", "--search", dest="search")
    parser.add_argument("-p", "--price", dest="price", action="store_true")
    args = vars(parser.parse_args())
    return args
