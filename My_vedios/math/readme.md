## 数学类视频
>### 1.[〔manim | 圆锥曲线〕利用抛物线定义解决一道动点问题](https://www.bilibili.com/video/BV1z3411K7cF/?spm_id_from=333.999.0.0&vd_source=5d2eb1cf9e3234b2a4b508f94b748174) 
>* #### 相关代码：[parabola_1.py](https://github.com/Gillott/My_manimCE/blob/main/My_vedios/math/parabola_1.py)，[func_math.py](https://github.com/Gillott/My_manimCE/blob/main/My_vedios/math/func_math.py)  
>### 2.[〔manim | 待定〕未命名]()
>* #### 相关代码：无  
## `func_math.py`
#### `func_math.py` 用于存放一些视频制作所需要使用的额外源码。
>**NOTE**  
>- #### 源码虽多，但并非全为本人原创_(:з」∠)_
>    #### 例如：
>    * #### 获取圆外一点与圆所成切点的相应坐标的函数 ```get_tangent_line``` 取自 UP 主 [josepa ](https://space.bilibili.com/99579008) 的专栏：
>        * #### https://b23.tv/2mY0kDx
>    * #### 另一些优秀的轮子大多取自 MK 官方文档或者 GitHub：
>        * #### https://docs.manim.org.cn
>        * #### https://github.com/manim-kindergarten/manim_sandbox
>- #### 部分自定义类需要导入第三方文件才能使用
>    #### Example
>    * #### `ThreeSVG` 相关 SVG 文件：[good.svg](https://github.com/Gillott/My_manimCE/blob/main/My_vedios/math/source/good.svg)，[coin.svg](https://github.com/Gillott/My_manimCE/blob/main/My_vedios/math/source/coin.svg)，[favo.svg](https://github.com/Gillott/My_manimCE/blob/main/My_vedios/math/source/favo.svg)
>    * #### `ThreeSVG` 相关源码及使用示例：
```py
 class ThreeSVG(VGroup):
    """一键三连"""
    def __init__(self,**kwargs):
        VGroup.__init__(self,**kwargs)
        svg1 = SVGMobject("D:\\SVG\\good.svg").set_opacity(1).set_color(RED)
        svg2 = SVGMobject("D:\\SVG\\coin.svg").set_opacity(1).set_color(ORANGE)
        svg3 = SVGMobject("D:\\SVG\\favo.svg").set_opacity(1).set_color(PINK)
        VGroup(svg1,svg2,svg3).arrange_submobjects(buff=1.3)
        self.add(svg1,svg2,svg3)
```
```py
from manim import *
class ThreeSVG_Example(Scene):
    def construct(self):
        vmob = ThreeSVG()
        self.add(vmob)
```
![ThreeSVG_Example](https://github.com/Gillott/My_manimCE/blob/main/My_vedios/math/source/ThreeSVG_Example_ManimCE_v0.16.0.post0.png)
## 一键三连，请。∠( ᐛ 」∠)
