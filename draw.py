import pygame
import math

class DrawInformation:
	"""
	Manages the drawing details, window properties, and color palette.
	Calculates the dynamic sizing of bars based on window dimensions and list size.
	"""
	# Dark Theme Colors
	BLACK = 0, 0, 0
	WHITE = 255, 255, 255
	GREEN = 50, 205, 50      
	RED = 255, 82, 82        
	YELLOW = 255, 215, 0     
	BLUE = 100, 149, 237     
	
	BACKGROUND_COLOR = 30, 30, 40 

	GRADIENTS = [
		(120, 160, 200),
		(140, 180, 220),
		(160, 200, 240)
	]

	FONT_COLOR = 220, 220, 220 
	
	SIDE_PAD = 100
	TOP_PAD = 160 
	BOTTOM_PAD = 120

	# Complexity Data Dictionary for Educational overlay
	ALGO_INFO = {
		"Bubble Sort": {"Time": "O(n²)", "Space": "O(1)"},
		"Insertion Sort": {"Time": "O(n²)", "Space": "O(1)"},
		"Selection Sort": {"Time": "O(n²)", "Space": "O(1)"},
		"Merge Sort": {"Time": "O(n log n)", "Space": "O(n)"},
		"Quick Sort": {"Time": "O(n log n)", "Space": "O(log n)"},
		"Heap Sort": {"Time": "O(n log n)", "Space": "O(1)"},
		"Counting Sort": {"Time": "O(n + k)", "Space": "O(k)"}
	}

	def __init__(self, width, height, list_of_vals):
		"""Initialize the Pygame window and list parameters."""
		self.width = width
		self.height = height

		self.window = pygame.display.set_mode((width, height))
		pygame.display.set_caption("Sorting Algorithm Visualizer")
		self.set_list(list_of_vals)

	def set_list(self, list_of_vals):
		"""
		Set the current list to be sorted and calculate bar dimensions.
		
		Args:
			list_of_vals (list): The list of integers to visualize.
		"""
		self.list = list_of_vals
		self.min_val = min(list_of_vals)
		self.max_val = max(list_of_vals)

		self.block_width = round((self.width - self.SIDE_PAD) / len(list_of_vals))
		self.block_height = math.floor((self.height - self.TOP_PAD - self.BOTTOM_PAD) / (self.max_val - self.min_val + 1)) 
		self.start_x = self.SIDE_PAD // 2

def draw(draw_info, algo_name, ascending, fps, stats, color_positions={}):
	"""
	Main rendering function. Draws header, metrics, footer, and the graph.
	
	Args:
		draw_info (DrawInformation): The state object containing window and list data.
		algo_name (str): Name of the current algorithm.
		ascending (bool): True if sorting in ascending order.
		fps (int): Current Frames Per Second.
		stats (dict): Dictionary containing comparison and swap counts.
		color_positions (dict): Specific coloring for active bars {index: color}.
	"""
	draw_info.window.fill(draw_info.BACKGROUND_COLOR)

	# --- Fonts ---
	title_font = pygame.font.SysFont('arial', 36, bold=True)
	info_font = pygame.font.SysFont('arial', 22)
	stats_font = pygame.font.SysFont('arial', 20)
	controls_font = pygame.font.SysFont('arial', 18)

	# --- Header Section (Centered) ---
	# Title
	title = title_font.render("Sorting Algorithm Visualizer", 1, draw_info.WHITE)
	draw_info.window.blit(title, (draw_info.width/2 - title.get_width()/2 , 10))

	# Algo Name & FPS
	sub_text = f"{algo_name}  |  {'Ascending' if ascending else 'Descending'}  |  FPS: {fps}"
	algo_surface = info_font.render(sub_text, 1, draw_info.BLUE)
	draw_info.window.blit(algo_surface, (draw_info.width/2 - algo_surface.get_width()/2 , 55))

	# Complexity Info
	if algo_name in draw_info.ALGO_INFO:
		data = draw_info.ALGO_INFO[algo_name]
		comp_text = f"Time: {data['Time']}  |  Space: {data['Space']}"
		comp_surface = stats_font.render(comp_text, 1, (180, 180, 180)) # Light Grey
		draw_info.window.blit(comp_surface, (draw_info.width/2 - comp_surface.get_width()/2 , 85))

	# Live Metrics (Comparisons, Swaps)
	# Comparisons: Orange, Swaps: Yellow
	metrics_text = f"Comparisons: {stats['comps']}   |   Swaps: {stats['swaps']}"
	metrics_surface = stats_font.render(metrics_text, 1, (255, 165, 0)) # Orange
	draw_info.window.blit(metrics_surface, (draw_info.width/2 - metrics_surface.get_width()/2 , 115))

	# --- Visualization ---
	draw_list(draw_info, color_positions)

	# --- Footer (Instructions) ---
	y_base = draw_info.height - 100
	
	controls1 = controls_font.render("R - Reset | SPACE - Start | Arrows - Speed/Size", 1, draw_info.FONT_COLOR)
	draw_info.window.blit(controls1, (draw_info.width/2 - controls1.get_width()/2 , y_base))

	controls2 = controls_font.render("1-Bubble | 2-Select | 3-Insert | 4-Merge | 5-Quick | 6-Heap | 7-Count", 1, draw_info.FONT_COLOR)
	draw_info.window.blit(controls2, (draw_info.width/2 - controls2.get_width()/2 , y_base + 30))

	pygame.display.update()

def draw_list(draw_info, color_positions={}, clear_bg=False):
	"""
	Renders the list of values as vertical bars.

	Args:
		draw_info (DrawInformation): State object.
		color_positions (dict): Specific coloring for active bars {index: color}.
		clear_bg (bool): Whether to clear the background (used for partial updates).
	"""
	lst = draw_info.list

	if clear_bg:
		clear_rect = (draw_info.SIDE_PAD//2, draw_info.TOP_PAD, 
					  draw_info.width - draw_info.SIDE_PAD, 
					  draw_info.height - draw_info.TOP_PAD - draw_info.BOTTOM_PAD + 20)
		pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)

	for i, val in enumerate(lst):
		x = draw_info.start_x + i * draw_info.block_width
		bar_height = (val - draw_info.min_val) * draw_info.block_height + 5
		graph_bottom = draw_info.height - draw_info.BOTTOM_PAD
		y = graph_bottom - bar_height

		color = draw_info.GRADIENTS[i % 3]

		if i in color_positions:
			color = color_positions[i] 

		# Draw Bar
		pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, bar_height))
		
		# Optional: Subtle Outline for 'Modern' feel (if bar width allows)
		if draw_info.block_width > 4:
			# Dark outline to separate bars visually
			pygame.draw.rect(draw_info.window, (20, 20, 30), (x, y, draw_info.block_width, bar_height), 1)

	if clear_bg:
		pygame.display.update()
