import MapReduce
import sys

"""
My solution for asymmetric friendships
"""

mr = MapReduce.MapReduce()

def mapper(record):
    mr.emit_intermediate(record[0], record[1])
    mr.emit_intermediate(record[1], record[0])

def reducer(key, list_of_values):
    for x in list_of_values:
        if list_of_values.count(x) == 1:
            mr.emit((key, x))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
