# Industrial_disasters
산업재해 관련 프로젝트 - 판례 분석 등

#  프로젝트의 목적
근로자가 자신에게 발생했거나 발생 할 가능성이 있는 산업재해 판례 정보를 손쉽게 조회 해 볼 수 있는 서비스를 만드는 것이 궁극적인 목표.

# 최근에 내려받은 데이터들
처음에는 빠르게 데이터를 받아 공유하기 위해 로컬에서 돌아가는 로직으로 구현했으나, python 개발 환경이 없는 분들이 쉽게 데이터를 받을 수 있도록 하기 위해 웹 기반의 시스템을 다시 개발하고 있습니다. 시스템 개발 중에 데이터를 새로 받는 경우가 있는데, 개발 환경 없는 분들 중 최신 데이터가 필요한 분들은 아래 공유 폴더에서 데이터를 받아 보시기 바랍니다.
https://drive.google.com/drive/folders/1gKOPq0uhw_P0eIyBnG9eYKw3MhMC1mUE?usp=sharing


## 관련 프로젝트

### 웹 기반 판례 데이터 조회
https://github.com/Code-for-Korea/sanjae.server


###  산재 판례 데이터 수집
https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15041878

근로복지공단_산재보험 판례 판결문 조회 서비스 데이터 활용

- 사용법
 1. api_industrial_disasters.py 에 발급받은 라이센스 키(Encoded)를 extract_sentence_details.py와 같은 위치에 userkey.py라고 만들고, 아래와 같은 변수명에 본인의 키를 설정함.
    
    encSvcKey ='----------YOUR ENCODING KEY-------------------'

 2. extract_sentence_details.py 를 실행함
 3. 각 사건 상세 내용이 기록 된 엑셀 파일이 'sentenc_날짜.xlsx' 형식으로 생성 됨.
 4. 연관 재판 정보는 상세 내용 파일의 마지막 컬럼을 엑셀의 데이터 분리 기능으로 쉼표와 빼기를 구분자로 하여 나누면 됨.

- 보완 할 사항
 1. 추출 된 판례 데이터 자체도 소중하지만, 근로자가 자신과 관련 된 질병에 대한 판례를 검색 해 보는데 활용 할 수 있게 해야 함.
 2. 현재는 이 과정이 수동으로 되고 있기 때문에, 판례 내용에서 검색에 필요한 정보를 추출해 내는 것을 다음 단계의 프로젝트로 정함.
