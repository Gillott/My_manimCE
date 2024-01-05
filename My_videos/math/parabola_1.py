"""
如果想运行以下（屎山）代码，
请先保证你已经安装成功manimCE，
并且可以使用func_math.py里被调用的函数。
此代码渲染后的效果见：https://www.bilibili.com/video/BV1z3411K7cF
"""


from manim import *
from func_math import *


class ZesTex(Tex):
    def __init__(self, *tex_strings, arg_separator="", **kwargs):
        super().__init__(*tex_strings, arg_separator=arg_separator,tex_template=TexTemplateLibrary.ctex,**kwargs)
        self.scale(0.65)
        

class CaptionText(Text):
    """字幕"""
    def __init__(self, text: str,**kwargs):
        super().__init__(text,font='Source Han Sans SC',weight=MEDIUM,**kwargs)
        self.scale(0.6).to_corner(DOWN,buff=0.3)

                
#场景类
class Math(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        blue = '#0DC4F2'
#更新两点连线    
        def update_zes_line(dot1,dot2):
            def updater(line):
                line.put_start_and_end_on(dot1.get_center(),dot2.get_center())
            return updater
#抛物线方程
        def func(x):
            return x**2/4
        def func_1(x):
            return -x**2/4
#准线        
        def func2(y):
            return 0
#坐标轴
        ax = Axes(
            x_range=[-7,3],x_length=10,
            y_range=[-2.5,5],y_length=7.5,
        ).scale(0.6).shift(DOWN*0.4)
        labels = ax.get_axis_labels(x_label="x", y_label="y")
#原点
        o = Dot(ax.c2p(0,0))
#抛物线图像        
        f_xy = ax.plot(
            func,
            color=MAROON,
            x_range=[-4,4],
            use_smoothing=True
        ).rotate(-PI/2,about_point=ax.c2p(0,0))
        f_xy_0 = ax.plot(
            func,
            color=MAROON,
            x_range=[-4,2.5],
            use_smoothing=True
        ).rotate(-PI/2,about_point=ax.c2p(0,0))
        f_xy_1 = ax.plot(
            func_1,
            color=MAROON,
            x_range=[-2.5,4],
            use_smoothing=True
        ).rotate(PI/2,about_point=ax.c2p(0,0))
        f_xy_2 = ax.plot(
            func_1,
            color=MAROON,
            x_range=[-2.5,2*np.sqrt(5)-4+0.01],
            use_smoothing=True
        ).rotate(PI/2,about_point=ax.c2p(0,0))
#准线图像
        y = DashedVMobject(ax.plot(func2,x_range=[-6,3]).rotate(-PI/2,about_point=ax.c2p(-1,0)))
#焦点
        f = Dot(ax.c2p(1,0))
        note_f = Tex('F').scale(0.6)
        note_f.add_updater(lambda x:x.next_to(f,DOWN*0.2))
#抛物线上的动点P
        p = Dot(ax.i2gp(f_xy.t_max,f_xy), color=MAROON)
        note_p = Tex('P').scale(0.6).set_color(MAROON)
        note_p.add_updater(lambda x:x.next_to(p,RIGHT,buff=0.1))
#准线垂足v
        e = Dot(ax.c2p(-1,ax.p2c(p.get_center())[1],0))
        e.add_updater(lambda x:x.become(Dot(ax.c2p(-1,ax.p2c(p.get_center())[1],0))))
        note_e = Tex('E').scale(0.6)
        note_e.add_updater(lambda x:x.next_to(e,DR*0.1))
#直线x=2
        y_1 = Line(ax.c2p(-2,4.8),ax.c2p(-2,-3)).set_color(GREEN).set_sheen(0.3,DOWN)
    #垂足
        h = Dot(ax.c2p(-2,ax.p2c(p.get_center())[1],0)).set_color(GREEN_A)
        h.add_updater(lambda x:x.become(Dot(ax.c2p(-2,ax.p2c(p.get_center())[1],0)).set_color(GREEN_A)))
        note_h = Tex('H').scale(0.6).set_color(GREEN_A)
        note_h.add_updater(lambda x:x.next_to(h,LEFT,buff=0.1))
#圆心
        c = Dot(ax.c2p(-5,3)).set_color(RED_C)
        note_c = Tex('C').scale(0.6).set_color(RED_C)
        note_c.add_updater(lambda x:x.next_to(c,DOWN,buff=0.1))
#圆图像
        cir = Circle(
            radius=np.sqrt(2)*0.6
        ).move_to(c.get_center()).set_color([ORANGE,PINK]).set_sheen_direction(UL)
        circle = Circle(
            radius=1.21,
            stroke_width=2
        ).move_to(c.get_center()).set_color([BLUE,DARK_BROWN]).set_sheen_direction(UL)
#切线
        line_1 = TangentLine(cir, alpha=0.0)
        line_2 = TangentLine(cir, alpha=0.25)
#切线交点        
        q = Dot(get_intersect(line_1,line_2,line_1))
        note_q = Tex('Q').scale(0.6).set_color(YELLOW_A)
        note_q.add_updater(lambda x:x.next_to(q,UR,buff=0.1))
#绘制过原点与q点的正比例函数图像        
        def get_zes_graph(t):
            x = ax.p2c(q.get_center())[0]
            y = ax.p2c(q.get_center())[1]
            k = y/x
            return k*t
        zes_graph = ax.plot(get_zes_graph,x_range=[-4,3]).set_color(YELLOW_B)

        q_copy = Dot(ax.i2gp(-0.8,zes_graph)).set_color(YELLOW_A)
        note_q_copy = Tex('Q').scale(0.6).set_color(YELLOW_A)
        note_q_copy.add_updater(lambda x:x.next_to(q_copy,UR,buff=0.0001))
        
        t1 = ValueTracker(ax.p2c(q_copy.get_center())[0]).add_updater(
            lambda x:x.set_value(ax.p2c(q_copy.get_center())[0])
        )
        t2 = ValueTracker(ax.p2c(q_copy.get_center())[1]).add_updater(
            lambda x:x.set_value(ax.p2c(q_copy.get_center())[1])
        )
        t3 = ValueTracker(ax.p2c(c.get_center())[0]).add_updater(
            lambda x:x.set_value(ax.p2c(c.get_center())[0])
        )      
        t4 = ValueTracker(ax.p2c(c.get_center())[1]).add_updater(
            lambda x:x.set_value(ax.p2c(c.get_center())[1])
        )

        tan_dot2 = Dot(
                ax.c2p(
                    get_tangent_line(
                        t1.get_value(),
                        t2.get_value(),
                        t3.get_value(),
                        t4.get_value(),
                        np.sqrt(2)
                    )[0],
                        get_tangent_line(
                        t1.get_value(),
                        t2.get_value(),
                        t3.get_value(),
                        t4.get_value(),
                        np.sqrt(2)
                    )[1],
                )
            )
        tan_dot2.scale(0.1).set_color(RED)
        
        tan_dot1 = Dot(
                ax.c2p(
                    get_tangent_line(
                        t1.get_value(),
                        t2.get_value(),
                        t3.get_value(),
                        t4.get_value(),
                        np.sqrt(2)
                    )[2],
                        get_tangent_line(
                        t1.get_value(),
                        t2.get_value(),
                        t3.get_value(),
                        t4.get_value(),
                        np.sqrt(2)
                    )[3],
                )
            )
        tan_dot1.scale(0.1).set_color(RED)

        line1 = Line().set_color(DARK_BROWN).add_updater(lambda x:x.become(Line(q_copy,tan_dot1).set_color(DARK_BROWN)))
        line2 = Line().set_color(BLUE).add_updater(lambda x:x.become(Line(q_copy,tan_dot2).set_color(BLUE)))

        tan_dot2.add_updater(
            lambda x:x.become(
                Dot(
                    ax.c2p(
                        get_tangent_line(
                        t1.get_value(),
                        t2.get_value(),
                        t3.get_value(),
                        t4.get_value(),
                        np.sqrt(2)
                    )[0],
                        get_tangent_line(
                        t1.get_value(),
                        t2.get_value(),
                        t3.get_value(),
                        t4.get_value(),
                        np.sqrt(2)
                    )[1],
                    )
                ).scale(0.1).set_color(RED)
            )
        )

        tan_dot1.add_updater(
            lambda x:x.become(
                Dot(
                    ax.c2p(
                        get_tangent_line(
                        t1.get_value(),
                        t2.get_value(),
                        t3.get_value(),
                        t4.get_value(),
                        np.sqrt(2)
                    )[2],
                        get_tangent_line(
                        t1.get_value(),
                        t2.get_value(),
                        t3.get_value(),
                        t4.get_value(),
                        np.sqrt(2)
                    )[3],
                    )
                ).scale(0.1).set_color(RED)
            )
        )
#切点
        m = Dot().add_updater(lambda x:x.move_to(tan_dot1)).set_color(DARK_BROWN)
        note_m = Tex('M').scale(0.6).add_updater(lambda x:x.next_to(m,UP*0.2))
        n = Dot().add_updater(lambda x:x.move_to(tan_dot2)).set_color(BLUE)
        note_n = Tex('N').scale(0.6).add_updater(lambda x:x.next_to(n,DR*0.1))

#绘制连线
        line_oq = Line(o,q_copy)
        line_pq = Line(p,q_copy).set_color(blue)
        line_fq = Line(f,q_copy).set_color(YELLOW)
        line_ph = Line(p,h).set_color(blue)
        line_mn = Line(m,n).set_color([BLUE,DARK_BROWN])
        line_cm = Line(c,m).set_color(DARK_BROWN)
        line_cn = Line(c,n).set_color(BLUE)

        line_pf = DashedLine(p,f).set_color('#AC47D1')
        line_pe = DashedLine(p,e)
        line_cf = DashedLine(c,f)
        line_cq = DashedLine(c,q_copy)
        
#更新连线
        line_oq.add_updater(update_zes_line(o,q_copy))
        line_pq.add_updater(update_zes_line(p,q_copy))
        line_fq.add_updater(update_zes_line(f,q_copy))
        line_ph.add_updater(update_zes_line(p,h))
        line_mn.add_updater(update_zes_line(m,n))
        line_cm.add_updater(update_zes_line(c,m))
        line_cn.add_updater(update_zes_line(c,n))

        line_pf.add_updater(lambda x:x.become(DashedLine(p,f).set_color('#AC47D1')))
        line_pe.add_updater(lambda x:x.become(DashedLine(p,e)))
        line_cf.add_updater(lambda x:x.become(DashedLine(c,f)))
        line_cq.add_updater(lambda x:x.become(DashedLine(c,q_copy)))
    #直角
        rig_1 = RightAngle(y_1,line_ph,quadrant=(1.5,-1.5))
#用于绘制轨迹的点
        dot_1 =Dot().scale(0.1).move_to(q)

#q点轨迹
        trace = TracedPath(dot_1.get_start,stroke_color=[BLUE,DARK_BROWN,])
        
        
        
#文字部分
    #标题
        title = ZesTex(
            r'已知P是',
            r'抛物线$y^{2}=4x$',
            r'上的一点，',
            r'过点P作',
            r'直线$x=-2$',
            r'的垂线，垂足为$H$，',
            r'直线$l$',
            r'经过原点，',
            r'由$l$上的一点$Q$向',
            r'圆$C$:$\left (  x+  5\right ) ^{2} +\left ( y-3 \right ) ^{2} =2$',
            r'引两条切线，',
            r'分别切圆$C$于$M$、$N$两点，且',
            r'$\triangle MQN$为直角三角形',
            r'，则',
            r'$\left | PQ \right |$',
            r'$+$',
            r'$\left | PH \right | $',
            r'的最小值是?',
        ).to_corner(UP,buff=0.2)

        part_1 = ZesTex(
            '抛',
            '物',
            '线',
            r'$y^{2}=4x$',
        ).set_color(MAROON).set_sheen(0.35,DOWN)
        part_2 = ZesTex(
            r'直',
            '线',
            r'$x=-2$',
        ).set_color(GREEN).set_sheen(0.5,DOWN)
        part_3 = ZesTex(
            r'直',
            '线',
            r'$l$',
        ).set_color(YELLOW).set_sheen(0.5,DOWN)
        part_4 = ZesTex(
            r'圆',
            r'$C:$',
            r'$\left (  x+  5\right ) ^{2}$',
            r'$+\left ( y-3 \right ) ^{2}$',
            r'=',
            r'2',
        ).set_color_by_gradient(ORANGE,PINK)
        parts = VGroup(title[1].copy(),title[4].copy(),title[6].copy(),title[9].copy())

        parts_copy = VGroup(part_1,part_2,part_3,part_4)

        caption_1 = CaptionText("华罗庚先生曾说过，“数形结合百般好,隔离分家万事非。”")

        caption_2 = CaptionText('圆锥曲线更是离不开数形结合思想')

        caption_3 = CaptionText('因此我们不妨先从图像上进行分析',)
        
        captions = VGroup(caption_1,caption_2,caption_3)

        self.play(Write(title),rate_functions=linear,run_time=5)    

        text2 = Text("若有兴趣可暂停自行计算后跳转至视频末端查看答案",font='Source Han Sans SC',weight=BOLD,)
        text2.to_corner(DOWN,buff=1.2).scale(0.5)

        self.play(FadeIn(text2),run_time=1.5)
        self.wait(2)
        self.play(FadeOut(text2))

        for i in range(0,3):
            self.play(Write(captions[i]),run_time=1.5)
            self.wait(1.5)
            self.play(FadeOut(captions[i]))

        self.play(*map(Create,[ax,labels]),run_time=3)

        for i in range(0,4):
            parts_copy[i].to_edge(LEFT).to_corner(UP,buff=i+3)
            self.play(ReplacementTransform(parts[i],parts_copy[i]),run_time=1.5)

        self.play(Wiggle(parts_copy[0]),run_time=1.5)
        self.play(Create(f_xy),run_time=1.7)

        caption_4 = CaptionText('已知P是抛物线上一动点')

        self.play(Write(caption_4),Create(p),Write(note_p),run_time=1.5)

        self.play(MoveAlongPath(p,f_xy_0),rate_functions=linear,run_time=2.7)
        self.play(MoveAlongPath(p,f_xy_1),rate_functions=linear,run_time=2.7)
        
        self.play(FadeOut(caption_4))
        self.wait(1.5)
        caption_5 = CaptionText('过P作直线x=-2 的垂线，垂足为H ')

        self.play(ReplacementTransform(parts_copy[1].copy(),y_1))
        self.play(Write(caption_5),run_time=1.5)
        self.play(*map(Create,[line_ph,note_h,h,rig_1]))
        
        self.play(title[-2].animate.set_color(blue))
        self.play(FadeOut(caption_5))
        
        caption_6 = CaptionText('直线 l 为过原点的任意一条直线')
        self.play(Write(caption_6),run_time=1.5)
        self.play(GrowFromPoint(zes_graph,ax.c2p(0,0)))

        self.play(Rotate(zes_graph,PI/3,about_point=o.get_center()),run_time=2.7)
        self.play(Rotate(zes_graph,-PI/3,about_point=o.get_center()),run_time=2.7)

        def update_zes_graph(obj):
            obj.become(ax.plot(get_zes_graph,x_range=[-4,3]).set_color(YELLOW_B))
        zes_graph.add_updater(update_zes_graph)

        self.play(FadeOut(caption_6))
        caption_7 = CaptionText('圆C的图像如图所示')
        self.play(Write(caption_7),run_time=1.5)

        self.play(ReplacementTransform(parts_copy[3].copy(),cir))

        self.play(FadeOut(caption_7))
        self.play(*map(FadeIn,[c,note_c]))

        for i in range(0,4):
            self.play(LaggedStartMap(FadeOut,parts_copy[i],shift=LEFT,run_time=0.8))

        caption_8 = CaptionText('由抛物线的定义可知：')

        self.play(Write(caption_8),run_time=1.5)
        self.play(caption_8.animate.shift(UP*0.6))
        self.wait()
        caption_9 = CaptionText('抛物线上任一点到焦点与准线的距离相等')

        self.play(FadeIn(caption_9,shift=DOWN),run_time=1.5)
        self.play(Indicate(caption_9,color=[RED,BLUE]),run_time=3)
        self.wait()
        self.play(*map(FadeOut,[rig_1]))
        self.play(*map(FadeOut,[caption_8,caption_9]))

        solution_0 = ZesTex('如图：').to_edge(LEFT).to_corner(UP,buff=2.2)

        solution_0_1 = MathTex(
            r'\left | PE \right | =\left | PF \right | ',
            tex_to_color_map={r'\left | PF \right | ':'#AC47D1'}
        ).next_to(solution_0,DOWN,buff=0).scale(0.65).align_to(solution_0,LEFT)

        self.play(Create(y),run_time=1.5)
        self.play(*map(Create,[line_pe,line_pf]))
        
        self.play(Create(e),FadeIn(f))
        self.play(*map(FadeIn,[note_f,note_e]))
        self.play(MoveAlongPath(p,f_xy_0),run_time=5)

        self.play(*map(Write,[solution_0,solution_0_1]))

        solution_1_1 = MathTex(
            r'\therefore ',
            r'\left | PH \right | =',
            r'\left | PE \right | +1',
            tex_to_color_map={r'\left | PH \right | ':blue,},
        ).next_to(solution_0_1,DOWN,buff=0).scale(0.8).align_to(solution_0_1,LEFT)

        solution_1_2 = MathTex(
            r'\therefore ',
            r'\left | PH \right | =',
            r'\left | PF \right | +1',
            tex_to_color_map={
                r'\left | PH \right | ':blue,
                r'\left | PF \right | ':'#AC47D1'}
        ).next_to(solution_0_1,DOWN,buff=0).scale(0.8).align_to(solution_0_1,LEFT)

        self.play(FadeIn(solution_1_1,shift=DOWN))
        self.play(TransformMatchingTex(solution_1_1,solution_1_2))

        self.play(*map(FadeOut,[solution_0,solution_0_1]))
        self.play(solution_1_2.animate.to_edge(RIGHT).to_corner(UP,buff=2.2),run_time=1.8)

        caption_10 = CaptionText('Q为直线 l 上一点')
        self.play(Write(caption_10),run_time=1.5)

        self.play(Create(q_copy))
        self.play(Write(note_q_copy))

        caption_11 = CaptionText('过Q点作圆C的两条切线，切点分别为M、N')

        self.play(FadeOut(caption_10))
        self.play(Write(caption_11),run_time=1.5)
        
        self.play(
            t1.animate.set_value(ax.p2c(q_copy.get_center())[0]),
            t2.animate.set_value(ax.p2c(q_copy.get_center())[1]),
            t3.animate.set_value(ax.p2c(c.get_center())[0]),
            t4.animate.set_value(ax.p2c(c.get_center())[1])
        )

        self.play(*map(Create,[tan_dot1,line1,tan_dot2,line2]))
        
        self.play(*map(Create,[m,n]))
        
        self.play(*map(Write,[note_m,note_n]))
        self.play(FadeOut(caption_11))

        framebox1 = SurroundingRectangle(title[12], buff = .1).set_color([BLUE,RED])
        self.play(Create(framebox1))

        caption12 = CaptionText('移动点Q，使得三角形为直角三角形')

        self.play(Write(caption12))
        self.play(Create(line_mn))
        self.play(q_copy.animate.move_to(q),run_time=3,rate_function=linear)
        
        
        self.play(FadeOut(caption12))
        caption13 = CaptionText('此时四边形MCNQ为正方形')
        self.play(Write(caption13),run_time=1.5)

        self.play(*map(Create,[line_cm,line_cn]))
        self.play(FadeOut(line_mn))

        dot = Dot(ax.c2p(-7,2))

        self.play(self.camera.frame.animate.scale(0.6).move_to(dot),run_time=1.8)

        def update_curve(mob):
            mob.move_to(dot.get_center())

        self.camera.frame.add_updater(update_curve)

        self.remove(caption13)

        rig_2 = RightAngle(line_cm,line1,quadrant=(-0.5,-0.5)).set_color(DARK_BROWN)
        rig_3 = RightAngle(line_cn,line2,quadrant=(-0.5,-0.5)).set_color(BLUE)

        self.play(*map(Create,[rig_2,rig_3]))

        brace1 = Brace(line_cm, direction=line_cm.copy().rotate(PI / 2).get_unit_vector())
        b1text = brace1.get_tex("\sqrt{2} ").scale(0.4).next_to(brace1,LEFT*0.02)

        brace2 = Brace(line1, direction=line1.copy().rotate(-PI/2).get_unit_vector())
        b2text = brace2.get_tex("\sqrt{2} ").scale(0.4).next_to(brace2,UP*0.02)

        self.play(*map(Create,[brace1,brace2]))
        self.play(*map(Create,[b1text,b2text]))

        self.play(Create(line_cq))

        solution_2 = ZesTex(
            '易得',
            r'$\left | CQ \right | =2$'
        ).to_edge(LEFT).to_corner(UP,buff=2.2)
        self.play(GrowFromPoint(solution_2,point=ax.c2p(-5+np.sqrt(2)/2,3+np.sqrt(2)/2)),run_time=1.8)

        solution_3 = ZesTex(
            r'$\therefore$',
            r'Q在以C为圆心，\\以2为半径的圆上'
        ).next_to(solution_2,DOWN,buff=0).align_to(solution_2,LEFT)

        self.play(Write(solution_3,run_time=1.5),FadeOut(zes_graph))
        self.play(*map(Uncreate,[line_cm,line_cn,line1,line2,brace1,b1text,brace2,b2text,rig_2,rig_3,m,note_m,n,note_n]))
        
        self.add(trace)
        self.play(
            Rotate(dot_1,2*PI,about_point=c.get_center()),
            Rotate(q_copy,2*PI,about_point=c.get_center()),
            Rotate(c,2*PI,about_point=c.get_center()),
            run_time=7,
            rate_function=linear
        )
        self.add(circle)
        self.wait()
        self.camera.frame.remove_updater(update_curve)

        self.play(Restore(self.camera.frame),run_time=3,rate_function=linear)

        caption14 = CaptionText('连接PQ')

        self.play(Write(caption14),run_time=1.5)
        self.play(Create(line_pq))
        self.play(title[-4].animate.set_color(blue))

        self.play(*map(FadeOut,[solution_2,solution_3]))
        self.play(FadeOut(caption14))

        solution4 = MathTex(
            r'\because',
            r'\left | PH \right | =',
            r'\left | PF \right | +1',
            tex_to_color_map={
                r'\left | PH \right | ':blue,
                r'\left | PF \right | ':'#AC47D1'}
        ).to_edge(LEFT).to_corner(UP,buff=2.2).scale(0.8)

        self.play(TransformMatchingTex(solution_1_2,solution4))

        solution5 = MathTex(
            r'\therefore\left | PQ \right | +\left | PH \right | ',
            tex_to_color_map={
                r'\left | PH \right | ':blue,
                r'\left | PQ \right | ':blue}
        ).next_to(solution4,DOWN,buff=0).scale(0.8).align_to(solution4,LEFT)

        solution6 = MathTex(
            r'=\left | PQ \right | +',
            r'\left | PF \right |+1',    
        ).next_to(solution5,DOWN,buff=0).scale(0.8).align_to(solution5,LEFT)


        self.play(FadeIn(solution5,shift=DOWN),run_time=1.5)
        self.wait(0.8)
        self.play(FadeIn(solution6,shift=DOWN),run_time=1.5)

        solution7 = Tex(
            r'易得C、F、P、Q三点共线时，',
            tex_template=TexTemplateLibrary.ctex,
        ).next_to(solution6,DOWN,buff=2).scale(0.8).align_to(solution6,LEFT)
        solution8 = Tex(
            r'$\left | PQ \right | +$',
            r'$\left | PF \right |+1$',
            '最小',
            tex_template=TexTemplateLibrary.ctex,
        ).next_to(solution7,DOWN,buff=0).scale(0.8).align_to(solution7,LEFT)

        self.play(*map(FadeIn,[solution7,solution8]),run_time=2)
        
        self.play(Create(line_cf))
        self.play(
            Rotate(q_copy,-71*PI/180,about_point=c.get_center(),rate_function=linear,run_time=2.6),
            Rotate(c,-71*PI/180,about_point=c.get_center(),rate_function=linear,run_time=2.6)
        )
        self.play(MoveAlongPath(p,f_xy_2),rate_function=linear,run_time=2.8)
        self.play(Create(line_fq),run_time=2)
        self.play(
            f.animate.set_color(YELLOW),
            note_f.animate.set_color(YELLOW)
        )

        solution9 = Tex(
            r'即：',
            r'$\left ( \left |  PQ\right |+\left | PH \right |   \right ) _{min}$ ',
            tex_template=TexTemplateLibrary.ctex,
        ).next_to(solution8,DOWN,buff=0).scale(0.8).align_to(solution8,LEFT)

        solution10 = Tex(
            r'$=$',
            r'$\left | QF \right |$',
            r'$ +1=$',
            r'$\left | CF \right | -\left | CQ \right | $',
            r'+1'
            r'$=3\sqrt{5} -1$',
            tex_template=TexTemplateLibrary.ctex,
        ).next_to(solution9,DOWN,buff=0).scale(0.8).align_to(solution9,LEFT)
        solution10[1].set_color(YELLOW)
        solution10[3].set_color(YELLOW)
        self.play(*map(Write,[solution9,solution10]),run_time=2.5)
        self.wait(3)