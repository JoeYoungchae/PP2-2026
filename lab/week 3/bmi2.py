# 문제

# 여러 학생들의 키와 몸무게를 리스트로 입력 받아 BMI 리스트를 출력하는
# 함수와 테스트하는 함수를 작성하시오.
# BMI 함수는 지난 시간에 작성한 get_bmi 함수를 이용하여 작성하시오.

def get_bmi(weight_kg:float, height_cm:float) -> float:
    bmi = weight_kg / (height_cm/100) ** 2
    return bmi


def get_bmis(weights, heights):
    bmis = []

    for i in range(len(weights)):
        bmi = get_bmi(weights[i], heights[i])
        bmis.append(bmi)

    return bmis


def test():
    heights = [175, 160, 180]
    weights = [72, 55, 80]

    bmis = get_bmis(weights, heights)

    print("키:", heights)
    print("몸무게:", weights)
    print("BMI:", bmis)


if __name__ == "__main__":
    test()
