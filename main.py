from pathlib import Path
import shutil
import re


class Pasta:

    teste = Path.home() / 'Downloads'

    def __init__(self) -> None:
        self.path = Pasta.teste
        self.path_tratado = self.tratamento_paste(self.path.glob('*'))

    def tratamento_paste(self, files):
        """
        análisa os arquivos da pasta Download e retorna um caminho de arquivo tratado como pasta
        Ex: c:/user/Downloads/teste.txt retorna c:/user/Downloads/_txt 
        """
        sets_file = files
        sets = set({})

        for file in sets_file:

            pastas = Path(file).suffix
            pastas = re.sub(r'.jpg|.png|.gif|.bmp', '.imagem', pastas)
            pastas = re.sub(r'.7z|.zip|.rar', '.ArquivoZipado',
                            pastas).replace('.', '/_')

            if pastas != '':
                pastas_tratada = str(self.path) + str(pastas)
                sets.add(pastas_tratada)
        return sets

    def constructor_path(self):
        """
        Recebe valor das pastas tratadas já e as cria atráves do mkadir 
        """
        paste_no_repeate = self.path_tratado
        for pastas in paste_no_repeate:
            pasta = Path(pastas)
            pasta.mkdir(parents=True, exist_ok=True)

    def mover_arquivos(self):
        """
        pega os arquivos da pasta Download e os encaminha para a respectiva pasta que é pega pela função de tratamento da Path
        se o arquivo já exisitir ele renomeia com um _copy, terá tratamentos futuros melhores 
        """
        sets_file = self.path.glob('*')
        for file in sets_file:

            if Path(file).is_file() == True:
                for arquivo in self.tratamento_paste([file]):
                    format = arquivo + f'/{file.name}'
                    pasta = Path(format)
                    if Path(arquivo).exists() == True:
                        if pasta.exists() == True:
                            file = file.rename(
                                self.path / f'{file.name[0:-len(file.suffix)]}_copy{file.suffix}')
                    else:
                        self.constructor_path()
                    shutil.move(file, arquivo)

        return 'arquivos ajustados'


p = Pasta()
print(p.mover_arquivos())
