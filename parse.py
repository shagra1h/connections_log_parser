import sys
import os.path
import os
from datetime import datetime


def write_to_file(uniqSteamids):
    output_filename = 'results_' + datetime.now().strftime("%d_%m_%Y") + '.txt'
    output_file = open(output_filename, 'w', encoding='cp866')
    output_file.write("Уникальных steamid : " + str(uniqSteamids) + '\n')
    output_file.close()
    print("Успешно! результаты в файле", output_filename)


if __name__ == '__main__':
    input_file = open('connected_30082017.log', 'r', encoding='utf-8')
    uniq_steamids = 0
    steams = []
    for line in input_file:
        steamid = line.split()[4]
        if steamid not in steams:
            steams.append(steamid)
            uniq_steamids += 1
    input_file.close()
    write_to_file(uniq_steamids)
