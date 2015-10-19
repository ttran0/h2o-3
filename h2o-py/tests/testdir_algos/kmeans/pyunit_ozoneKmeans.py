

import h2o, tests

def ozoneKM():
  # Connect to a pre-existing cluster
    # connect to localhost:54321

  train = h2o.import_file(path=tests.locate("smalldata/glm_test/ozone.csv"))

  # See that the data is ready
  print train.describe()

  # Run KMeans
  my_km = h2o.kmeans(x=train,
                     k=10,
                     init = "PlusPlus",
                     max_iterations = 100)

  my_km.show()
  my_km.summary()

  my_pred = my_km.predict(train)
  my_pred.describe()


pyunit_test = ozoneKM
