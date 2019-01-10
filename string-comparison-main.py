


# RESOURCES, SETTINGS AND DEFINITIONS ----------------------------


stopwords = ['the', 'and', 'to', 'for', 'by', '|', "aren't", 'has', 'her', 'hers', 'its', 'themselves', 'who', 'index', 'php', 'pdf', 'html', 'htm', 'jsp', 'cgi' 'shtml', 'asp', 'having', 'my', 'nor', 've', "hasn't", 'yours', 'so', 'out', 'until', 'against', 'from', 'through', 'shan', 'are', 'that', 'me', 'at', 'between', 'into', 'very', 'those', 'll', 'wouldn', 'to', 'such', 'other', 'we', 'were', "didn't", 'won', 'being', 'doesn', 'myself', 'just', 'you', 'down', "haven't", 'whom', "should've", 'i', 'during', 'only', 'before', 'an', 'on', 'too', 'because', 'o', 'these', "mustn't", 'own', 'can', 'isn', 'why', "you'll", 'after', 'm', "doesn't", 'each', 'where', 'will', "shan't", 'ma', 'here', 'your', 'more', 'don', 'no', 'it', "you're", 'any', 'both', 'further', 'his', "shouldn't", 'now', "isn't", 'some', 'is', 'mustn', "won't", 'all', 'theirs', 'do', 'y', 'been', 'while', 'our', 'few', 'once', 'same', 're', "mightn't", 'there', 'd', 'didn', 'wasn', 'and', "she's", 'how', 'have', "it's", "don't", 'then', 'haven', 'ours', 'himself', 'aren', 'did', 'hadn', 'she', 'was', 'a', 'of', "couldn't", 't', "you'd", 'does', 'not', 'by', 'should', 'as', 'ain', 'up', 'am', 'herself', "you've", 'over', 'when', 'which', 'yourselves', 'shouldn', "weren't", 's', "needn't", "wouldn't", 'their', "wasn't", 'the', 'them', "hadn't", 'had', 'below', 'for', 'needn', 'under', 'weren', 'with', 'or', 'he', 'doing', 'mightn', 'they', 'in', 'if', 'couldn', 'what', 'off', 'yourself', 'but', 'above', 'about', 'ourselves', 'most', "that'll", 'itself', 'than', 'again', 'hasn', 'this', 'him', 'be']
objects = ["de", "no", "es", "fi", "dk", "se", "es", "es"]
synonymCheck = False

synonymMatchedList = []
outputDictionaryList = []
keywordObject = []
listBDictionaryList = []
listBDictionary = {}
fullKeywordMatch = 'False'
keywordMatch = ''
pathCompleteness = ''
elementString = ''
processMessage = ''
urlChoice = ''



def wordOrPluralInList(checkList,referenceList,i):
    import pattern
    from pattern.text.en import pluralize
    from pattern.text.en import singularize
    if checkList[i] in referenceList or pluralize(checkList[i]) in referenceList or singularize(checkList[i]) in referenceList:
        return True




def wordOrPluralInListNoLoop(checkList,referenceList):
    import pattern
    from pattern.text.en import pluralize
    from pattern.text.en import singularize
    if checkList in referenceList or pluralize(checkList) in referenceList or singularize(checkList) in referenceList:
        return True
    else:
        return False




def isExactMatch(check,reference):
    if check == reference:
        return True




def isfullKeywordMatch(checkList,referenceList):
    if str(referenceList)[1:-1].find(str(checkList)[1:-1])>=0:    
        return True



