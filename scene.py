from manim import *

class InverseFunctionAndMatrix(Scene):
    def construct(self):
        func = MathTex("f(x) = \\frac{ax+b}{cx+d}").shift(1.5*UP + 4.5*LEFT)
        func_arr = MathTex("\\Longleftrightarrow").shift(1.5*UP + 2*LEFT)
        func_inv = MathTex("f^{-1}(x) = ", "\\frac{dx-b}{-cx+a}", "\\ (", "ad-bc", " \\neq 0)").shift(1.5*UP + 2.5*RIGHT)
        mat = MathTex("A = \\begin{bmatrix} a & b \\\\ c & d \\end{bmatrix}").shift(1.5*DOWN + 5.5*LEFT)
        mat_arr = MathTex("\\Longleftrightarrow").shift(1.5*DOWN + 3*LEFT)
        mat_inv = MathTex("A^{-1} = ", "\\frac{1}{", "ad-bc", "}", "\\begin{bmatrix} d & -b \\\\ -c & a \\end{bmatrix}", "\\ (", "ad-bc", " \\neq 0)").shift(1.5*DOWN + 2.5*RIGHT)
        
        self.wait(2)
        self.play(Write(func))
        self.wait()
        self.play(DrawBorderThenFill(func_inv))
        self.wait(0.5)
        self.play(DrawBorderThenFill(func_arr), run_time = 1)
        self.wait(2)
        self.play(Write(mat))
        self.wait()
        self.play(DrawBorderThenFill(mat_inv))
        self.wait(0.5)
        self.play(DrawBorderThenFill(mat_arr), run_time = 1)
        self.wait()
        self.play(Circumscribe(func_inv[1], time_width = 0.25, color = GREEN), Circumscribe(mat_inv[4], time_width = 0.25, color = GREEN), run_time = 2)
        self.wait()
        self.play(Circumscribe(func_inv[3], time_width = 0.25, color = BLUE), Circumscribe(mat_inv[2], time_width = 0.25, color = BLUE), Circumscribe(mat_inv[6], time_width = 0.25, color = BLUE), run_time = 2)
        self.wait()
        self.play(FadeOut(func, func_arr, func_inv, mat, mat_arr, mat_inv))
        self.wait(1.5)


        func = MathTex("y = \\frac{ax+b}{cx+d}")
        func_y = MathTex("\\frac{ky}{k} = \\frac{ax+b}{cx+d}\\ (k \\neq 0)")
        eq1 = MathTex("\\begin{cases} ax+b = ky \\\\ cx + d = k \\end{cases}")
        mat1 = MathTex("\\begin{bmatrix} a & b \\\\ c & d \\end{bmatrix} \\begin{bmatrix} x \\\\ 1 \\end{bmatrix} = k\\begin{bmatrix} y \\\\ 1 \\end{bmatrix}")
        mat2 = MathTex("{\\begin{bmatrix} a & b \\\\ c & d \\end{bmatrix}}^{-1} \\begin{bmatrix} a & b \\\\ c & d \\end{bmatrix} \\begin{bmatrix} x \\\\ 1 \\end{bmatrix} = k {\\begin{bmatrix} a & b \\\\ c & d \\end{bmatrix}}^{-1} \\begin{bmatrix} y \\\\ 1 \\end{bmatrix}")
        mat3 = MathTex("\\begin{bmatrix} x \\\\ 1 \\end{bmatrix} = k {\\begin{bmatrix} a & b \\\\ c & d \\end{bmatrix}}^{-1} \\begin{bmatrix} y \\\\ 1 \\end{bmatrix}")
        mat4 = MathTex("\\begin{bmatrix} x \\\\ 1 \\end{bmatrix} = \\frac{k}{ad-bc} \\begin{bmatrix} d & -b \\\\ -c & a \\end{bmatrix} \\begin{bmatrix} y \\\\ 1 \\end{bmatrix}")
        mat5 = MathTex("\\frac{ad-bc}{k} \\begin{bmatrix} x \\\\ 1 \\end{bmatrix} = \\begin{bmatrix} d & -b \\\\ -c & a \\end{bmatrix} \\begin{bmatrix} y \\\\ 1 \\end{bmatrix}")
        eq2 = MathTex("\\begin{cases} \\frac{ad-bc}{k} x = dy - b \\\\ \\frac{ad-bc}{k} = -cy + a \\end{cases}")
        eq3 = MathTex("(-cy + a)x = dy - b")
        func_inv = MathTex("x = \\frac{dy-b}{-cy+a}")
        arr1 = MathTex("\\Longrightarrow")
        arr2 = MathTex("\\Longrightarrow")

        self.play(Write(func))
        self.wait(2)
        self.play(ReplacementTransform(func, func_y))
        self.wait(2)
        self.play(func_y.animate.move_to([-3, 0, 0]))
        self.play(DrawBorderThenFill(arr1.move_to([0.4, 0, 0])), Write(eq1.move_to([3, 0, 0])))
        self.wait(3)
        self.play(Unwrite(func_y), run_time = 1)
        self.play(arr1.animate.move_to([-0.5, 0, 0]), eq1.animate.move_to([-3.5, 0, 0]))
        self.play(Write(mat1.move_to([3, 0, 0])))
        self.wait(3)
        self.play(Unwrite(arr1), Unwrite(eq1), run_time = 1)
        self.play(mat1.animate.move_to([0, 0, 0]))
        self.wait(2)
        self.play(ReplacementTransform(mat1, mat2))
        self.wait(3)
        self.play(ReplacementTransform(mat2, mat3))
        self.wait(3)
        self.play(ReplacementTransform(mat3, mat4))
        self.wait(3)
        self.play(ReplacementTransform(mat4, mat5))
        self.wait(3)
        self.play(mat5.animate.move_to([-3.5, 0, 0]))
        self.play(DrawBorderThenFill(arr2.move_to([1, 0, 0])), Write(eq2.move_to([4.5, 0, 0])))
        self.wait(3)
        self.play(Unwrite(mat5), run_time = 1)
        self.play(eq2.animate.move_to([-3.5, 0, 0]), arr2.animate.move_to([-0.2, 0, 0]))
        self.play(Write(eq3.move_to([3.3, 0, 0])))
        self.wait(3)
        self.play(ReplacementTransform(eq3, func_inv.move_to([3.5, 0, 0])), eq2.animate.move_to([-3, 0, 0]), arr2.animate.move_to([0.5, 0, 0]))
        self.wait(2)
        self.play(Unwrite(arr2), Unwrite(eq2), run_time = 1)
        self.play(func_inv.animate.move_to([0, 1, 0]).scale(1.5).set_color_by_gradient(GREEN, TEAL, BLUE))
        self.wait()

        instagram_id = MathTex("\\mathrm{@shun400hz}").shift([0, -2, 0]).scale(1.5)
        instagram_id.set_color_by_gradient("#FA7E1E", "#D62976", "#962FBF", "#4F5BD5")
        self.play(DrawBorderThenFill(instagram_id))
        self.wait(3)


