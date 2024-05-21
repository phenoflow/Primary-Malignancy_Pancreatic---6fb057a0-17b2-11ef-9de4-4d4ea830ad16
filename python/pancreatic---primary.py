# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"49629.0","system":"readv2"},{"code":"96635.0","system":"readv2"},{"code":"35795.0","system":"readv2"},{"code":"8166.0","system":"readv2"},{"code":"95783.0","system":"readv2"},{"code":"95609.0","system":"readv2"},{"code":"39870.0","system":"readv2"},{"code":"8771.0","system":"readv2"},{"code":"97875.0","system":"readv2"},{"code":"98825.0","system":"readv2"},{"code":"48537.0","system":"readv2"},{"code":"35535.0","system":"readv2"},{"code":"34388.0","system":"readv2"},{"code":"63102.0","system":"readv2"},{"code":"32294.0","system":"readv2"},{"code":"40810.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('primary-malignancy_pancreatic-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["pancreatic---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["pancreatic---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["pancreatic---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
