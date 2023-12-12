
from muncher.importer import Importer
class Merger:
    def __init__(self, dfLst): #dfLst is a list of type importer data sets
        for i in range(len(dfLst)):
            if not isinstance(dfLst[i], Importer):
                raise TypeError("merger only accept type importer data sets, the list contains non-importer data")
        self.dfs = dfLst
        
    def commonCols(self): #Find the common columns of each pair of the data sets in the dfLst
        commonCols = {}
        
        for i in range(len(self.dfs)):
            dfnames = self.dfs
            
            for j in range(i+1, len(self.dfs)):
                pointer1 = set(self.dfs[i].colnames())
                pointer2 = set(self.dfs[j].colnames())
                
                commonSet = pointer1.intersection(pointer2)
                
                commonCols[(i, j)] = list(commonSet)
                
        return commonCols
    
    def __getitem__(self,key):
        return self.dfs[key]
    
    def leftMerge(self, dfIdx, key): #dfIdx is a list of data set idex, key is the common column given in commonCols
        #merge every column in the second data set of dfIdx into first data set of dfIdx
        if len(dfIdx) != 2:
            raise ValueError("leftMerge only takes length 2 list of integers")
        if not isinstance(dfIdx, list):
            raise TypeError("leftMerge only takes list type object")
        
        mainDf = self.dfs[dfIdx[0]]
        
        intoDf = self.dfs[dfIdx[1]]
        
        mergedDf = self.mergeHelper(mainDf, intoDf, key)
        
        return mergedDf
        
    
    def mergeHelper(self, df1, df2, key): #A helper function for leftMerge
        
        keyDf2 = df2[0,:].index(key)
        
        newDf = df1
        
        for i in range(len(df2[0,:])):
            if df2[0,i] != key:
                curLst = []
                for j in range(len(df2[:,:])):
                    curLst.append(df2[j,i])
                newDf.addcol(curLst)
        
        return newDf
