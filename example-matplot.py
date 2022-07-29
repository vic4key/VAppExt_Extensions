import sys, os
import VExt

__name__    = "Example Matplot"
__version__ = "1.x"
__author__  = "Vic P."
__summary__ = "The summary of the extension"
__url__     = "https://github.com/vic4key/VAppExt.git"

def matplot_20(): # https://matplotlib.org/3.5.0/gallery/statistics/histogram_multihist.html#sphx-glr-gallery-statistics-histogram-multihist-py
  import numpy as np
  import matplotlib.pyplot as plt

  np.random.seed(19680801)

  n_bins = 10
  x = np.random.randn(1000, 3)

  fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(nrows=2, ncols=2)

  colors = ['red', 'tan', 'lime']
  ax0.hist(x, n_bins, density=True, histtype='bar', color=colors, label=colors)
  ax0.legend(prop={'size': 10})
  ax0.set_title('bars with legend')

  ax1.hist(x, n_bins, density=True, histtype='bar', stacked=True)
  ax1.set_title('stacked bar')

  ax2.hist(x, n_bins, histtype='step', stacked=True, fill=False)
  ax2.set_title('stack step (unfilled)')

  # Make a multiple-histogram of data-sets with different length.
  x_multi = [np.random.randn(n) for n in [10000, 5000, 2000]]
  ax3.hist(x_multi, n_bins, histtype='bar')
  ax3.set_title('different sample sizes')

  fig.tight_layout()
  plt.show()

  return

def matplot_21(): # https://matplotlib.org/3.5.0/gallery/animation/random_walk.html#sphx-glr-gallery-animation-random-walk-py
  import numpy as np
  import matplotlib.pyplot as plt
  import matplotlib.animation as animation

  # Fixing random state for reproducibility
  np.random.seed(19680801)

  def random_walk(num_steps, max_step=0.05):
    """Return a 3D random walk as (num_steps, 3) array."""
    start_pos = np.random.random(3)
    steps = np.random.uniform(-max_step, max_step, size=(num_steps, 3))
    walk = start_pos + np.cumsum(steps, axis=0)
    return walk

  def update_lines(num, walks, lines):
    for line, walk in zip(lines, walks):
      # NOTE: there is no .set_data() for 3 dim data...
      line.set_data(walk[:num, :2].T)
      line.set_3d_properties(walk[:num, 2])
    return lines

  # Data: 40 random walks as (num_steps, 3) arrays
  num_steps = 30
  walks = [random_walk(num_steps) for index in range(40)]

  # Attaching 3D axis to the figure
  fig = plt.figure()
  ax = fig.add_subplot(projection="3d")

  # Create lines initially without data
  lines = [ax.plot([], [], [])[0] for _ in walks]

  # Setting the axes properties
  ax.set(xlim3d=(0, 1), xlabel='X')
  ax.set(ylim3d=(0, 1), ylabel='Y')
  ax.set(zlim3d=(0, 1), zlabel='Z')

  # Creating the Animation object
  ani = animation.FuncAnimation(fig, update_lines, num_steps, fargs=(walks, lines), interval=100)

  plt.show()

  return

def matplot_22(): # https://matplotlib.org/3.5.0/gallery/widgets/range_slider.html#sphx-glr-gallery-widgets-range-slider-py
  import numpy as np
  import matplotlib.pyplot as plt
  from matplotlib.widgets import RangeSlider

  # generate a fake image
  np.random.seed(19680801)
  N = 128
  img = np.random.randn(N, N)

  fig, axs = plt.subplots(1, 2, figsize=(10, 5))
  plt.subplots_adjust(bottom=0.25)

  im = axs[0].imshow(img)
  axs[1].hist(img.flatten(), bins='auto')
  axs[1].set_title('Histogram of pixel intensities')

  # Create the RangeSlider
  slider_ax = plt.axes([0.20, 0.1, 0.60, 0.03])
  slider = RangeSlider(slider_ax, "Threshold", img.min(), img.max())

  # Create the Vertical lines on the histogram
  lower_limit_line = axs[1].axvline(slider.val[0], color='k')
  upper_limit_line = axs[1].axvline(slider.val[1], color='k')

  def update(val):
    # The val passed to a callback by the RangeSlider will
    # be a tuple of (min, max)

    # Update the image's colormap
    im.norm.vmin = val[0]
    im.norm.vmax = val[1]

    # Update the position of the vertical lines
    lower_limit_line.set_xdata([val[0], val[0]])
    upper_limit_line.set_xdata([val[1], val[1]])

    # Redraw the figure to ensure it updates
    fig.canvas.draw_idle()

  slider.on_changed(update)
  plt.show()

  return

def VExt_Load():
  return

def VExt_Unload():
  return

class Window(VExt.UI.Window):
  def __init__(self):
    super().__init__()
    return

  def on_menu_define(self):
    result = super().on_menu_define()
    result = [
      {
        "caption": "Display UI",
        "index": 1,
        "children": [
          {
            "caption": "Statistics Subplots",
            "index": 20,
            "children": [],
          },
          {
            "caption": "Animated 3D Random Walk",
            "index": 21,
            "children": [],
          },
          {
            "caption": "Image Thresholding",
            "index": 22,
            "children": [],
          },
        ],
      },
      {
        "caption": "Information",
        "index": 2,
        "children": [],
      },
    ]
    return result

  def on_menu_execute(self, idx, lp):
    super().on_menu_execute(idx, lp)
    if idx == 20: matplot_20()
    if idx == 21: matplot_21()
    if idx == 22: matplot_22()
    elif idx == 2: VExt.API.message_box(f"{__name__} {__version__}\n\nCopyright (c) {__author__}", f"Information")
    return

  def on_menu_update(self, idx, lp):
    result = super().on_menu_update(idx, lp)
    result = (True, False)
    return result
