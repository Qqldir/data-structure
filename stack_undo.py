# 문서 편집기의 되돌리기(undo) 기능

def editor_with_undo():
    text = ""
    stack = []

    while True:
        command = input("명령어 (입력/실행/undo/종료): ")
        if command == "입력":
            content = input("추가할 내용: ")
            stack.append(text)  # 현재 상태 저장
            text += content
        elif command == "undo":
            if stack:
                text = stack.pop()
                print("되돌리기 완료.")
            else:
                print("되돌릴 수 없습니다.")
        elif command == "실행":
            print("현재 문서 내용:", text)
        elif command == "종료":
            break

# editor_with_undo() 
