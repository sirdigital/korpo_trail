from helpers import *
from assets.choises import *
from assets import config


class StoryManager:
    def load_texts(self):
        with open('assets/texts.txt', 'r') as f:
            for line in f.readlines():
                splitted = line.split('dawidbodych')
                self.texts[splitted[0]] = splitted[1]

    def __init__(self):
        self.name = input('Podaj imię piwne: ')
        self.texts = {}
        self.load_texts()
        self.reputation_points = 0
        self.time_passed = 0
        self.equipment = {
            'beer': 5,
            'food': 5,
            'comilitones': 3,
            'filisters': 2
        }
        self.choose_your_destiny()
        self.choose_departure_time()
        self.specify_equipment()

    def show_equipment(self):
        print('\nTwój zestaw:')
        for k, v in self.equipment.items():
            print('{}: {}'.format(config.equipment_mapping[k], v))

    def choose_your_destiny(self):
        destiny = ask_for_choice('Wybierz swoją postać:', [
            'Comiliton Świeżak',
            'Comiliton Abstynent',
            'Comiliton Śmieszek',
            'Comiliton Legenda'
        ])

        if destiny == '1':
            self.reputation_points = 10
        elif destiny == '2':
            self.reputation_points = 25
        elif destiny == '3':
            self.reputation_points = 50
        else:
            self.reputation_points = 100

    def choose_departure_time(self):
        print('Wiadomość nt. tego co jak wyruszysz za późno albo za wcześnie')
        time = ask_for_choice('Wybierz godzinę rozpoczęcia komersu:', ['17:00', '18:00', '19:00', '20:00', '21:00'])

        self.time_passed = (int(time)-1) * 60

    def specify_equipment(self):
        choice = None
        print('\nSkompletuj swój zestaw komersowy.\n')
        while choice != '5' and self.reputation_points > 0:
            print('Masz jeszcze {} punktów reputacji do wydania.'.format(self.reputation_points))
            choice = ask_for_choice('Na co chcesz je spędzić?', ['Piwo (1 p.r./szt.)', 'Jedzenie (2 p.r./szt.)',
                                                                 'Kompetentni comilitoni (4 p.r./szt.)',
                                                                 'Spokojni filistrzy (6 p.r./szt.)',
                                                                 'Kończę zakupy'])
            if choice == '5':
                break

            how_much = None
            while type(how_much) != int:
                try:
                    how_much = int(input('Ile sztuk: '))
                except ValueError:
                    print('To nie jest poprawna liczba!')

            item_cost, item_name = (inventory_config[choice][key] for key in ['cost', 'name'])

            if self.reputation_points >= item_cost * how_much:
                self.equipment[item_name] += how_much
                self.reputation_points -= item_cost * how_much
            else:
                print('Masz za mało punktów reputacji!')

        self.show_equipment()
