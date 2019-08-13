#!/usr/bin/env python3
from template_fsf import template
import argparse
import os
import datetime

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generates folder structure for results for different analysis")
    parser.add_argument('directory', type=str, help="Directory in which to create sub-xx folders",
                        )
    parser.add_argument('starting_number', type=int, help="Starting value of x e.g. 3 inclusive",
                        )
    parser.add_argument('ending_number', type=int, help="Ending value of x, e.g. 49 inclusive",
                        )
    parser.add_argument('number_of_runs', type=int, help="Number of runs per subject",
                        )
    parser.add_argument('-v', '--verbose', help="prints verbosely every action", action="store_true")
    args = parser.parse_args()

    if args.starting_number > args.ending_number:
        raise (ValueError("starting_number is larger than ending_number, that can't happen"))

    if not os.path.isdir(args.directory):
        raise (OSError("Path specified does not exist, try again"))

    abs_path = args.directory

    for x in range(args.starting_number, args.ending_number + 1):
        for y in range(args.number_of_runs):
            sub = "sub-%02d" % x
            run = "run-%02d" % (y + 1)
            with open(os.path.join(abs_path, "{}_{}.fsf".format(sub, run)), "w") as fsf:
                fsf.write(template.format(sub=sub, run=run))

            print("CREATED FILE {}".format(
                os.path.join(abs_path, "{}_{}.fsf".format(sub, run)))) if args.verbose else None


    print("FINISHED CREATING .FSF FILES.") if args.verbose else None

