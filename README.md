# my-database

Provides a REST API to interact with the Postgres instance running on premises on the Raspberry pi400

It has the following features:

/query?db={database}&query={query}
Example: "/query?db=publicdb&query=SELECT%20*%20FROM%20countries;"

Returns a JSON response containing an array of records

Local Usage:
```
curl "http://127.0.0.1:8000/query?db=publicdb&query=SELECT%20*%20FROM%20countries;"
```

Production Usage:
```
curl "https://36zzg0nyfi.execute-api.us-east-1.amazonaws.com/api/query?db=publicdb&query=SELECT%20*%20FROM%20countries;"
```