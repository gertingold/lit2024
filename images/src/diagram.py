from pyx import canvas, color, deco, deformer, path, text, unit

text.set(text.LatexEngine, texenc='utf8')
text.preamble(r'''\usepackage{roboto}
                  \usepackage[T1]{fontenc}
                  \renewcommand{\familydefault}{\sfdefault}
                  ''')

command_color = color.hsb(0.14, 0.3, 1)
command_color_dark = color.hsb(0.14, 1, 0.8)
final_color = color.hsb(0.3, 0.2, 1)
final_color_dark = color.hsb(0.3, 1, 0.8)
alert_color = color.hsb(0.05, 0.2, 1)
alert_color_dark = color.hsb(0.05, 1, 0.8)
rounded = deformer.smoothed(0.3)

unit.set(xscale=1.3)

def make_diagram(highlight=False):
    c = canvas.canvas()
    t1 = text.text(0, 8.1, 'Jupyter Notebooks')
    t2 = text.text(16, 8.1, 'Markdown-Dateien', [text.halign.right])
    tbb1 = t1.bbox()
    tbb2 = t2.bbox()
    t2b = text.text(tbb2.left(), tbb2.bottom()-0.75, r'\scriptsize = Markedly Structured Text', [text.valign.top])
    tbb2b = t2b.bbox()
    if highlight:
        c.fill(path.rect(tbb2.left()-0.1, tbb2b.bottom()-0.1, tbb2.width()+0.2, tbb2.top()-tbb2b.bottom()+0.2),
               [alert_color, deco.stroked([alert_color_dark])])
    c.insert(t1)
    c.insert(t2)
    c.insert(t2b)
    c.text(tbb2.left(), tbb2.bottom()-0.3, r'\footnotesize MyST Markdown', [text.valign.top])
    c.stroke(path.line(tbb1.right()+0.2, (tbb1.top()+tbb1.bottom())/2,
                       tbb2.left()-0.2, (tbb1.top()+tbb1.bottom())/2),
             [deco.barrow, deco.earrow])
    t3 = text.text((tbb1.right()+tbb2.left())/2, (tbb1.top()+tbb1.bottom())/2+0.3,
                   'jupytext', [text.halign.center])
    p = t3.bbox().enlarged(0.1).path()
    c.fill(p, [command_color, rounded, deco.stroked([command_color_dark])])
    c.insert(t3)
    t4 = text.text((tbb1.right()+tbb2.left())/2, (tbb1.top()+tbb1.bottom())/2-0.3,
                   'mystnb-to-jupyter', [text.halign.center, text.valign.top])
    p = t4.bbox().enlarged(0.1).path()
    c.fill(p, [command_color, rounded, deco.stroked([command_color_dark])])
    c.insert(t4)
    t6 = text.text(16, 2, 'Veröffentlichung auf github.io', [text.halign.right])
    tbb6 = t6.bbox()
    c.insert(t6)
    xrc = (tbb6.left()+tbb6.right())/2
    t5 = text.text(xrc, 5, 'Versionskontrolle auf GitHub', [text.halign.center])
    c.insert(t5)
    tbb5 = t5.bbox()
    c.stroke(path.line(xrc, tbb2b.bottom()-0.2, xrc, tbb5.top()+0.2), [deco.earrow])
    c.stroke(path.line(xrc, tbb5.bottom()-0.2, xrc, tbb6.top()+0.2), [deco.earrow])
    t5b = text.text(xrc, (tbb5.bottom()+tbb6.top())/2, 'GitHub actions', [text.halign.center, text.valign.middle])
    tbb5b = t5b.bbox().enlarged(0.1)
    c.fill(tbb5b.path(), [command_color, rounded, deco.stroked([command_color_dark])])
    c.insert(t5b)
    t7 = text.text(xrc, 0.3, 'gertingold.github.io', [text.halign.center])
    tbb7 = t7.bbox().enlarged(0.15)
    c.fill(tbb7.path(), [final_color, deco.stroked([final_color_dark])])
    c.stroke(path.line(xrc, tbb6.bottom()-0.2, xrc, tbb7.top()+0.2), [deco.earrow])
    c.insert(t7)
    t9 = text.text(5.5, 2.5, 'HTML', [text.halign.center])
    tbb9 = t9.bbox().enlarged(0.15)
    c.fill(tbb9.path(), [final_color, deco.stroked([final_color_dark])])
    c.insert(t9)
    c.stroke(path.line(tbb2.left()-0.2, tbb2.bottom(), 6, 5))
    c.stroke(path.line((tbb1.left()+tbb1.right())/2, tbb1.bottom()-0.2, 5, 5))
    c.stroke(path.line(5.5, 5, 5.5, 3), [deco.earrow])
    t8 = text.text(5.5, 5, 'jupyter-book', [text.halign.center, text.valign.middle])
    tbb8 = t8.bbox().enlarged(0.1)
    c.fill(tbb8.path(), [command_color, rounded, deco.stroked([command_color_dark])])
    c.insert(t8)

    if highlight:
        filename = 'diagram_2.png'
    else:
        filename = 'diagram_1.png'
    
    c.writeGSfile(filename, device='png16m', resolution=300)

make_diagram()
make_diagram(highlight=True)
