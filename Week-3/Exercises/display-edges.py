from expyriment import design, control, stimuli

exp = design.Experiment(name = "4_squares")
control.initialize(exp)

width, height = exp.screen.size

sq1 = stimuli.Rectangle(size = (100, 100), colour = (255, 0, 0), line_width=1, position = (-((width/2)-50), ((height/2)-50)))
sq2 = stimuli.Rectangle(size = (100, 100), colour = (255, 0, 0), line_width=1, position = (((width/2)-50), ((height/2)-50)))
sq3 = stimuli.Rectangle(size = (100, 100), colour = (255, 0, 0), line_width=1, position = (-((width/2)-50), -((height/2)-50)))
sq4 = stimuli.Rectangle(size = (100, 100), colour = (255, 0, 0), line_width=1, position = (((width/2)-50), -((height/2)-50)))

sq1.present(clear=True, update=False)
sq2.present(clear=False, update=False)
sq3.present(clear=False, update=False)
sq4.present(clear=False, update=True)

exp.keyboard.wait()

control.end()
