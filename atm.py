#잔액초기화 // 통장잔고
balance = 1000

while True: #조건이 True면 계속 작동한다.
    num = input("사용 목적을 번호로 선택 해 주세요(1.입금, 2.출금, 3.영수증보기, 4.종료): ")


    # 4를 입력하면 종료라는 출력 메세지
    # 개발할때 최소한의 자원만 쓸 수 있도록 고려를 해보는게 더 좋습니다.
    

    # 2번 출금 기능 코드
    if num == '2':
        withdraw_amount = int(input('출금할 금액을 입력해 주세요 : '))

        # withdraw_amount = min(balance, withdraw_amount) --> 파이썬의 내장함수 min을 사용한 방법.

        if balance >= withdraw_amount:
        
            balance -= withdraw_amount

            print(f'출금하신 금액은 {withdraw_amount}원이고, 현재 잔액은 {balance}입니다.')

        elif balance <= withdraw_amount:
            
            print(f'출금하실 금액이 잔액보다는 작아야 합니다.')
    
    # 1번 입금 기능 코드
    if num == '1':
        # 얼마를 입금할거야?
        deposit_amount = int(input("입금할 금액을 입력해 주세요 : "))
        # balance
        balance += deposit_amount #결과를 별도의 저장공간에 담아줘야한다.    

        print(f'입금하신 금엑은 {deposit_amount}원이고, 현재 잔액은 {balance} 입니다.')    

    
    
    # 4번 종료 기능 코드
    if num == '4':
        print('종료')
        break