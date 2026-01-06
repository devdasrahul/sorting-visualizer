"""
Main Application Entry Point.

Handles the Pygame event loop, user input, and orchestrates the sorting visualization.
"""
import pygame
import random
import math
from draw import DrawInformation, draw
from sorting_algorithms import bubble_sort, insertion_sort, selection_sort, merge_sort, quick_sort, heap_sort, counting_sort

pygame.init()

def generate_starting_list(n, min_val, max_val):
	"""
	Generates a list of random integers.

	Args:
		n (int): Number of elements.
		min_val (int): Minimum value.
		max_val (int): Maximum value.
	
	Returns:
		list: List of random integers.
	"""
	lst = []
	for _ in range(n):
		val = random.randint(min_val, max_val)
		lst.append(val)
	return lst

def main():
	"""Main game loop for the Sorting Visualizer."""
	run = True
	clock = pygame.time.Clock()

	n = 50
	min_val = 0
	max_val = 100

	lst = generate_starting_list(n, min_val, max_val)
	draw_info = DrawInformation(800, 600, lst)
	sorting = False
	ascending = True

	sorting_algorithm = bubble_sort
	sorting_algo_name = "Bubble Sort"
	sorting_algorithm_generator = None

	fps = 60
	
	# Stats Tracking
	stats = {
		'comps': 0,
		'swaps': 0
	}

	ALGORITHM_MAP = {
		pygame.K_1: (bubble_sort, "Bubble Sort"),
		pygame.K_2: (selection_sort, "Selection Sort"),
		pygame.K_3: (insertion_sort, "Insertion Sort"),
		pygame.K_4: (merge_sort, "Merge Sort"),
		pygame.K_5: (quick_sort, "Quick Sort"),
		pygame.K_6: (heap_sort, "Heap Sort"),
		pygame.K_7: (counting_sort, "Counting Sort")
	}

	while run:
		clock.tick(fps)

		if sorting:
			try:
				# Generator now yields a tuple: (color_positions, comp_inc, swap_inc)
				color_positions, comp_inc, swap_inc = next(sorting_algorithm_generator)
				draw(draw_info, sorting_algo_name, ascending, fps, stats, color_positions)
				
				# Update stats
				stats['comps'] += comp_inc
				stats['swaps'] += swap_inc
				
				# Pass color_positions to draw list if we want to redraw here, 
				# but draw() handles the full redraw.
				# Wait, draw() needs color_positions!
				# The variable 'draw' function call above currently doesn't accept color_positions.
				# Let's check draw definition: def draw(draw_info, algo_name, ascending, fps, stats):
				# It calls draw_list(draw_info).
				# I need to modify draw() to accept optional color_positions or call draw_list explicitly.
				# Actually, easier to just pass it to draw since it clears screen and redraws everything.
				# But wait, draw() definition I wrote earlier doesn't take color_positions.
				# I need to update draw() too or misuse it.
				# I will modify draw() call inside here to pass color_positions via a new arg or modifying draw logic.
				# Let's modify the draw function usage here:
				# Oops, I missed adding color_positions argument to the 'high level' draw() function in draw.py.
				# It only calls draw_list().
				# I can assign color_positions to draw_list manually inside 'draw' if I pass it.
				# Let's fix this in main loop by calling the sub-functions if needed, or better, 
				# update draw.py to accept it.
				# Since I can't update draw.py in this tool call easily without overwrite,
				# I will use the `draw_list` directly or just assume `draw` handles it if I updated it...
				# Wait, I did update draw.py in previous step.
				# Definition: def draw(draw_info, algo_name, ascending, fps, stats):
				# It calls: draw_list(draw_info) -> NO COLOR POSITIONS PASSED!
				# This means animation colors won't show!
				# I must FIX draw.py to accept color_positions.

			except StopIteration:
				sorting = False
		else:
			draw(draw_info, sorting_algo_name, ascending, fps, stats) # Default black bars

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if event.type != pygame.KEYDOWN:
				continue

			if event.key == pygame.K_r:
				lst = generate_starting_list(n, min_val, max_val)
				draw_info.set_list(lst)
				sorting = False
				stats['comps'] = 0
				stats['swaps'] = 0
			elif event.key == pygame.K_SPACE and not sorting:
				sorting = True
				stats['comps'] = 0
				stats['swaps'] = 0
				sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
			elif event.key == pygame.K_a and not sorting:
				ascending = True
			elif event.key == pygame.K_d and not sorting:
				ascending = False
			
			elif event.key in ALGORITHM_MAP and not sorting:
				sorting_algorithm, sorting_algo_name = ALGORITHM_MAP[event.key]
			
			elif event.key == pygame.K_UP:
				fps = min(120, fps + 10)
			elif event.key == pygame.K_DOWN:
				fps = max(1, fps - 10)
			elif event.key == pygame.K_RIGHT and not sorting:
				n = min(200, n + 5)
				lst = generate_starting_list(n, min_val, max_val)
				draw_info.set_list(lst)
			elif event.key == pygame.K_LEFT and not sorting:
				n = max(5, n - 5)
				lst = generate_starting_list(n, min_val, max_val)
				draw_info.set_list(lst)

	pygame.quit()

if __name__ == "__main__":
	main()
