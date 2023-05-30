import numpy as np

# https://numpy.org/doc/stable/user/absolute_beginners.html#whats-the-difference-between-a-python-list-and-a-numpy-array

# 배열 생성
a = np.arange(6)
# [0, 1, 2, 3, 4, 5]

# 배열 안의 배열 - 2차월 형태
a2 = a[np.newaxis, :]
# [[0, 1, 2, 3, 4, 5]]

a.shape, a2.shape
# (6,) (1, 6)

# Numpy 배열 요소는 모두 숫자여야 한다.

a_list = [0, "1", 2.0, 3]
n_array = np.array(a_list)
# ['0', '1', '2.0', '3']


b = np.array([[1], [2], [3]])
b[0] #index 
b[1]
b[2]


# c = np.array([1, 2, 3])
# c = np.zeros(2)
# c = np.zeros([2, 3]) # [row, col]
# c = np.ones(2)
# c = np.ones([2, 3])
# c = np.empty(3) # 임의의 수
# c = np.empty([2, 3])

# c = np.arange(1, 4) # 시작값, 끝값
# c = np.arange(1, 11, 2) #시작, 끝, 등차간격


d = np.linspace(0, 50, num=5) 

x = np.ones([2, 3], dtype=np.int64) # 데이터 타입 지정해서 생성 
print(x)