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

        self.play(*[FadeOut(mob)for mob in self.mobjects])

        WhatAre = TextMobject("What are exponent laws?").set_color(color=[BLUE, RED])
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

        self.play(Write(Laws[0:6], run_time=6))

        self.play(Laws[2:6].move_to, (LEFT*3+DOWN*0.5))
        self.wait(1)

        self.play(Write(Laws[6:]))
        self.wait(1)

        self.play(*[FadeOut(mob)for mob in self.mobjects])

        self.wait(2)

class ProductPowers(MovingCameraScene):
    def construct(self):
       
        start = TextMobject("Product of Powers").set_color(color=[BLUE, RED])
        start.scale(1.5)- 37

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
        
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        
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
        
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        self.wait()

        PExamples2 = VGroup(
           TexMobject("5^3 \\cdot 5^1 = 5^{3+1}").move_to(UP*1),
           TexMobject("5^3 \\cdot 5^1 = 5^{4}"),
           TexMobject("5^{4}").move_to(DOWN*1))
        
        PExamples2.set_color(color=[ORANGE, PINK])
        PExamples2.scale(2)

        self.play(Write(PExamples2[0]))
        self.wait(1)
        
        self.play(TransformFromCopy(PExamples2[0], PExamples2[1]))
        self.wait(2)
        
        self.play(TransformFromCopy(PExamples2[1], PExamples2[2]))
        self.wait(2)
        
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        
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
        
        EQuestions = TextMobject("Example Questions:").move_to(UP*2.75)
        EQuestions.scale(1.75)
        EQuestions.set_color(color=[BLUE, RED])

        self.wait()
        self.play(Write(EQuestions))

        ExampleQuestionsQuotient = VGroup(
            TexMobject("3^7 \divisionsymbol 3^4 = 3^{7-4}").move_to(DOWN*1),
            TexMobject("3^7 \divisionsymbol 3^4 = 3^{3}").move_to(DOWN*1.75),
            TexMobject("3^3").move_to(DOWN*2.5))
        
        ExampleQuestionsQuotient.set_color(color=[ORANGE, PINK])
        ExampleQuestionsQuotient.scale(1.75)

        self.play(QuotientExplain[1].move_to, UP*1)
        self.wait(2)

        self.play(TransformFromCopy(QuotientExplain[1], ExampleQuestionsQuotient[0]))
        self.wait(2)

        self.play(TransformFromCopy(ExampleQuestionsQuotient[0], ExampleQuestionsQuotient[1]))
        self.wait(2)

        self.play(TransformFromCopy(ExampleQuestionsQuotient[1], ExampleQuestionsQuotient[2]))
        self.wait(2)

        self.play(*[FadeOut(mob)for mob in self.mobjects])

        self.wait()

        ExampleQuestionsQuotient2 = VGroup(
            TexMobject("8^3 \divisionsymbol 8^6 = 8^{3-6}").move_to(UP*1),
            TexMobject("8^3 \divisionsymbol 8^6 = 8^{-3}"),
            TexMobject("8^{-3}").move_to(DOWN*1))

        ExampleQuestionsQuotient2.set_color(color=[ORANGE, PINK])
        ExampleQuestionsQuotient2.scale(2)


        self.play(Write(ExampleQuestionsQuotient2[0]))
        self.wait(2)

        self.play(TransformFromCopy(ExampleQuestionsQuotient2[0], ExampleQuestionsQuotient2[1]))
        self.wait(2)

        self.play(TransformFromCopy(ExampleQuestionsQuotient2[1], ExampleQuestionsQuotient2[2]))
        self.wait(2)

        self.play(*[FadeOut(mob)for mob in self.mobjects])

        self.wait()

        ExampleQuestionsQuotient3 = VGroup(
            TexMobject("19^9 \divisionsymbol 19^4 = 19^{9-4}").move_to(UP*1),
            TexMobject("19^9 \divisionsymbol 19^4 = 19^{5}"),
            TexMobject("19^{5}").move_to(DOWN*1))

        ExampleQuestionsQuotient3.set_color(color=[ORANGE, PINK])
        ExampleQuestionsQuotient3.scale(2)


        self.play(Write(ExampleQuestionsQuotient3[0]))
        self.wait(2)

        self.play(TransformFromCopy(ExampleQuestionsQuotient3[0], ExampleQuestionsQuotient3[1]))
        self.wait(2)

        self.play(TransformFromCopy(ExampleQuestionsQuotient3[1], ExampleQuestionsQuotient3[2]))
        self.wait(2)

        self.play(*[FadeOut(mob)for mob in self.mobjects])

        self.wait()

