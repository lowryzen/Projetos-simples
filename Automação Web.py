from selenium import webdriver

class Web_auto:
    def __init__(self, url:str):
        self.navegador = webdriver.Firefox()
        self.navegador.get(url)

    def __str__(self):
        return self.navegador.title

    def clicar(self, local, nome, segundos_espera=0):
        """Informe o local do código html e o nome que deseja clicar, e quantos segundos deseja esperar até clicar"""

        self.navegador.implicitly_wait(segundos_espera)
        clique = self.navegador.find_element(local, nome)
        clique.click()

    def pegar_info(self, local, nome, segundos_espera=0):
        """Pega as informações com base no local do html e o nome, e quantos segundos deseja esperar até carregar"""

        self.navegador.implicitly_wait(segundos_espera)
        info = self.navegador.find_element(local, nome)
        print(info.text)