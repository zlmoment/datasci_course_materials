import MapReduce
import sys

"""
My solution for unique trims
"""

mr = MapReduce.MapReduce()

def mapper(record):
    dna = record[1][:-10]
    mr.emit_intermediate(dna, "")

def reducer(key, list_of_values):
    mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
