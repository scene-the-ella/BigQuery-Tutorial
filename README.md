# AnoIn-BigQuery
Tutoial of getting image url using BigQuery <br>
Google BigQuery에 데이터셋을 적재하고 이용하는 튜토리얼을 소개합니다. 
> Environment: Google BigQuery, Serverless API(Google Functions)

# Architecture
<img src="/Architecture.png" width="700px">

## Execution result
~~~
Row(('https://raw.githubusercontent.com/ryfeus/gcf-packs/master/tensorflow2.0/example/test.png',), {'url': 0})
~~~

## Execution
~~~
python geturl.py
~~~

## References
<ol> - Client library usages(Quick start): https://cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries</ol>
<ol> - DML: https://cloud.google.com/bigquery/docs/reference/standard-sql/dml-syntax</ol>
