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
* add alternative HZZ samples (Herwig)
* add HZZ samples with tau decays --> need to find the EVNTs
* add Hmumu samples 
* add a section where it is explained the generation of events: LHE files using job options, split per batch and then showered by subgroups
* add a section where the standard setup of LHE files is described (accuracy, PDF sets and so on)
* add a section for alternative samples (alternative PS or decay generator)
* start to integrate NRML samples as well
'''