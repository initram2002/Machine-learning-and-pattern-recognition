import numpy as np

def load_spot_file(path: str):
	"""Read N and a list of (row, col) integer pairs from text file."""
	with open(path, 'r') as f:
		# Read the first line separately to get N
		N = int(f.readline().strip())
		# Read the rest of the file for coordinates
		coords = np.loadtxt(f, dtype=int)
	return N, coords
	
# 5 x 5 kernel (centre at index [2,2])
KERNEL = np.array([[0.2, 0.2, 0.2, 0.2, 0.2],
				   [0.2, 0.5, 0.5, 0.5, 0.2],
				   [0.2, 0.5, 1.0, 0.5, 0.2],
				   [0.2, 0.5, 0.5, 0.5, 0.2],
				   [0.2, 0.2, 0.2, 0.2, 0.2]], dtype=float)
									 
def light_map(N, spots):
	room = np.zeros((N, N), dtype=float)
	
	for r, c in spots:
		# boundaries of the full 5x5 kernel centred at (r,c)
		r0, r1 = r - 2, r + 3 # Python slices are half-open
		c0, c1 = c - 2, c + 3
		
		# clip to room borders
		rs, re = max(r0, 0), min(r1, N)
		cs, ce = max(c0, 0), min(c1, N)
		
		# corresponding indices inside the kernel
		ks = rs - r0
		ke = re - r0
		ls = cs - c0
		le = ce - c0
		
		room[rs:re, cs:ce] += KERNEL[ks:ke, ls:le]
		
	return room
	
def print_map(M):
	"""Pretty-print with one decimal digit"""
	for row in M:
		print(" ".join(f"{v:0.1f}" for v in row))
		
# Example
N, coords = load_spot_file("spotlights.txt")
print_map(light_map(N, coords))
