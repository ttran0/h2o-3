

import h2o, tests

def pyunit_pop():

  pros = h2o.import_file(tests.locate("smalldata/prostate/prostate.csv"))
  nc = pros.ncol
  popped_col = pros.pop(pros.names[0])

  print pros.dim
  print popped_col.dim

  assert popped_col.ncol==1
  assert pros.ncol==nc-1


pyunit_test = pyunit_pop
