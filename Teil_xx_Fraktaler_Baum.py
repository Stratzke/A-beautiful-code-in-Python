import pygame as pg
import math


def zeichne_Baum(x, y, θ, tiefe):
  if not tiefe: return
  x2 = x + math.cos(θ) * tiefe * länge
  y2 = y + math.sin(θ) * tiefe * länge
  farbe.hsva = (120, tiefe*sv, tiefe*sv)
  pg.draw.line(fenster, farbe, (x, y), (x2, y2), 1)
  zeichne_Baum(x2, y2, θ - β, tiefe - 1)
  zeichne_Baum(x2, y2, θ + β, tiefe - 1)


β, länge, tiefe = math.radians(20), 5, 14
clock, BREITE, HÖHE = pg.time.Clock(), 800, 600
fenster = pg.display.set_mode((BREITE, HÖHE))
farbe, sv = pg.Color(0), 100/tiefe

zeichne_Baum(BREITE/2, HÖHE, math.radians(-90), tiefe)
pg.display.flip()

while True:
  clock.tick(5)
  for ereignis in pg.event.get():
    if ereignis.type == pg.QUIT: quit()
