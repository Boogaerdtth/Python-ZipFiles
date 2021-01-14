__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os
from pathlib import Path
from zipfile import ZipFile

main_dir = Path(os.getcwd())
cache_dir = Path("cache")

#1
def clean_cache():
  try:
    os.mkdir(cache_dir)
  except FileExistsError:
    file_list = os.listdir(cache_dir)
    for file in file_list:
      try:
        os.remove(cache_dir / file)
      except FileNotFoundError:
        print('There has been a error')


#2
def cache_zip(x, cache_dir):
  try:
    with ZipFile(x, 'r') as zip:
      zip.extractall(cache_dir)
  except FileNotFoundError:
    print('error')

#3
def cached_files():
  content = os.scandir(cache_dir)
  files = []
  for file in content:
    if os.path.isfile(cache_dir / file.name):
      files.append(str(main_dir / cache_dir / Path(file.name)))
  return files

#4
def find_password(files):
  for file in files:
    for item in open(file).readlines():
      if 'password' in item:
        print(item.split()[1])
  return 'nothing found'


if __name__ == '__main__':
  clean_cache()
  cache_zip('data.zip', 'cache')
  files = cached_files()
  find_password(files)
  clean_cache()
