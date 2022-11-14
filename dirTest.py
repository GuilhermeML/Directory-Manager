import os

#path must have regular slashes
path = ''

f = open("out.txt", "a", encoding="utf-8")

def dirHandling(path):
    path_list = os.listdir(path)
    
    for each in path_list:
        path_item = path + "/" + each

        #verify if item in directory is a diretory
        if(os.path.isdir(path_item)):
            f.write(f'\n{each} é um diretório.\n')
            f.write(path_item + '\n')

            #verify if directory has itens
            if (bool(os.listdir(path_item))):
                dirHandling(path_item)
            else:
                f.write(f'O diretório {each} está vazio.\n\n')
        else:
            f.write(f'-{each}\n')

dirHandling(path)