import time
 
# define a recursive function to create partial sums by row
def recSumAtRow(rowData, rowNum):
    # iterate over the given row
    for i in range(len(rowData[rowNum])):
        # add the largest of the values below-left or below-right
        rowData[rowNum][i] += max([rowData[rowNum+1][i],rowData[rowNum+1][i+1]])
    # base case
    if len(rowData[rowNum])==1: return rowData[rowNum][0]
    # recursive case
    else: return recSumAtRow(rowData, rowNum-1)
 
# read in the data
rows = []
with open('problem-18-data') as f:
    for line in f:
        rows.append([int(i) for i in line.rstrip('\n').split(" ")])
 
 
start = time.time()
result = recSumAtRow(rows, len(rows)-2) # start at second to last row
elapsed = time.time() - start
 
 
print "%s found in %s seconds" % (result ,elapsed)
