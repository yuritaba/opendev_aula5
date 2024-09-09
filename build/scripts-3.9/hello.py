#!python
import gettext
from dev_aberto import hello
from babel.dates import format_date
import locale

# Definindo o diretório onde os arquivos de tradução serão armazenados
gettext.bindtextdomain('cli', 'locale')
gettext.textdomain('cli')
_ = gettext.gettext  # Função para marcar strings a serem traduzidas

# Definir o locale para datas
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')  # Troque para 'en_US.UTF-8' conforme necessário

if __name__ == '__main__':
    date, name = hello()
    # Formatar a data de acordo com o locale atual
    formatted_date = format_date(date, locale='pt_BR')  # ou 'en_US'
    # Marcar a string para tradução
    print(_('Último commit feito em:'), formatted_date, _(' por'), name)