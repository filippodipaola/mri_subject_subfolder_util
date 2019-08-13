#!/usr/bin/env python3
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
    parser.add_argument('-v', '--verbose', help="prints verbosely every action", action="store_true")
    args = parser.parse_args()

    if args.starting_number > args.ending_number:
        raise (ValueError("starting_number is larger than ending_number, that can't happen"))

    if not os.path.isdir(args.directory):
        raise (OSError("Path specified does not exist, try again"))

    abs_path = args.directory

    for i in range(args.starting_number, args.ending_number + 1):
        path = os.path.join(abs_path, "sub-%02d" % i)
        try:
            os.mkdir(path)
            print("[%s] PATH CREATED: %s" % (datetime.datetime.now(), path)) if args.verbose else None
        except OSError as e:
            print("Could not create directory for %s" % path)
            raise e

    print("[%s] SUBDIRECTORY CREATION COMPLETE IN DIRECTORY %s" % (datetime.datetime.now(),
                                                                  abs_path)) if args.verbose else None