def isWordPresentInList(checkList,referenceList,referenceListName):
    global checkLevelDictionary
    global matchedList
    global notMatchedList
    global exactMatch
    global fullKeywordMatch
    matchedList = []
    matchedDict = {}
    notMatchedList = []
    exactMatch = 'false'
    fullKeywordMatch = 'false'
    #stopWordRemove(checkList)
    if isExactMatch(checkList,referenceList) == True:
        exactMatch = 'True'
    elif isfullKeywordMatch(checkList,referenceList) == True:
        fullKeywordMatch = 'True'
    for i in range(len(checkList)):
        try:
            if wordOrPluralInList(checkList,referenceList,i) == True:
                matchedList.append(checkList[i])
            else:    
                notMatchedList.append(checkList[i])
                continue
        except: 
            break
    objectMatchCheck(keywordObject, pathObject)
    matchCalculator(checkList, matchedList, referenceList)    
    checkLevelDictionary = {"list A Original": listAItemRaw,
                            "list A Item": listAItem,
                            "List B Item Original": listBDictionary.get(pathListRaw),
                            "list B Item": pathListRaw,
                            "list A Item length": len(checkList),
                            "list B Item length": len(referenceList),
                            str(referenceListName) + ' exact match':exactMatch,
                            str(referenceListName) + ' full list A Item match':fullKeywordMatch,
                            str(referenceListName) + ' words matched':matchedList,
                            str(referenceListName) + ' words matched count':len(matchedList),
                            #'Object match': objectMatch,
                            'Match %': matchPercent}
                            #str(referenceListName) + ' words matched (syn) count':''}
    if synonymCheck == True:
        isWordSynonymInList(notMatchedList, referenceList, referenceListName)







def matchCalculator(checkList, matchedList, referenceList):
    global matchPercent
    matchPercent = ''
    if len(referenceList) >= len(checkList):
        matchPercent = round((len(matchedList)/len(referenceList)+objectMatch),2)
    elif len(checkList) > len(referenceList):
        matchPercent = round((len(matchedList)/len(checkList)+objectMatch),2)
    elif exactMatch == True:
        matchPercent = round(1/1)
    else:
        matchPercent = round(0/1)



        
def objectIdentify(list):
    global matchedObject
    matchedObject = []
    try:
        for i in range(len(objects)):
            if wordOrPluralInList(list, objects, i) == True:
                matchedObject.append(list[i])
                return
    except:
        matchedObject.append('Object not found')




def objectMatchCheck(keywordObject, pathObject):
    global objectMatch
    objectMatch = 0.0
    keywordObjectString = str(keywordObject)
    keywordObjectStringCleaned = keywordObjectString.replace('[','').replace(']','').replace('\'','')
    pathObjectString = str(pathObject)
    pathObjectStringCleaned = pathObjectString.replace('[','').replace(']','').replace('\'','')
    if wordOrPluralInListNoLoop(keywordObjectStringCleaned,pathObjectStringCleaned) == False:
        objectMatch = -0.3



def elementCleaner(element_name):
    import re
    element_name = element_name.lower()
    element_name = re.sub(r"[^a-zA-Z\d\s_&:%;=#+|,£$]", '', element_name)# this removes all Nan characters except those specified
    element_name = element_name.replace('  ',' ') # this replaces the double space left from the unwanted pythonic removal of hyphen from ' - ' with a single space
    element_name = re.sub(r"[_&:;=#+,]", ' ', element_name) # this replaces the matching characters with a space
    element_name = element_name.replace('   ',' ').replace('  ',' ').replace(' | ',' ') # this cleans up any remaining double spaces
    return element_name



def titleStringSplitter(separator, element_name):
    if titleSplitString != '':
        separator = titleSplitString
        preElementList = element_name.lower().rsplit(separator, 1)[0]
        elementList = ' '.join(preElementList.split())
        element_name = elementList
        return element_name
    else:
        preElementList = element_name.lower()
        elementList = ' '.join(preElementList.split())
        element_name = elementList
        return element_name






def elementGrabber(element_name, keyword_list):
    global elementString
    global elementOut
    global elementList
    elementString = element_name
    import urllib
    from urllib import request
    try:    
        html = urllib.request.urlopen(keyword_list).read().decode('utf8')
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        element_name = soup.find(element_name)
        element_name = element_name.text
        element_name = titleStringSplitter(titleSplitString, element_name)
        element_name = elementCleaner(element_name)   
        elementOut = element_name
        print('elementOut = ' + str(elementOut))
    except:
        print('\nWorking on ' + str(elementString) + '.. Element cannot be retrieved')
        elementOut = 'Element irretrievable'




