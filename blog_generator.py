from datetime import datetime

def generate_blog():
    title = "자동 생성 블로그 글"
    content = f"""
제목: {title}

이 글은 AI로 자동 생성되었습니다.
작성 시간: {datetime.now()}

내용:
AI를 활용하면 반복 작업을 줄이고 생산성을 높일 수 있습니다.
"""
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(content)

    print("블로그 생성 완료!")

if __name__ == "__main__":
    generate_blog()
