__author__ = 'wyb'
# -*- coding:utf-8 -*-
# -------------------------------------------
'''
批量生成md5值
'''
# -------------------------------------------
import os
import sys
import time


def remove_old_md5sum():
    for r, d, f in os.walk(input_path):
        for f_ in f:
            if f_.endswith('.txt'):
                os.remove(os.path.join(r, f_))


def create_new_md5sum():
    for r, d, f in os.walk(input_path):
        for f_ in f:
            val = os.popen('md5sum %s' % (os.path.join(r, f_))).read()
            md5sum = val.split(' ')[0]
            output_md5sum = md5sum + ' ' + f_
            with open('/home/wyb/data/test/%s/md5sum.txt' % os.path.split(os.path.split(os.path.join(r, f_))[0])[1], 'a+'
            ) as f_txt:
                f_txt.write(output_md5sum + '\n')


if __name__ == '__main__':
    start = time.time()
    if len(sys.argv) is not 2:
        print 'Usage:'
        print 'python create_md5sum.py input_path'
    input_path = sys.argv[1]
    remove_old_md5sum()
    create_new_md5sum()
    end = time.time()
    print 'Time consuming is %s seconds!' % (end-start)
    print 'Task finished!'


