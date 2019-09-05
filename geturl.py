import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:\\Users\\KKS\\Documents\\Anain\\default_key\\tutorial-ai-party-bd0ea38a2606.json"

from google.cloud import bigquery
client = bigquery.Client()

query = (
    "SELECT url FROM `tutorial-ai-party.test_image.info` "
)

query_job = client.query(
    query,
    # Location must match that of the dataset(s) referenced in the query.
    location="US",
) 

for row in query_job: 
    assert row[0] == row.url == row["url"]
    print(row)