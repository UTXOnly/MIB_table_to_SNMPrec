#!/bin/bash

#Download MIB table, remove the first line containing "---", output to file_to_analyize.yaml
#curl https://bestmonitoringtools.com/mibdb/mibs_yml/${1}.yaml | tail -n +2 > file_to_analyize.yaml

curl https://bestmonitoringtools.com/mibdb/mibs_csv/${1}.csv | tail -n +1 > file_to_analyize.csv
#https://bestmonitoringtools.com/mibdb/mibs_csv/IF-MIB.csv
wait

mib_name=$1
echo $mib_name
export mib_name
#python3 scan_and_seperate.py
python3 csv_to_objects.py