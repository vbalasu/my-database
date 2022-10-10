from chalice import Chalice
from chalicelib import mysecrets

app = Chalice(app_name='my-database')

def execute_query(db, query):
    import psycopg2
    import pandas as pd
    from sqlalchemy import create_engine
    alchemyEngine   = create_engine(f'postgresql+psycopg2://{mysecrets.user}:{mysecrets.password}@{mysecrets.host}/{db}', pool_recycle=3600);
    conn    = alchemyEngine.connect()
    df = pd.read_sql(query, conn)
    records = df.to_dict(orient='records')
    return records

@app.route('/query')
def do_query():
    try:
        db = app.current_request.query_params.get('db')
        assert db is not None
    except:
        return 'db not specified'
    try:
        query = app.current_request.query_params.get('query')
        assert query is not None
    except:
        return 'query not specified'
    return execute_query(db, query)

@app.route('/')
def index():
    return {'hello': 'world'}


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
