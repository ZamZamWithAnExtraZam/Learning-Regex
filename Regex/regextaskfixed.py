import re

def RemovingOfNewLines(inputFile):
    ReturnInputString = " "
    file = open(inputFile, "r")
    for LINE in file:
        ReturnInputString = ReturnInputString + " " + LINE.strip()
    ReturnInputString = ReturnInputString + "\n"
    file.close()
    return ReturnInputString

def Find(content, dictNames, largerGenderR):
    currentnumberMaleR = 0
    currentnumberFemaleR = 0

    for n in range(1, 1001):
        pattern1 = fr"<td>\s*{n}\s*</td>\s*<td>\s*(\w+)"
        pattern2 = fr"<td>\s*{n}\s*</td>\s*<td>\s*\w+\s*</td>\s*<td>\s*(\w+)"

        for npatterns in range(1, 3):
            currentpattern = locals()[f"pattern{npatterns}"]
            match = re.findall(currentpattern, content)

            if match:
                if match[0] in dictNames:
                    if currentpattern == pattern1:
                        currentnumberMaleR += 1
                    elif currentpattern == pattern2:
                        currentnumberFemaleR += 1
                else:
                    if currentpattern == pattern1:
                        dictNames[match[0]] = n - currentnumberMaleR
                    elif currentpattern == pattern2:
                        dictNames[match[0]] = n - currentnumberFemaleR
            else:
                print("Error finding data")

    if currentnumberMaleR == currentnumberFemaleR:
        return [dictNames, 2]
    elif currentnumberMaleR > currentnumberFemaleR:
        return [dictNames, 1]
    else:
        return [dictNames, 0]

def Output(dictNames, largerGenderR):
    HaveInstance = True
    number = 1

    while HaveInstance:
        Instances = [key for key, value in dictNames.items() if value == number]
        if len(Instances) == 0:
            HaveInstance = False
            break

        elif len(Instances) == 1:
            if largerGenderR == 1:
                print(f"Ranking in popularity overall: {number} Female: {Instances[0]}")
            elif largerGenderR == 0:
                print(f"Ranking in popularity overall: {number} Male: {Instances[0]}")
            number += 1

        elif len(Instances) == 2:
            print(f"Ranking in popularity overall: {number} Male: {Instances[0]}, Female: {Instances[1]}")
            number += 1

contentFile = "BabyNames2010.html"
lGR = 'N'
dictNames = {}

content = RemovingOfNewLines(contentFile)
result = Find(content, dictNames, lGR)
dictNames, largerGenderR = result
Output(dictNames, largerGenderR)
