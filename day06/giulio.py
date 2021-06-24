#!/usr/bin/python
import sys
import argparse

def main(filename, test):
    all_answers = []
    current_answer = []
    counter = 0
    
    with open(filename) as f:
        if test:
            testResults = f.readline()
            print(testResults)
        for line in f:
            if line == "\n":
                all_answers.append(current_answer)
                counter += len(set(current_answer))
                current_answer = []
            else:
                current_answer += line.rstrip()
    counter += len(set(current_answer))
    print("The sum answers with at least one yes is", counter)
                






if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Whatever this is going to do")
    parser.add_argument("filename", type = str, help = "The name of the input file")
    parser.add_argument("--test", action="store_true", help="If it is a test, it reads the first line which contains the expected output")


    args = parser.parse_args()
    sys.exit(main(args.filename,args.test))
