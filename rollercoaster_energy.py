from vpython import *
import math

scene = canvas(title="롤러코스터 역학적 에너지", width=800, height=400, background=color.black)

# 1. 코사인 함수를 이용한 곡선 트랙 생성
track = curve(color=color.white, radius=0.1)
for x in range(-100, 101):
    xx = x * 0.1
    yy = 3 * math.cos(0.5 * xx)
    track.append(vec(xx, yy, 0))

# 2. 롤러코스터 수레(공) 생성
cart = box(pos=vec(-10, 3 * math.cos(-5), 0), size=vec(0.4, 0.4, 0.4), color=color.cyan)

# 3. 실시간 에너지 변화를 그릴 그래프 설정
g_energy = graph(title="에너지 변화 그래프", xtitle="시간(t)", ytitle="에너지(J)", width=800, height=300)
line_Ep = gcurve(color=color.blue, label="위치에너지 (Ep)")
line_Ek = gcurve(color=color.red, label="운동에너지 (Ek)")
line_E  = gcurve(color=color.green, label="역학적 에너지 총합 (E)")

g = 9.8      # 중력 가속도
m = 1.0      # 롤러코스터 질량
v = 1.0      # 초기 속도
x = -10.0    # 출발 X 좌표
dt = 0.01    # 시간 간격
t = 0        # 누적 시간

while x < 100:
    rate(100)
    
    # 트랙 방정식: y = 3 * cos(0.5 * x)
    # 현재 위치에서의 접선의 기울기 계산 (미분)
    slope = -1.5 * math.sin(0.5 * x)
    theta = math.atan(slope) # 기울기를 각도(라디안)로 변환
    
    # 경사면 방향의 실제 가속도 (a = -g * sin(theta))
    a = -g * math.sin(theta)
    
    # 속도와 이동거리 적분
    v = v + a * dt
    ds = v * dt
    
    # 롤러코스터 좌표 업데이트
    x = x + ds * math.cos(theta)
    y = 3 * math.cos(0.5 * x)
    cart.pos = vec(x, y, 0)

 # 기준면을 화면 가장 아래(y = -3)로 설정하여 높이 h 계산
    h = y + 3
    
    # 에너지 공식 계산 (속도의 제곱은 v * v 로 표현)
    Ep = m * g * h
    Ek = 0.5 * m * v * v
    E = Ep + Ek
    
    # 그래프에 현재 프레임의 데이터 플롯
    line_Ep.plot(t, Ep)
    line_Ek.plot(t, Ek)
    line_E.plot(t, E)
    
    t = t + dt
    