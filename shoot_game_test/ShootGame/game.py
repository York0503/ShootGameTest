#專案組成
#1.code程式碼
#2.assets(靜態資料照片.圖檔)
# 可以跑正個資料夾
# __main__主程式架構
# game 維持由序運作得循環 while迴圈
# modles 做好的object放置處
# utils 基礎佈屬於任何地方的邏輯，簡稱雜物堆

#學習架構 project邏輯 function分工

import pygame
from utils import load_sprite

class SpaceRocks:
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((800, 600))
        self.background = load_sprite("space")

    def main_loop(self):
        while True:
            self._handle_input()
            self._process_game_logic()
            self._draw()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Space Rocks")

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                quit()

    def _process_game_logic(self):
        pass

    def _draw(self):
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()