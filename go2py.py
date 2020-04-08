import os
import template
import utils
import sys


output = []

if len(sys.argv) != 2:
    print('No input src file.')
    sys.exit()

src_path = sys.argv[1]
src_home, src_name = os.path.split(sys.argv[1])

with open(src_path) as f:
    for line in f:
        output.append(line)

for k,line in enumerate(output):
    if 'package' in line:
        output.insert(k+1 , 'import "C"\n')
        break

go_out = open('lib%s'%src_name,'wb+')

src_pre = src_name.split('.')[0]
py_out = open('%s.py'%src_pre,'wb+')
py_out.write('''import ctypes\ncdll=ctypes.CDLL("./lib%s.so")\n'''%src_pre.encode())
for line in output:
    func = utils.find_func(line)
    if func:
       code = template.FuncTemplate(name = func['name'],args_type = func['args_type'], res_type = func['res_type'])
       go_out.write(code['go'])
       py_out.write(code['py'])
    go_out.write(line) 
go_out.close()
py_out.close()
os.system('''go build -buildmode=c-shared -o lib%s.so lib%s'''%(src_pre, src_name))

