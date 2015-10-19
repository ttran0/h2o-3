

import h2o, tests

def space_headers():
    
    

    f = h2o.import_file(path=tests.locate("smalldata/jira/citibike_head.csv"))

    print f.names

    f["starttime"].show()

    h2o_median = f["start station id"].median()

    assert h2o_median == 444, "Expected median for \"start station id\" to be 444, but got {0}".format(h2o_median)


pyunit_test = space_headers
