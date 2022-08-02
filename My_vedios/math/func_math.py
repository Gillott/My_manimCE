"""
这里存放着一些功能函数（基本都直接把源码复制了过来），
1.获取两条直线交点坐标的函数 get_intersect()
来自MK官方文档：https://docs.manim.org.cn/documentation/utils/space_ops.html
2.获取圆外一点与圆切点的函数 get_tangent_line()
来自@bilibili_UP主josepa的专栏:https://b23.tv/2mY0kDx
"""

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

##############################################################

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

#################################################################

class NBisector():
    """此类用于绘制N等分线（一条）"""
    def __init__(self,n:int,line1:Line,line2:Line):
        self.n = n 
        self.line1 = line1
        self.line2 = line2

    def get_the_line(self,line:Line):
        """请输入靠左边的Line"""
        dot = Dot(get_intersect(self.line1,self.line2,line))
        angle = Angle(self.line1,self.line2)
        angle_value = angle.get_value()
        rotate_dot = Dot(line.get_all_points()[3]).rotate((PI-angle_value)/self.n,about_point=dot.get_center())
        line_copy = Line(dot,rotate_dot)
        return line_copy

class ZesNBisector(NBisector):
    """更优雅的作图"""
    def __init__(self,n:int,line1:Line,line2:Line):
        NBisector.__init__(self,n,line1,line2)
    
    def get_the_line(self,line:Line):
        """请输入靠左边的Line"""
        dot = Dot(get_intersect(self.line1,self.line2,line))
        angle = Angle(self.line1,self.line2)
        angle_value = angle.get_value()
        rotate_dot = Dot(line.get_all_points()[3]).rotate((PI-angle_value)/self.n,about_point=dot.get_center())
        line_copy = Line(dot,rotate_dot)
        return VGroup(line_copy,dot)

    def get_zes_line(self,line_1:Line,line_2:Line):
        vg = self.get_the_line(line_1)
        line_a = vg[0].scale(100)
        intersection = Dot(get_intersect(line_a,line_2,line_2))
        target = Line(vg[1],intersection)
        return VGroup(intersection,target)

##################################################################################
    
class VerticalLine():
    """作直线外一点到此直线的一条垂线段"""
    def __init__(self,line:Line,dot:Dot):
        self.a = line.get_vector()[0]
        self.b = line.get_vector()[1]
        #self.c = line.get_vector()[2]
        self.dot = dot
        self.line = linear
        
    def calculate(self):
        def func(numbers:list):
            x,y = numbers[0],numbers[1]
            return [
            x*self.a + y*self.b ,
            np.sqrt((x-self.a)**2 + (y-self.b)**2) - 100
        ]  
        return fsolve(func,[0,0])

    def get_zes_line(self,line:Line):
        vec = self.calculate()
        dot1 = Dot(point=[vec[0]+self.dot.get_center()[0],vec[1]+self.dot.get_center()[1],0])
        line1 = line.copy().scale(100)
        line2 = Line(dot1,self.dot).scale(100)
        interpoint = Dot(get_intersect(line1,line2,line2))
        target_line = Line(self.dot,interpoint)
        return VGroup(interpoint,target_line)
