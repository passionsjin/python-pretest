## PEP8
- 파이썬 개선 제안서로 협업을 위한 스타일 가이드로 사용된다.

### 들여쓰기
- 한번의 들여쓰기에는 4개의 스페이스 사용.
- 줄바꿈이 일어나는 요소들은 수직으로 정렬.

### Whitespace
- 한줄의 문자 길이가 79자 이하.
- 함수와 클래스는 빈 줄 두개로 구분.
- 클래스에서 메서드는 빈줄 하나로 구분.
- 변수 할당 앞 뒤에 하나의 스페이스만  사용..
- 리스트 인덱스, 함수 호출, 키워드 인수 할당에는 스페이스를 사용하지않는다.

### naming
- 함수, 변수, 숙성: lowercase_underscore
- protected 인스턴스 속성: _leading_underscore
- private 인스턴스 속성: __double_leading_underscore
- 클래스와 예외: CapitalizeWord (camel)
- Module 수준 상수: ALL_CAPS

### Expression
- ```if not a is b``` 보다는 ```if a is not b``` 를 사용
- 한줄로 된 if, for, except 등 복합문을 쓰지않는다.
- import는 항상 파일 맨 위에 놓는다
- import시 항상 절대 이름을 사용. ```import foo``` 대신 ```from bar import foo```

