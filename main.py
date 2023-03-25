 
from pathlib import Path
import shutil
import re

class Pasta:

    teste = Path.home() / 'Downloads'  

    def __init__(self) -> None:
        self.path = Pasta.teste      
        self.path_tratado = self.tratamento_paste(self.path.glob('*'))
      
      
    def tratamento_paste(self, files):
        
        sets_file = files
        sets = set({})
        
        for file in sets_file:
                        
            pastas = Path(file).suffix
            pastas = re.sub(r'.jpg|.png|.gif|.bmp', '.imagem', pastas)
            pastas = re.sub(r'.7z|.zip|.rar', '.ArquivoZipado', pastas).replace('.', '/_')
            
            if pastas != '':
                pastas_tratada = str(self.path) + str(pastas)
                sets.add(pastas_tratada)        
        return sets  
                  
        
    def constructor_path(self):
        paste_no_repeate = self.path_tratado
        for pastas in paste_no_repeate:
            pasta = Path(pastas)
            pasta.mkdir(parents=True, exist_ok=True) 
         
    def mover_arquivos(self):
        sets_file = self.path.glob('*')
        for file in sets_file:
            
            if Path(file).is_file() == True:
                for arquivo in self.tratamento_paste([file]):
                    format = arquivo + f'/{file.name}'
                    t = Path(format)
                    if t.exists() == True:
                        file = file.rename(self.path / f'{file.name[0:-len(file.suffix)]}_copy{file.suffix}')
                    shutil.move(file, arquivo)
                    
                    
        return 'arquivos ajustados'
        
        
        
        
p = Pasta()
print(p.mover_arquivos())

