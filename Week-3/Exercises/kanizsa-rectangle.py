from expyriment import design, control, stimuli
exp = design.Experiment(name = "kanisza_square", background_colour = (100, 100, 100))
control.initialize(exp)

width, height = exp.screen.size

def kanizsa_square(aspect = [1, 1], rect_scale = 1, circle_scale = 1):
    len = width/4
    w, l = [a*len for a in aspect]
    w *= rect_scale
    l *= rect_scale
    r = (width/20)*circle_scale
    square = stimuli.Rectangle(size = (w, l), colour = (100, 100, 100))
    cir1 = stimuli.Circle(radius=r, colour = (0, 0, 0), position = (-(w/2), (l/2)))
    cir2 = stimuli.Circle(radius=r, colour = (255, 255, 255), position = (-(w/2), -(l/2)))
    cir3 = stimuli.Circle(radius=r, colour = (0, 0, 0), position = ((w/2), (l/2)))
    cir4 = stimuli.Circle(radius=r, colour = (255, 255, 255), position = ((w/2), -(l/2)))

    cir1.present(clear=True, update=False)
    cir2.present(clear=False, update=False)
    cir3.present(clear=False, update=False)
    cir4.present(clear=False, update=False)
    square.present(clear=False, update=True)

kanizsa_square(aspect = [2, 1], rect_scale = 0.5, circle_scale = 0.25)

exp.keyboard.wait()

control.end()