"""
这里存放着一些功能函数（基本都直接把源码复制了过来），
1.获取两条直线交点坐标的函数 get_intersect()
来自MK官方文档：https://docs.manim.org.cn/documentation/utils/space_ops.html
2.获取圆外一点与圆切点的函数 get_tangent_line()
来自@bilibili_UP主josepa的专栏:https://b23.tv/2mY0kDx
3.放了一些自己写的类（作用应该都标明清楚了吧）
"""

from manim import*
#SVG 图片类
############################################
class MurCat(VGroup):
    """mur猫表情包"""
    def __init__(self,**kwargs):
        VGroup.__init__(self,**kwargs)
        svg = SVGMobject("D:\\SVG\\murCat.svg").set_color(WHITE)
        self.add(svg)
        
class ThreeSVG(VGroup):
    """一键三连"""
    def __init__(self,**kwargs):
        VGroup.__init__(self,**kwargs)
        svg1 = SVGMobject("D:\\SVG\\good.svg").set_opacity(1).set_color(GRAY)
        svg2 = SVGMobject("D:\\SVG\\coin.svg").set_opacity(1).set_color(GRAY)
        svg3 = SVGMobject("D:\\SVG\\favo.svg").set_opacity(1).set_color(GRAY)
        self.add(svg1,svg2,svg3)
        
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

#################################################################################3
#计算 VMobject 距离
def get_norm(vector:Vector):
    vec = vector.copy()
    norm = np.sqrt(vec[0]**2 + vec[1]**2 + vec[2]**2)
    return norm
def get_length_beteen_two_points(dot1,dot2):
    vec = dot1 - dot2
    length = get_norm(vec)
    return length
def get_length_beteen_two_dots(dot1:Dot,dot2:Dot):
    vec = dot1.get_center() - dot2.get_center()
    length = np.sqrt(vec[0]**2 + vec[1]**2 + vec[2]**2)
    return length

    
def get_line_length(line:Line):
    vec = line.get_vector()
    length = np.sqrt(vec[0]**2 + vec[1]**2 + vec[2]**2)
    return length
def get_angle_between_two_vecs(vec1,vec2):
    module1 = get_length_beteen_two_dots(Dot([vec1]),Dot())
    module2 = get_length_beteen_two_dots(Dot([vec2]),Dot())
    a = module1*module2
    b = vec1[0]*vec2[0] + vec1[1]*vec2[1]
    cos = b/a
    angle = math.acos(cos)
    return angle
def get_angle_between_two_lines(line1:Line,line2:Line):
    vec1 = line1.get_vector()
    vec2 = line2.get_vector()
    return get_angle_between_two_vecs(vec1,vec2)

#############################################################################################

class VerticalLine():
    """"作直线外一点到此直线的垂线段"""
    def __init__(self,line:Line,dot:Dot):
        self.a = line.get_vector()[0]
        self.b = line.get_vector()[1]
        self.dot = dot
        self.line = line
        
    def calculate(self):
        def func(numbers:list):
            x,y = numbers[0],numbers[1]
            return [
            x*self.a + y*self.b ,
            np.sqrt((x-self.a)**2 + (y-self.b)**2) - 40
        ]  
        return fsolve(func,[0,0])

    def get_zes_line(self):
        vec = self.calculate()
        dot1 = Dot(point=[vec[0]+self.dot.get_center()[0],vec[1]+self.dot.get_center()[1],0])
        line1 = self.line.copy().scale(100)
        line2 = Line(dot1,self.dot).scale(100)
        interpoint = Dot(get_intersect(line1,line2,line2)).scale(0.5)
        target_line = Line(self.dot.scale(0.5),interpoint)
        return VGroup(interpoint,target_line)

###############################################################################################

class NBisector():
    """作一条n等分线"""
    def __init__(self,line1:Line,line2:Line,n=2):
        self.vec1 = line1.get_vector()
        self.vec2 = line2.get_vector()
        self.l1 = line1
        self.l2 = line2
        self.n = n
    
    def get_the_bisector(self,line:Line) -> Line :
        module1 = get_length_beteen_two_dots(Dot([self.vec1]),Dot())
        module2 = get_length_beteen_two_dots(Dot([self.vec2]),Dot())
        a = module1*module2
        b = self.vec1[0]*self.vec2[0] + self.vec1[1]*self.vec2[1]
        cos = b/a
        angle = (PI-math.acos(cos))/self.n
        target = line.copy().rotate(angle,about_point=get_intersect(self.l1,self.l2,line))
        return target

class ZesNBisector(NBisector):
    """作一条n等分线并交于第三边"""
    def __init__(self,line1:Line,line2:Line,n=2):
        NBisector.__init__(self,line1,line2,n)

    def get_the_bisector(self, line: Line):
        module1 = get_length_beteen_two_dots(Dot([self.vec1]),Dot())
        module2 = get_length_beteen_two_dots(Dot([self.vec2]),Dot())
        a = module1*module2
        b = self.vec1[0]*self.vec2[0] + self.vec1[1]*self.vec2[1]
        cos = b/a
        angle = (PI-math.acos(cos))/self.n
        target = line.copy().rotate(angle,about_point=get_intersect(self.l1,self.l2,line))
        dot = Dot(get_intersect(self.l1,self.l2,self.l2))
        return VGroup(dot,target)

    def get_zes_Line(self,line_1:Line,line_2:Line):
        """line_1：line1或line2，line_2：第三条边
        """
        vg = self.get_the_bisector(line_1)
        line_a = vg[1].scale(1000)
        line_b = line_2.copy().scale(1000)
        intersection = Dot(get_intersect(line_a,line_b,line_2))

        target = Line(vg[0].scale(0.1),intersection.copy().scale(0.1))
        return VGroup(vg[0].scale(0.5),target,intersection.scale(0.5))
   ######3###########################################################
    ##########################################################        

