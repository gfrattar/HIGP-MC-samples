import helpers

def main():
    
    print("Hello world")
    
    listsToProcess = ['RML.txt']
    
    for ltp in listsToProcess:
        listOfSamples = helpers.ParseInputList(ltp)
    
    webpageLines = []
    
    for sample in listOfSamples:
        webpageLines.append( helpers.PrepareTableLine(sample) )
        
    # print(webpageLines)
    
    #Header of the tables
    #| Decay mode | Production mode | DSID | Generator | jobOption | Notes |
    
    for line in webpageLines:
        print(line)
    
if __name__ == "__main__":
    main()
    
'''
Notes on the webpage development:
* add samples from other subgroups when available
'''