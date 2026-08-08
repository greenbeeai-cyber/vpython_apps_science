from vpython import *

scene = canvas(title = "RGB color 🪅", background = color.black, width = 800, height = 600)
screen = cylinder(pos=vec(0,0,0), axis=vec(0,0,0.1), radius=2, color=color.black)

light_R = sphere(pos=vec(-1.5, -1, 0), radius=0.5, color=color.red, emissive=True)
light_G = sphere(pos=vec(0, 1.5, 0), radius=0.5, color=color.green, emissive=True)
light_B = sphere(pos=vec(1.5, -1, 0), radius=0.5, color=color.blue, emissive=True)

def change_color(s):
    # s는 조작된 슬라이더 객체입니다.
    # 스크린의 색상을 슬라이더 R, G, B 값의 조합으로 변경합니다.
    screen.color = vec(sl_R.value, sl_G.value, sl_B.value)
    
    # 조명 구슬 자체의 투명도(opacity)도 조절하여 시각적 피드백 제공
    light_R.opacity = sl_R.value
    light_G.opacity = sl_G.value
    light_B.opacity = sl_B.value

# 5. UI 요소 추가 (텍스트와 슬라이더)
scene.append_to_caption('\n\n')

# Red 슬라이더
scene.append_to_caption('Red (빨강): ')
sl_R = slider(min=0, max=1, value=0, length=200, bind=change_color)
scene.append_to_caption('\n\n')

# Green 슬라이더
scene.append_to_caption('Green (초록): ')
sl_G = slider(min=0, max=1, value=0, length=200, bind=change_color)
scene.append_to_caption('\n\n')

# Blue 슬라이더
scene.append_to_caption('Blue (파랑): ')
sl_B = slider(min=0, max=1, value=0, length=200, bind=change_color)

# 현재 값을 보여주는 텍스트 라벨 (vpython의 wtext 기능 사용)
# text_val = wtext(text="현재 RGB 값 -> R: 0.0 / G: 0.0 / B: 0.0")

while True:
    rate(100)