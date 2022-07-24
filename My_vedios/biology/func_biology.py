


from manim import*

class ZesTable():
"""
ZesTable()类用于绘制生物棋盘法的表格，
当然，你也可以尝试使用manimCE自带的Table()类代替
"""
    def __init__(self,rows:int,cols:int,width=1.5,height=1,):
        """构建表格框架"""       
        self.rows = rows            #行数
        self.cols = cols            #列数
        self.width = width          #单个矩形的宽度
        self.height = height        #单个矩形的高度

    def get_zes_table(self): 
        """绘制表格"""
        self.rectangles = VGroup(*[ Rectangle(WHITE,width =self.width,height=self.height)for i in range(self.rows*self.cols)])
        self.rectangles.arrange_in_grid(rows=self.rows,buff=0)
        return self.rectangles

    def get_zes_text(self,text:list):
        """填写表格内容,输入的为一个list列表"""
        n = 0
        texts = VGroup(*[Text('') for i in range(self.rows*self.cols)])
        while n < len(text):
            texts[n].become(Text(text[n],font='Source Han Sans SC',weight=MEDIUM).scale(0.66))
            n += 1
            continue
        return texts

    def get_the_first_text(self,a,b):
        """若需额外绘制斜线表头可调用此方法,
        并且最好令get_zes_text中的实参list第一个元素为"",
        以及需额外将此对象调整位置使之与表格第一个空对齐#move_to(obj[0])
        """
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

        t1 = Text(a).scale(0.7).set_color(RED)
        t1.move_to(tri1).shift(RIGHT*0.3,UP*0.15)
        t2 = Text(b).scale(0.7).set_color(BLUE)
        t2.move_to(tri2).shift(LEFT*0.3,DOWN*0.15)
        
        return VGroup(t1,t2,tri1,tri2)

    class FillRectangleToCenter():
    def __init__(self,rec:Rectangle):
        self.rec = rec

    def get_rec_dots(self):
        points = self.rec.get_all_points()
        lists = [points[0],points[4],points[7],points[11]]
        dots = VGroup(*[Text('') for i in range(4)])
        for i in range(4):
            dots[i].become(Dot(lists[i]))

        return dots 

    def fill_with_color(self,color=WHITE,opacity=1):
        dots = self.get_rec_dots()

        dot_a = dots[0].scale(0.001)
        dot_b = dots[1].scale(0.001)
        dot_c = dots[2].scale(0.001)
        dot_d = dots[3].scale(0.001)

        rec_copy = self.rec.copy()

        l_ab = Line(dot_a,dot_b,stroke_width=5).set_color(color).set_opacity(opacity)
        l_bc = Line(dot_b,dot_c,stroke_width=5).set_color(color).set_opacity(opacity)
        l_cd = Line(dot_c,dot_d,stroke_width=5).set_color(color).set_opacity(opacity)
        l_da = Line(dot_d,dot_a,stroke_width=5).set_color(color).set_opacity(opacity)
        
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
#################################################################
    
"""以下是用于给矩形上色的两个类
（基于dt，运行起来可能会很费力）
""""

class FillRectangleToCenter():
    def __init__(self,rec:Rectangle):
        self.rec = rec

    def get_rec_dots(self):
        points = self.rec.get_all_points()
        lists = [points[0],points[4],points[7],points[11]]
        dots = VGroup(*[Text('') for i in range(4)])
        for i in range(4):
            dots[i].become(Dot(lists[i]))

        return dots 

    def fill_with_color(self,color=WHITE,opacity=1):
        dots = self.get_rec_dots()

        dot_a = dots[0].scale(0.001)
        dot_b = dots[1].scale(0.001)
        dot_c = dots[2].scale(0.001)
        dot_d = dots[3].scale(0.001)

        rec_copy = self.rec.copy()

        l_ab = Line(dot_a,dot_b,stroke_width=5).set_color(color).set_opacity(opacity)
        l_bc = Line(dot_b,dot_c,stroke_width=5).set_color(color).set_opacity(opacity)
        l_cd = Line(dot_c,dot_d,stroke_width=5).set_color(color).set_opacity(opacity)
        l_da = Line(dot_d,dot_a,stroke_width=5).set_color(color).set_opacity(opacity)
        
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

class FillRectangleToRight():
    def __init__(self,rec:Rectangle):
        self.rec = rec

    def get_rec_dots(self):
        points = self.rec.get_all_points()
        lists = [points[0],points[4],points[7],points[11]]
        dots = VGroup(*[Text('') for i in range(4)])
        for i in range(4):
            dots[i].become(Dot(lists[i]))

        return dots 

    def fill_with_color(self,color=WHITE,opacity=1,v=1):
        dots = self.get_rec_dots()

        dot_a = dots[0].scale(0.001)
        dot_b = dots[1].scale(0.001)
        dot_c = dots[2].scale(0.001)
        dot_d = dots[3].scale(0.001)

        rec_copy = self.rec.copy()
        
        target1 = dot_b.copy()
        target2 = dot_c.copy()
        target_line1 = Line(dot_b,dot_c,stroke_width=5).set_color(color).set_opacity(opacity)
        target_line2 = Line(dot_b,dot_c,stroke_width=5).set_color(color).set_opacity(opacity).shift(RIGHT*0.2)
            
        def updater_dot(target):
            def anim(obj,dt):
                obj.shift(
                        (target.get_center() - obj.get_center())*dt*1.5*v
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
