import json
import VExt

__name__    = "Sample Python"
__version__ = "1.2"
__author__  = "Vic P."
__summary__ = "The summary of the extension"
__url__     = "https://github.com/vic4key/VAppExt.git"

def VExt_Load():
  return

def VExt_Unload():
  return

class Window(VExt.UI.Window):
  def __init__(self):
    super().__init__()
    return

  def on_new(self):
    return

  def on_open(self, file_path):
    lines = []
    return lines

  def on_menu_define(self):
    result = [
      {
        "caption": "Menu 1.0",
        "index": 10,
        "children": [],
      },
      {
        "caption": "Menu 1.1",
        "index": 11,
        "children": [
          {
            "caption": "Sub Menu 2.0",
            "index": 20,
            "children": [],
          },
          {
            "caption": "Sub Menu 2.1",
            "index": 21,
            "children": [],
          },
          {
            "caption": "Sub Menu 2.2",
            "index": 22,
            "children": [],
          },
        ],
      },
      {
        "caption": "Information",
        "index": 12,
        "children": [],
      },
    ]
    return result

  def on_menu_execute(self, idx, lp):
    if idx == 12: VExt.API.message_box(f"{__name__} {__version__}\n\nCopyright (c) {__author__}", f"Information")
    else: VExt.API.message_box(f"idx = {idx:d}, lp = 0x{lp:08x}", f"{__name__}")
    return

  def on_menu_update(self, idx, lp):
    result = (idx % 2 == 0, idx % 2 == 0)
    return result

  def on_message(self, msg):
    VExt.API.log(json.dumps(msg), VExt.logging_level_t.info)
    return
