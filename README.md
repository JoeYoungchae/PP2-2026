# PP2-2026

2026년도 프로그래밍 II(Programming II) 수업에서 작성한 Python 실습 코드와 노트북을 모아 둔 저장소입니다. 주차별 예제와 프로그래밍 문제를 통해 Python 기초 문법, 자료형, 파일 입출력, 클래스와 객체를 학습합니다.

## 저장소 구성

```text
.
├── .vscode
│   └── launch.json             # 현재 Python 파일을 해당 폴더에서 디버그 실행
├── hello.py                    # Hello, World! 예제
├── markdown.md                 # Markdown 문법 샘플
├── mynotebook.ipynb            # 개인 노트북
└── lab
    ├── week 2                  # BMI 계산, 함수 실습
    ├── week 3                  # 리스트, 튜플, 세트, 딕셔너리, 타입 힌트 실습
    ├── week 4
    │   ├── learn8.ipynb        # 수업 실습
    │   └── programming         # prob1.py ~ prob9.py
    ├── week 5
    │   ├── learn12.ipynb       # 수업 실습
    │   └── programming         # prog1.py ~ prog7.py
    ├── week 6
    │   ├── learn10.ipynb       # 파일 입출력 수업 실습
    │   ├── file.txt            # 파일 입출력 실습 파일
    │   └── programming
    │       ├── input.txt       # 파일 입출력 문제에서 사용하는 입력 파일
    │       ├── prog1.py        # 파일의 줄을 읽어 출력
    │       ├── prog2.py        # 파일에서 가장 긴 단어 찾기
    │       ├── prog3.py        # 입력한 파일의 행 번호에 해당하는 줄 출력
    │       ├── prog4.py        # A.txt부터 Z.txt까지 파일 생성
    │       ├── prog5.py        # 파일에 줄 추가
    │       └── prog5.txt       # prog5.py에서 변환하는 텍스트 파일
    └── week 7
        └── learn11.ipynb       # 수업 실습
```

## 실행 방법

Python이 설치된 환경에서 터미널을 열고 실행하려는 프로그램이 있는 폴더로 이동합니다. 예를 들어 6주차 `prog1.py`는 다음과 같이 실행합니다.

```powershell
cd "lab\week 6\programming"
python .\prog1.py
```

6주차 `prog1.py`와 `prog2.py`는 `input.txt`를 현재 작업 폴더에서 찾으므로 `programming` 폴더에서 실행해야 합니다. `prog3.py`는 입력한 파일 이름을 현재 작업 폴더에서 찾습니다. VS Code에서는 저장소의 **Python: Current File** 디버그 구성을 사용하면 현재 파일이 있는 폴더를 작업 폴더로 설정해 실행할 수 있습니다.

## 참고

- 주차별 실습 코드는 학습 과정에서 작성한 예제와 문제 풀이입니다.
- 일부 프로그램은 사용자 입력을 받거나 파일을 생성합니다. 실행 전 각 파일의 문제 설명과 입력 파일을 확인하세요.
