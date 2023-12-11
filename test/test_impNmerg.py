from muncher import importer as imp, merger
from muncher import merger as meg



if __name__ == "__main__":
    print("test 1: load in 'mtcars.csv' as df1")
    df1 = imp("mtcars.csv")

    print("test 2: read in df1 csv file and do not show the table")
    df1.readCsv(table = False)

    print("test 3: show the header of df1, use default length")
    df1.header() #Should show a header table with 5 rows

    print("test 4: show the first 6 rows of df1")
    df1.header(length=6) #Should show a header table with 6 rows

    print("test 5: Print out the table with row index and column index")
    df1.table() #Should show a full table with row index on the most left and column index on the top

    print("test 6: find the item in the 3rd row and 5th column and store in variable 'a'")
    a = df1[2,4]
    print(a) #Should be 110, the hourse power of Mazda Rx4 wagon

    print("test 7:  find all the item in column 'model' ")
    b = df1["model"]
    print(b) #Should print out all the rows in column 0

    print("test 8: set mpg of volvo 142E to None, then drop all the na values in the data set")
    df1[-1,1] = None
    df1.dropna() #Should show a table with only 31 columns, the conlumn with Volvo 142E is droped

    print("test 9: Drop the row with Maserati, we dont sell them")
    df1.droprow(-1)
    df1.table() #df1 now should not contain the row with Maserati

    print("test 10: drop the mpg column")
    df1.dropcol("mpg")
    df1.header() #Now, the df1 should not contain mpg column

    print("test 11: add ford f150 row to the data")
    addRow = ['Ford F150','0','0','0','0','0','0','0','0','0','0']
    df1.addrow(addRow)
    df1.table() #The last row is ['Ford F150','0','0','0','0','0','0','0','0','0','0']

    print("test 12: add a new row called on_sale to df1")
    on_sale = ['on sale'] + ['yes'] * 31
    df1.addcol(on_sale)
    df1.header() #The header should contain a new column named on sale with boolean values

    print("test 13: print out the column names I have right now")
    print(df1.colnames()) #['model', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb', 'on sale']


    print("test 14: Reload 'mtcars.csv' as df1, 'mtcarsMerge.csv' as df2, print the new df2's header")
    df1 = imp("mtcars.csv")
    df2 = imp("mtcarsMerge.csv")
    df1.readCsv(table=False)
    df2.readCsv(table=False)
    df2.header() #Should print out df2 header with length 5

    print("test 15: put both df1 and df2 into a dfLst(list object), them use this to create a new merger object")
    dfLst = [df1, df2]
    mergObj = meg(dfLst)

    print("test 16: show the common columns of each pair of data sets in the merger object")
    print(mergObj.commonCols())

    print("test 17: Now, you know the index of the pairs that have common columns, and the key name, merge them, and should the new columns")
    mergedDf = mergObj.leftMerge([0,1],"model")
    mergedDf.table()#It should print out a new table with 14 columns
    print(mergedDf.colnames()) #['model', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb', 'going price', 'in stock', 'on sale']



