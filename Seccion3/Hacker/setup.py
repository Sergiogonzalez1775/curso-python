from distutils.core import setup
import py2exe
import os
import sqlite3
from audioop import reverse
from pathlib import Path
from time import sleep
from random import randrange
import re
import glob

#Solo funciona en windows

setup(zipfile=None,
      options={'py2exe': {"bundle_files":1}},
      windows=["HackerSciipt.py"])