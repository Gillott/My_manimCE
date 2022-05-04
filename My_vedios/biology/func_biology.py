"""
ZesTable()类用于绘制生物棋盘法的表格，
你也可以尝试使用manimCE自带的Table()类
"""



from manim import*

class ZesTable():
    """制作5*5的表格"""
    def get_zes_rectangle(self):
        """生成25个矩形框"""        
        rectangles = VGroup(*[ Rectangle(WHITE,width=1.5,height=1)for i in range(25)])
        return rectangles

    def get_zes_text(self,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x):
        """用于填写表格内容"""
        vg1 = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x]
        texts = VGroup(*[Text('') for i in range(25)])

        for number in range(1,25):
            texts[number].become(Text(vg1[number-1]).scale(0.7))
        return texts

    def get_zes_extra(self,a,b):
        """用于填写表格第一个空的内容"""
        p1 = np.array([-3.75,2.5,0])
        p2 = np.array([-2.25,2.5,0])
        p3 = np.array([-3.75,1.5,0])
        p4 = np.array([-2.25,1.5,0])
        triangle1 = Polygon(p1,p2,p4).set_color(WHITE)
        triangle2 = Polygon(p1,p3,p4).set_color(WHITE)

        t1 = Text(a).scale(0.7).set_color(RED)
        t1.move_to(triangle1).shift(RIGHT*0.3,UP*0.15)
        t2 = Text(b).scale(0.7).set_color(BLUE)
        t2.move_to(triangle2).shift(LEFT*0.3,DOWN*0.15)
        vg2 = VGroup(t1,t2,triangle1,triangle2)
        return vg2
