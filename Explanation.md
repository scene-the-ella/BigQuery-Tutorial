# AnoIn-BigQuery
Tutoial of getting image url using BigQuery. <br>
이 문서에서는 Google BigQuery에 데이터셋을 적재하고 이용하는 튜토리얼을 소개합니다. <br>
> <li>Environment: Google BigQuery, Serverless API(Google Functions) </li><br>
> <li>#AnotherIntelligence_어나인(이하 AnoIn)와 함께 합니다. </li>

# BigQuery
Google의 BigQuery는 Serverless ML API에 필요한 리소스들을 적재하고 관리할 수 있는 서비스입니다. 
기존 SQL 언어를 그대로 사용하기 때문에 익숙하게 데이터를 관리할 수 있고, GCP와의 연동이 쉬운 장점이 있습니다. 

AnotherIntelligence AI Engineer Party의 첫 번째 문제를 위한 튜토리얼인 Chris님의 [Serverless ML API 완성](https://brunch.co.kr/@chris-song/91?fbclid=IwAR3WG5_D5ZKRSDdxCIX5oypgzkuLiLbcxgp8oFydZjECmIIvaOXGs3I_lQg
)에 이어서 BigQuery에 데이터정보를 적재하고 사용하는 방법을 공유드리려고 합니다.

BigQuery에 데이터셋을 적재하고 사용하는 방법은 크게 세 가지가 있는데요. 하나는 [공개 데이터셋을 이용하는 법](https://console.cloud.google.com/bigquery?p=bigquery-public-data&page=project), 
하나는 [로컬의 데이터셋을 불러오는 방법](https://cloud.google.com/bigquery/docs/loading-data-local?hl=ko#loading_data_from_a_local_data_source), 마지막은 새로운 데이터셋을 생성하는 방법입니다. 

# Architecture
<img src="/Architecture.png" width="700px">
이번 튜토리얼에서 다룰 기본 아키텍처는 위와 같습니다. *Serverless ML API 완성*의 API 요청 명령과 연관지어 설계하였습니다. 
우선 새로운 데이터셋을 생성하고, 위 아키텍처의 명령어 중 데이터의 위치를 뜻하는 IMAGE URL 부분을 BigQuery에 적재하고 가져오는 방식입니다. 

# 데이터셋 생성 Query
대중적으로 많이 사용하는 SQL문을 사용하기 때문에 많은 어려움은 없을 것으로 예상되나, DML에 익숙하지 않으신 분들은 [DML Doc](https://cloud.google.com/bigquery/docs/reference/standard-sql/dml-syntax?hl=ko) 을
보시면 도움이 되시리라 생각합니다. 데이터 생성 구문은 다음과 같이 작성하여 쿼리를 처리합니다. 
~~~
INSERT [*데이터셋이름*].[*테이블이름*] ([*가져올열*])
VALUES("[*이미지가 존재하는 온라인 주소*]")
~~~
 
 # URL 가져오기 Query
제 아키텍처에서는 이미지 URL을 가져오는 작업이 필요하기 때문에 다음과 같은 구문을 사용합니다. 
~~~
INSERT [*데이터셋이름*].[*테이블이름*] ([*가져올열*])
VALUES("[*이미지가 존재하는 온라인 주소*]")
~~~

# Client Library 사용하기
Query작업을 GCP와 바인딩하여 사용하기 위해서는 Google BigQuery API를 사용해야 합니다. 이를 위해서 다음 [빠른 시작](https://cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries?hl=ko) 문서를
참고하셔서 *시작하기 전에* 파트를 통해 준비사항을 완료해주시면 됩니다.
이 후 
 ~~~
 pip install --upgrade google-cloud-bigquery
 ~~~
 문으로 클라이언트 라이브러리를 설치합니다. 
 
 # Query in python
 Query문을 python으로 작성한 코드인 bqtest.py에서 주의하실 점은 다음과 같은 부분입니다.
 ~~~
 import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:\\Users\\KKS\\Documents\\Anain\\default_key\\tutorial-ai-party-bd0ea38a2606.json"
 ~~~
 위의 시작하기 전에 파트에서 생성하였던 jason의 경로를 지정해주셔야 쿼리를 사용하는데 있어서 문제가 없습니다!

## Execution
~~~
python geturl.py
~~~

## Execution result
~~~
Row(('https://raw.githubusercontent.com/ryfeus/gcf-packs/master/tensorflow2.0/example/test.png',), {'url': 0})
~~~
위의 실행결과에 따라 가져오게 된 IMAGE 위치 URL을 이용해서 API 요청을 하시면 됩니다.

## References
<li> Client library usages(Quick start): https://cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries</li>
<li> DML: https://cloud.google.com/bigquery/docs/reference/standard-sql/dml-syntax</li>
