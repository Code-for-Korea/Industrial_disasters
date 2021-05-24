'''
Code for Korea - #p-산업재해
판결문에서 근로자의 직업과 질병명을 추출

가이드
@바른생활 심원일 네 안녕하세요. 월요일에 포럼 모임 있었습니다. 논의 된 것은 시민들이 찾아 볼 수 있게, 즉 종사자/질병을 키워드로 서치하고 이후 원문을 볼수 있는 방법 논의 되었습니다. 1) 판결문 질병분류 설정은 주로 '이 사건 상병'이라는 키워드 앞에 있는 것 같고,
2) 종사자는 '업무에 종사'하여왔다 앞에 있는 용접일 것 같습니다. 어디는 업무 내용이라는 항에 있고 일정치 않은 것 같습니다. 그리고 데이터 파일 올리겠습니다.
@바른생활 심원일 여기 빨간 줄에 있는 것 앞에 '30여 년간 배관설비 및 용접 업무'와 '피부근염'이 업무/질병의 colum 에 값이면 찾기 편할 것 같습니다. (편집됨)


Required package
- xlrd

2021/05/12 바른생활 심원일
'''

import api_industrial_disasters
import pandas as pd

detail_sentence_xlsx_file_path = 'sentence.xlsx'
df = pd.read_excel(detail_sentence_xlsx_file_path)

print(df['판결문'][1])

