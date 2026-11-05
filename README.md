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
└── lab
    ├── week 2
    │   ├── bmi.py
    │   ├── happy.py
    │   └── selfstudy.ipynb
    ├── week 3
    │   ├── bmi2.py
    │   ├── collections.ipynb
    │   ├── listex.ipynb
    │   └── typehint.ipynb
    ├── week 4
    │   ├── learn8.ipynb
    │   └── programming
    │       └── prob1.py ~ prob9.py
    ├── week 5
    │   ├── learn12.ipynb
    │   └── programming
    │       └── prog1.py ~ prog7.py
    ├── week 6
    │   ├── file.txt
    │   ├── kkk.png
    │   ├── learn10.ipynb
    │   ├── save.p
    │   └── programming
    │       ├── input.txt
    │       ├── prog1.py ~ prog4.py
    │       ├── prog5.py
    │       └── prog5.txt
    ├── week 7
    │   └── learn11.ipynb
    ├── week 9
    │   ├── cobutton.py
    │   ├── hellogui.py
    │   └── learn9.ipynb
    └── week 10
        ├── learn9.ipynb
        └── Programming
            └── prog1.py ~ prog6.py
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
