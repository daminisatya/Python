import time
 
# read file, containing the numbers
rows = []
FILE = open("triangle.txt", "r")
for blob in FILE: rows.append([int(i) for i in blob.split(" ")])
 
start = time.time()
 
for i,j in [(i,j) for i in range(len(rows)-2,-1,-1) for j in range(i+1)]:
    rows[i][j] +=  max([rows[i+1][j],rows[i+1][j+1]])
 
elapsed = time.time() - start
 
print "%s found in %s seconds" % (rows[0][0],elapsed)
