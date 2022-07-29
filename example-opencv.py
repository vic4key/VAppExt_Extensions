import sys, os
import VExt

__name__    = "Example OpenCV"
__version__ = "1.x"
__author__  = "Vic P."
__summary__ = "The summary of the extension"
__url__     = "https://github.com/vic4key/VAppExt.git"

def main():
  import cv2
  import numpy as np
  import matplotlib.pyplot as plt

  identity = np.array((
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]))

  edge = np.array((
    [0,  1,  0],
    [1, -4,  1],
    [0,  1,  0]))

  boxblur = (1.0 / 9) * np.array(
    [[1, 1, 1],
     [1, 1, 1],
     [1, 1, 1]])

  gaussian = (1.0 / 16) * np.array(
    [[1, 2, 1],
     [2, 4, 2],
     [1, 2, 1]])

  emboss = np.array(
    [[-2, -1,  0],
     [-1,  1,  1],
     [ 0,  1,  2]])

  square = np.array(
    [[ 0,  2,  0],
     [-2, -1,  2],
     [ 0, -2,  0]])

  small_blur = np.ones((7, 7), dtype="float") * (1.0 / (7 * 7))
  large_blur = np.ones((21, 21), dtype="float") * (1.0 / (21 * 21))

  sharpen = np.array((
    [0, -2, 0],
    [-2, 10, -2],
    [0, -2, 0]))

  laplacian = (1.0 / 16) * np.array(
    [[ 0,  0, -1,  0,  0],
     [ 0, -1, -2, -1,  0],
     [-1, -2, 16, -2, -1],
     [ 0, -1, -2, -1,  0],
     [ 0,  0, -1,  0,  0]])

  sobel_left = np.array((
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]))

  sobel_right = np.array((
    [1, 0, -1],
    [2, 0, -2],
    [1, 0, -1]))

  sobel_top = np.array((
    [-1, -2, -1],
    [ 0,  0,  0],
    [ 1,  2,  1]))

  sobel_bottom = np.array((
    [ 1,  2,  1],
    [ 0,  0,  0],
    [-1, -2, -1]))

  filters = [
    ("Identity", identity),
    ("Edge", edge),
    ("Box Blur", boxblur),
    ("Square", square),
    ("Gaussian", gaussian),
    ("Emboss", emboss),
    ("Small blur", small_blur),
    ("Large blur", large_blur),
    ("Sharpen", sharpen),
    ("Laplacian", laplacian),
    ('Sobel Left', sobel_left),
    ('Sobel Right', sobel_right),
    ('Sobel Top', sobel_top),
    ('Sobel Bottom', sobel_bottom)
  ]

  image_gray = cv2.imread('Samples/cat.jpg', cv2.IMREAD_GRAYSCALE)

  fig = plt.figure(figsize=(12, 8))
  fig.subplots_adjust(hspace=0.3, wspace=0.1)

  for i, filter in enumerate(filters):
    axes = fig.add_subplot(3, 5, i+1)
    axes.set(title=filter[0])
    axes.grid(False)
    axes.set_xticks([])
    axes.set_yticks([])
    image_gray_viz = cv2.filter2D(image_gray, -1, filter[1])
    axes.imshow(image_gray_viz, cmap='gray', vmin=0, vmax=255)

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
        "children": [],
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
    if idx == 1: main()
    elif idx == 2: VExt.API.message_box(f"{__name__} {__version__}\n\nCopyright (c) {__author__}", f"Information")
    return

  def on_menu_update(self, idx, lp):
    result = super().on_menu_update(idx, lp)
    result = (True, False)
    return result
