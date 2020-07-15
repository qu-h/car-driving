'''
https://upload.wikimedia.org/wikipedia/commons/5/5b/Vietnam_road_sign_P101.svg
https://upload.wikimedia.org/wikipedia/commons/f/f3/Vietnam_road_sign_P102.svg
https://upload.wikimedia.org/wikipedia/commons/9/9c/Vietnam_road_sign_P103a.svg
'''
import os


def rename():
  sign_dir = f'sa-hinh'
  for root, _, files in os.walk(sign_dir):
    for f in files:
      if '_Cau' in f:
        f_new = f.replace('450-cau-hoi-sat-hach-lai-xe_Cau','').lower()
        os.rename( f'{root}/{f}',f'{root}/{f_new}')


if __name__ == "__main__":
    rename()