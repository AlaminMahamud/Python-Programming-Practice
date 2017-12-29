tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

for i in range(0,3):
    print(tableData[0][i].rjust(10),tableData[1][i].rjust(10), tableData[2][i].rjust(10))
