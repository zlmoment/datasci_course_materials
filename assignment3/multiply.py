import MapReduce
import sys

"""
My solution for matrix multiplication
"""

mr = MapReduce.MapReduce()

def mapper(record):
    if record[0] == "a":
        for k in range(0, 5):
            mr.emit_intermediate((record[1], k), record)
    else:
        for i in range(0, 5):
            mr.emit_intermediate((i, record[2]), record)
        

def reducer(key, list_of_values):
    result = 0
    fromA = [0] * 5
    fromB = [0] * 5

    for value in list_of_values:
        if value[0] == 'a':
            fromA[value[2]] = value[3]
        else:
            fromB[value[1]] = value[3]

    for j in range(0, 5):
        result += fromA[j] * fromB[j];

    mr.emit((key[0], key[1], result))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
