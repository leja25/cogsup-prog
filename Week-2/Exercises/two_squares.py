from expyriment import design, control, stimuli

exp = design.Experiment(name = "Square")

control.initialize(exp)

square_g = stimuli.Rectangle(size = (50, 50), colour = (0, 255, 0), position = (-125, 0))
square_r = stimuli.Rectangle(size = (50, 50), colour = (255, 0, 0), position = (125, 0))

square_g.present(clear=True, update=False)
square_r.present(clear=False, update=True)
exp.keyboard.wait()

control.end()