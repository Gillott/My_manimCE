from manim import*
import numpy as np

def get_length_beteen_two_points(point1,point2):
    vec = point1 - point2
    length = np.sqrt(vec[0]**2 + vec[1]**2 + vec[2]**2)
    return length

def get_norm(vector:Vector):
    vec = vector.copy()
    norm = np.sqrt(vec[0]**2 + vec[1]**2 + vec[2]**2)
    return norm

def get_mob_length(mob1:VMobject,mob2:VMobject):
    point1 = mob1.get_center()
    point2 = mob2.get_center()
    return get_length_beteen_two_points(point1,point2)

def get_zes_orbit(mob1:VMobject,mob2:VMobject):
    radius = get_mob_length(mob1,mob2)
    orbit = Circle(radius=radius*0.8).rotate(PI/2).move_to(mob2.get_center()).set_opacity(0)
    return(orbit)


class ZesText(Text):
    """字幕"""
    def __init__(self, text: str,**kwargs):
        super().__init__(text,font='Source Han Sans SC',weight=MEDIUM,**kwargs)


class MurCat(VGroup):
    """mur猫表情包"""
    def __init__(self,**kwargs):
        VGroup.__init__(self,**kwargs)
        svg = SVGMobject("D:\\SVG\\murCat.svg").set_color(WHITE)
        self.add(svg)


class ZesArrow(VGroup):
    """向上箭头"""
    def __init__(self,**kwargs):
        VGroup.__init__(self,**kwargs)
        arrow = Polygon(
            [0,4.5,0],
            [-2,0,0],
            [-0.5,0,0],
            [-0.5,-8,0],
            [1,-8,0],
            [1,0,0],
            [2,0,0]
        ).scale(0.1).set_opacity(1).set_color(WHITE)
        self.add(arrow)

class ZesTable():
    """制作表格"""
    def __init__(self,rows:int,cols:int,width=1.5,height=1,):
        """初始化表格参数"""       
        self.rows = rows
        self.cols = cols 
        self.width = width
        self.height = height

    def get_zes_table(self): 
        self.rectangles = VGroup(*[ Rectangle(WHITE,width =self.width,height=self.height)for i in range(self.rows*self.cols)])
        self.rectangles.arrange_in_grid(rows=self.rows,buff=0)
        return self.rectangles

    def get_zes_text(self,text:list):
        """填写表格内容,"""
        n = 0
        texts = VGroup(*[Text('') for i in range(self.rows*self.cols)])
        while n < len(text):
            texts[n].become(Text(text[n],font='Source Han Sans SC',weight=MEDIUM).scale(0.66))
            n += 1
            continue
        return texts

    def get_the_first_text(self,a,b):
        """绘制并填写斜线表头"""
        rec = Rectangle(width=self.width,height=self.height)
        points = rec.get_all_points()
        #p1 = np.array([-3.75,2.5,0])
        p1 = np.array(points[3])
        #p2 = np.array([-2.25,2.5,0])
        p2 = points[0]
        #p3 = np.array([-3.75,1.5,0])
        p3 = points[7]
        #p4 = np.array([-2.25,1.5,0])
        p4 = points[-4]
        tri1 = Polygon(p1,p2,p4).set_color(WHITE)
        tri2 = Polygon(p1,p3,p4).set_color(WHITE)

        t1 = Text(a,font='Source Han Sans SC',weight=MEDIUM).scale(0.7).set_color(RED)
        t1.move_to(tri1).shift(RIGHT*0.3,UP*0.15)
        t2 = Text(b,font='Source Han Sans SC',weight=MEDIUM).scale(0.7).set_color(BLUE)
        t2.move_to(tri2).shift(LEFT*0.3,DOWN*0.15)
        
        return VGroup(t1,t2,tri1,tri2)


class FillRectangleToCenter():
    def __init__(self,rec:Rectangle,color=WHITE,opacity=1):
        
        self.rec = rec
        self.color = color
        self.opacity = opacity
        
    def get_rec_dots(self):
        points = self.rec.get_all_points()
        lists = [points[0],points[4],points[7],points[11]]
        dots = VGroup(*[Text('') for i in range(4)])
        for i in range(4):
            dots[i].become(Dot(lists[i]))
        return dots 

    def fill_with_color(self):
        dots = self.get_rec_dots()
        dot_a = dots[0].scale(0.001)
        dot_b = dots[1].scale(0.001)
        dot_c = dots[2].scale(0.001)
        dot_d = dots[3].scale(0.001)

        rec_copy = self.rec.copy()

        l_ab = Line(dot_a,dot_b,stroke_width=5).set_color(self.color).set_opacity(self.opacity)
        l_bc = Line(dot_b,dot_c,stroke_width=5).set_color(self.color).set_opacity(self.opacity)
        l_cd = Line(dot_c,dot_d,stroke_width=5).set_color(self.color).set_opacity(self.opacity)
        l_da = Line(dot_d,dot_a,stroke_width=5).set_color(self.color).set_opacity(self.opacity)
        
        def updater_dot(target):
            def anim(obj,dt):
                obj.shift(
                    (target.get_center() - obj.get_center())*dt*1.3
                )
            return anim

        def put_line_on(a,b):
            def update(line):
                line.put_start_and_end_on(a.get_center(),b.get_center())
            return update

        dot_a.add_updater(updater_dot(dot_b))
        dot_b.add_updater(updater_dot(dot_c))
        dot_c.add_updater(updater_dot(dot_d))
        dot_d.add_updater(updater_dot(dot_a))

        #self.add(dot_a,dot_b,dot_c,dot_d)

        l_ab.add_updater(put_line_on(dot_a,dot_b))
        l_bc.add_updater(put_line_on(dot_b,dot_c))
        l_cd.add_updater(put_line_on(dot_c,dot_d))
        l_da.add_updater(put_line_on(dot_d,dot_a))

        trace = VGroup()
        trace.add_updater(lambda a:a.add(
            l_ab.copy().clear_updaters(),
            l_bc.copy().clear_updaters(),
            l_cd.copy().clear_updaters(),
            l_da.copy().clear_updaters(),
        ))
        
        return VGroup(rec_copy,dot_a,dot_b,dot_c,dot_d,l_ab,l_bc,l_cd,l_da,trace,rec_copy)



