from imagem.ajustes.brilho import ajustar_brilho
from imagem.efeitos.foto.vinheta import aplicar
from imagem.formatos.jpg import carregar
from imagem.formatos.png import salvar
from imagem.tela.redimensionar import pixels
from imagem.efeitos.foto import vinheta
from imagem.formatos import jpg, png
from imagem.tela.redimensionar import pixels


arquivo = input('Digite o nome do arquivo jpg: ')


dados = carregar(arquivo)
dados = pixels(dados, 600, 400)
dados = ajustar_brilho(dados, 0.7)
dados = aplicar(dados, 0.8, '0032af')


nome = input('Salvar como png: ')
salvar(dados, f'{nome}.png')


arquivo = input('Digite o nome do arquivo jpg: ')


dados = jpg.carregar(arquivo)
dados = pixels(dados, 600, 400)
dados = ajustar_brilho(dados, 0.7)
dados = vinheta.aplicar(dados, 0.8, '0032af')


nome = input('Salvar como png: ')
png.salvar(dados, f'{nome}.png')
