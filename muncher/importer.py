class importer:
    #initial
    def __init__(self, file):
        self.file = file
        self.data = []
    
    #read data function
    def readCsv(self, spliter = ",", table = True):
        with open(self.file, 'r') as file:
            # Read lines from the file
            lines = file.readlines()
            
            for line in lines:
                row = line.strip().split(spliter)                
                self.data.append(row)
                
            if table == True:
                self.table()
                
    #Get original data
    def getData(self):
        return self.data
        
    #Create a easy visual table for data
    def table(self):
        colWidthLst = []
        for i in range(len(self.data[0])):
            maxLen = 0
            for row in self.data:
                curLen = len(str(row[i]))
                if curLen > maxLen:
                    maxLen = curLen
            colWidthLst.append(maxLen)
        
        formats = []
        rowNumWidth = len(str(len(self.data))) + len(" ->")
        
        for v in colWidthLst:
            curFormat = "{:<" + str(v) + "}"
            formats.append(curFormat)
            
            
        rowFormat = " | ".join(formats)
        
        colID = []
        for i in range(len(self.data[0])):
            colID.append(i)
        print(" " * rowNumWidth, "|", rowFormat.format(*colID))
        
        
        for idx, row in enumerate(self.data, start=0):
            rownum = f"{idx} ->"
            print(f"{rownum:<{rowNumWidth}} |", rowFormat.format(*row))
            
    def colnames(self):
        return self.data[0][:]
            
    def __getitem__(self, position):
        if isinstance(position, tuple):
            x, y = position
            if isinstance(x, slice):
                eleLst = []
                for row in self.data:
                    eleLst.append(row[y])
                return eleLst
            if isinstance(y,slice):
                return self.data[x][:]
            if isinstance(x, int) and isinstance(y,int):
                return self.data[x][y]
            
        if isinstance(position, str):
            y = self.data[0].index(position)
            eleLst = []
            for row in self.data[1:]:
                eleLst.append(row[y])
            return eleLst
            
    
    def __setitem__(self, position, value):
        x, y = position
        self.data[x][y] = value
    
    
    def header(self,length = 5):
        colWidthLst = []
        for i in range(len(self.data[0])):
            maxLen = 0
            for row in self.data[:length]:
                curLen = len(str(row[i]))
                if curLen > maxLen:
                    maxLen = curLen
            colWidthLst.append(maxLen)
        
        formats = []
        for v in colWidthLst:
            curFormat = "{:<" + str(v) + "}"
            formats.append(curFormat)
            
        rowFormat = " | ".join(formats)
        for row in self.data[:length]:
            tableRow = rowFormat.format(*row)  # Format the row
            print(tableRow)
            
    def dropna(self, naVal = None):
        cleanedDf = []
        
        for row in self.data:
            if naVal not in row:
                cleanedDf.append(row)
                
        self.data = cleanedDf
        
        self.table()
        
    def addrow(self, row):
        if not isinstance(row, list):
            raise TypeError("Input row is not a list")
        if len(row) == len(self.data[0]):
            self.data.append(row)
        if len(row) != len(self.data[0]):
            raise ValueError("The length of the new row does not match the row length of the data frame")
            
    def addcol(self, col):
        if not isinstance(col, list):
            raise TypeError("Input column is not a list")
        if len(col) != len(self.data):
            raise ValueError("The length of the new column does not match the column length of the data frame")
            
        if len(col) == len(self.data):
            for i in range(len(col)):
                self.data[i].append(col[i])
                
    def droprow(self, rowidx):
        self.data.pop(rowidx)
        
    def dropcol(self, colid):
        if isinstance(colid, int):
            newdf = []
            for row in self.data:
                row.pop(colid)
                newdf.append(row)
            self.data = newdf
            
        if isinstance(colid, str):
            y = self.data[0].index(colid)
            newdf = []
            for row in self.data:
                row.pop(y)
                newdf.append(row)
            self.data = newdf
        