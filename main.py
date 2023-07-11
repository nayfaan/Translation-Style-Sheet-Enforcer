import csv
import re
from operator import itemgetter

def run():
    jp = ""
    with open("input/jp.txt", "r") as jp_txt:
        jp = jp_txt.read()
    
    ss = []
    with open('input/ss.csv', newline='', encoding='utf-8') as ss_csv:
        ss_reader = csv.reader(ss_csv, delimiter=',')
        for row in ss_reader:
            if (row[0] and row[1]):
                ss.append(row)
                
                # Name split
                split_test = re.sub("[\(（].*?[\)）]","",row[0])
                if re.search("・", split_test):
                    jp_split = re.split("・", split_test)
                    en_split = re.split("\s", row[1])
                    
                    ss.append([jp_split[0],en_split[0]])
                    ss.append([jp_split[1],en_split[1]])
                    
                # Brackets
                bracket_check = re.search("(.*?)[\(（](.*?)[\)）]",row[0])
                if bracket_check:
                    ss.append([bracket_check[0],row[1]])
                    ss.append([bracket_check[1],row[1]])    
                
    ss = sorted(ss, key=itemgetter(0))
    ss.reverse()
                
    for row in ss:
        jp_raw = re.sub("[（|(].*[）|)]","",row[0])
        en_strip = row[1].strip()
        jp = re.sub(jp_raw,jp_raw + "(" + en_strip + ")",jp)
        
    with open("output/jp_ss.txt", "w") as jp_ss_txt:
        jp_ss_txt.write(jp)
    
if __name__ == "__main__":
    run()
