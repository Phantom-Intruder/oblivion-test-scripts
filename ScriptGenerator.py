import requests
import re
from time import sleep

urls = ['https://elderscrolls.fandom.com/wiki/A_Brush_With_Death_(Oblivion)'
    , 'https://elderscrolls.fandom.com/wiki/Corruption_and_Conscience'
        ]


file1 = open("commandsChe.bat", "w")
for url in urls:
    x = requests.get(url)
    exp = re.findall(r'QuestID">(.*)</td>', x.text)
    for k in range(100):
        file1.write("SetStage " + exp[0] + " " + str(k+1))
        print("SetStage " + exp[0] + " " + str(k+1))
        file1.write("\n")
    file1.write("completequest " + exp[0])
    print("completequest " + exp[0])
    file1.write("\n")
    sleep(2)

file1.close()
# print(requests.get("https://elderscrolls.fandom.com/wiki/A_Watery_Grave").text)
# print(exp[0])
