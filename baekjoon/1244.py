switch_num = int(input())
switch_status = list(map(int, input().split()))
student_num = int(input())

# print(f"스위치 수: {switch_num}, 학생 수: {student_num}, 스위치 상태: {switch_status}")

arr = []
for i in range(student_num):
    arr.append(list(map(int, input().split())))

# print(f"[성별, 받은 수]: {arr}")

for i in range(student_num):
    gender = arr[i][0]
    received_num = arr[i][1]
    print(f"성별: {gender}, 받은 수: {received_num}")

    # 남자인 경우
    if gender == 1:
        for j in range(switch_num):
            # 스위치 번호가 받은 수의 배수일 때
            if (j + 1) % received_num == 0:
                # print(f"스위치 {j + 1}번은 {received_num}의 배수")
                # 상태 역전
                if switch_status[j] == 0:
                    switch_status[j] = 1
                    # print(f"스위치 {j + 1}번을 0 -> 1로 변경")
                    # print(f"변경된 스위치 상태: {switch_status}")
                else:
                    switch_status[j] = 0
                    # print(f"스위치 {j + 1}번을 1 -> 0로 변경")
                    # print(f"변경된 스위치 상태: {switch_status}")
        print(f"변경된 스위치 상태: {switch_status}")

    # 여자인 경우
    if gender == 2:
        # 좌우로 움직일 수 있는 한계 설정
        limit = received_num
        if (switch_num - received_num - 1) < limit:
            limit = switch_num - received_num - 1

        # 인덱스 범위 계산
        cursor = 0
        for j in range(0, limit + 1):
            a = switch_status[received_num - 1 - j]
            b = switch_status[received_num - 1 + j]
            # print(f"{a}와 {b} 비교")

            if a == b:
                # print(f"{a}와 {b}가 같음")
                cursor = j
            else:
                # print(f"{a}와 {b}가 같지 않음, 중단")
                break

        min_index = received_num - 1 - cursor
        max_index = received_num - 1 + cursor

        print(f"인덱스 범위: {min_index} ~ {max_index}")

        # 범위 내 스위치 상태 역전
        for j in range(min_index, max_index + 1):
            if switch_status[j] == 0:
                print(f"스위치 {j + 1}번을 0 -> 1로 변경")
                switch_status[j] = 1
            else:
                print(f"스위치 {j + 1}번을 1 -> 0로 변경")
                switch_status[j] = 0
        print(f"변경된 스위치 상태: {switch_status}")

print(*switch_status)