def printTable(message1, message2, leftWidth, rightWidth):
    print(message1.ljust(leftWidth, '.') + message2.rjust(rightWidth))





def csvOutput(outputcsv):
    print('\nAssembling output columns...')
    import csv
    toCSV = outputDictionaryList
    keys = toCSV[0].keys()
    with open(outputcsv, 'w', newline='', encoding='utf-8-sig') as output_file: # needs to be written another way to avoid the double spaced lines in python 3
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(toCSV)
    print('\n' + str(outputcsv) + ' generated')




def keystringCount():
    for index, row in df.iterrows():
        keystring = df[0][index]
        if keystring != '':
            allKeystringsList.append(keystring)




def singleRowCounter(x):
    global rowCount
    rowCount = 0
    for index, row in df.iterrows():
        rowContents = df[x][index]
        if rowContents == '':
            break
        rowCount +=1




def listABCounter():
    print('\nCounting list items...\n')
    singleRowCounter(0)
    global listACount
    listACount = rowCount
    singleRowCounter(1)
    global listBCount
    listBCount = rowCount
    comparisonCount = int(listACount)*int(listBCount)
    print('Main list contains ' + str(listACount) + ' items\nComparison list contains ' + str(listBCount) + ' items\n' + str(comparisonCount) + ' match % checks will be performed\n')




def columnLengthCounter():
    listABCounter()
    global allKeystringsList
    allKeystringsList = []
    keystringCount()
    global listBItemsList
    listBItemsList = []





def csvLoader():
    global df
    global csvLoaderWhilecounter
    csvLoaderWhilecounter = 0
    import pandas as pd
    while csvLoaderWhilecounter == 0:
        print('\nEnter the name of the csv file in your python directory folder containing your data e.g. filename.csv:')
        inputfile = input()    
        try:
            if inputfile != '':
                print('\n\nLoading ' + str(inputfile) + '...')
                df = pd.read_csv(inputfile, keep_default_na=False, header=None)
            else:
                df = pd.read_csv('rydoo200400test-http.csv', keep_default_na=False, header=None)
            try:
                print('Successfully loaded ' + str(inputfile))
            except:
                print('\n\nInput file loaded successfully')
            csvLoaderWhilecounter += 1    
        except:
            import os
            currentDirectory = os.getcwd()
            print('\nThat file could not be found in ' + str(currentDirectory) + ', please ensure the file is present in that directory.')
            
        



def progressDisplay(processMessage, listLength, index):
    processProgress = str(int((round((index/listLength),2)*100))) + '% complete'
    printTable(processMessage, processProgress, 100, 20) 





def optionalCreateCsv():
    print('\n\nIf you wish to create a results csv, enter the desired filename e.g. results.csv, or press enter to skip:')
    import sys
    outputcsv = input()
    if outputcsv == '':
        sys.exit()
    else:
        csvOutput(outputcsv)




def listABComparisonIterator(listAItem):
    global pathListRaw
    global pathObject
    for index in range(len(listBItemsList)):
        pathListRaw = listBItemsList[index]
        pathList = pathListRaw.split(' ')
        objectIdentify(pathList)
        pathObject = matchedObject
        isWordPresentInList(itemWordList, pathList, 'Path')
        outputDictionaryList.append(checkLevelDictionary.copy())




def processMessageSelect():
    if currentRow > 0:
        processMessage = 'Initialising... Preparing to compare \'' + str(listAItem) + '\' against ' + str(len(listBItemsList)) + ' items...'
    else:    
        processMessage = 'Comparing \'' + str(listAItem) + '\' against ' + str(len(listBItemsList)) + ' items...'




