import os, platform
os.system('xdg-open https://facebook.com/groups/3017062245271082/')
os.system('git pull')
bit = platform.architecture()[0]
if bit == '64bit':
    import kmk
elif bit == '32bit':
    import mkm
