import VExt

__name__    = "Example PySide6 - OneDark"
__version__ = "1.x"
__author__  = "Vic P."
__summary__ = "The summary of the extension"
__url__     = "https://github.com/vic4key/VAppExt.git"

def main():
  VExt.run_extension_wrapper("example-pyside-onedark", "main")
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
