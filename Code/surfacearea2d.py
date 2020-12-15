
# Surface Area of 2D objects. 

from manimlib.imports import *

class Thumnbail(Scene):
    def construct(self):
        
        ThumnbailContent = TextMobject("Surface Area").move_to(UP*0.75)
        ThumnbailContentII = TextMobject("Of 2D")
        ThumnbailContentIII = TextMobject("Objects").move_to(DOWN*0.75)

        ThumnbailGroup = VGroup(ThumnbailContent, ThumnbailContentII, ThumnbailContentIII).scale(3).set_color(color=[BLUE_C, PURPLE_C])

        self.add(ThumnbailGroup)

class SquareArea(Scene):
    def construct(self):

        SquareWords = TextMobject("Surface area of a Square").set_color(color=[BLUE_C, PURPLE_C]).scale(2)

        self.play(Write(SquareWords))
        self.wait(2)

        self.play(FadeOut(SquareWords))

        SquareDiagram = Square(fill_opacity=0.5).set_color(color=YELLOW_B)

        self.play(ShowCreation(SquareDiagram), run_time=2)
        self.wait()

        self.play(SquareDiagram.move_to, UP) 

        ImagineSquare = TextMobject("Let's imagine this square is 5cm wide.").scale(1.25).set_color(color=[BLUE_C, PURPLE_C]).move_to(DOWN*2)

        self.play(Write(ImagineSquare))
        self.wait(2)
        
        self.play(FadeOutAndShiftDown(ImagineSquare))

        self.play(SquareDiagram.move_to, DOWN*0.25)

        FiveCMWide = TextMobject("5cm").scale(0.85).move_to(DOWN*2).set_color(color=[ORANGE, PINK])
        
        self.play(Write(FiveCMWide))
        self.wait()

        self.play(
            SquareDiagram.move_to, LEFT*3,
            FiveCMWide.move_to, LEFT*3+DOWN*1.5
        )

        self.wait()
