import imagem.ajustes.brilho
import imagem.efeitos.foto.vinheta
import imagem.formatos.jpg
import imagem.formatos.png
import imagem.tela.redimensionar


arquivo = input('Digite o nome do arquivo jpg: ')


dados = imagem.formatos.jpg.carregar(arquivo)
dados = imagem.tela.redimensionar.pixels(dados, 600, 400)
dados = imagem.ajustes.brilho.ajustar_brilho(dados, 0.7)
dados = imagem.efeitos.foto.vinheta.aplicar(dados, 0.8, '0032af')


nome = input('Salvar como png: ')
imagem.formatos.png.salvar(dados, f'{nome}.png')

##

arquivo = input('Digite o nome do arquivo jpg: ')


dados = imagem.formatos.jpg.carregar(arquivo)
dados = imagem.tela.redimensionar.pixels(dados, 600, 400)
dados = imagem.ajustes.brilho.ajustar_brilho(dados, 0.7)
dados = imagem.efeitos.foto.vinheta.aplicar(dados, 0.8, '0032af')


nome = input('Salvar como png: ')
imagem.formatos.png.salvar(dados, f'{nome}.png')


##