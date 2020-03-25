
go_arg_dic = {'string':'*C.char', 'int':'int'}
go_ret_dic = {'string':'C.CString', 'int':'int'}
py_arg_dic = {'string':'*C.char', 'int':'int'}
py_ret_dic = {'string':'ctypes.c_char_p', 'int':''}
def FuncTemplate(**kwargs):
    name = kwargs['name']
    args_type = kwargs['args_type']
    res_type = kwargs['res_type']
    args = ','.join(map(lambda x,k:'arg%s '%k+x,args_type,range(len(args_type))))
    go_args = ','.join(map(lambda x,k:'arg%s'%k,args_type,range(len(args_type))))
    return  {'go':'''//export _%s\nfunc _%s(%s) (%s){return %s(%s(%s))}\n\n'''%(name,name,args, go_arg_dic[res_type],go_ret_dic[res_type],name, go_args),'py':'''_{n}=cdll._{n}\n_{n}.restype = {res_type}\ndef {n}({a}):\n    return _{n}({a})\n'''.format(n=name,res_type = py_ret_dic[res_type],a=go_args)}


