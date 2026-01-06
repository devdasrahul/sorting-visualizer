"""
Sorting Algorithms Implementation

Updates:
- Generators now yield (color_dict, comps_inc, swaps_inc)
- 'comps_inc' = 1 means increment comparison counter by 1.
- 'swaps_inc' = 1 means increment swap counter by 1.
"""

def bubble_sort(draw_info, ascending=True):
	lst = draw_info.list
	for i in range(len(lst) - 1):
		for j in range(len(lst) - 1 - i):
			num1 = lst[j]
			num2 = lst[j + 1]

			# Visualize Comparison (Red)
			yield ({j: draw_info.RED, j + 1: draw_info.RED}, 1, 0) # 1 comp

			if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
				lst[j], lst[j + 1] = lst[j + 1], lst[j]
				draw_info.list = lst
				# Visualize Swap (Yellow)
				yield ({j: draw_info.YELLOW, j + 1: draw_info.YELLOW}, 0, 1) # 1 swap
	
	return lst

def insertion_sort(draw_info, ascending=True):
	lst = draw_info.list

	for i in range(1, len(lst)):
		current = lst[i]
		
		while True:
			ascending_sort = i > 0 and lst[i - 1] > current and ascending
			descending_sort = i > 0 and lst[i - 1] < current and not ascending
			
			if i > 0:
				# Comparison
				yield ({i: draw_info.RED, i - 1: draw_info.RED}, 1, 0)

			if not ascending_sort and not descending_sort:
				break

			lst[i] = lst[i - 1]
			i = i - 1
			lst[i] = current
			draw_info.list = lst
			# Swap (Shift is practically a write/swap operation in visualizer terms)
			yield ({i: draw_info.YELLOW, i + 1: draw_info.YELLOW}, 0, 1)
	
	return lst

def selection_sort(draw_info, ascending=True):
	lst = draw_info.list

	for i in range(len(lst)):
		min_idx = i
		for j in range(i+1, len(lst)):
			# Comparison
			yield ({i: draw_info.GREEN, j: draw_info.RED, min_idx: draw_info.BLUE}, 1, 0)

			if (lst[j] < lst[min_idx] and ascending) or (lst[j] > lst[min_idx] and not ascending):
				min_idx = j
				yield ({i: draw_info.GREEN, j: draw_info.BLUE, min_idx: draw_info.BLUE}, 0, 0)

		lst[i], lst[min_idx] = lst[min_idx], lst[i]
		draw_info.list = lst
		# Swap
		yield ({i: draw_info.YELLOW, min_idx: draw_info.YELLOW}, 0, 1)

	return lst

def quick_sort(draw_info, ascending=True):
	lst = draw_info.list
	yield from _quick_sort_helper(draw_info, lst, 0, len(lst) - 1, ascending)
	return lst

def _quick_sort_helper(draw_info, lst, low, high, ascending):
	if low < high:
		pi_generator = _partition(draw_info, lst, low, high, ascending)
		pi = yield from pi_generator
		yield from _quick_sort_helper(draw_info, lst, low, pi - 1, ascending)
		yield from _quick_sort_helper(draw_info, lst, pi + 1, high, ascending)

def _partition(draw_info, lst, low, high, ascending):
	pivot = lst[high]
	i = low - 1
	
	for j in range(low, high):
		# Comparison
		yield ({j: draw_info.RED, high: draw_info.BLUE, i+1: draw_info.GREEN}, 1, 0)
		
		if (lst[j] <= pivot and ascending) or (lst[j] >= pivot and not ascending):
			i += 1
			lst[i], lst[j] = lst[j], lst[i]
			draw_info.list = lst
			# Swap
			yield ({i: draw_info.YELLOW, j: draw_info.YELLOW, high: draw_info.BLUE}, 0, 1)

	lst[i + 1], lst[high] = lst[high], lst[i + 1]
	draw_info.list = lst
	# Pivot Swap
	yield ({i + 1: draw_info.YELLOW, high: draw_info.YELLOW}, 0, 1)
	
	return i + 1

def merge_sort(draw_info, ascending=True):
	lst = draw_info.list
	yield from _merge_sort_helper(draw_info, lst, 0, len(lst) - 1, ascending)
	return lst

