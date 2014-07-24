import MapReduce
import sys

"""
My solution for join
"""

mr = MapReduce.MapReduce()

def mapper(record):
    mr.emit_intermediate(record[1], record)

def reducer(key, list_of_values):
    for x in list_of_values:
      if x[0] == "order":
        order = x
    for y in list_of_values:
      if y[0] == "line_item":
        mr.emit(order + y)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
