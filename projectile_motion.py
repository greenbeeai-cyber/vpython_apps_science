from vpython import *
import math

scene = canvas(title="포물선 운동 시뮬레이터", width=800, height=400, background=color.black)
ground = box(pos=vec(0, -0.2, 0), size=vec(100, 0.4, 10), color=color.green)

# 이상적인 공 (노란색) only gravity
ball_ideal = sphere(pos=vec(-20, 0, -2), radius=0.5, color=color.blue, make_trail=True, emissive = True)
# 현실적인 공 (빨간색 - 공기저항)
ball_real = sphere(pos=vec(-20, 0, 2), radius=0.5, color=color.red, make_trail=True, emissive = True)

g = vec(0, -9.8, 0) # 중력 가속도 벡터 (아래로 9.8)
v0 = 20 # 초기 발사 속력
launch_angle = 45 # 45도 각도로 발사 

# 각도를 라디안으로 변환
angle_rad = math.radians(launch_angle)

# 삼각비를 이용해 속도를 분해 (X방향은 cos, Y방향은 sin)
vx = v0 * math.cos(angle_rad)
vy = v0 * math.sin(angle_rad)

# 두 공에 동일한 초기 속도 부여
ball_ideal.v = vec(vx, vy, 0)
ball_real.v = vec(vx, vy, 0)

m = 1.0 # 공의 질량
k = 0.1 # 공기 저항 계수 (이 값이 클수록 저항이 심함)
dt = 0.01 # 시간 간격



while ball_ideal.pos.y >= 0 or ball_real.pos.y >= 0:
    rate(100) # 초당 100프레임 재생
    
    # 1. 이상적인 공 (진공 상태: 중력만 작용)
    if ball_ideal.pos.y >= 0:
        F_ideal = m * g # 힘 = 질량 x 중력가속도
        ball_ideal.v = ball_ideal.v + (F_ideal / m) * dt
        ball_ideal.pos = ball_ideal.pos + ball_ideal.v * dt
        
    # 2. 현실적인 공 (공기 저항 작용)
    if ball_real.pos.y >= 0:
        # 합력 = 중력 - (저항계수 * 현재 속도)
        F_real = m * g - k * ball_real.v
        ball_real.v = ball_real.v + (F_real / m) * dt
        ball_real.pos = ball_real.pos + ball_real.v * dt

    