def _merge_sort_helper(draw_info, lst, left, right, ascending):
	if left >= right:
		return

	mid = (left + right) // 2
	yield from _merge_sort_helper(draw_info, lst, left, mid, ascending)
	yield from _merge_sort_helper(draw_info, lst, mid + 1, right, ascending)
	yield from _merge(draw_info, lst, left, mid, right, ascending)

def _merge(draw_info, lst, left, mid, right, ascending):
	temp = []
	i = left
	j = mid + 1

	while i <= mid and j <= right:
		# Comparison
		yield ({i: draw_info.RED, j: draw_info.RED}, 1, 0)
		
		if (lst[i] <= lst[j] and ascending) or (lst[i] >= lst[j] and not ascending):
			temp.append(lst[i])
			i += 1
		else:
			temp.append(lst[j])
			j += 1
	
	while i <= mid:
		yield ({i: draw_info.RED}, 0, 0) # Visualizing access
		temp.append(lst[i])
		i += 1

	while j <= right:
		yield ({j: draw_info.RED}, 0, 0) # Visualizing access
		temp.append(lst[j])
		j += 1

	for idx, val in enumerate(temp):
		lst[left + idx] = val
		draw_info.list = lst
		# Write back (Write operation ~ Swap/Set)
		yield ({left + idx: draw_info.GREEN}, 0, 1) 

def heap_sort(draw_info, ascending=True):
	lst = draw_info.list
	n = len(lst)

	# Build max heap
	for i in range(n // 2 - 1, -1, -1):
		yield from _heapify(draw_info, lst, n, i, ascending)

	# Extract elements
	for i in range(n - 1, 0, -1):
		lst[i], lst[0] = lst[0], lst[i]
		draw_info.list = lst
		# Swap
		yield ({i: draw_info.GREEN, 0: draw_info.YELLOW}, 0, 1)
		
		yield from _heapify(draw_info, lst, i, 0, ascending)
	
	return lst

def _heapify(draw_info, lst, n, i, ascending):
	largest = i
	left = 2 * i + 1
	right = 2 * i + 2
	
	# Node View Comp
	yield ({i: draw_info.BLUE, left: draw_info.RED if left < n else -1, right: draw_info.RED if right < n else -1}, 0, 0)

	if ascending:
		if left < n:
			yield( {}, 1, 0) # Comp
			if lst[left] > lst[largest]:
				largest = left
		if right < n:
			yield( {}, 1, 0) # Comp
			if lst[right] > lst[largest]:
				largest = right
	else:
		if left < n:
			yield( {}, 1, 0) # Comp
			if lst[left] < lst[largest]:
				largest = left
		if right < n:
			yield( {}, 1, 0) # Comp
			if lst[right] < lst[largest]:
				largest = right

	if largest != i:
		lst[i], lst[largest] = lst[largest], lst[i]
		draw_info.list = lst
		# Swap
		yield ({i: draw_info.YELLOW, largest: draw_info.YELLOW}, 0, 1)
		yield from _heapify(draw_info, lst, n, largest, ascending)

def counting_sort(draw_info, ascending=True):
	lst = draw_info.list
	if not lst:
		return lst
		
	min_val = min(lst)
	max_val = max(lst)
	range_val = max_val - min_val + 1
	
	count = [0] * range_val
	output = [0] * len(lst)

	for i in range(len(lst)):
		yield ({i: draw_info.RED}, 0, 0) # Read
		count[lst[i] - min_val] += 1
		
	if ascending:
		for i in range(1, len(count)):
			count[i] += count[i - 1]
	else:
		for i in range(len(count)-2, -1, -1):
			count[i] += count[i+1]
			
	if ascending:
		for i in range(len(lst) - 1, -1, -1):
			val = lst[i]
			idx = count[val - min_val] - 1
			output[idx] = val
			count[val - min_val] -= 1
			yield ({i: draw_info.RED}, 0, 0) # Read
	else:
		for i in range(len(lst) - 1, -1, -1):
			val = lst[i]
			idx = count[val - min_val] - 1
			output[idx] = val
			count[val - min_val] -= 1
			yield ({i: draw_info.RED}, 0, 0)

	for i in range(len(lst)):
		lst[i] = output[i]
		draw_info.list = lst
		# Write
		yield ({i: draw_info.GREEN}, 0, 1) 
	
	return lst
