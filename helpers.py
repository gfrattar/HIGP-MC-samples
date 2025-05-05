import os.path
import re

generatorDict = {}
generatorDict["Ph"] = "Powheg"
generatorDict["aMC"] = "Madgraph_aMCatNLO"
generatorDict["Py8"] = "Pythia 8"
generatorDict["H7"] = "Herwig 7"

def ParseInputList(ltp):

    if not os.path.isfile(ltp):
        raise RuntimeError("Input list does not exist, please check the file {}. Exiting!".format(ltp))
    
    infile = open(ltp,'r')
    
    samples = []
    for line in infile:
        samples.append(line.replace('\n',''))

    return samples


def GetGenerator(sampleShortName):
    
    generatorString = ''
    
    genShortName = sampleShortName.split('_')[0]
    
    print(genShortName)
    
    if 'Ph' in genShortName:
        generatorString += generatorDict["Ph"]

    if 'aMC' in genShortName:
        if generatorString != '':
            generatorString += ' + '
        generatorString += generatorDict["aMC"]
        
    if 'Py8' in genShortName:
        if generatorString != '':
            generatorString += ' + '
        generatorString += generatorDict["Py8"]
        
    if 'H7' in genShortName:
        if generatorString != '':
            generatorString += ' + '
        generatorString += generatorDict["H7"]
            
    return generatorString

def GetProductionMode(processShortName):
    
    if 'ggH' in processShortName:
        return "ggH"
    elif 'VBFH' in processShortName:
        return "VBFH"
    elif 'WpH' in processShortName:
        return "WpH"
    elif 'WmH' in processShortName:
        return "WmH"
    elif 'ggZH' in processShortName:
        return "ggZH"
    elif 'ZH' in processShortName:
        return "ZH"
    elif 'ttH' in processShortName:
        return "ttH"
    elif 'bbH' in processShortName:
        return "bbH"
    elif 'tHjb' in processShortName:
        return "tHjb"
    elif 'tWH' in processShortName:
        return "tWH"
    elif 'ggZllH' in processShortName:
        return "gg->Z(ll)H"
    elif 'qqZllH' in processShortName:
        return "qq/qg->Z(ll)H"

def GetDecayMode(processShortName):
    if 'HZZ' in processShortName or 'ZZ4l' in processShortName:
        return 'ZZ*->4l'
    if 'Hmumu' in processShortName:
        return 'µµ'
    if 'HWW_WWlvlv' in processShortName or 'WWlvlv' in processShortName:
        return 'WW*->lvlv'
    if 'HWW_WWlvqq' in processShortName or 'WWqqlv' in processShortName:
        return 'WW*->lvqq'
    
    return ''
    #To add here the other decay modes based on the samples list I get from the other conveners
    
def GetSampleNotes(name, dsid):
    notes = ''
    if 'notau' in name:
        notes += 'No taus in ZZ decay'
        
    if 'ZZ4l' in name and 'tau' not in name:
        notes += 'No taus in ZZ decay'
    #To add eventual other notes based on the samples I receive from the other conveners
    
    if 'tauFilt' in name or 'taufilt' in name:
        notes += 'Tau filter'

    if 'VpTbias' in name:
        notes += 'Generation cross-section biased in V pT'

    if notes == '':
        return ' - '
    
    return notes    
    

def PrepareTableLine(sample):
    
    print("Parsing the line ")
    print(sample)
    
    regexp = re.search(r'mc23_13p6TeV\.([0-9]+)\.([A-Za-z0-9_]+)\.[a-z]+\.[A-Z_]+\.([esrp_0-9]+)', sample)
    DSID = regexp.group(1)
    name = regexp.group(2)
    tags = regexp.group(3)
    
    print("DSID --> " + DSID)
    print("Name --> " + name)
    print("Tags --> " + tags)
    
    generator = GetGenerator(name)
    productionMode = GetProductionMode(name)
    decayMode = GetDecayMode(name)
    sampleNote = GetSampleNotes(name,DSID)
    DSID_initials = ''.join(DSID[0:3])+'xxx'        
    joName = 'mc.'+name+'.py'
    print("JO name --> " + joName)
    
    if decayMode == None: print("------ > Issue with decay mode")
    if productionMode == None: print("------ > Issue with production mode")
    if DSID == None: print("------ > Issue with DSID")
    if generator == None: print("------ > Issue with generator")
    if DSID_initials == None: print("------ > Issue with DSID_initials")
    if joName == None: print("------ > Issue with joName")
    if sampleNote == None: print("------ > Issue with sampleNote")
    
    pageLine = "| " + decayMode + " | " + productionMode + " | " + DSID + " | " + generator + " |  [[https://gitlab.cern.ch/atlas-physics/pmg/mcjoboptions/-/tree/master/" + DSID_initials + "/" + DSID + "/" + joName + "][Link]] | " + sampleNote + " |"
    
    return pageLine