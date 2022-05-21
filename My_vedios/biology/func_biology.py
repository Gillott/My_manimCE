"""
ZesTable()类用于绘制生物棋盘法的表格，
当然，你也可以尝试使用manimCE自带的Table()类代替
"""


from manim import*

class ZesTable():
    """制作表格"""
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
        while n < self.rows*self.cols:
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
