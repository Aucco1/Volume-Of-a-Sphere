import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
from mpmath import mp
import textwrap

def get_volume_str(radius, precision):
    mp.dps = precision + 10
    vol = mp.pi * (radius**3) * 4/3
    return str(vol)[:precision + 4]

RADIUS = 5
MAX_PRECISION = 100
TOTAL_FRAMES = 150

full_number_str = get_volume_str(RADIUS, MAX_PRECISION)

plt.style.use('dark_background')
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_axis_off()

surf = None

title_text = fig.text(0.5, 0.90, f"Volume of Sphere (r={RADIUS})", 
                      ha='center', fontsize=16, color='white', weight='bold')



dpi_text = fig.text(0.5, 0.86, "", ha='center', fontsize=12, 
                    color='#ff00ff', weight='bold')

vol_text = fig.text(0.5, 0.05, "", ha='center', va='bottom', fontsize=10, 
                    color='#00ffcc', fontfamily='monospace')

def generate_sphere(radius, resolution):
    res = max(4, int(resolution))
    u = np.linspace(0, 2 * np.pi, res)
    v = np.linspace(0, np.pi, res)
    x = radius * np.outer(np.cos(u), np.sin(v))
    y = radius * np.outer(np.sin(u), np.sin(v))
    z = radius * np.outer(np.ones(np.size(u)), np.cos(v))
    return x, y, z

def update(frame):
    global surf
    
    progress = frame / (TOTAL_FRAMES - 1)
    current_resolution = 4 + (progress * 56)
    
    x, y, z = generate_sphere(RADIUS, current_resolution)
    
    if surf:
        surf.remove()
        
    surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='viridis', 
                           alpha=0.6, linewidth=0.5, edgecolors='#333333')
    
    ax.view_init(elev=20, azim=frame * (360/TOTAL_FRAMES))
    
    chars_to_show = int(progress * len(full_number_str))
    if chars_to_show < 4: chars_to_show = 4

    current_string = full_number_str[:chars_to_show]
    decimal_count = max(0, len(current_string) - 4)
    
    wrapped_string = textwrap.fill(f"V = {current_string}", width=60)
    
    vol_text.set_text(wrapped_string)
    dpi_text.set_text(f"Decimal Place: {decimal_count}")
    
    return surf, vol_text, dpi_text

anim = FuncAnimation(fig, update, frames=TOTAL_FRAMES, interval=50, blit=False)
plt.show()