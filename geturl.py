#Reference: https://cloud.google.com/bigquery/docs/

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="\PATH\filename.json"

from google.cloud import bigquery
client = bigquery.Client()

query = (
    "SELECT url FROM `[PROJECTNAME].[DATASETNAME].[TABLENAME]` "
)

query_job = client.query(
    query,
    # Location must match that of the dataset(s) referenced in the query.
    location="US",
) 

for row in query_job: 
    assert row[0] == row.url == row["url"]
    print(row)