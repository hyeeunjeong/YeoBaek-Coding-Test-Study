# O(g(n)) = {f(n) | 모든 n ≥ n0에 대하여 f(n) ≤ c × g(n)인 양의 상수 c와 n0가 존재한다}
# 함수 f(n) = a1n + a0, 양의 정수 c, n0가 주어질 경우 O(n) 정의를 만족하는지 알아보자.

# 첫째 줄에 함수 f(n)을 나타내는 정수 a1, a0가 주어진다. (0 ≤ |ai| ≤ 100)
# 다음 줄에 양의 정수 c가 주어진다. (1 ≤ c ≤ 100)
# 다음 줄에 양의 정수 n0가 주어진다. (1 ≤ n0 ≤ 100)

# 예시
# f(n) = 7n + 7
# g(n) = n
# c = 8
# n0 = 1이다
# f(1) = 14, c × g(1) = 8 이므로 정의를 만족하지 않음.

a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

f1 = a1 * n0 + a0
g1 = c * n0

if f1 <= g1 and a1 <= c:
  print(1)
else:
  print(0)