def listItemSplit(listItem):
    global itemWordList
    itemWordList = listItem.lower().replace('\t', '').split(' ')
    return itemWordList
    #print('This is itemWordList based on list A item: ' + str(itemWordList))



def stopWordRemove(inputList):
    stopWordsFound = []
    global itemWordListSwr
    itemWordListSwr = []
    for i in range(len(stopwords)):
        if stopwords[i] in inputList:
            inputList.remove(stopwords[i])
            stopWordsFound.append(stopwords[i])          
    itemWordListSwr = inputList
    return itemWordListSwr          
    #if len(stopWordsFound)>0:   
        #print('\n' + str(len(stopWordsFound)) + ' stopwords removed from ' + str(listName) + ': ' + str(stopWordsFound))


def listItemJoin(inputList):
    listItemJoined = ' '.join(inputList)
    return listItemJoined




def listsplitStopwordremoveRejoin(listItem):
    global listItemStopwordsRemoved
    listItemStopwordsRemoved = ''
    itemWordList = listItemSplit(listItem)
    #print('itemWordList = ' + str(itemWordList))
    itemWordListSwr = stopWordRemove(itemWordList)
    #print('itemWordListSwr = ' + str(itemWordListSwr))
    listItemJoined = listItemJoin(itemWordListSwr)
    #print('listItemJoined = ' + str(listItemJoined))
    listItemStopwordsRemoved = listItemJoined
    return listItemStopwordsRemoved



def URLToPathStringConvert(fullUrl, urlChoice):
    import urllib
    from urllib.parse import urlparse
    global pathString
    fullUrl = urlparse(fullUrl).path
    fullUrlList = urlparse(fullUrl).path.split('/')
    fullUrlListPreCleaned = [item for item in fullUrlList if item != '']
    fullUrlListCleaned = []
    for i in range(len(fullUrlListPreCleaned)):
        if '.' in fullUrlListPreCleaned[i]:
            fullUrlListCleaned.append('x')            
            fullUrlListCleaned[i] = fullUrlListPreCleaned[i].split('.',1)[0]
        else:
            fullUrlListCleaned.append('x')
            fullUrlListCleaned[i] = fullUrlListPreCleaned[i] 
    ##Folder number
    #print('URL to string converter is working with: ' + str(pathListCleaned))
    #print('urlChoice is: ' + str(urlChoice))
    try:        
        if int(urlChoice) > 0:
            try:
                pathPreOut = fullUrlListCleaned[(int(urlChoice)-1)].replace('-',' ').replace('_',' ').replace('%20',' ').replace('   ',' ').replace('  ',' ')
                pathString = pathPreOut
                return pathString
            except:
                pathPreOut = ''
                pathString = pathPreOut
                return pathString
                #print('Folder level ' + str(urlChoice) + ' not found in URL')
    except:
        ##Folder range
        if '-' in urlChoice:
            pathStringPreOut = ' '.join(fullUrlListCleaned[(int(urlChoice[0])-1):int(urlChoice[-1])]).replace('-',' ').replace('_',' ').replace('%20',' ').replace('   ',' ').replace('  ',' ')
        ##Last folder
        elif urlChoice == 'L':
            pathStringPreOut = fullUrlListCleaned[-1].replace('-',' ').replace('_',' ').replace('%20',' ').replace('   ',' ').replace('  ',' ')
        ##All folders
        else:
            pathStringPreOut = ' '.join(fullUrlListCleaned).replace('-',' ').replace('_',' ').replace('%20',' ').replace('   ',' ').replace('  ',' ')
        ## Convert the output list to a string
        try:    
            if len(pathStringPreOut[1]) > 1:
               pathString = ' '.join(pathStringPreOut)
            else:
                pathString = pathStringPreOut   
        except:
          import random
          fallbackId = random.randint(1,99999999) # This is so the list B dictionary can trace every processed item back to the original; it assigns a unique ID in lieu of a unique output string
          if pathStringPreOut == '':
              pathString = 'Path unavailable ' + str(urlChoice) + ' (' + str(fallbackId) + ')'
          else:    
              pathString = pathStringPreOut
    return pathString





