import os, json, subprocess
from datetime import datetime
import VExt

__name__    = "Daily Backup Environment Variables"
__version__ = "1.0"
__author__  = "Vic P."
__summary__ = "The summary of the extension"
__url__     = "https://github.com/vic4key/VAppExt.git"

def reg_backup(suffix_file_name, reg_key):
  dir = os.path.join(VExt.API.extensions_dir(), "backup-environment-variables")
  if not os.path.exists(dir): os.mkdir(dir) # make sure the backup folder exists
  time = datetime.now().strftime("%Y%d%m_%H%M%S") # eg. 20220730_1234
  subprocess.call(
    f"regedit /e \"{dir}\\{time}_{suffix_file_name}.reg\" \"{reg_key}\"", creationflags=subprocess.CREATE_NO_WINDOW)
  return

def backup_environment_variables():
  try:
    reg_backup("usr", R"HKEY_CURRENT_USER\Environment")
    reg_backup("sys", R"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment")
  except Exception as e:
    print(e)
  return

def VExt_Load():
  backup_environment_variables()
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
        "caption": "Backup Now",
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
    if idx == 1:
      backup_environment_variables()
      print("Environment Variables Backup Succeed")
    elif idx == 2: VExt.API.message_box(f"{__name__} {__version__}\n\nCopyright (c) {__author__}", f"Information")
    return

  def on_menu_update(self, idx, lp):
    result = (True, False)
    return result