class EvaluateExpressions(MovingCameraScene):
    def construct(self):


        EvaluateExpressions = TextMobject("Let's evaluate some expressions using the Product and").move_to(UP*0.5)
        EvaluateExpressions2 = TextMobject("Quotient exponent laws that we learned.").move_to(DOWN*0.5)

        PExpressions = VGroup(EvaluateExpressions, EvaluateExpressions2).set_color(color=[BLUE, RED])


        self.play(Write(PExpressions), run_time=3)
        self.wait(2)

        self.play(FadeOut(PExpressions))
        self.wait()

        ExpressionI = VGroup(
            TexMobject("3^2 \\cdot 3^4 \divisionsymbol\small 3^3").move_to(UP*2),
            TexMobject("= 3^{2+4} \divisionsymbol\small 3^3").move_to(UP*1),
            TexMobject("= 3^6 \divisionsymbol\small 3^3"),
            TexMobject("= 3^{6-3}").move_to(DOWN*1),
            TexMobject("= 3^3").move_to(DOWN*2),
            TexMobject("= 27").move_to(DOWN*3)).set_color(color=[ORANGE, PINK]).scale(2)

        for i in range(5):
            self.play(Write(ExpressionI[i]))
            self.play(self.camera_frame.move_to, ExpressionI[i], self.camera_frame.set_width, 
            ExpressionI[i].get_width()*1.75)
            self.wait(1)

        self.play(*[FadeOut(mob)for mob in self.mobjects])

        self.wait()

        ExpressionII = VGroup(
            TexMobject("6^6 \divisionsymbol 6^5 \cdot 6^2").move_to(UP*2),
            TexMobject("= 6^{6-5} \cdot 6^2").move_to(UP*1),
            TexMobject("= 6^1 \cdot 6^2"),
            TexMobject("= 6^{1+2}").move_to(DOWN*1),
            TexMobject("= 6^3").move_to(DOWN*2),
            TexMobject("= 216").move_to(DOWN*3)).set_color(color=[ORANGE, PINK]).scale(2)

        for i in range(5):
            self.play(Write(ExpressionII[i]))
            self.play(self.camera_frame.move_to, ExpressionII[i], self.camera_frame.set_width, 
            ExpressionII[i].get_width()*1.75)
            self.wait(1)

        self.play(*[FadeOut(mob)for mob in self.mobjects])

class PowerOfPower(MovingCameraScene):
    def construct(self):

        PowerOfPowerText = TextMobject("Power of Power").set_color(color=[BLUE, RED])
        PowerOfPowerText.scale(2)


        self.play(Write(PowerOfPowerText))
        self.wait()

        self.play(PowerOfPowerText.move_to, UP*3)
        self.wait()

        PowerOfPowerExplain = VGroup(
            TextMobject("We can raise a power to a power.").move_to(UP*0.5),
            TextMobject("For example, $3^2$ raised to the power 4").move_to(DOWN*0.5),
            TextMobject("is written as $(3^2)^4$").move_to(DOWN*1.5),
            TextMobject("$(3^2)^4$ is a power of a power.").move_to(DOWN*2.5))

        PowerOfPowerExplain.set_color(color=[BLUE, RED])
        self.play(Write(PowerOfPowerExplain), run_time=6)
        self.wait(2)

        self.play(*[FadeOut(mob)for mob in self.mobjects])
        self.wait()

        PowerOfPowerExplainII = VGroup(
            TextMobject("To raise a power to a power, multiply the exponents.").move_to(UP*1),
            TexMobject("(a^m)^n = a^{m\\cdot n}").move_to(DOWN*0.5),
            TextMobject("This is the formula for Power of a Power").move_to(DOWN*2))

        PowerOfPowerExplainII.set_color(color=[BLUE, RED])
        PowerOfPowerExplainII[1].scale(2)
        PowerOfPowerExplainII[1].set_color(color=[ORANGE, PINK])

        self.play(Write(PowerOfPowerExplainII), run_time=5)

        self.play(*[FadeOut(mob)for mob in self.mobjects])

        LExamplesPower = TextMobject("Let's do some example questions:").set_color(color=[BLUE, RED])
        LExamplesPower.scale(1.5)
        self.play(Write(LExamplesPower))
        self.wait()
        
        self.play(FadeOut(LExamplesPower))
        self.wait()

        ExampleQuestionsPowerOfPower = VGroup(
            TexMobject("(4^2)^3").move_to(UP*1),
            TexMobject("= 3^{2 \\cdot 3}"),
            TexMobject("= 3^6").move_to(DOWN*1)).set_color(color=[ORANGE, PINK]).scale(1.5)

        for i in range(3):
            self.play(Write(ExampleQuestionsPowerOfPower[i]))
            self.play(self.camera_frame.move_to, ExampleQuestionsPowerOfPower[i], self.camera_frame.set_width, 
            ExampleQuestionsPowerOfPower[i].get_width()*2)
            self.wait(1)

        self.play(*[FadeOut(mob)for mob in self.mobjects])

        self.wait()

        ExampleQuestionsPowerOfPowerII = VGroup(
            TexMobject("(6^7)^2").move_to(UP*1),
            TexMobject("= 6^{7 \\cdot 2}"),
            TexMobject("= 6^{14}").move_to(DOWN*1)).set_color(color=[ORANGE, PINK]).scale(1.5)

        for i in range(3):
            self.play(Write(ExampleQuestionsPowerOfPowerII[i]))
            self.play(self.camera_frame.move_to, ExampleQuestionsPowerOfPowerII[i], self.camera_frame.set_width, 
            ExampleQuestionsPowerOfPowerII[i].get_width()*2)
            self.wait(1)

        self.play(*[FadeOut(mob)for mob in self.mobjects])

        self.wait()

class PowersWithExponentZero(MovingCameraScene):
    def construct(self):

        startingWords = TextMobject("Powers with an Exponent").move_to(UP*0.5)
        startingWordsII = TextMobject("of Zero.").move_to(DOWN*0.5)

        SWords = VGroup(startingWords, startingWordsII).scale(2).set_color(color=[BLUE, RED])

        self.play(Write(SWords))
        self.wait()

        self.play(*[FadeOut(mob)for mob in self.mobjects])