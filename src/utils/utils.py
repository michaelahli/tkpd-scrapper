# method to get value from elements
def GetListValues(list):
    for a in list:
        return a.text.replace(",", "")