class Pokemon:
    def __init__(self, name: str, poketype: str):
        self.name = name
        self.poketype = poketype

    def __str__(self):
        return f'{self.name}/{self.poketype}'


if __name__ == '__main__':
    assert str(Pokemon(name='Bulbasaur', poketype='grass')) == "Bulbasaur/grass"
    assert str(Pokemon(name='Pikachu', poketype='electric\r\npower')) == "Pikachu/electric\r\npower"
    assert str(Pokemon(name='Squirtle', poketype='water' * 30)) == "Squirtle/" + 'water' * 30
