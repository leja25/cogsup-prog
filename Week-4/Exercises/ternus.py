from expyriment import design, control, stimuli
from expyriment.misc.constants import K_SPACE, C_GREEN, C_RED, C_BLUE

def make_circles(pos_col_list, rad=40, tags = False):
    circles = [stimuli.Circle(radius = rad, position = poscol[0]) for poscol in pos_col_list]

    for circle in circles:
        circle.preload()

    return circles

def make_tags(pos_col_list, rad = 10):
    tags = [stimuli.Circle(radius = rad, position = poscol[0], colour = poscol[1]) for poscol in pos_col_list]
    for tag in tags:
        tag.preload()
    return tags

def timed_draw(stims):
    t0 = exp.clock.time
    exp.screen.clear()
    for i in stims:
        i.present(clear = False, update = False)
    exp.screen.update()
    draw_time = exp.clock.time - t0

    return draw_time

def present_for(stims, num_frames):
    if num_frames == 0:
        return
    
    dt = timed_draw(stims)
    exp.clock.wait(num_frames*(1000/60)-dt) #draw time subtraction ensures that when this function is used to construct the ISI, the drawing time does not add time to the ISI

exp = design.Experiment(name="ternus")
control.set_develop_mode()
control.initialize(exp)

w, h = exp.screen.size

pos_cols = [[(w/10, 0), C_GREEN], [(-w/10, 0), C_RED], [((-w/10)*3, 0), C_BLUE]]
#fix 1, fix 2, move 1
isi = 6*(1000/60)
pos1 = ((-w/10)*3, 0)
pos2 = ((w/10)*3, 0)
count = 0
circles = make_circles(pos_cols, rad = 40)

while True:
    present_for(circles, num_frames = 18) # present circles for 18 frames minus draw time
    present_for([], num_frames = (isi/(1000/60))) #presents blank screen
    if count%2 == 0:
        circles[-1].reposition(pos2) #on even trials change to the right
    else:
        circles[-1].reposition(pos1) #on odd trials change moving circle to the left
    count += 1
    if exp.keyboard.check(K_SPACE):
        break

control.end()