def print_four(s):
	print(s)
	print(s)
	print(s)
	print(s)

def print_wide_beam(w):
	print('+ - - - - ' * w + '+')

def do_x_times(func, arg, x):
	for i in range(x):
		func(arg)

def draw_grid_section(w):
	print_wide_beam(w)
	print_four('|         ' * w + '|')

def draw_w_x_h_grid(w, h):
	do_x_times(draw_grid_section, w, h)
	print_wide_beam(w)

draw_w_x_h_grid(4,4)
draw_w_x_h_grid(6,6)