#-*-coding: utf-8 -*一
from turtle import * # 描画環境turtleをインポート
# rose_window_recursion(四角形の4頂点，内分比，繰り返し回数）
def rose_window_recursion(points, ratio, depth):
    rectangle(points)
    new_points = deviding_points(points, ratio)
    if depth== 0:
        up()
        setpos(-200, -200)
    else:
        rose_window_recursion(new_points, ratio, depth - 1)

def deviding(p0 , p1 , r ):
    return p0*(1-r) + p1*r

#以下は補助的な関数
# rectangle(四角形の4 頂点）
def rectangle(points):
    [[xO, yO], [x1, y1], [x2, y2], [x3, y3]] = points
    up()
    setpos(xO, yO)
    down()
    setpos(x1, y1)
    setpos(x2, y2)
    setpos(x3, y3)
    setpos(xO, yO)
# 2点の内分点を求める．
# deviding_point(点A, 点B, 内分比）
def deviding_point(pO, p1, ratio):
    [xO, yO] = pO
    [x1, y1] = p1
    xr = deviding(xO, x1, ratio)
    yr= deviding(yO, y1, ratio)
    return [xr, yr]
#四角形の各辺の内分点を求める
# deviding_points( 四角形の4頂点内分比）
def deviding_points(points, ratio):
    [pO, p1, p2, p3] = points
    prO = deviding_point(pO, p1, ratio)
    pr1 = deviding_point(p1, p2, ratio)
    pr2 = deviding_point(p2, p3, ratio)
    pr3 = deviding_point(p3, pO, ratio)
    return [pr0, pr1, pr2, pr3]