from manimlib.imports import *

class WelcomeScene(Scene):
    def construct(self):

        WelcomeText = TextMobject("Hello Everyone").set_color(color=[BLUE, RED])
        WelcomeText.scale(1.5)

        WelcomeText2 = TextMobject("Today we will be learning about Exponent Laws").set_color(color=[BLUE, RED])
        WelcomeText2.move_to(DOWN*0.5)
        WelcomeText2.scale(1)

        self.play(Write(WelcomeText))
        self.wait(1)

        self.play(WelcomeText.move_to, (UP*1))
        self.wait(0.5)

        self.play(Write(WelcomeText2))
        self.wait(1)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects])

        WhatAre = TextMobject("What are exponent laws?").set_color(color=[BLUE, RED])
        WhatAre.move_to(UP*2.5)
        WhatAre.scale(1.5)

        self.play(Write(WhatAre))
        self.wait(2)
        self.play(FadeOut(WhatAre))
        
        Laws = VGroup(
            TextMobject("Exponent Laws are a set of rules to help us with Powers").move_to(UP*3),
            TextMobject("Here are the Rules we will be covering today:").move_to(UP*2),
            TextMobject("- Product of Powers").move_to(UP*1),
            TextMobject("- Quotient of Powers"),
            TextMobject("- Power of a Power").move_to(DOWN*1),
            TextMobject("- Power with Exponent Zero").move_to(DOWN*2),
            TextMobject("These are not all the laws but").move_to(RIGHT*3),
            TextMobject("the ones we will be learning today.").move_to(DOWN*1+RIGHT*3))

        Laws.set_color(color=[BLUE, RED])
        Laws[2:].scale(0.75)

        self.play(Write(Laws[0:6], run_time=5))

        self.play(Laws[2:6].move_to, (LEFT*3+DOWN*0.5))
        self.wait(1)

        self.play(Write(Laws[6:]))
        self.wait(1)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects])

        self.wait(2)

class ProductPowers(MovingCameraScene):
    def construct(self):
       
        start = TextMobject("Product of Powers").set_color(color=[BLUE, RED])
        start.scale(1.5)

        self.play(Write(start))
        self.play(start.move_to, (UP*3))

        ProductExplain = VGroup(
            TextMobject("To multiply powers with the same base, add the exponents.").move_to(UP*1),
            TexMobject("a^m \\cdot a^n = a^{m+n}").move_to(DOWN*0.5),
            TextMobject("This is the formula for Product of Powers").move_to(DOWN*2))

        ProductExplain.set_color(color=[BLUE, RED])
        ProductExplain[1].set_color(color=[ORANGE, PINK])
        ProductExplain[1].scale(2)

        self.play(Write(ProductExplain[0]))
        self.wait()

        self.play(Write(ProductExplain[1:], run_time=3))
        self.wait()

        self.play(
            FadeOut(ProductExplain[0]),
            FadeOut(start),
            FadeOut(ProductExplain[2]))
        
        Must = TextMobject("All powers must have the same base for").move_to(UP*2)
        Must2 = TextMobject("these exponent laws.").move_to(UP*1)
    
        MustG = VGroup(Must, Must2).set_color(color=[BLUE, RED])
        
        self.play(Write(MustG))
        
        self.wait(2)
        
        self.play(FadeOut(MustG))

        Lexamples = TextMobject("Let's do some example questions:").move_to(UP*2)
        Lexamples.set_color(color=[BLUE, RED])
        Lexamples.scale(1.5)

        Product = VGroup(
            TexMobject("2^3 \\cdot 2^4 = 2^{3+4}").move_to(DOWN*1),
            TexMobject("2^3 \\cdot 2^4 = 2^{7}").move_to(DOWN*2))

        Product.set_color(color=[ORANGE, PINK])
        Product.scale(2)

        self.wait()

        self.play(Write(Lexamples))
        self.wait()

        self.play(FadeOut(Lexamples))
        self.wait()
        
        self.play(ProductExplain[1].move_to, (UP*1.5))
        self.wait()

        self.play(TransformFromCopy(ProductExplain[1], Product[0]))
        self.wait(2)

        self.play(TransformFromCopy(Product[0], Product[1]))
        self.wait(2)
        
        self.play(FadeOut(ProductExplain[1]))
        self.play(FadeOut(Product[0]))
 
        
        self.play(Product[1].move_to, (DOWN*1))
        
        ProductAYCS = TextMobject("As you can see, we added the exponents since").move_to(UP*2)
        ProductAYCS2 = TextMobject("we are multiplying.").move_to(UP*1)
        
        ProductGroup = VGroup(ProductAYCS, ProductAYCS2).set_color(color=[BLUE, RED])
        ProductGroup.scale(1.25)
        
        self.play(Write(ProductGroup))
        self.wait(2)
        
        self.play(
            *[FadeOut(mob)for mob in self.mobjects])
        
        ONEMEX = TextMobject("Here are a few more examples:").set_color(color=[BLUE, RED])
        ONEMEX.scale(1.5)
        
        PExamples = VGroup(
            TexMobject("7^9 \\cdot 7^1 = 7^{9+1}"),
            TexMobject("7^9 \\cdot 7^1 = 7^{10}").move_to(DOWN*1),
            TexMobject("7^{10}").move_to(DOWN * 2))
        
        PExamples.set_color(color=[ORANGE, PINK])
        PExamples.scale(2)
        
        self.play(Write(ONEMEX))
        self.wait(1)
        
        self.play(ONEMEX.move_to, (UP*2.5))
        self.wait(1)
        
        self.play(Write(PExamples[0]))
        self.wait(1)
        
        self.play(TransformFromCopy(PExamples[0], PExamples[1]))
        self.wait(2)
        
        self.play(TransformFromCopy(PExamples[1], PExamples[2]))
        self.wait(2)
        
        self.play(
            *[FadeOut(mob)for mob in self.mobjects])
        
