# -*- coding: utf-8 -*-
class Game:
    def __init__(self, start_step):
        self.start_step = start_step

    def start(self):
        step = self.start_step.next_step()
        while step is not None:
            step = step.next_step()


class GameStep:
    def __init__(self, question, next_steps, description=''):
        self.description = description
        self.question = question
        self.next_steps = next_steps
        self.placeholder = self.create_placeholder()

    @staticmethod
    def create_placeholder():
        return 'Выберите: {}/{}\n'

    @staticmethod
    def read_step(self):
        return raw_input(self.placeholder.format(*self.next_steps))

    def next_step(self):
        if self.description != '':
            print self.description
        print self.question
        selected_step = ''
        while selected_step not in self.next_steps:
            selected_step = self.read_step(self)
        return self.next_steps[selected_step]


class EndStep:
    def __init__(self, description=''):
        self.description = description

    def next_step(self):
        if self.description != '':
            print self.description
        return None


good_end_step = EndStep(
    description='Утка маляр вернулась домой. '
                'Еще один день прожит. Вы победили.')
bad_end_step = EndStep(
    description='Утка маляр продалась в рабство. '
                'Вы проиграли :с')
bad_end_step_2 = EndStep(
    description='Утка переутомилась. '
                'Вы проиграли :с')
step4_2 = GameStep(
    'Пойти домой?',
    {'да': good_end_step, 'нет': bad_end_step_2},
    description='Утка маляр прошла еще 10км. Утке захотелось пойти домой.'
)
step4_1 = GameStep(
    'Бежать или продаться в рабство?',
    {'бежать': step4_2, 'рабство': bad_end_step},
    description='Утка очень вкусно поела. Официант принес счет на 1000$'
)
step3_1 = GameStep(
    'Заказать бургер или салат?',
    {'салат': step4_1, 'бургер': step4_1},
    description='Утка-маляр зашла в кафе. К ней подошел официант.'
)
step3_2 = GameStep(
    'Зайти в кафе?',
    {'да': step3_1, 'нет': step4_2},
    description='Что-то захотелось есть.'
)
step2_2 = GameStep(
    'На улице начался дождь. Пойти в кафе или вернуться домой?',
    {'в кафе': step3_1, 'домой': good_end_step},
    description='Утка-маляр пошла гулять без зонта.'
)
step2_1 = GameStep(
    'Надеть куртку?',
    {'да': step3_2, 'нет': step3_2},
    description='На улице холодно.'
)
step1 = GameStep(
    'Взять ей зонтик?',
    {'да': step2_1, 'нет': step2_2},
    description='Утка-маляр решила погулять.'
)

if __name__ == '__main__':
    game = Game(step1)
    game.start()
