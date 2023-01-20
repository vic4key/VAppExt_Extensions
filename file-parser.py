import sys, os
import VExt
import exif
import yaml
import LnkParse3
import pydicom as dcm
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata

__name__    = "File Parser"
__version__ = "1.x"
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
    try:
      # https://hachoir.readthedocs.io/
      # hachoir-metadata --parser-list
      hachoir_parser_list = [
        # [archive]
        ".bzip2", ".cab", ".gzip", ".mar", ".tar", ".zip",
        # [audio]
        ".aiff", ".flac", ".mpeg_audio", ".real_audio", ".sun_next_snd",
        # [container]
        ".matroska", ".ogg", ".real_media", ".riff", ".swf",
        # [file_system]
        ".iso9660",
        # [image]
        ".bmp", ".cr2", ".gif", ".ico", ".jpeg", ".pcx", ".png", ".psd", ".targa", ".tiff", ".wmf", ".xcf",
        # [misc]
        ".ole2", ".pcf", ".torrent", ".ttf",
        # [program]
        ".exe",
        # [video]
        ".asf", ".flv", ".mov"
      ]

      lines = []

      file_ext = os.path.splitext(file_path)[1].lower()
      
      if file_ext in [".txt", ".log", ".ini", ".md"]:
        with open(file_path, "rt") as f: lines = f.read().splitlines()

      elif file_ext in [".jpg"]:
        with open(file_path, "rb") as file:
          img = exif.Image(file)
          if img.has_exif:
            lines = [f"{tag}: <{img.get(tag)}>"\
              for tag in dir(img) if not tag.startswith(("_", "get", "has"))]

      elif file_ext in [".dcm"]:
        ds = dcm.read_file(file_path)
        lines.extend([str(e) for e in ds.file_meta])
        lines.extend([str(e) for e in ds.formatted_lines()])

      elif file_ext in [".lnk"]:
        with open(file_path, "rb") as f:
          lnk = LnkParse3.lnk_file(f)
          j = lnk.get_json(get_all=True)
          s = yaml.dump(j, sort_keys=False)
          lines = s.split("\n")

      elif file_ext in hachoir_parser_list:
        parser = createParser(file_path)
        meta_data = extractMetadata(parser)
        lines = meta_data.exportPlaintext()

      else: VExt.API.log(f"Unsupported parsing file format {file_ext}", VExt.logging_level_t.error)

    except Exception as e:
      VExt.API.log(f"Error parsing file format {file_ext}", VExt.logging_level_t.error)

    return lines

  def on_menu_define(self):
    result = [
      {
        "caption": "Hello World",
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
    if idx == 1: VExt.API.message_box("I am written in Python", "Hello World")
    if idx == 2: VExt.API.message_box(f"{__name__} {__version__}\n\nCopyright (c) {__author__}", f"Information")
    return

  def on_menu_update(self, idx, lp):
    result = (True, False)
    return result
