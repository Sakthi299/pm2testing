# python script
import sys
import os
import subprocess

urls = input("Enter URL for GitRepo")
lists = urls.split('/',4)
space = lists[4].split('.')
print(space[0])

subprocess.call('git init', shell=True)
subprocess.call('git remote add origin %s' %urls,shell=True)
subprocess.call('git fetch',shell=True)
subprocess.call('git remote set-head origin -a',shell=True)
subprocess.call('git rev-list origin/HEAD --count',shell=True)


