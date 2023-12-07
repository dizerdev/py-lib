import requests

# Usando request get e escrevendo arquivo png
url_logo_impacta = (
 'https://www.impacta.edu.br/themes/wc_agenciar3/images/logo-new.png'
)

response = requests.get(url_logo_impacta)

with open('logo-impacta.png', 'wb') as f:
    f.write(response.content)
