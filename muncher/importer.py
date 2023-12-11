class importer:
    def __init__(self, file):
        self.file = file
        self.data = []
    
    #read csv data function
    def readCsv(self, spliter = ",", table = True):
        with open(self.file, 'r') as file:
            lines = file.readlines()
            
            for line in lines:
                row = line.strip().split(spliter)                
                self.data.append(row)
                
            if table == True:
                self.table()
                
    #function that outputs self.data
    def getData(self):
        return self.data
        
    #Create a table for dataset
    def table(self):
        colWidthLst = [] #list that stores the maximum width of each column

        for i in range(len(self.data[0])): #Double loop that treverse every element in each row
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
        
        #Print the column number at the top of the data tabel
        colID = []
        for i in range(len(self.data[0])):
            colID.append(i)
        print(" " * rowNumWidth, "|", rowFormat.format(*colID))
        
        #Print out the row number followed by the elements in each row splited by " | " 
        for idx, row in enumerate(self.data, start=0):
            rownum = f"{idx} ->"
            print(f"{rownum:<{rowNumWidth}} |", rowFormat.format(*row))
            
    #output a list of column names 
    def colnames(self):
        return self.data[0][:]
            
    #this function allows user to find the item in ith row and jth col by df[i,j] instead of df[i][j]
    def __getitem__(self, position):
        #Case 1: input position is a tuple that contains 2 things(x,y)
        if isinstance(position, tuple) and len(position) == 2: 
            x, y = position 
            if isinstance(x, slice): #Case that if user want every row
                eleLst = []
                for row in self.data:
                    eleLst.append(row[y])
                return eleLst
            
            if isinstance(y,slice): #Case that if user want every column
                return self.data[x][:]
            
            if isinstance(x, int) and isinstance(y,int): #Case that if user want a specific item
                return self.data[x][y]
            
        # Case 2: User input a string to find all the elements in a specific named column
        if isinstance(position, str): 
            y = self.data[0].index(position)
            eleLst = []
            for row in self.data[1:]:
                eleLst.append(row[y])
            return eleLst
            
    #Set new value
    def __setitem__(self, position, value):
        x, y = position
        self.data[x][y] = value
    
    #Prints out header table, header do not have col number and row number, the default is 5 rows.
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
        
    #Add one new row to the bottom of the dataframe
    def addrow(self, row):
        if not isinstance(row, list):
            raise TypeError("Input row is not a list")
        if len(row) == len(self.data[0]):
            self.data.append(row)
        if len(row) != len(self.data[0]):
            raise ValueError("The length of the new row does not match the row length of the data frame")
            
    #Add one new column to the most right hand side of the data frame
    def addcol(self, col):
        if not isinstance(col, list):
            raise TypeError("Input column is not a list")
        if len(col) != len(self.data):
            raise ValueError("The length of the new column does not match the column length of the data frame")
            
        if len(col) == len(self.data):
            for i in range(len(col)):
                self.data[i].append(col[i])
                
    #Drop the row by it's index
    def droprow(self, rowidx):
        self.data.pop(rowidx)
        
    #Drop the column by it's name/str or index
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
        
