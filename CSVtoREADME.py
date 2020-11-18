#!/usr/bin/env python

'''
    Copyright (C) 2020 PRE-list

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


import argparse
import csv


def main(delimiter):

    papers = []
    with open('tools.csv', newline='') as f:
        reader = csv.DictReader(f, delimiter=delimiter, quotechar='"')
        for row in reader:
            papers.append(row)

    papers = list(enumerate(sorted(papers, key=lambda k: k['Year']), start=1))

    with open('README.md', 'w') as f:
        f.write("PRE-list\n")
        f.write("========\n\n")
        f.write("List of (automatic) protocol reverse engineering tools/methods/approaches for " + \
                "network protocols\n")

        f.write("\n# Overview\n\n")
        f.write("NetT: input is a network trace (e.g. pcap)<br />\n" + \
                "ExeT: input is an execution trace (code/binary at hand)<br />\n" + \
                "PF: output is protocol format (describing the syntax)<br />\n" + \
                "PFSM: output is protocol finite state machine (describing semantic/sequential " + \
                "logic)<br />\n\n")
        f.write("| Name | Year | NetT | ExeT | PF | PFSM |\n")
        f.write("|------|------|------|------|----|------|\n")
        for cite, paper in papers:
            f.write("| " + paper['Name'] + " [[" + str(cite) + "]](#" + str(cite) + ") | " + \
                    paper['Year'] + " | " + \
                    paper['NetT'] + " | " + \
                    paper['ExeT'] + " | " + \
                    paper['PF'] + " | " + \
                    paper['PFSM'] + " |\n")

        f.write("\n# References\n\n")
        for cite, paper in papers:
            f.write('#### [' + str(cite) + ']\n')
            f.write(paper['Paper(s)'])
            if paper['Link to paper']:
                f.write(" [PDF](" + paper['Link to paper'] + ")")
            f.write("\n")


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Transform tools.cvs into a README.md for Github repo")

    parser.add_argument("--delimiter", default=";", 
                        help="Delimiter used in .csv file", metavar="DELIM")
    # TODO add argument for csv file and check if file exists

    args = parser.parse_args()

    main(args.delimiter)
