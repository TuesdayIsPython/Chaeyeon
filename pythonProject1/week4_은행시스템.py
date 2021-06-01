prompt = """
...1. 예금 입금
...2. 예금 출금
...3. 잔액 조회
...4. 업무 종료하기
...
... 수행하실 업무를 입력하세요 : """

number=0
money = 10000000
while number !=4:
    print(prompt)
    number = int(input())
    print (number)
    if number ==2:
        print("예금 출금하시겠습니까? 현재 출금 가능한 금액은 %d원입니다" %money)
        out = int(input("출금하실 금액을 입력해주세요. "))
        if out > 10000000:
            print("출금 금액이 출금가능 금액을 초과하셨습니다. 은행 시스템을 재시작합니다.")
        else:
            money = money-out

    elif number ==1:
        print("예금 입급하시겠습니까?")
        get = int(input("입금하실 금액을 입력해주세요:"))
        print("입금하신 금액은 %d원입니다." %get)
        money = money + get

    elif number ==3:
        print("잔액 조회를 도와드리겠습니다. ")
        print("현재 잔액은 %d원입니다. " %money)
    else:
        print("은행 시스템을 종료합니다.")