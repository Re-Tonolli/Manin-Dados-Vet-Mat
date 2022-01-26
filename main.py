from manim import *


def create_square(x, y, grid: NumberPlane):
    size_square = (grid.c2p(1, 0) - grid.c2p(0, 0))[0]
    square = Square(side_length=size_square, color=ORANGE, fill_color=ORANGE, fill_opacity=0.7).move_to(
        size_square / 2 * RIGHT + size_square / 2 * UP)
    square.shift(x * size_square * RIGHT + y * size_square * UP)
    return square


def create_number(x, y, grid: NumberPlane, number):
    size_square = (grid.c2p(1, 0) - grid.c2p(0, 0))[0]
    number_text = MathTex(str(number)).move_to(size_square / 2 * RIGHT + size_square / 2 * UP)
    number_text.shift(x * size_square * RIGHT + y * size_square * UP)
    return number_text


class Laranja(Scene):
    def construct(self):
        self.wait(1)
        title = Tex("Dados Matriciais e Vetoriais")
        self.play(Write(title))
        self.wait(2)
        subtitle_1 = Tex("Dados Matriciais")
        self.play(TransformMatchingShapes(title, subtitle_1))
        self.wait(2)
        self.play(subtitle_1.animate.to_edge(UP).scale(0.5))

        # COMPARAÇãO COM A LARANJA
        laranja = ImageMobject("laranja_inteira.png")
        self.play(FadeIn(laranja))
        self.wait(2)

        # SUBSTITUIÇÃO DA LARANJA POR UM CIRCULO E CRIAÇÃO
        laranja_fake = Circle(radius=1.7, color=ORANGE, fill_color=ORANGE, fill_opacity=0.5)
        self.play(FadeOut(laranja), FadeIn(laranja_fake))
        matrix = NumberPlane(x_range=[-3.4, 3.4], y_range=[-2.3, 2.3])
        self.play(Write(matrix))
        self.wait(2)
        laranja_pixelada = VGroup(create_square(0, 0, matrix),
                                  create_square(0, 1, matrix),
                                  create_square(1, 0, matrix),
                                  create_square(0, -1, matrix),
                                  create_square(0, -2, matrix),
                                  create_square(1, -1, matrix),
                                  create_square(-1, 0, matrix),
                                  create_square(-1, 1, matrix),
                                  create_square(-2, 0, matrix),
                                  create_square(-1, -1, matrix),
                                  create_square(-1, -2, matrix),
                                  create_square(-2, -1, matrix))
        for square in laranja_pixelada:
            self.play(FadeIn(square), run_time=0.5)
        self.play(FadeOut(laranja_fake))
        numeros = VGroup(create_number(0, 0, matrix, 1),
                         create_number(0, 1, matrix, 1),
                         create_number(1, 0, matrix, 1),
                         create_number(0, -1, matrix, 1),
                         create_number(0, -2, matrix, 1),
                         create_number(1, -1, matrix, 1),
                         create_number(-1, 0, matrix, 1),
                         create_number(-1, 1, matrix, 1),
                         create_number(-2, 0, matrix, 1),
                         create_number(-1, -1, matrix, 1),
                         create_number(-1, -2, matrix, 1),
                         create_number(-2, -1, matrix, 1),
                         create_number(1, 1, matrix, 0),
                         create_number(2, 1, matrix, 0),
                         create_number(2, 0, matrix, 0),
                         create_number(2, -1, matrix, 0),
                         create_number(2, -2, matrix, 0),
                         create_number(1, -2, matrix, 0),
                         create_number(-2, -2, matrix, 0),
                         create_number(-3, -2, matrix, 0),
                         create_number(-3, -1, matrix, 0),
                         create_number(-3, 0, matrix, 0),
                         create_number(-3, 1, matrix, 0),
                         create_number(-2, 1, matrix, 0), )
        for number in numeros:
            self.play(FadeIn(number), run_time=0.5)
        self.wait(2)
        self.play(FadeOut(matrix), FadeOut(numeros))
        matriz_num = Matrix([[0, 0, 1, 1, 0, 0], [0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 1, 0, 0]]).to_edge(
            RIGHT)
        self.wait(2)
        self.play(laranja_pixelada.animate.to_edge(4 * LEFT), Write(matriz_num))
        self.wait(2)
        self.play(FadeOut(matriz_num))
        matrix_hd = NumberPlane(x_range=[-14, 14, 1], y_range=[-8, 8, 1], x_length=14, y_length=9)
        laranja_hd = VGroup(create_square(0, 0, matrix_hd),
                            create_square(0, -1, matrix_hd),
                            create_square(-1, -1, matrix_hd),
                            create_square(-1, 0, matrix_hd),
                            create_square(-1, 1, matrix_hd),
                            create_square(0, 1, matrix_hd),
                            create_square(1, 1, matrix_hd),
                            create_square(1, 0, matrix_hd),
                            create_square(1, -1, matrix_hd),
                            create_square(1, -2, matrix_hd),
                            create_square(0, -2, matrix_hd),
                            create_square(-1, -2, matrix_hd),
                            create_square(-2, -2, matrix_hd),
                            create_square(-2, -1, matrix_hd),
                            create_square(-2, 0, matrix_hd),
                            create_square(-2, 1, matrix_hd),
                            create_square(-2, 2, matrix_hd),
                            create_square(-1, 2, matrix_hd),
                            create_square(0, 2, matrix_hd),
                            create_square(1, 2, matrix_hd),
                            create_square(2, 1, matrix_hd),
                            create_square(2, 0, matrix_hd),
                            create_square(2, -1, matrix_hd),
                            create_square(2, -2, matrix_hd),
                            create_square(1, -3, matrix_hd),
                            create_square(0, -3, matrix_hd),
                            create_square(-1, -3, matrix_hd),
                            create_square(-2, -3, matrix_hd),
                            create_square(-3, -2, matrix_hd),
                            create_square(-3, -1, matrix_hd),
                            create_square(-3, 0, matrix_hd),
                            create_square(-3, 1, matrix_hd)).to_edge(4.5 * RIGHT)
        self.play(FadeIn(laranja_hd))
        size_grid1 = Tex('(4 x 6)').next_to(laranja_pixelada, DOWN, buff=0.5)
        size_grid2 = Tex('(6 x 8)').next_to(laranja_hd, DOWN, buff=1.0)
        self.play(Write(size_grid1), Write(size_grid2))
        self.wait(2)
        self.play(FadeOut(laranja_hd), FadeOut(laranja_pixelada), FadeOut(size_grid1), FadeOut(size_grid2))

        # DESVANTAGENS MATRICIAL
        desvantagem = Tex('Desvantagens').scale(1.5)
        self.play(FadeIn(desvantagem))
        self.play(desvantagem.animate.to_edge(3 * UP + LEFT).scale(0.5))
        self.wait(2)

        desv_bullet = BulletedList('Falta de precisão e feição nos dados',
                                   'Baixa qualidade',
                                   'Requer grande espaço de armazenamento').move_to(1 * UP + 2.7 * LEFT).scale(0.5)

        desv_to_transform = BulletedList('Falta de precisão nos dados',
                                         'Baixa qualidade',
                                         'Requer grande espaço de armazenamento')

        self.play(FadeIn(desv_to_transform[0].move_to(ORIGIN)))
        self.wait(1)
        self.play(ReplacementTransform(desv_to_transform[0], desv_bullet[0]))
        self.wait(2)
        self.play(FadeIn(desv_to_transform[1].move_to(ORIGIN)))
        self.wait(1)
        self.play(ReplacementTransform(desv_to_transform[1], desv_bullet[1]))
        self.wait(2)
        self.play(FadeIn(desv_to_transform[2].move_to(ORIGIN)))
        self.wait(1)
        self.play(ReplacementTransform(desv_to_transform[2], desv_bullet[2]))
        self.wait(2)
        self.play(FadeOut(desvantagem), FadeOut(desv_bullet[0]), FadeOut(desv_bullet[1]), FadeOut(desv_bullet[2]))
        self.wait(1)

        # VANTAGENS MATRICIAL
        vantagem = Tex('Vantagens').scale(1.5)
        self.play(FadeIn(vantagem))
        self.play(vantagem.animate.to_edge(3 * UP + LEFT).scale(0.5))
        self.wait(2)

        van_bullet = BulletedList('Estrutura simples',
                                  'Modelagens de cálculo se tornam mais fáceis',
                                  'Não é necessário alto poder de processamento'). \
            move_to(1 * UP + 2.7 * LEFT).scale(0.5)

        van_to_transform = BulletedList('Estrutura simples',
                                        'Modelagens de cálculo se tornam mais fáceis',
                                        'Não é necessário alto poder de processamento')

        self.play(FadeIn(van_to_transform[0].move_to(ORIGIN)))
        self.wait(1)
        self.play(ReplacementTransform(van_to_transform[0], van_bullet[0]))
        self.wait(2)
        self.play(FadeIn(van_to_transform[1].move_to(ORIGIN)))
        self.wait(1)
        self.play(ReplacementTransform(van_to_transform[1], van_bullet[1]))
        self.wait(2)
        self.play(FadeIn(van_to_transform[2].move_to(ORIGIN)))
        self.wait(1)
        self.play(ReplacementTransform(van_to_transform[2], van_bullet[2]))
        self.wait(2)
        self.play(FadeOut(vantagem), FadeOut(van_bullet[0]), FadeOut(van_bullet[1]), FadeOut(van_bullet[2]))
        self.wait(1)

        # DADOS VETORIAIS
        subtitle_2 = Tex('Dados Vetoriais')
        self.play(subtitle_1.animate.move_to(ORIGIN).scale(2))
        self.play(TransformMatchingShapes(subtitle_1, subtitle_2))
        self.wait(2)
        self.play(subtitle_2.animate.to_edge(UP).scale(0.5))
        self.wait(1)

        # APRESENTAÇÃO DA SIMBOLOGIA
        ponto = Dot().scale(2).to_edge(6 * LEFT)
        ponto_final = Dot().to_edge(6 * UP + 12 * RIGHT)
        ponto_inicio = Dot().to_edge(6 * DOWN + 12 * LEFT)
        linha = Line(start=ponto_inicio, end=ponto_final)
        poligono1 = Polygon([6, 0, 0], [4.5, 1.5, 0], [3, 1, 0], [2.5, -0.5, 0], [5, -1.5, 0], color=WHITE)
        self.play(FadeIn(ponto))
        self.wait(1)
        self.play(Write(linha))
        self.wait(1)
        self.play(Write(poligono1))
        self.wait(1)
        self.play(FadeOut(ponto), FadeOut(linha), FadeOut(poligono1))
        self.wait(1)

        # CRIAÇÃO DE UMA POLIGONAL VETORIAL COM SEUS ELEMENTOS
        eixos = Axes(
            x_range=(0, 10, 2),
            y_range=(0, 10, 2),
            x_axis_config={'include_numbers': True},
            y_axis_config={'include_numbers': True},
        )
        eixo_x = eixos.get_x_axis().set_color(WHITE)
        eixo_y = eixos.get_y_axis().set_color(WHITE)
        self.play(Write(eixo_x), Write(eixo_y))
        self.wait(1)
        dot_ref1 = Dot().move_to(eixos.c2p(2, 0))
        dot_ref2 = Dot().move_to(eixos.c2p(0, 6))
        dot_ref3 = Dot().move_to(eixos.c2p(6, 0))
        dot_ref4 = Dot().move_to(eixos.c2p(0, 8))
        dot1 = Dot().move_to(eixos.c2p(2, 6)).scale(2)
        dot2 = Dot().move_to(eixos.c2p(6, 8))
        line_dash1 = DashedLine(dot_ref1, dot1)
        line_dash2 = DashedLine(dot_ref2, dot1)
        line_dash3 = DashedLine(dot_ref3, dot2)
        line_dash4 = DashedLine(dot_ref4, dot2)
        tex_dot1 = Tex('(2,6)').next_to(dot1, UP)
        tex_dot2 = Tex('(6,8)').next_to(dot2, UP)
        self.play(Write(line_dash1), Write(line_dash2))
        self.wait(0.5)
        self.play(Write(dot1), Write(tex_dot1))
        self.wait(0.5)
        self.play(Write(line_dash3), Write(line_dash4))
        self.wait(0.5)
        self.play(Write(dot2), Write(tex_dot2))
        self.wait(1)
        self.play(FadeOut(line_dash1), FadeOut(line_dash2), FadeOut(line_dash3), FadeOut(line_dash4))
        line = Line(eixos.c2p(2, 6), eixos.c2p(6, 8))
        self.wait(0.5)
        self.play(Write(line))
        line2 = Line(eixos.c2p(6, 8), eixos.c2p(7, 4))
        dot_line2 = Dot().move_to(eixos.c2p(7, 4))
        tex_line2 = Tex('(7,4)').next_to(dot_line2, DOWN)
        line3 = Line(eixos.c2p(7, 4), eixos.c2p(4, 2))
        dot_line3 = Dot().move_to(eixos.c2p(4, 2))
        tex_line3 = Tex('(4,2)').next_to(dot_line3, DOWN)
        line4 = Line(eixos.c2p(4, 2), eixos.c2p(2, 6))
        self.play(Write(dot_line2), Write(line2), Write(tex_line2))
        self.play(Write(dot_line3), Write(line3), Write(tex_line3))
        self.play(Write(line4))
        self.wait(1)
        poligono2 = Polygon(
            eixos.c2p(2, 6),
            eixos.c2p(6, 8),
            eixos.c2p(7, 4),
            eixos.c2p(4, 2), color=WHITE, fill_color=GREEN, fill_opacity=0.5)
        self.play(Write(poligono2))
        self.wait(1)
        self.play(FadeOut(poligono2),
                  FadeOut(line4),
                  FadeOut(tex_line3),
                  FadeOut(line3),
                  FadeOut(dot_line3),
                  FadeOut(tex_line2),
                  FadeOut(line2),
                  FadeOut(dot_line2),
                  FadeOut(line),
                  FadeOut(tex_dot2),
                  FadeOut(dot2),
                  FadeOut(tex_dot1),
                  FadeOut(dot1),
                  FadeOut(eixos))

        # DESVANTAGENS VETORIAL
        desvantagem = Tex('Desvantagens').scale(1.5)
        self.play(FadeIn(desvantagem))
        self.play(desvantagem.animate.to_edge(3 * UP + LEFT).scale(0.5))
        self.wait(2)

        desv_bullet = BulletedList('Alta complexidade e difícil manipulação',
                                   'Demanda de alto poder de processamento',
                                   'Necessário treinamento').move_to(1 * UP + 2.7 * LEFT).scale(0.5)

        desv_to_transform = BulletedList('Alta complexidade e difícil manipulação',
                                         'Demanda de alto poder de processamento',
                                         'Necessário treinamento')

        self.play(FadeIn(desv_to_transform[0].move_to(ORIGIN)))
        self.wait(1)
        self.play(ReplacementTransform(desv_to_transform[0], desv_bullet[0]))
        self.wait(2)
        self.play(FadeIn(desv_to_transform[1].move_to(ORIGIN)))
        self.wait(1)
        self.play(ReplacementTransform(desv_to_transform[1], desv_bullet[1]))
        self.wait(2)
        self.play(FadeIn(desv_to_transform[2].move_to(ORIGIN)))
        self.wait(1)
        self.play(ReplacementTransform(desv_to_transform[2], desv_bullet[2]))
        self.wait(2)
        self.play(FadeOut(desvantagem), FadeOut(desv_bullet[0]), FadeOut(desv_bullet[1]), FadeOut(desv_bullet[2]))
        self.wait(1)

        # VANTAGENS VETORIAL
        vantagem = Tex('Vantagens').scale(1.5)
        self.play(FadeIn(vantagem))
        self.play(vantagem.animate.to_edge(3 * UP + LEFT).scale(0.5))
        self.wait(2)

        van_bullet = BulletedList('Dados precisos e confiáveis',
                                  'Elevada resolução',
                                  'Requer pouco espaço de armazenamento'). \
            move_to(1 * UP + 2.7 * LEFT).scale(0.5)

        van_to_transform = BulletedList('Dados precisos e confiáveis',
                                        'Elevada resolução',
                                        'Requer pouco espaço de armazenamento')

        self.play(FadeIn(van_to_transform[0].move_to(ORIGIN)))
        self.wait(1)
        self.play(ReplacementTransform(van_to_transform[0], van_bullet[0]))
        self.wait(2)
        self.play(FadeIn(van_to_transform[1].move_to(ORIGIN)))
        self.wait(1)
        self.play(ReplacementTransform(van_to_transform[1], van_bullet[1]))
        self.wait(2)
        self.play(FadeIn(van_to_transform[2].move_to(ORIGIN)))
        self.wait(1)
        self.play(ReplacementTransform(van_to_transform[2], van_bullet[2]))
        self.wait(2)
        self.play(FadeOut(vantagem), FadeOut(van_bullet[0]), FadeOut(van_bullet[1]), FadeOut(van_bullet[2]))
        self.wait(1)

        # APLICAÇÕES
        subtitle_3 = Tex('Aplicações')
        self.play(subtitle_2.animate.move_to(ORIGIN).scale(2))
        self.play(TransformMatchingShapes(subtitle_2, subtitle_3))
        self.wait(2)
        self.play(subtitle_3.animate.to_edge(UP).scale(0.5))
        self.wait(1)

        # Textos
        self.play(FadeIn(subtitle_1.move_to(2 * UP + 4 * LEFT)))
        self.play(subtitle_1.animate.scale(1))
        self.wait(1)

        self.play(FadeIn(subtitle_2.move_to(2 * UP + 3 * RIGHT)))
        self.play(subtitle_2.animate.scale(1))
        self.wait(1)

        linha_sep = Line(start=4 * UP, end=3 * DOWN).scale(0.5)
        self.play(Write(linha_sep))
        self.wait(1)

        # Matricial
        mat_bullet = BulletedList('What3Words',
                                  'Sensoriamento Remoto'). \
            move_to(1 * UP + 3.5 * LEFT).scale(0.5)

        self.play(FadeIn(mat_bullet[0]))
        self.wait(1)
        self.play(FadeIn(mat_bullet[1]))
        self.wait(1)

        # Vetorial
        vec_bullet = BulletedList('QGis',
                                  'Arquivo DWG',
                                  'Arquivo KML'). \
            move_to(1 * UP + 3.5 * RIGHT).scale(0.5)

        self.play(FadeIn(vec_bullet[0]))
        self.wait(1)
        self.play(FadeIn(vec_bullet[1]))
        self.wait(1)

        self.play(FadeOut(subtitle_1), FadeOut(subtitle_2), FadeOut(linha_sep),
                  FadeOut(mat_bullet[0]), FadeOut(mat_bullet[1]),
                  FadeOut(vec_bullet[0]), FadeOut(vec_bullet[1]))
        self.wait(1)

        # REFERENCIAS
        subtitle_4 = Tex('Referências')
        self.play(subtitle_3.animate.move_to(ORIGIN).scale(2.0))
        self.play(TransformMatchingShapes(subtitle_3, subtitle_4))
        self.wait(2)
        self.play(subtitle_4.animate.to_edge(UP).scale(0.5))
        self.wait(1)

        ref_bullet = BulletedList(
            'CÂMARA, G. et al. Introdução a Ciência da Geoinformação. São José dos Campos: INEP, 2001.',
            'DAVIS, B.E. Dados Matriciais (Raster) e Dados Vetoriais (Vector): Raster and vector data.',
            'BRASIL. Rede SPUGeo. Apostila de Sistema de Informações Geográficas.'). \
            move_to(1 * UP + 2 * LEFT).scale(0.5)

        self.play(FadeIn(ref_bullet[0]))
        self.wait(1)
        self.play(FadeIn(ref_bullet[1]))
        self.wait(1)
        self.play(FadeIn(ref_bullet[2]))
        self.wait(1)

        self.play(FadeOut(ref_bullet[0]), FadeOut(ref_bullet[1], ref_bullet[2] , subtitle_4))
        self.wait(1)

        # FECHAMENTO
        subtitle_5 = Tex('UNESP - BAURU',
                         'Engenharia Civil',
                         'GeoProcessamento')
        subtitle_6 = Tex('Renan Tonolli Mondini',
                         'Bruno de Moraes Thomazella')
        subtitle_7 = Tex('Luiz Henrique Soares da Silva')

        self.play(Write(subtitle_5[0].move_to(2.5 * UP).scale(1)))
        self.play(Write(subtitle_5[1].move_to(1.9 * UP).scale(0.7)))
        self.play(Write(subtitle_5[2].move_to(1.5 * UP).scale(0.6)))
        self.play(Write(subtitle_6[0].move_to(0.5 * DOWN).scale(0.5)))
        self.play(Write(subtitle_6[1].move_to(1 * DOWN).scale(0.5)))
        self.play(Write(subtitle_7[0].move_to(1.5 * DOWN).scale(0.5)))
        self.wait(1)
        self.play(FadeOut(subtitle_5), FadeOut(subtitle_6), FadeOut(subtitle_7))
