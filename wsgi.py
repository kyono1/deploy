# 엔트리 파일
# 아파치 서버가 가장 먼저 찾는 파일

import sys
import os

cur_dir = os.getcwd()

#에러출력은 표준출력으로
sys.stdout = sys.stderr
sys.path.insert(0, cur_dir)

from run import app as application

