from mlproject.distance import haversine

def test_distance():
    assert haversine(0,0,0,0)==0
