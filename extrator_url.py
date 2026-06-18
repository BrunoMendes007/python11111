class ExtratorURL:
    def__init__(self,url):
        self.url = self.sanatizada_url(url)
        self.valida_url()

        def sanatizada_url(self, url):
            return url.strip()

        def valida_url(self):
            if self.url == "";
                raise ValueError("A URL está vazia")    

extrator_url =ExtratorURL("bytebank.com/cambio?moedasDestino=dolar&quantidade=100&moedaOrigem=real")
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
