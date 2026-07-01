endereco = "Rua Guairacá 1931, casa, Centro, Pitanga, Pr, 85200-057"

import re #Regular Expession
#5 dígitos + hífen + 3 dígitos

padrao = re.compile("[0-9]{5}[-][0-9]{3}")

busca = padrao.search(endereco)
if busca:
    cep = busca.group()
    print(cep)