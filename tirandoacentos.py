'''Projeto criado para facilitar a abertura de empresas, pois não pode conter acentos no CNAE '''

def objeto_social(objeto):
       
    # Tire todos os acentos e "Ç"    
        objeto = objeto.replace('Ç', 'C')
        objeto = objeto.replace('Á', 'A').replace('Â', 'A').replace('Ã', 'A').replace('À', 'A')
        objeto = objeto.replace('É', 'E').replace('Ê', 'E').replace('È', 'E')
        objeto = objeto.replace('Í', 'I').replace('Î', 'I').replace('Ì', 'I')
        objeto = objeto.replace('Ó', 'O').replace('Ô', 'O').replace('Õ', 'O').replace('Ò', 'O')
        objeto = objeto.replace('Ú', 'U').replace('Û', 'U').replace('Ù', 'U')
        objeto = objeto.replace(';', ' ')       
        objeto = objeto.replace('-', '')
        objeto = objeto.replace('1', '').replace('2', '').replace('3', '').replace('4', '').replace('5', '')
        objeto = objeto.replace('6', '').replace('7', '').replace('8', '').replace('9', '').replace('0', '')
        objeto = objeto.replace('/', '')
        objeto = objeto.replace('  ', ' ')
        objeto = objeto.replace('\t', ',')
        objeto = objeto.replace(',  ,', ', ')
        objeto = objeto.strip()
        objeto = objeto + '.'
        objeto = objeto.replace('..', '.')
        objeto = objeto.replace('RESULTADO INDISPONIVEL','')
        objeto = objeto.replace('SIM','')
        objeto = objeto.replace('PRINCIPAL','')
        objeto = objeto.replace('SECUNDARIO','')
        objeto = objeto.replace(',,',',')
        objeto = objeto.replace('  ,',',')
        objeto = objeto.replace(' ,',',')
        objeto = objeto.replace(',.','.')
        objeto = objeto.replace('  ',' ')
        if objeto[0] == ',':
          return(objeto[1::])
        else:
          return(objeto)

objeto = input('Digite o objeto social: ').upper()
objeto_social(objeto)
