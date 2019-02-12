from helpers import *


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
        self.choose_your_destiny()
        self.choose_departure_time()
        print(self.reputation_points)
        print(self.time_passed)

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
