import os

inputFolder = 'input'
modelsNames = os.listdir(inputFolder)
for m in modelsNames:
    p = inputFolder+'/'+m
    print(p)
    rs = os.system(f'python extract_mview.py {p}')
    if rs ==0 :
        folderName = m.split('.')[0]
        np = inputFolder+f'/{folderName}'
        os.system(f'python extract_model.py {np}')

print('....Done....')