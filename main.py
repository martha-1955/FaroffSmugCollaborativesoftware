import os
for i in range(366):
    d = str(i)+' days ago'
    with open('hack.txt','a') as file:
        file.write(d+'\n')
        os.system('git add hack.txt')
        os.system('git commit --date="'+d+'" -m fast hack')

os.system('git push -u origin master')        