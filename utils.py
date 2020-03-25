import re

def find_func(line):
    m = re.match(r"func\s+(?P<name>\w+)\s*[(](?P<args_type>.+)[)]\s*(?P<res_type>\w+)\s*", line)
    if m:
        res = m.groupdict()
        res['args_type'] = map(lambda x:x.split()[-1],res['args_type'].split(','))
        return res
    return None