def modeSelector(currentList): # for list B ask - Use same settings as list A? # also option to return only the 1 or 3 strongest matches
    global tryAgainWhileCounter #can this be deleted?
    global listBMode
    global mode
    global sameMode
    tryAgainWhileCounter = 0 #can this be deleted?
    if currentList == 'List A':
        print('\nUse the same settings for the main list? y/n')
        sameMode = input()
        if sameMode == 'y':
            mode = listBMode
            if mode == '2':
                urlChoice = listBUrlChoice
                return urlChoice
            return
        else:    
            print('\n\nSelect mode for this list:\n\n1. String mode\n2. URL path mode\n3. URL element mode\n')
            mode = input()
            listBMode = mode
            #urlChoiceSelector(currentList,0)
            urlChoice = urlChoiceSelector(currentList,0)
            #print('modeSelector resulted in urlCHoice = ' + str(urlChoice))
            return urlChoice
    else:    
        print('\n\nSelect mode for this list:\n\n1. String mode\n2. URL path mode\n3. URL element mode\n')
        mode = input()
        listBMode = mode
        #urlChoiceSelector(currentList,0)
        urlChoice = urlChoiceSelector(currentList,0)
        #print('modeSelector resulted in urlCHoice = ' + str(urlChoice))
        return urlChoice        



def urlChoiceSelector(currentList,urlChoice):
    global listBUrlChoice
    if mode == '2':
        print('\n\nAbout to convert URLs in this list to strings for comparison.. \n\nTo use entire path, press \'e\'. \nTo use the 1st, 2nd or 3rd folder etc, type its number. \nTo use the last folder, type L. \nTo use a range of folders, type the range e.g. 2-4\n')
        urlChoice = input()
        if currentList == 'List B':
            listBUrlChoice = urlChoice
        #print('urlChoiceSelector has run, urlChoice = ' + str(urlChoice))
        return(urlChoice)


def elementSelector(listXItem):
    global tryAgainWhileCounter
    global chosenElement
    global titleSplitString
    global sameMode
    if currentList == 'List B':
        sameMode = 'n'
    if sameMode == 'n':
        while tryAgainWhileCounter == 0:
            print('\n\nWhich HTML element would you like to extract from each URL for comparison?\n\n1: Title\n2: H1\n')
            elementChoice = input()
            if elementChoice == '1':
                chosenElement = 'title'
                print('\n\nWould you like to ignore all characters after a certain string, e.g. to remove appended brand after \'|\' or the brand name? If so, enter the string, or press enter to skip\n')
                titleSplitString = input()
                tryAgainWhileCounter += 1
                print('\n\nCollecting HTML elements for items in this list... \n')
                break
            elif elementChoice == '2':
                chosenElement = 'h1'
                titleSplitString = ''
                tryAgainWhileCounter += 1
                break
            else:
                print('\nPlease try specifying the desired element again, entering either 1 or 2\n\n')
                continue




def modeProcessIterator(listXItem, currentList):
    if mode == '2':
        pathString = URLToPathStringConvert(listXItem, urlChoice)
        if currentList == 'List B':
            listItemStopwordsRemoved = listsplitStopwordremoveRejoin(pathString)
            #print('listItemStopwordsRemoved = ' + str(listItemStopwordsRemoved))
            pathString = listItemStopwordsRemoved
            listBItemsList.append(pathString)
            #print('Before listBDictionaryAdd, variable \'listXItem\' = ' + str(listXItem))
            listBDictionaryAdd(listXItem, pathString)
            listBDictionary.update(listBDictionaryLine)
            #print('listBDictionary = ' + str(listBDictionary))
            #pause = input()
            #listBDictionaryList.append(listBDictionaryLine.copy()) ## this is getting added cumulatively and killing the computer, how to prevent..
            #print('List B reference dictionary list = ' + str(listBDictionaryList))
            #pause = input()
        else:
            listAItem = pathString
            return listAItem
    elif mode == '3':
        elementSelector(listXItem)
        elementGrabber(chosenElement, listXItem)
        if currentList == 'List B':
            listBItemsList.append(elementOut)
            listBDictionaryAdd(listXItem, elementOut)
            listBDictionary.update(listBDictionaryLine)
        else:
            listAItem = elementOut
            return listAItem
    else:
        if currentList == 'List B':
            listBItemsList.append(listXItem)
        else:
            listAItem = listXItem
            return listAItem





