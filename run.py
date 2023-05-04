
import os
import sys
import subprocess
import shutil

# Do python version check b/c we use recent stuff after
if sys.version_info.major == 3 and sys.version_info.minor <= 10:
  print('''
WARNING: This copy of python (v{major}.{minor}) may not have libraries we use, we expect python 3.11 or later.
'''.format(major=sys.version_info.major, minor=sys.version_info.minor))


import tomllib

def main(args=sys.argv):
  game_toml_file = args[1] if len(args) > 1 else 'mm-game.toml'
  
  print(f'Reading game from {game_toml_file}...')

  if not os.path.exists(game_toml_file) and os.path.exists(game_toml_file+'.example'):
    game_toml_file_example = game_toml_file+'.example'
    print(f'Did not find {game_toml_file}, but did find {game_toml_file_example}')
    print(f'Copying {game_toml_file_example} to {game_toml_file}')
    shutil.copyfile(game_toml_file_example, game_toml_file)

  if not os.path.exists(game_toml_file):
    print(f'ERROR> No game file at {game_toml_file}!')
    return

  with open(game_toml_file, 'rb') as game_toml_fd:
    game_config = tomllib.load(game_toml_fd)

  #print(f'game_config={game_config}')
  




if __name__ == '__main__':
  main()








