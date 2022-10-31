#!/bin/bash

#Download MIB table, remove the first line containing "---", output to file_to_analyize.yaml
curl https://bestmonitoringtools.com/mibdb/mibs_yml/${1}.yaml | tail -n +2 > file_to_analyize.yaml

wait

python3 scan_and_seperate.py