class QuotientPowers(Scene):
    def construct(self):
        
        start = TextMobject("Quotient of Powers").set_color(color=[BLUE, RED])
        start.scale(1.5)

        self.play(Write(start))
        self.play(start.move_to, (UP*3))

        QuotientExplain = VGroup(
            TextMobject("To divide powers with the same base, subtract the exponents.").move_to(UP * 1),
            TexMobject("a^m \divisionsymbol a^n = a^{m-n}").move_to(DOWN*0.5),
            TextMobject("This is the formula for Quotient of Powers").move_to(DOWN*2))
        
        QuotientExplain.set_color(color=[BLUE, RED])
        QuotientExplain[1].set_color(color=[ORANGE, PINK])
        QuotientExplain[1].scale(2)
    
        self.play(Write(QuotientExplain[0]))
        self.wait()
    
        self.play(Write(QuotientExplain[1:], run_time=3))
        self.wait()
    
        self.play(
            FadeOut(QuotientExplain[0]),
            FadeOut(start),
            FadeOut(QuotientExplain[2]))
        
        EQuestions = TextMobject("Example Questions:").move_to(UP*2.5)
        EQuestions.scale(1.75)
        EQuestions.set_color(color=[BLUE, RED])

        self.wait()
        self.play(Write(EQuestions))

        ExampleQuestionsQuotient = VGroup(
            TexMobject("3^7 \divisionsymbol 3^4 = 3^{7-4}").move_to(DOWN*0.25),
            TexMobject("3^7 \divisionsymbol 3^4 = 3^{3}").move_to(DOWN*0.5),
            TexMobject("3^3").move_to(DOWN*75))

        ExampleQuestionsQuotient.set_color(color=[ORANGE, PINK])
        ExampleQuestionsQuotient.scale(1.75)

        self.play(QuotientExplain[1].move_to, UP*1)
        self.wait()

        self.play(TransformFromCopy(QuotientExplain[1], ExampleQuestionsQuotient[0]))
        self.wait()

        self.play(TransformFromCopy(ExampleQuestionsQuotient[0], ExampleQuestionsQuotient[1]))
        self.wait()