class VerticalLine():
    """Fran NB!"""
    def __init__(self,line:Line,dot:Dot):
        self.line = line
        self.dot = dot.get_center()

    def get_zes_dot_and_line(self):
        dot_a = self.line.get_all_points()[1]
        vec1 = dot_a - self.dot
        unit_vec = self.line.copy().rotate(PI/2).get_vector()
        unit = get_line_length(self.line)
        vec2 = unit_vec/unit
        vec3 = np.dot(vec1,vec2)*vec2
        dot = vec3 + self.dot
        line2 = Line(self.dot,dot)
        return VGroup(Dot(dot).scale(0.5),line2)

class DashedVerticalLine():
    """Fran NB!"""
    def __init__(self,line:Line,dot:Dot):
        self.line = line
        self.dot = dot.get_center()

    def get_zes_dot_and_line(self):
        dot_a = self.line.get_all_points()[1]
        vec1 = dot_a - self.dot
        unit_vec = self.line.copy().rotate(PI/2).get_vector()
        unit = get_line_length(self.line)
        vec2 = unit_vec/unit
        vec3 = np.dot(vec1,vec2)*vec2
        dot = vec3 + self.dot
        line2 = DashedLine(self.dot,dot)
        return VGroup(Dot(dot).scale(0.5),line2)
#####################################################################
class InterpointFromTwoCircles(VGroup):
    def __init__(self,cir1,cir2,color='#8a8eff',scale=1):
        super().__init__()
        vmob = Difference(cir1,cir2)
        points = vmob.get_all_points()
        m1 = cir1.get_all_points()[0]
        m2 = cir2.get_all_points()[0]
        dot_c = Dot(cir1.get_center())
        c1 = dot_c.get_center()
        c2 = cir2.get_center()
        radiu1 = get_length_beteen_two_points(m1,c1)
        radiu2 = get_length_beteen_two_points(m2,c2)
        list1 = []
        for i in range(len(points)):   
            if -0.01 < get_length_beteen_two_points(points[i],c1) - radiu1 < 0.01:
                if -0.01 < get_length_beteen_two_points(points[i],c2) - radiu2 < 0.01:
                    list1.append(points[i])
        if len(list1) > 0:
            dot1 = Dot(list1[0]).set_color(color).scale(scale)
            dot1_c = dot1.copy()
            dot2 = None
            self.add(dot1)
            i = 1
            if len(list1) > 2:
                while i <= len(list1)-1:
                    if (list1[i] == list1[0]).all():
                        i += 1
                        continue
                    else:
                        dot2 = Dot(list1[i]).set_color(color).scale(scale)
                        break
            if dot2 == None:
                self.add(dot1,dot1_c)
            else:
                self.add(dot1,dot2)
        else:
            dot1 = Dot().set_opacity(0)
            dot1_c = dot1.copy()
            self.add(dot1,dot1_c)

class InterpointFromCircleAndLine(VGroup):
    def __init__(self,cir:Circle,line:Line,color='#8a8eff',scale=1):
        super().__init__()
        cir_center = cir.get_center()
        line1 = line
        line2 = line1.copy().rotate(TAU)
        points1 = line1.get_all_points()
        points2 = line2.get_all_points()
        if (cir_center != points1[0]).all():
            vec1 = cir_center - points1[0]
            vec2 = cir_center - points2[0]
        else:
            vec1 = cir_center - points1[0]
            vec2 = cir_center - points2[0]
        unit_vec0 = line.get_unit_vector()
        unit_vec1 = vec1/get_norm(vec1)
        unit_vec2 = vec2/get_norm(vec2)
        if self.judge(unit_vec0,unit_vec1) != 0 and self.judge(unit_vec0,unit_vec2) != 0:
            cir_c = cir.copy().flip(axis=line.get_vector(),about_point=line.get_center())
            dots = InterpointFromTwoCircles(cir,cir_c,color)
            for dot in dots:
                self.add(dot)
        else:
            m = Dot(cir.get_all_points()[0])
            dot_c = Dot(cir.get_center())
            radiu = get_length_beteen_two_dots(m,dot_c)
            vec = line.get_unit_vector()
            dot1 = Dot(dot_c.get_center()).shift(vec*radiu).set_color(color).scale(scale)
            dot2 = Dot(dot_c.get_center()).shift(-vec*radiu).set_color(color).scale(scale)
            self.add(dot1,dot2)
    def judge(self,vec1,vec2):
        if vec1[0]*vec2[1] - vec1[1]*vec2[0] == 0:
            return 0
        else:
            return 1
