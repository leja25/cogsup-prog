from expyriment import design, control, stimuli

# customisable parameters!!
## square size
s = 100
## square colour
s_colour = (0, 255, 0) #r g b
## gap size
g = 20
## number of columns
cols = 10
## number of rows
rows = 6
## background colour
bg_colour = (254, 1, 154)

exp = design.Experiment(name = "hermann_grid", background_colour = bg_colour)
control.initialize(exp)

col_count = cols
k = cols
x_coords = []

#even number of columns
if cols % 2 == 0:
    while col_count >= 1:
        x_coords.append(((k/2)-0.5))
        k -=2
        col_count -=1

#odd number of columns
if cols % 2 != 0:
    while col_count >= 1:
        x_coords.append(((k-1)/2))
        k -= 2
        col_count -= 1

row_count = rows
j = rows
y_coords = []

#even rows
if rows % 2 == 0:
    while row_count >= 1:
        y_coords.append(((j/2)-0.5))
        j -=2
        row_count -=1

#odd rows
if rows % 2 != 0:
    while row_count >= 1:
        y_coords.append(((j-1)/2))
        j -= 2
        row_count -= 1

coords = []

for h in range(rows):
    for i in range(cols):
        ls = []
        ls.append(x_coords[i-1])
        ls.append(y_coords[h-1])
        coords.append(ls)

exp.screen.clear()

for i in range(len(coords)+1):
   square = stimuli.Rectangle(size = (s, s), 
                              colour = s_colour, 
                              position = ((((coords[i-1][0])*g)+((coords[i-1][0])*s)), 
                                          ((coords[i-1][1])*g)+((coords[i-1][1])*s)))
   
   square.present(clear = False, update = False)

exp.screen.update()
exp.keyboard.wait()

control.end()