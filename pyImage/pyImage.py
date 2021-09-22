#!/usr/bin/env python3
import os
from PIL import Image

cwd = os.getcwd()
path = cwd + '/images/'
# new_path = cwd + '/opt/icons/'
new_path = path

if not os.path.exists(new_path):
    os.makedirs(new_path)

for file in os.listdir(path):
    if not file.startswith('.'):
        im = Image.open(path + file)
        im.convert('RGB').rotate(90).resize(
            (128, 128)).save(new_path + file, 'JPEG')
        im.close()

# #!/usr/bin/env python3
# from multiprocessing import Pool
# import os
# from PIL import Image

# dr = "/opt/icons/"
# if not os.path.exists(dr):
#     os.mkdir(dr)

# tasks = [i for i in os.walk(".")]
# tasks = tasks[0][2] # Try printing output of os.walk to understand

# def run(task):
#     try:
#         if not task.endswith(".jpeg"): return None
#         im = Image.open(task)
#         im = im.rotate(270).resize((128,128)).convert("RGB")
#         im.save(dr + task, "jpeg")
#     except OSError as e:
#         print(task, e)

# p = Pool(len(tasks))
# p.map(run, tasks)
