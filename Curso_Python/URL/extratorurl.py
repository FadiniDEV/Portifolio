import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url(self.url)
        

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self, url):
        if not self.url:
            raise ValueError("Bota a url certa corno!")
        
        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrao_url.match(url)
        if not match:
            raise ValueError("Bota a url certa corno!")
        

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao+1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor
    
    def __len__(self, url):
        return len(url)
    
    def __str__(self, url):
        return url + "\n" + "Parametros: " + self.get_url_parametros() + "\n" + "URL Base: " + self.get_url_base()
    
    def __eq__(self, other):
        return self.url == other.url

#url = "https://www.bytebank.com/cambio?quantidade=73&moedaOrigem=dolar&moedaDestino=real"