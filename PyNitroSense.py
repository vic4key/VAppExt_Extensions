import os, sys, clr
import VExt

__name__    = "Nitro Sense"
__version__ = "1.0"
__author__  = "Vic P."
__summary__ = "The summary of the extension"
__url__     = "https://github.com/vic4key/VAppExt.git"

def VExt_Load():
  try:
    NS_DIR = R"C:\VAppExt\Extensions\NitroSense_DLL"
    sys.path.append(NS_DIR)
    clr.AddReference("NitroSense")
    sys.path.append(os.path.join(NS_DIR, "NitroSense.dll"))
  except Exception as e:
    print(repr(e))
  return

def VExt_Unload():
  return

class Window(VExt.UI.Window):
  def __init__(self):
    super().__init__()
    return

  def on_menu_define(self):
    result = [
      {
        "caption": "Fix Fan Noise",
        "index": 10,
        "children": [],
      },
      {
        "caption": "Information",
        "index": 12,
        "children": [],
      },
    ]
    return result

  def on_menu_update(self, idx, lp):
    result = (True, False)
    return result

  def on_menu_execute(self, idx, lp):
    if idx == 10:
      try:
        from NitroSense import NitroSense
        NitroSense.fix_fan_noise_caused_by_high_fan_speed(fan_speed_noise_rpm=3000, debug=False)
      except Exception as e:
        print(repr(e))
    elif idx == 12:
      VExt.API.message_box(f"{__name__} {__version__}\n\nCopyright (c) {__author__}", f"Information")
    else:
      VExt.API.message_box(f"idx = {idx:d}, lp = 0x{lp:08x}", f"{__name__}")
    return