class FillRectangleToRight(VGroup):
    def __init__(self,rec:Rectangle,color=WHITE,opacity=1):
        VGroup.__init__(self)
        self.rec = rec
        self.color = color 
        self.opacity = opacity
        self.add(self.fill_with_color())
        

    def get_rec_dots(self):
        points = self.rec.get_all_points()
        lists = [points[0],points[4],points[7],points[11]]
        dots = VGroup(*[Text('') for i in range(4)])
        for i in range(4):
            dots[i].become(Dot(lists[i]))

        return dots 

    def fill_with_color(self):
        dots = self.get_rec_dots()

        dot_a = dots[0].scale(0.001)
        dot_b = dots[1].scale(0.001)
        dot_c = dots[2].scale(0.001)
        dot_d = dots[3].scale(0.001)

        rec_copy = self.rec.copy()
        
        target1 = dot_b.copy()
        target2 = dot_c.copy()
        target_line1 = Line(dot_b,dot_c,stroke_width=5).set_color(self.color).set_opacity(self.opacity)
        target_line2 = Line(dot_b,dot_c,stroke_width=5).set_color(self.color).set_opacity(self.opacity).shift(RIGHT*0.2)
            
        def updater_dot(target):
            def anim(obj,dt):
                obj.shift(
                        (target.get_center() - obj.get_center())*dt*1.5
                    )
            return anim

        def put_line_on(a,b):
            def update(line):
                line.put_start_and_end_on(a.get_center(),b.get_center())
            return update

        target1.add_updater(updater_dot(dot_a))
        target2.add_updater(updater_dot(dot_d))
        target_line1.add_updater(put_line_on(target1,target2))
        target_line2.add_updater(put_line_on(target1,target2))

        trace = VGroup()
        trace.add_updater(lambda a:a.add(target_line1.copy().clear_updaters()))

        return VGroup(rec_copy,target1,target2,target_line1,trace,rec_copy)


class SwallowIn(Homotopy):

    def __init__(self, mobject, target, **kwargs):
        #config(self, kwargs, locals())

        distance = max(
            get_norm(mobject.get_corner(UL)-target), 
            get_norm(mobject.get_corner(UR)-target), 
            get_norm(mobject.get_corner(DL)-target), 
            get_norm(mobject.get_corner(DR)-target),
            )
        
        def homotopy(x, y, z, t):
            position = np.array([x, y, z])
            vect = position - target
            length = get_norm(vect)
            move = t * distance
            if move >= length:
                return target
            else:
                ratio = 1 - move/length
                return target + np.array([ratio * vect[0], np.sqrt(ratio) * vect[1], 0])

        super().__init__(homotopy, mobject, **kwargs)

class RotateToRight(VGroup):
    def __init__(self,mob1:VMobject,mob2:VMobject):
        self.mob1 = mob1
        self.mob2 = mob2
        self.a = mob1.get_center()
        self.b = mob2.get_center()
        self.rotate()

    def get_about_point(self):
        length = get_length_beteen_two_points(self.a,self.b)
        dot = Dot([interpolate(self.a,self.b,0.5)])
        about_point = dot.copy().shift(UP*length*np.sqrt(3)/2)
        return about_point

    def rotate(self):
        point = self.get_about_point().get_center()

        def rotate_with_updater(mob1:VMobject,dt):
            mob1.rotate((PI*4 - 3/PI)*dt)
            mob1.rotate(dt*PI/3,about_point=point)

        self.mob1.add_updater(rotate_with_updater)


class RotateAndShiftToRight(RotateToRight):
    def __init__(self,mob1:VMobject,mob2:VMobject,orbit:VMobject,run_time=1):
        self.mob1 = mob1
        self.mob2 = mob2
        self.orbit = orbit
        self.run_time = run_time
        self.rotate()

    def rotate(self):
        self.mob1.add_updater(lambda x:x.move_to(self.orbit.get_start()))
        def rotate1(mob:VMobject,dt):
            mob.move_to(self.mob2.get_center())
            mob.rotate(2*PI*dt,about_point=self.mob2.get_center())
        def rotate2(mob:VMobject,dt):
            mob.move_to(self.orbit.get_start())
            mob.rotate(6*PI*dt,about_point=mob.get_center())
        
        self.mob1.add_updater(rotate2)
        self.orbit.add_updater(rotate1)


class DialogBox(VGroup):
    def __init__(self,width=3,height=1,color=WHITE):
        super().__init__()
        self.box = RoundedRectangle(corner_radius=0.2,height=height,width=width).set_color(color).set_opacity(0.3)
        self.sector = Sector(outer_radius=height/3, inner_radius=0).set_color(color).rotate(3*PI/2)
        self.b_c = self.box.copy().set_stroke(opacity=1)
        self.add(self.box,self.sector,self.b_c)
        self.sector.next_to(self.box,DOWN,buff=0).shift(LEFT*width/3)
