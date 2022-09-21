from collections import deque
import math

class GraphJoyGo() : 
    def __init__(self, dt) : 
        self.dt = deque(dt)

    def FDT(self, dt) :                 # Frequency Distribution Table (FDT)
        def chkFrequency(s, e) : 
            result = 0
            while self.dt : 
                if s < self.dt[0] < e : 
                    result += 1
                    self.dt.popleft()
                else : return result
            return result
        n = len(self.dt)
        if n <= 200 : classNum = int(n**0.5-1)
        else : classNum = int(1 + 3.3*math.log10(n))
        interval = (max(self.dt)-min(self.dt)) // classNum
        quota = min(self.dt) - 0.5
        CF = 0                  # Cumulative Frequency (CF)
        CRF = 0                 # Cumulative Relative Frequency (CRF)
        print("|   계급    |     계급 간격     |   도수   |   상대도수  | 누적도수 | 누적상대도수|   계급값   |")
        for i in range(1, classNum+2) : 
            start = quota ; quota += interval ; end = quota
            frequency = chkFrequency(start, end)
            CF += frequency
            CRF += frequency/n
            print(f"|  제{i}계급  |    {start:>4} ~ {end:>4}    |    {frequency:>2}    |    {frequency/n:.3f}    |    {CF:>2}    |    {CRF:.3f}    |    {(start+end)/2}    |")
        print(f"|   합 계   |                   |    {CF:>2}    |    {CRF:.3f}    |          |             |            |")
        self.dt = deque(dt)

    def RFH(self, dt) :                 # Relative Frequency Histogram (RFH)
        def chkFrequency(s, e) : 
            result = 0
            while self.dt : 
                if s < self.dt[0] < e : 
                    result += 1
                    self.dt.popleft()
                else : return result
            return result
        n = len(self.dt)
        if n <= 200 : classNum = int(n**0.5-1)
        else : classNum = int(1 + 3.3*math.log10(n))
        interval = (max(self.dt)-min(self.dt)) // classNum
        quota = min(self.dt) - 0.5
        dtDict = {}
        for _ in range(1, classNum+2) : 
            start = quota ; quota += interval ; end = quota
            dtDict[(start+end)/2] = chkFrequency(start, end)
        for i in range(max(dtDict.values()), 0, -1) : 
            for j in dtDict : 
                if dtDict[j] >= i : print("  * ", end="   ")
                else : print(" ", end=" "*6)
            print("\n")

        for i in dtDict : 
            print(i, end="   ")
        print("\n")
        self.dt = deque(dt)

if __name__ == "__main__" : 
    print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠶⠶⠂⠀⠀⠀⢀⡀⠀⠀⠀⠀⢰⡆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠶⡆⢸⡏⢁⡩⢽⡆⣿⠉⣷⢸⡏⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠶⠴⠇⠸⠇⠘⠷⠾⠇⣿⠦⠏⠸⠇⠸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⢀⣀⡀⢀⡀⢀⢠⡞⠋⠛⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⣏⠀⣹⠘⣧⡏⠸⣇⠐⢲⡆⢾⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠋⠀⠈⠛⠉⠠⠜⠀⠀⠉⠛⠋⠁⠈⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
    data = []
    while True : 
        cmd = int(input("\n[system] 예제 데이터 사용 - 0 / 데이터 직접 입력 - 1 / 도수분포표 작성 - 2 / 상대 도수 히스토그램 작성 - 3 / 프로그램 종료 - 4\n         : "))
        if cmd==0 : 
            data = sorted(list(map(int, "41 32 30 23 24 32 11 39 24 46 50 18 41 14 33 50 38 25 32 16 43 19 35 22 46 43 10 22 17 47 66 48 25 43 28 31 12 25 12 48".split(" "))))
            print("\n[system] 예제 데이터가 적용되었습니다.")
            graphJoyGo = GraphJoyGo(data)
        elif cmd==1 : 
            data = sorted(list(map(int, input("\n[system] 데이터값을 공백으로 구분하여 입력하세요.\n         : ").split())))
            graphJoyGo = GraphJoyGo(data)
        elif cmd==2 or cmd==3 : 
            if data : 
                print("")   
                if cmd==2 : graphJoyGo.FDT(data)
                else : graphJoyGo.RFH(data)
            else : print("\n[system] 아직 데이터값을 입력하지 않았습니다. 데이터값을 입력하세요.")
        elif cmd==4 : print("\n[system] 프로그램을 종료합니다.") ; break
        else : print("\n[system] 입력 허용 범위 이내로 입력해주세요.")