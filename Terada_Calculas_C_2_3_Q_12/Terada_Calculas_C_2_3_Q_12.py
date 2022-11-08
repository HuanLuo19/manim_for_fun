from manimlib import *

class CauchyMeanQuestion(Scene):

    def construct(self):
        # show title
        title = Text(
            """
            《寺田微积分》 2.3章 例题12
            ——柯西中值定理的扩张
            
            """,
            font_size=40,
            t2c={"《寺田微积分》": YELLOW}
        )

        self.wait(2)
        self.play(Write(title))
        self.wait(2)
        self.play(title.animate.scale(0.8).to_corner(UL))
        
        # show questions
        questiontitle = TexText(
            '函数$f(x),g(x),h(x)$在区间$[a,b]$内可微',
            font_size=35
        )
        question1 = TexText(
            '（1）证明：在区间$[a,b]$内至少存在一个常数$c$满足下列等式',
            font_size=35
        )
        equ_matrix_cd = Tex("\\begin{vmatrix} f(a) & g(a) & h(a) \\\\ f(b) & g(b) & h(b) \\\\ f'(c) & g'(c) & h'(c) \\end{vmatrix}", "=", "0"
        ).scale(0.8)
        question2 = TexText(
            "（2）利用（1）的结论推导柯西中值定理：（$g'(c) \\ne 0$）",
            font_size=35
        )
        cauchy = Tex("""
            \\frac{f(b)-f(a)}{g(b)-g(a)} = \\frac{f'(c)}{g'(c)}
            """
        ).scale(0.8)
        q_title_lines = VGroup(questiontitle, question1, equ_matrix_cd, question2, cauchy).arrange(DOWN, aligned_edge=LEFT).shift(0.4 * DOWN)
        equ_matrix_cd.shift(2.8 * RIGHT)
        cauchy.shift(3 * RIGHT)

        self.play(Write(q_title_lines[0]))
        self.wait(2)
        self.play(Write(q_title_lines[1]))
        self.play(FadeIn(q_title_lines[2], UP))
        self.wait(2)
        self.play(Write(q_title_lines[3]))
        self.play(FadeIn(q_title_lines[4], UP))
        self.wait()

        #5-second countdown
        counttime = 5
        while counttime > 0:
            counttext = Text(str(counttime)).to_corner(DR).scale(2)
            self.play(Write(counttext, run_time=1))
            counttime -= 1
            self.remove(counttext)
        self.wait()

        # show solution to (1)
        self.play(FadeOut(title), FadeOut(questiontitle), FadeOut(question1), FadeOut(question2), FadeOut(cauchy))
        markq11 = Text('（1）思路：').to_corner(UL)
        self.play(FadeIn(markq11), run_time=1)
        self.play(equ_matrix_cd.animate.move_to(4 * LEFT).scale(1.125))

        
        col1_matrix_cd = VGroup(equ_matrix_cd[0][6:10], equ_matrix_cd[0][18:22], equ_matrix_cd[0][30:35])
        ideas = Tex(
            "f(a)", "f(b)", "f'(c)", "\\times\\times = 0", "\\text{中值定理？}"
        )
        ideas.arrange(DOWN, buff=0.5)
        ideas_brace = Brace(ideas, direction=RIGHT)
        idea_group = VGroup(ideas, ideas_brace)
        self.play(ShowCreationThenDestructionAround(col1_matrix_cd))
        self.play(ShowCreationThenDestructionAround(equ_matrix_cd[1]+equ_matrix_cd[2]))
        self.play(Write(idea_group[0]), run_time=1.5)
        self.wait()
        self.play(Write(idea_group[1]))

        # Rolle's theorem
        rolle_rect = Rectangle(height=5, width=4).shift(4.5 * RIGHT).set_stroke(TEAL)
        rolle_title = Text("罗尔中值定理", color = TEAL)
        rolle_tex = TexText(
            """
            对于区间$(a,b)$上连续， \n
            $[a,b]$上可微的函数$f(x)$， \n
            若有：
            """,
            """
            $f(a) = f(b)$ \n
            """,
            """
            则在区间$[a,b]$内至少 \n
            存在一个常数$c$满足：
            """,
            """
            $f'(c) = 0$
            """
        )
        rolle_text_group = VGroup(rolle_title, rolle_tex).arrange(DOWN, buff=0.9).move_to(rolle_rect).scale(0.7)
        self.play(ShowCreation(rolle_rect))
        self.play(Write(rolle_text_group, run_time=2.5))
        self.wait()
        self.play(rolle_tex[1].animate.set_color(BLUE), ideas[0].animate.set_color(BLUE), ideas[1].animate.set_color(BLUE))
        self.wait()
        self.play(rolle_tex[3].animate.set_color(YELLOW), ideas[2].animate.set_color(YELLOW), ideas[3].animate.set_color(YELLOW))
        self.wait()
        self.play(rolle_tex.animate.set_color(WHITE), ideas.animate.set_color(WHITE))
        self.wait()

        # create F'(x)
        equ_fcd = Tex("F'(c)", "=", "0").next_to(equ_matrix_cd, DOWN, aligned_edge=ORIGIN)
        equ_fcd[0].set_color(YELLOW)
        create_func_text = Text("构造函数").scale(0.8).set_color(YELLOW).next_to(equ_fcd[0], UP).shift(0.2 * UP)
        self.play(Indicate(equ_matrix_cd), Indicate(rolle_tex[3]), run_time=2)
        self.play(equ_matrix_cd[0][30:45].animate.set_color(YELLOW))
        self.play(
            equ_matrix_cd.animate.shift(1 * UP),
            FadeIn(create_func_text, DOWN),
            TransformMatchingShapes(equ_matrix_cd[0].copy(), equ_fcd[0]
            )
        )
        self.play(FadeIn(equ_fcd[1]+equ_fcd[2]))
        self.play(FadeOut(idea_group+rolle_text_group+rolle_rect+create_func_text))
        self.play(VGroup(equ_matrix_cd, equ_fcd).animate.move_to(3 * LEFT))
