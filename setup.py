from distutils.core import setup
import os
from pathlib import Path
from shutil import copyfile
from time import sleep
from random import randrange
import sqlite3
import re
import glob


setup(zipfile=None,
      options={'pyexe': {"bundle_files": 1}},
      console=["hackerscript.py"])
