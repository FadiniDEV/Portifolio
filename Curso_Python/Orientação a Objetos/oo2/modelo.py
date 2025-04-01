class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.tittle()

    def __str__(self):
        return f'Nome: {self._nome} - Likes: {self._likes}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self._nome} - {self.duracao} min - {self._likes} Likes'
        
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self._nome} - {self.temporadas} Temporadas - {self._likes} Likes'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self,item):
        return self._programas[item]
    
    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)

vingadores = Filme('vingadores - guerra da minha pika', 2023, 200)
atlanta = Serie('atlantica', 2018, 2)
tmep = Filme("Todo mundo em panico", 1999, 100)
demolidor = Serie("demolidor", 2016, 2)

vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist("Fim de semana", filmes_e_series)

print(f"Tamanho da playlist: {len(playlist_fim_de_semana)}")

for programa in playlist_fim_de_semana:
    print(programa)

