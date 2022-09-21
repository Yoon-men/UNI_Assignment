from collections import deque
import math

def FDT(dt) :                 # Frequency Distribution Table (FDT)
    def chkFrequency(s, e) : 
        result = 0
        while dt : 
            if s < dt[0] < e : 
                result += 1
                dt.popleft()
            else : return result
        return result
    n = len(dt)
    if n <= 200 : classNum = int(n**0.5-1)
    else : classNum = int(1 + 3.3*math.log10(n))
    interval = (max(dt)-min(dt)) // classNum
    quota = min(dt) - 0.5
    CF = 0                  # Cumulative Frequency (CF)
    CRF = 0                 # Cumulative Relative Frequency (CRF)
    print("|   계급    |     계급 간격     |   도수   |   상대도수  |  누적도수 | 누적상대도수|   계급값   |")
    for i in range(1, classNum+2) : 
        start = quota ; quota += interval ; end = quota
        frequency = chkFrequency(start, end)
        CF = frequency
        CRF += frequency/n
        print(f"|  제{i}계급  |    {start:>4} ~ {end:>4}    |    {frequency:>2}    |    {frequency/n:.3f}    |    {CF:>3}    |    {CRF:.3f}    |    {(start+end)/2}    |")

def RFH() :                 # Relative Frequency Histogram (RFH)

    pass                # Test code / please delete the contents of this line.

if __name__ == "__main__" : 
    print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠶⠶⠂⠀⠀⠀⢀⡀⠀⠀⠀⠀⢰⡆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠶⡆⢸⡏⢁⡩⢽⡆⣿⠉⣷⢸⡏⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠶⠴⠇⠸⠇⠘⠷⠾⠇⣿⠦⠏⠸⠇⠸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⢀⣀⡀⢀⡀⢀⢠⡞⠋⠛⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⣏⠀⣹⠘⣧⡏⠸⣇⠐⢲⡆⢾⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠋⠀⠈⠛⠉⠠⠜⠀⠀⠉⠛⠋⠁⠈⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """)
    print("[system] 데이터값을 공백으로 구분하여 입력하세요.\n         : (41부터 시작하는 리스트가 입력 완료되었다고 가정)")                # Test code / please delete the contents of this line.
    # data = deque(sorted(list(map(int, input("[system] 데이터값을 공백으로 구분하여 입력하세요.\n         : ").split()))))             # Test code / please unlock the contents of this line.
    data = deque(sorted(list(map(int, "41 32 30 23 24 32 11 39 24 46 50 18 41 14 33 50 38 25 32 16 43 19 35 22 46 43 10 22 17 47 66 48 25 43 28 31 12 25 12 48".split(" ")))))
    startType = int(input("\n[system] '도수분포표'를 그리려면 1번, '상대 도수 히스토그램'을 그리려면 2번을 입력하세요.\n         : "))
    print("\n")
    if startType==1 : print("[system] : ") ; FDT(data)
    else : RFH(data)