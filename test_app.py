import app

def test_execute_query():
    response = app.execute_query(db='publicdb', query='SELECT * FROM countries;')
    assert type(response) is list