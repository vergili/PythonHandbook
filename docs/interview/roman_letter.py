
class converter :
    def __init__(self):
        self.romanLetterMap = dict()
        self.romanLetterMap['I']= 1
        self.romanLetterMap["V"] = 5
        self.romanLetterMap["X"] = 10
        self.romanLetterMap["L"] = 50
        self.romanLetterMap["C"] = 100
        self.romanLetterMap["D"] = 500
        self.romanLetterMap["M"] = 1000
        print(self.romanLetterMap)

    def convertToRoman(self,roman):
        if roman is None or len(roman) <= 0 :
            return None
        prev=None
        result = 0
        for i in range(len(roman)):
            romanLetter = roman[i]
            if romanLetter not in self.romanLetterMap:
                print("invalid letter sequence")
                break
            result += self.romanLetterMap[romanLetter]
            if prev is not None and self.romanLetterMap[prev] < self.romanLetterMap[romanLetter]:
                result -= 2* self.romanLetterMap[prev]
            prev = romanLetter
        return result


print converter().convertToRoman('ML')

