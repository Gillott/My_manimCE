## 数学类视频
>### 1.[〔manim | 圆锥曲线〕利用抛物线定义解决一道动点问题](https://www.bilibili.com/video/BV1z3411K7cF/?spm_id_from=333.999.0.0&vd_source=5d2eb1cf9e3234b2a4b508f94b748174) 
>* #### 相关代码：[parabola_1.py](https://github.com/Gillott/My_manimCE/blob/main/My_vedios/math/parabola_1.py)，[func_math.py](https://github.com/Gillott/My_manimCE/blob/main/My_vedios/math/func_math.py)  
>### 2.[〔manim | 待定〕未命名]  
>* #### 相关代码：无  
## `func_math.py`
>**NOTE**
>- #### `func_math.py` 主要用于存放部分轮子的源码  
>- #### Example
>    * #### `ThreeSVG` 相关 SVG 文件：[good.svg](https://github.com/Gillott/My_manimCE/blob/main/My_vedios/math/good.svg)，[coin.svg](https://github.com/Gillott/My_manimCE/blob/main/My_vedios/math/coin.svg)，[favo.svg](https://github.com/Gillott/My_manimCE/blob/main/My_vedios/math/favo.svg)
>    * #### `ThreeSVG` 相关代码：
```py
 class ThreeSVG(VGroup):
    """一键三连"""
    def __init__(self,**kwargs):
        VGroup.__init__(self,**kwargs)
        svg1 = SVGMobject("D:\\SVG\\good.svg").set_opacity(1).set_color(GRAY)
        svg2 = SVGMobject("D:\\SVG\\coin.svg").set_opacity(1).set_color(GRAY)
        svg3 = SVGMobject("D:\\SVG\\favo.svg").set_opacity(1).set_color(GRAY)
        self.add(svg1,svg2,svg3)
```
