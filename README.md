# PP2-2026

2026년도 프로그래밍 II(Programming II) 수업에서 작성한 Python 실습 코드와 노트북을 모아 둔 저장소입니다.
교재 내용을 정리하고, 교재에서 제시된 문제의 프로그램을 직접 작성하며 학습합니다.

교재: 파워 유저를 위한 파이썬 EXPRESS

---

## 저장소 구성

```text
.
PP2-2026
├── .gitignore
├── README.md
├── hello.py
├── markdown.md
├── mynotebook.ipynb
└── lab                         # 주차별 실습 자료
    ├── week 2                  # 2주차 실습
    │   ├── bmi.py              # BMI 계산 프로그램
    │   ├── happy.py            # Python 프로그램
    │   └── selfstudy.ipynb     # Python 실습 노트북
    ├── week 3                  # 3주차 실습
    │   ├── bmi2.py             # BMI 계산 프로그램
    │   ├── collections.ipynb   # 컬렉션 실습 노트북
    │   ├── listex.ipynb        # 리스트 실습 노트북
    │   └── typehint.ipynb      # 타입 힌트 실습 노트북
    ├── week 4                  # 4주차 실습
    │   ├── learn8.ipynb        # 챕터 8 수업 노트북
    │   └── programming         # 프로그래밍 문제 풀이 폴더
    │       └── prob1.py ~ prob9.py  # Python 문제 풀이 파일
    ├── week 5                  # 5주차 실습
    │   ├── learn12.ipynb       # 챕터 12 수업 노트북
    │   └── programming         # 프로그래밍 문제 풀이 폴더
    │       └── prog1.py ~ prog7.py  # Python 문제 풀이 파일
    ├── week 6                  # 6주차 실습
    │   ├── file.txt
    │   ├── kkk.png
    │   ├── learn10.ipynb       # 챕터 10 수업 노트북
    │   ├── save.p
    │   └── programming         # 프로그래밍 문제 풀이 폴더
    │       ├── input.txt       # 문제 풀이 입력 파일
    │       ├── prog1.py ~ prog5.py  # Python 문제 풀이 파일
    │       └── prog5.txt
    ├── week 7                  # 7주차 실습
    │   └── learn11.ipynb       # 챕터 11 수업 노트북
    ├── week 9                  # 9주차 실습
    │   ├── cobutton.py         # Tkinter GUI 프로그램
    │   ├── hellogui.py         # Tkinter GUI 프로그램
    │   └── learn9.ipynb        # 챕터 9 수업 노트북
    └── week 10                 # 10주차 실습
        ├── learn9.ipynb        # 챕터 9 실습 노트북
        └── Programming         # 프로그래밍 문제 풀이 폴더
            └── prog1.py ~ prog6.py  # Python 문제 풀이 파일
```

---

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