def listBDictionaryAdd(original, processed):
    global listBDictionaryLine
    listBDictionaryLine = {processed: original}
    #print('listBDictionaryLine = ' + str(listBDictionaryLine))




def listBBuilder(): # List B needs to have a dictionary so the original List B item can be stored against the processed item.
    #print('ListBBuilder urlChoice start = ' + str(urlChoice))
    for index, row in df.iterrows():
        listBItemRaw = df[1][index]
        if listBItemRaw != '':
            listBItem = listBItemRaw.replace('\t','')
            modeProcessIterator(listBItem, currentList)
            if mode == '3':
                processMessage = 'Downloading ' + str(chosenElement) + ' for ' + str(listBItemRaw)
                progressDisplay(processMessage, listBCount, index)
                #pathDeclare = 'Downloading next HTML element'
                #pathProgress = str(int((round((index/listBCount),2)*100))) + '% complete'
                #printTable(pathDeclare, pathProgress, 100, 20)
        #join them up
    print('\nComparison list ready\n')
    #print('listBItemsList = ' + str(listBItemsList))
    #print('List B reference dictionary list created: ' + str(listBDictionaryList))



def listAItemCleaner(listAItemRaw):
    global listAItem
    if mode != '2':
        listAItem = listAItemRaw.replace('\t', '')
    else:
        listAItem = listAItemRaw
    return listAItem    
    #print('urlChoice = ' + str(urlChoice)) # urlChoice for list A isn't being recorded
    ###if mode == '2':
        ###URLToPathStringConvert(listAItemCleaned, urlChoice) # moving this up to modeselector, and doing it for all modes
        ###listAItem = pathString
    ###else:
        ###listAItem = listAItemCleaned
    #print(listAItem)
    #pause = input()





def listARowIterator():
    global currentRow
    global listAItem
    global listAItemRaw
    currentRow = 0
    print('\nChecking each main list item for level of match against the ' + str(len(listBItemsList)) + ' items in the comparison list...\n')
    for index, row in df.iterrows():
        listAItemRaw = df[0][index]
        if listAItemRaw == '':
            break
        listAItem = listAItemCleaner(listAItemRaw)
        listAItem = modeProcessIterator(listAItem, currentList)
        listItemStopwordsRemoved = listsplitStopwordremoveRejoin(listAItem)
        listAItem = listItemStopwordsRemoved
        processMessageSelect()
        progressDisplay(listAItemRaw, listACount, index)
        listItemSplit(listAItem)
        objectIdentify(itemWordList)
        keywordObject = str(matchedObject)
        listABComparisonIterator(listAItem)
        currentRow += 1
    print('\n100% complete. End of main list reached.')



## Next:

    ##
    ##Make UrlToPathStringConvert more elegant and shorter by using and adjusting the regex from elementGrabber
    ##How will the user interact with objectMatch
    ##Storing dictionaries for {word: folderLevel}, so matches on the same level are scored as more important
    ##Option to show only the best X matches; might be better to see if the program will give a csv result on pythonanywhere first.
    ##Option to paste lists of strings into web interface; good for show.


## MAIN FLOW


csvLoader()
columnLengthCounter()
currentList = 'List B'
urlChoice = modeSelector(currentList)
listBBuilder()
currentList = 'List A'
urlChoice = modeSelector(currentList)
listARowIterator()
optionalCreateCsv()

