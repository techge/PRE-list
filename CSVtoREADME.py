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
                "network protocols<br/><br/>\n\n")

        f.write("This is a collection of " + str(len(papers)) + " scientific papers about " + \
                "(automatic) protocol reverse engineering (PRE) methods and tools. " + \
                "The papers are categorized into different groups so that it is more easy " + \
                "to get an overview of existing solutions based on the problem you want to " + \
                "tackle.<br/><br/>\n\n" + \
                "The collection was started with help of the following two surveys and got " + \
                "extended afterwards:\n\n" + \
                "* J. Duchêne, C. Le Guernic, E. Alata, V. Nicomette, and M. Kaâniche, “State of the art of network protocol reverse engineering tools,” Journal of Computer Virology and Hacking Techniques, vol. 14, no. 1, pp. 53–68, Feb. 2018, doi: 10.1007/s11416-016-0289-8.\n" + \
                "* B. D. Sija, Y.-H. Goo, K.-S. Shim, H. Hasanova, and M.-S. Kim, “A Survey of Automatic Protocol Reverse Engineering Approaches, Methods, and Tools on the Inputs and Outputs View,” Security and Communication Networks, vol. 2018, pp. 1–17, 2018, doi: 10.1155/2018/8370341.\n\n" + \
                "Please help extending this collection by adding papers to the `tools.ods`.\n\n")

        f.write("\n# Table of Contents\n\n")

        f.write("* [Overview](#overview-)\n")
        f.write("* [Input and Output](#input-and-output-)\n")
        f.write("* [Tested protocols](#tested-protocols-)\n")
        f.write("* [Source code](#source-code-)\n")
        f.write("* [References](#references-)\n\n")

        f.write("\n# Overview [&uarr;](#table-of-contents)\n\n")
        f.write("| Name | Year | NetT | ExeT | PF | PFSM | Other Output |\n")
        f.write("|------|------|------|------|----|------|--------------|\n")
        for cite, paper in papers:
            f.write("| " + paper['Name'] + " [[" + str(cite) + "]](#" + str(cite) + ") | " + \
                    paper['Year'] + " | " + \
                    paper['NetT'] + " | " + \
                    paper['ExeT'] + " | " + \
                    paper['PF'] + " | " + \
                    paper['PFSM'] + " | " + \
                    paper['Other Output'] + " |\n")

        f.write("\n# Input and Output [&uarr;](#table-of-contents)\n\n")
        f.write("NetT: input is a network trace (e.g. pcap)<br />\n" + \
                "ExeT: input is an execution trace (code/binary at hand)<br />\n" + \
                "PF: output is protocol format (describing the syntax)<br />\n" + \
                "PFSM: output is protocol finite state machine (describing semantic/sequential " + \
                "logic)<br />\n\n")
        f.write("| Name | Year | NetT | ExeT | PF | PFSM | Other Output |\n")
        f.write("|------|------|------|------|----|------|--------------|\n")
        for cite, paper in papers:
            f.write("| " + paper['Name'] + " [[" + str(cite) + "]](#" + str(cite) + ") | " + \
                    paper['Year'] + " | " + \
                    paper['NetT'] + " | " + \
                    paper['ExeT'] + " | " + \
                    paper['PF'] + " | " + \
                    paper['PFSM'] + " | " + \
                    paper['Other Output'] + " |\n")

        f.write("\n# Tested protocols [&uarr;](#table-of-contents)\n\n")
        f.write("| Name | Year | Text-based | Binary-based | Hybrid | Others |\n")
        f.write("|------|------|------------|--------------|--------|--------|\n")
        for cite, paper in papers:
            f.write("| " + paper['Name'] + " [[" + str(cite) + "]](#" + str(cite) + ") | " + \
                    paper['Year'] + " | " + \
                    paper['Text-based'] + " | " + \
                    paper['Binary-based'] + " | " + \
                    paper['Hybrid'] + " | " + \
                    paper['Others'] + " |\n")

        f.write("\n# Source Code [&uarr;](#table-of-contents)\n\n")
        f.write("Most papers do not provide the code used in the research. For the following " + \
                "papers exists (example) code.<br/>\n")
        f.write("| Name | Year | Source Code |\n")
        f.write("|------|------|-------------|\n")
        for cite, paper in papers:
            if paper['Source Code']:
                f.write("| " + paper['Name'] + " [[" + str(cite) + "]](#" + str(cite) + ") | " + \
                        paper['Year'] + " | " + \
                        paper['Website'] + " |\n")

        f.write("\n# References [&uarr;](#table-of-contents)\n\n")
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
