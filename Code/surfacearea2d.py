
# Surface Area of 2D objects. 

from manimlib.imports import *

class Thumnbail(Scene):
    def construct(self):
        
        ThumnbailContent = TextMobject("Surface Area").move_to(UP*0.75)
        ThumnbailContentII = TextMobject("Of 2D")
        ThumnbailContentIII = TextMobject("Objects").move_to(DOWN*0.75)

        ThumnbailGroup = VGroup(ThumnbailContent, ThumnbailContentII, ThumnbailContentIII).scale(3).set_color(color=[RED_C, GREEN_C])

        self.add(ThumnbailGroup)

class SquareArea(Scene):
    def construct(self):

        SquareWords = TextMobject("Surface area of a Square").set_color(color=[RED_C, GREEN_C]).scale(2)

        self.play(Write(SquareWords))
        self.wait(2)

        self.play(FadeOut(SquareWords))

        SquareDiagram = Square(fill_opacity=0.5).set_color(color=YELLOW_B)

        self.play(ShowCreation(SquareDiagram), run_time=2)
        self.wait()

        self.play(SquareDiagram.move_to, UP)

        ImagineSquare = TextMobject("Let's imagine this square is 5 feet wide.").scale(1.25).set_color(color=[RED_C, GREEN_C])

        