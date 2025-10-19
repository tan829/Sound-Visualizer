import pygame
import numpy as np
import sounddevice as sd
from random import uniform
import math

# 音频配置（全平台兼容）
samplerate = 44100
blocksize = 1024
current_volume = 0.0
current_pitch = 0.0

class Particle:
    def __init__(self, x, base_y, color):
        self.x = x
        self.y = base_y
        self.base_y = base_y
        self.color = color
        self.size = uniform(2, 4)
        self.speed = 0
        self.gravity = 0.05

    def update(self, volume):
        if self.speed == 0:
            self.speed = - (volume * 15 + 5)
        self.y += self.speed
        self.speed += self.gravity
        return self.y <= self.base_y + 10

    def draw(self, surface):
        alpha = int(255 - (self.y - (self.base_y - 200)) * 0.5)
        alpha = max(50, min(255, alpha))
        color_with_alpha = (*self.color, alpha)
        pygame.draw.circle(surface, color_with_alpha, (int(self.x), int(self.y)), int(self.size))

def audio_callback(indata, frames, time, status):
    global current_volume, current_pitch
    volume_raw = np.mean(np.abs(indata)) * 10
    current_volume = max(0.0, min(1.0, volume_raw))
    
    if current_volume < 0.05:
        current_pitch = 0.0
        return
    
    y = indata.flatten()
    zero_cross = np.sum(np.diff(np.sign(y)) != 0)
    current_pitch = max(100, min(1000, zero_cross * 5))

def main():
    pygame.init()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("声音粒子喷泉")
    clock = pygame.time.Clock()
    
    try:
        font = pygame.font.SysFont(["SimHei", "Microsoft YaHei", "Arial"], 22)
    except:
        font = pygame.font.SysFont(None, 22)
    
    particles = []
    fountain_x = screen_width // 2
    fountain_y = screen_height - 50
    
    try:
        with sd.InputStream(
            samplerate=samplerate,
            blocksize=blocksize,
            channels=1,
            callback=audio_callback,
            device=None
        ):
            running = True
            while running:
                screen.fill((10, 10, 20))
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            running = False
                
                particle_count = int(current_volume * 15)
                for _ in range(particle_count):
                    if current_pitch < 400:
                        r = int(50 + (current_pitch - 100) * 0.3)
                        g = int(50 + (current_pitch - 100) * 0.2)
                        b = int(200 - (current_pitch - 100) * 0.3)
                    else:
                        r = int(150 + (current_pitch - 400) * 0.2)
                        g = int(80 + (current_pitch - 400) * 0.1)
                        b = int(50)
                    r, g, b = min(255, r), min(255, g), min(255, b)
                    color = (r, g, b)
                    x = fountain_x + uniform(-30, 30)
                    particles.append(Particle(x, fountain_y, color))
                
                for p in particles[:]:
                    if not p.update(current_volume):
                        particles.remove(p)
                    else:
                        p.draw(screen)
                
                tips = [
                    f"音量: {current_volume:.2f}（说话/拍手控制粒子数量）",
                    f"音调: {int(current_pitch)}Hz（哼唱控制颜色）",
                    "按ESC退出"
                ]
                for i, tip in enumerate(tips):
                    text = font.render(tip, True, (200, 200, 255))
                    screen.blit(text, (10, 10 + i*30))
                
                pygame.display.flip()
                clock.tick(60)
    
    except Exception as e:
        print(f"错误：{e}")
        print("请检查麦克风权限或安装依赖")
    
    pygame.quit()

if __name__ == "__main__":
    main()