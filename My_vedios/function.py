from manim import*

def get_intersect(line1, line2, parallel):
    p1, p2 = line1.get_start_and_end()
    p3, p4 = line2.get_start_and_end()

    a1 = p2[1] - p1[1]
    b1 = p1[0] - p2[0]
    c1 = a1 * p1[0] + b1 * p1[1]

    
    a2 = p4[1] - p3[1]
    b2 = p3[0] - p4[0]
    c2 = a2 * p3[0] + b2 * p3[1]

    determinant = a1 * b2 - a2 * b1

    if determinant == 0:
        return parallel
    else:
        x = (b2 * c1 - b1 * c2) / determinant
        y = (a1 * c2 - a2 * c1) / determinant
        return x * RIGHT + y * UP


import math

def easeOutBounce(t):
    if t < 1 / 2.75:
        return 7.5625 * t * t
    elif t < 2 / 2.75:
        c = t - 1.5/2.75
        return 7.5625 * c * c + 0.75
    elif t < 2.5 / 2.75:
        c = t - 2.25 / 2.75
        return 7.5625 * c * c + .9375
    else:
        c = t - 2.625 / 2.75
        return 7.5625 * c * c + .984375

def easeInBounce(t):
    return 1 - easeOutBounce(1 - t)

def easeInOutBounce(t):
    if t < 0.5:
        return easeInBounce(2 * t)
    else:
        return easeOutBounce(2 * t - 1)
    


def easeOutElastic(t):
    s, a = 1.70158, 1
    
    if t == 0: return 0
    if t == 1: return 1

    p = 0.3
    if a < 1:
        a, s = 1, p / 4
    else:
        s = p / (2 * math.pi) * math.asin(1 / a)

    return a * pow(2, -10 * t) * math.sin((t - s) * (2 * math.pi) / p) + 1




def get_tangent_line(px, py, cx, cy, r):
  """
  :param px: 圆外点P横坐标
  :param py: 圆外点P纵坐标
  :param cx: 圆心横坐标
  :param cy: 圆心纵坐标
  :param r:  圆半径
  :return:   [q1x, q1y, q2x, q2y]
  """
  # 求点到圆心的距离
  distance = math.sqrt((px-cx)*(px-cx)+(py-cy)*(py-cy))
  # print('distance', distance)
  # 点p 到切点的距离
  length = math.sqrt(distance*distance-r*r)
  # print('length', length)
  if distance <= r:
    print("输入的数值不在范围内")
    return
  # 点到圆心的单位向量
  ux = (cx-px)/distance
  uy = (cy-py)/distance
  # print('ux', ux)
  # print('uy', uy)
  # 计算切线与圆心连线的夹角
  angle = math.asin(r/distance)
  
  # 向正反两个方向旋转单位向量
  q1x = ux * math.cos(angle)  -  uy * math.sin(angle)
  q1y = ux * math.sin(angle)  +  uy * math.cos(angle)
  q2x = ux * math.cos(-angle) -  uy * math.sin(-angle)
  q2y = ux * math.sin(-angle) +  uy * math.cos(-angle)
  # 得到新座标y
  q1x = q1x * length + px
  q1y = q1y * length + py
  q2x = q2x * length + px
  q2y = q2y * length + py
  
  return [q1x, q1y, q2x, q2y]
