from expyriment import design, control, stimuli
exp = design.Experiment(name = "kanisza_square", background_colour = (100, 100, 100))
control.initialize(exp)

width, height = exp.screen.size

len = width/4

cir1 = stimuli.Circle(radius=width/20, colour = (0, 0, 0), position = (-(len/2), (len/2)))
cir2 = stimuli.Circle(radius=width/20, colour = (255, 255, 255), position = (-(len/2), -(len/2)))
cir3 = stimuli.Circle(radius=width/20, colour = (0, 0, 0), position = ((len/2), (len/2)))
cir4 = stimuli.Circle(radius=width/20, colour = (255, 255, 255), position = ((len/2), -(len/2)))

square = stimuli.Rectangle(size = (len, len), colour = (100, 100, 100))

cir1.present(clear=True, update=False)
cir2.present(clear=False, update=False)
cir3.present(clear=False, update=False)
cir4.present(clear=False, update=False)
square.present(clear=False, update=True)

exp.keyboard.wait()

control.end()