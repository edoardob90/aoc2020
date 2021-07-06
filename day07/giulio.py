#!/usr/bin/python
import sys
import argparse

def main(filename, test):
    bagDict = {}
    with open(filename) as f:
        if test:
            testResults = f.readline()
            print(testResults)
        for line in f:
            aa = line.rstrip(".\n").split("bags contain ")
            if aa[1] == "no other bags":
                bagDict[aa[0]] = [""]
            else:
                inside = aa[1].split(", ")
                bagDict[aa[0]] = []
                for bag in inside:
                    bagDict[aa[0]].append(bag)








if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Whatever this is going to do")
    parser.add_argument("filename", type = str, help = "The name of the input file")
    parser.add_argument("--test", action="store_true", help="If it is a test, it reads the first line which contains the expected output")


    args = parser.parse_args()
    sys.exit(main(args.filename,args.test))
