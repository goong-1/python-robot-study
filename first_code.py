"""
[Python Execution Launcher]
설계: 코드가 성공적으로 실행되었음을 알리고 
현재의 실행 환경 정보를 출력합니다.
"""

import sys
import datetime

class CodeLauncher:
    def __init__(self, developer_name):
        self.developer = developer_name
        self.start_time = datetime.datetime.now()

    def launch_success(self):
        print("\n" + "🚀" * 20)
        print(f" [ 실행 성공: {self.developer} 아키텍트님 ]")
        print(f" 실행 시각: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 40)
        print(f" 사용 중인 파이썬: {sys.version.split()[0]}")
        print(f" 위치: {sys.executable}")
        print("\n 결과: 터미널(실행창)이 정상적으로 응답하고 있습니다!")
        print("🚀" * 20)

# --- 메인 실행부 (Main) ---
if __name__ == "__main__":
    # 질문자님의 닉네임으로 런처 가동
    my_url = "https://github.com/goong-1/python-robot-study.git"
    launcher = CodeLauncher("용인")
    launcher.launch_success()