# 
        matrix_Fxd = Tex(
            """
            \\begin{vmatrix}
            f(a) & g(a) & h(a) \\\\
            f(b) & g(b) & h(b) \\\\
            f'(x) & g'(x) & h'(x) \\\\
            \\end{vmatrix}
            """
        )
        matrix_Fxd.scale(0.9).arrange(RIGHT).next_to(equ_matrix_cd, RIGHT, aligned_edge=UP).shift(1.5 * RIGHT)
        matrix_Fxd[0][30:45].set_color(YELLOW)
        Fxd = Tex("F'(", "x", ")").next_to(matrix_Fxd, DOWN, aligned_edge=ORIGIN).align_to(equ_fcd, UP).set_color(YELLOW)
        VGroup(matrix_Fxd, Fxd).animate.move_to(3 * RIGHT)
        rarrow = Tex("\\rightarrow").move_to(ORIGIN).set_color(YELLOW)
        self.play(FadeIn(rarrow, RIGHT))
        self.play(FadeIn(matrix_Fxd[0][0:30]+matrix_Fxd[0][45::]))
        self.play(TransformMatchingShapes(equ_matrix_cd[0][30:45].copy(), matrix_Fxd[0][30:45]), TransformMatchingShapes(equ_fcd[0].copy(), Fxd))
        self.play(FadeOut(rarrow, RIGHT))
        self.wait(2)
        self.play(FadeOut(equ_matrix_cd+equ_fcd))
        eq_mk0 = Tex("=").move_to(2 * LEFT+2.8 * UP)
        self.play(matrix_Fxd.animate.set_color(WHITE), Fxd.animate.set_color(WHITE))
        self.play(
            Fxd.animate.next_to(eq_mk0, LEFT),
            matrix_Fxd.animate.next_to(eq_mk0, RIGHT),
            FadeIn(eq_mk0)
        )
        
        # lead to F(x)
        darrow_bbigg = Tex("\\Bigg\\downarrow")
        int_mark_1 = Tex("\\int").scale(0.5)
        int_darrow_group1 = VGroup(darrow_bbigg, int_mark_1).arrange(RIGHT).next_to(Fxd, DOWN)
        Fx = Tex("F(x)").next_to(int_darrow_group1, DOWN)
        self.play(FadeIn(int_darrow_group1, DOWN))
        self.play(TransformMatchingShapes(Fxd.copy(), Fx))
        darrow_big = Tex("\\big\\downarrow")
        int_mark_2 = Tex("\\int").scale(0.5)
        int_darrow_group2 = VGroup(darrow_big, int_mark_2).arrange(RIGHT).next_to(matrix_Fxd, DOWN)
        q_mk = Tex("?").scale(1.4).align_to(int_darrow_group2, LEFT).align_to(Fx, DOWN)
        self.play(FadeIn(int_darrow_group2, DOWN))
        self.play(TransformMatchingShapes(matrix_Fxd.copy(), q_mk))
        self.wait(2)
        self.play(
            FadeOut(int_darrow_group1+int_darrow_group2),
            Fx.animate.set_opacity(0.5).move_to(5 * LEFT+2.2 * UP),
            q_mk.animate.set_color(RED).move_to(4.1 * LEFT+2.2 * UP)
        )
        self.wait()

        # solve F(x)
        eq_mk1 = Tex("=").shift(1 * UP).align_to(Fxd, LEFT)
        solve_fxd_text1 = TexText("$\\Big|$全部拆开？$\\Big|$")
        solve_fxd_text1.next_to(eq_mk1, RIGHT)
        solve_fxd_text2 = TexText("对三阶以上行列式的计算失去普适性", "，打咩!")
        solve_fxd_text2[1].set_color(RED)
        self.play(TransformMatchingShapes(eq_mk0.copy(), eq_mk1))
        self.play(TransformMatchingShapes(matrix_Fxd.copy(), solve_fxd_text1))
        self.wait(2)
        self.play(Write(solve_fxd_text2[0]))
        self.wait()
        self.play(Write(solve_fxd_text2[1]), solve_fxd_text1.animate.set_color(RED))
        self.wait()
        self.play(Uncreate(solve_fxd_text1+solve_fxd_text2))
        self.wait()

        # cofactor
        cof_text = TexText(
            """
            注意到导数项都在同一列 \n
            """,
            "$\\rightarrow$","代数余子式"
        )
        (cof_text[1]+cof_text[2]).shift(1 * LEFT).set_color(YELLOW)
        cof_text.scale(0.5).next_to(matrix_Fxd, RIGHT, aligned_edge=DOWN)
        self.play(matrix_Fxd[0][30:45].animate.set_color(YELLOW), ShowCreationThenFadeAround(matrix_Fxd[0][30:45]))
        self.play(Write(cof_text[0]))
        self.wait()
        self.play(Write(cof_text[1]+cof_text[2]))
        fxd_mat = Tex("f'(x)").set_color(YELLOW)
        gxd_mat = Tex("g'(x)").set_color(YELLOW)
        hxd_mat = Tex("h'(x)").set_color(YELLOW)
        co_f = Tex("\\begin{vmatrix} g(a) & h(a) \\\\ g(b) & h(b) \\end{vmatrix}")
        co_g = Tex("(-1)\\begin{vmatrix} f(a) & h(a) \\\\ f(b) & h(b) \\end{vmatrix}")
        co_h = Tex("\\begin{vmatrix} f(a) & g(a) \\\\ f(b) & g(b) \\end{vmatrix}")
        co_equ_mat = VGroup(fxd_mat, co_f, Tex("+"), gxd_mat, co_g, Tex("+"),hxd_mat ,co_h).arrange(RIGHT).next_to(eq_mk1)
        self.play(eq_mk1.animate.shift(2 * LEFT))
        co_equ_mat.scale(0.7).next_to(eq_mk1)
        # show cofactor of f'(x)
        self.play(ShowCreationThenFadeAround(matrix_Fxd[0][30:35]))
        self.play(TransformMatchingShapes(matrix_Fxd[0][30:35].copy(), fxd_mat))
        self.play(ShowCreationThenFadeAround(matrix_Fxd[0][10:18]+matrix_Fxd[0][22:30]))
        self.play(TransformMatchingShapes((matrix_Fxd[0][10:18]+matrix_Fxd[0][22:30]).copy(), co_f))
        self.play(Write(co_equ_mat[2]))
        # show cofactor of g'(x)
        self.play(ShowCreationThenFadeAround(matrix_Fxd[0][35:40]))
        self.play(TransformMatchingShapes(matrix_Fxd[0][35:40].copy(), gxd_mat))
        self.play(ShowCreationThenFadeAround(matrix_Fxd[0][6:10]+matrix_Fxd[0][18:22]), ShowCreationThenFadeAround(matrix_Fxd[0][14:18]+matrix_Fxd[0][26:30]))
        self.play(TransformMatchingShapes((matrix_Fxd[0][6:10]+matrix_Fxd[0][18:22]+matrix_Fxd[0][14:18]+matrix_Fxd[0][26:30]).copy(), co_g))
        self.play(Write(co_equ_mat[5]))
        # show cofactor of h'(x)
        self.play(ShowCreationThenFadeAround(matrix_Fxd[0][40:45]))
        self.play(TransformMatchingShapes(matrix_Fxd[0][40:45].copy(), hxd_mat))
        self.play(ShowCreationThenFadeAround(matrix_Fxd[0][6:14]+matrix_Fxd[0][18:26]))
        self.play(TransformMatchingShapes((matrix_Fxd[0][6:14]+matrix_Fxd[0][18:26]).copy(), co_h))
        self.wait(2)

        brace_text_co_f = BraceText(co_f, "代数余子式：常数", brace_direction=BOTTOM).scale(0.7).shift(0.2 * UP)
        brace_text_co_g = BraceText(co_g, "常数", brace_direction=BOTTOM).scale(0.7).shift(0.2 * UP)
        brace_text_co_h = BraceText(co_h, "常数", brace_direction=BOTTOM).scale(0.7).shift(0.2 * UP)
        const_A = Tex("A")
        const_B = Tex("B")
        const_C = Tex("C")
        fxd_const = Tex("f'(x)").set_color(YELLOW)
        gxd_const = Tex("g'(x)").set_color(YELLOW)
        hxd_const = Tex("h'(x)").set_color(YELLOW)
        eq_mk2 = Tex("=").shift(1 * DOWN).align_to(eq_mk1, LEFT)
        co_equ_const = VGroup(const_A, fxd_const, Tex("+"), const_B, gxd_const, Tex("+"), const_C, hxd_const).arrange(RIGHT)
        co_equ_const.scale(0.7).next_to(eq_mk2)
        self.play(ShowCreation(brace_text_co_f), ShowCreation(brace_text_co_g), ShowCreation(brace_text_co_h))
        self.wait()
        self.play(Write(eq_mk2))
        self.play(TransformMatchingShapes(co_f.copy(), const_A))
        self.play(TransformMatchingShapes(fxd_mat.copy(), fxd_const))
        self.play(Write(co_equ_const[2]), TransformMatchingShapes(co_g.copy(), const_B))
        self.play(TransformMatchingShapes(gxd_mat.copy(), gxd_const))
        self.play(Write(co_equ_const[5]), TransformMatchingShapes(co_h.copy(), const_C))
        self.play(TransformMatchingShapes(hxd_mat.copy(), hxd_const))
        self.wait()
        able_to_int_text = Text("（可以积分了！）", t2c={"积分": GREEN}).scale(0.5).next_to(hxd_const, RIGHT)
        self.play(Write(able_to_int_text))
        self.wait()
        self.play(Uncreate(able_to_int_text))
        self.wait()
        
        # int F'(x) to F(x)
        kw = {"run_time": 2}
        to_isolate = ["\\rightarrow", "F(x)", "=", "\\int", "dx", "A", "B", "C"]
        eq_Fx1 = Tex("\\rightarrow F(x) = \\int F'(x)dx ", isolate=[*to_isolate]).scale(0.8).align_to(eq_mk2, LEFT)
        eq_Fx2 = Tex("\\rightarrow F(x) = \\int Af'(x) + Bg'(x) + Ch'(x) dx", isolate=[*to_isolate]).scale(0.8).align_to(eq_mk2, LEFT)
        eq_Fx3 = Tex("\\rightarrow F(x) = A\\int f'(x)dx + B\\int g'(x)dx + C\\int h'(x) dx", isolate=["f'(x)", "g'(x)", "h'(x)", *to_isolate]).scale(0.8).align_to(eq_mk2, LEFT)
        eq_Fx4 = Tex("\\rightarrow F(x) = Af(x) + Bg(x) + Ch(x)", isolate=["f(x)", "g(x)", "h(x)",*to_isolate]).scale(0.8).align_to(eq_mk2, LEFT)
        eq_Fx1234 = VGroup(eq_Fx1, eq_Fx2, eq_Fx3, eq_Fx4)
        eq_Fx1234.shift(2.2 * DOWN)
        for line in eq_Fx1234:
            line.set_color_by_tex_to_color_map({
                "\\rightarrow": GREEN,
                "f'(x)": YELLOW,
                "g'(x)": YELLOW,
                "h'(x)": YELLOW,
                "f(x)" : GREEN,
                "g(x)" : GREEN,
                "h(x)" : GREEN,
            })
        self.play(Write(eq_Fx1), **kw)
        self.wait(2)
        self.play(TransformMatchingTex(eq_Fx1, eq_Fx2, key_map={"F'(x)": "Af'(x) + Bg'(x) + Ch'(x)"}, **kw))
        self.wait()
        self.play(TransformMatchingTex(eq_Fx2, eq_Fx3, **kw))
        self.wait()
        self.play(TransformMatchingTex(eq_Fx3, eq_Fx4, key_map={"\\int f'(x)dx": "f(x)", "g'(x)": "g(x)", "h'(x)": "h(x)"}, **kw))
        self.wait()
        matrix_Fx = Tex(
            """
            \\begin{vmatrix}
            f(a) & g(a) & h(a) \\\\
            f(b) & g(b) & h(b) \\\\
            f(x) & g(x) & h(x) \\\\
            \\end{vmatrix}
            """
        )
        matrix_Fx.scale(0.9)
        matrix_Fx[0][30:42].set_color(GREEN)
        eq_mk3 = Tex("=").next_to(eq_Fx4, RIGHT)
        matrix_Fx.next_to(eq_mk3, RIGHT)
        cof_too_text = Text("（同样是代数余子式形式）", t2c={"代数余子式": GREEN}).scale(0.5).next_to(eq_Fx4, RIGHT)
        self.play(Write(cof_too_text))
        self.play(ShowCreationThenDestructionAround(eq_Fx4[3::]))
        self.play(ShowCreationThenDestructionAround(co_equ_const))
        self.play(ShowCreationThenDestructionAround(matrix_Fxd))
        self.play(Uncreate(cof_too_text))
        self.play(FadeIn(eq_mk3, RIGHT))
        self.play(TransformMatchingShapes(matrix_Fxd.copy(), matrix_Fx, **kw))
        self.wait(1)
        get_mk = TexText("$\checkmark$").move_to(q_mk).set_color(GREEN).scale(1.5)
        self.play(Fx.animate.set_opacity(1), FocusOn(Fx, color=GREEN), TransformMatchingShapes(q_mk, get_mk))
        self.wait(2)
        self.play(
            FadeOut(
            get_mk+Fxd+matrix_Fxd+cof_text+eq_mk1+eq_mk2+eq_mk3+co_equ_mat+co_equ_const+brace_text_co_f+brace_text_co_g+brace_text_co_h+eq_Fx4
            )
        )
        self.play(
            Fx.animate.next_to(eq_mk0, LEFT),
            matrix_Fx.animate.set_color(WHITE).next_to(eq_mk0, RIGHT)
        )

        # get F(a) = F(b)
        remember_text = Text("还记得罗尔中值定理吗？", t2c={"罗尔中值定理": TEAL}).scale(0.5).next_to(rolle_rect, UP)
        q_mk.next_to(rolle_tex[1], RIGHT).scale(0.7).set_color(RED)
        get_mk.move_to(q_mk).scale(0.8)
        self.play(Write(remember_text))
        self.wait()
        self.play(ShowCreation(rolle_rect), Write(rolle_text_group))
        self.play(FadeOut(remember_text))
        self.wait()
        self.play(rolle_tex[1].animate.set_color(BLUE))
        self.play(Write(q_mk))
        self.wait()

        Fa = Tex("F(a)").set_color(BLUE)
        matrix_Fa = Tex(
            """
            \\begin{vmatrix}
            f(a) & g(a) & h(a) \\\\
            f(b) & g(b) & h(b) \\\\
            f(a) & g(a) & h(a) \\\\
            \\end{vmatrix}
            """
        )
        matrix_Fa[0][30:42].set_color(BLUE)
        eq_Fa = VGroup(Fa, Tex("="), matrix_Fa, Tex("=0").set_color(BLUE)).arrange(RIGHT).move_to(0.9 * UP+3 * LEFT)
        Fb = Tex("F(b)").set_color(BLUE)
        matrix_Fb = Tex(
            """
            \\begin{vmatrix}
            f(a) & g(a) & h(a) \\\\
            f(b) & g(b) & h(b) \\\\
            f(b) & g(b) & h(b) \\\\
            \\end{vmatrix}
            """
        )
        matrix_Fb[0][30:42].set_color(BLUE)
        eq_Fb = VGroup(Fb, Tex("="), matrix_Fb, Tex("=0").set_color(BLUE), Tex("=F(a)").set_color(BLUE), ).arrange(RIGHT).next_to(eq_Fa, DOWN, aligned_edge=LEFT)

        self.play(TransformMatchingShapes(Fx.copy(), Fa))
        self.play(FadeIn(eq_Fa[1]))
        self.play(TransformMatchingShapes(matrix_Fx.copy(), matrix_Fa))
        self.wait(1)
        self.play(matrix_Fa.animate.set_color(WHITE))
        self.wait(2)

        det_prop_text = Text("行列式性质：\n存在相同行时，\n行列式的值为零", t2c={"相同行": BLUE, "零": BLUE}).scale(0.5).next_to(matrix_Fa, RIGHT, aligned_edge=DOWN)
        self.play(
            ShowCreationThenFadeAround(matrix_Fa[0][6:18]),
            ShowCreationThenFadeAround(matrix_Fa[0][30:42]),
            Write(det_prop_text), run_time=3
        )
        self.wait(2)
        self.play(Uncreate(det_prop_text))
        self.play(Write(eq_Fa[3]))
        self.wait(2)
        self.play(matrix_Fa[0][30:42].animate.set_color(BLUE))
        self.play(TransformMatchingShapes(eq_Fa.copy(), eq_Fb[0:4]))
        self.wait()
        self.play(TransformMatchingShapes(Fa.copy(), eq_Fb[4]))
        self.wait()
        self.play(FocusOn(rolle_tex[1], color=GREEN), TransformMatchingShapes(q_mk, get_mk))
        self.wait(2)
        self.play(FadeOut(Fx+eq_mk0+matrix_Fx+eq_Fa+eq_Fb+rolle_text_group+rolle_rect+get_mk))
        self.play()

        # solve question1
        markq12 = Text('（1）解：').to_corner(UL)
        equ_matrix_cd.set_color(WHITE).move_to(ORIGIN).scale(0.8)
        q1_group = VGroup(questiontitle.copy(), question1.copy(), equ_matrix_cd.copy()).set_opacity(0.6).arrange(DOWN).scale(0.6).to_corner(UR)
        self.play(FadeIn(q1_group))
        self.play(TransformMatchingShapes(markq11, markq12))

        matrix_Fx.set_color(WHITE)
        sol_q1_line0 = VGroup(Text("令"), Fx, Tex("="), matrix_Fx, TexText(",")).arrange(RIGHT)
        sol_q1_line1 = TexText("因为$f(x),g(x),h(x)$在区间$[a,b]$内可微，")
        sol_q1_line2 = TexText("所以$F(x)$在区间$[a,b]$内可微，")
        sol_q1_line3 = TexText("由罗尔定理，", "在区间$[a,b]$内至少存在一个常数$c$满足", "$F'(c)=0$，")
        sol_q1_line3[0][1:5].set_color(TEAL)
        sol_q1_line4 = VGroup(TexText("即满足$F(c)=$"), q1_group[2].copy().set_opacity(1).scale(2), TexText(",")).arrange(RIGHT)
        sol_q1_line5 = TexText("得证").set_color(GREEN)
        sol_q1_lines = VGroup(
            sol_q1_line0,
            sol_q1_line1,
            sol_q1_line2,
            sol_q1_line3,
            sol_q1_line4,
            sol_q1_line5
        ).scale(0.75).arrange(DOWN, aligned_edge=LEFT)

        self.play(Write(sol_q1_lines[0]))
        self.wait()
        self.play(Indicate(q1_group[0], color=GREEN))
        self.play(Write(sol_q1_lines[1]))
        self.play(Write(sol_q1_lines[2]))
        self.wait(2)
        self.play(Write(sol_q1_lines[3]))
        self.play(Write(sol_q1_lines[4]))
        self.wait(2)
        self.play(Indicate(sol_q1_lines[3][1], color=GREEN), Indicate(q1_group[1][0][6:27], color=GREEN))
        self.play(Indicate(sol_q1_lines[4][1], color=GREEN), Indicate(q1_group[2], color=GREEN))
        self.wait()
        self.play(Write(sol_q1_lines[5]))
        self.play(Flash(sol_q1_lines[5], color=GREEN, flash_radius=0.7))
        self.wait(3)
        self.play(FadeOut(
            q1_group+sol_q1_lines+markq12
            )
        )

        # back to title
        q_title_lines = VGroup(questiontitle, question1, equ_matrix_cd, question2, cauchy).arrange(DOWN, aligned_edge=LEFT).shift(0.4 * DOWN)
        equ_matrix_cd.shift(2.8 * RIGHT)
        cauchy.shift(3 * RIGHT)
        self.play(FadeIn(title+q_title_lines))

        get_mk.next_to(q_title_lines[1], LEFT)
        q_mk.next_to(q_title_lines[3], LEFT)
        hint_text = TexText("提示：令$h(x)=?$").set_color(RED).scale(0.5).next_to(q_mk, DOWN, aligned_edge=LEFT)
        end_text = Text("感谢观看~").set_color_by_gradient(GREEN, TEAL, BLUE)
        huan_mk = Text("@19_Huan").scale(0.5).to_corner(DR)

        self.play(ShowCreation(get_mk))
        self.wait()
        self.play(ShowCreation(q_mk))
        self.wait(2)
        self.play(Write(hint_text))
        self.wait(3)
        self.play(FadeOut(q_title_lines+get_mk+q_mk+hint_text))
        self.play(TransformMatchingShapes(title, end_text))
        self.wait(2)
        self.play(Write(huan_mk))
        self.wait(2)