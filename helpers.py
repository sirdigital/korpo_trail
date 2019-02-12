

def iterate_options(options):
    range_of_choosing = range(1, len(options)+1)

    for i in range_of_choosing:
        print('{}. {}'.format(str(i), options[i-1]))

    return [str(choice) for choice in range_of_choosing]


def ask_for_choice(question, options):
    print('\n{}\n'.format(question))
    valid_choices = iterate_options(options)

    choice = input('\nTwój wybór: ')

    while choice not in valid_choices:
        print('Wybierz cyfrę między {} a {}.\nSpróbuj ponownie.'.format(valid_choices[0], valid_choices[-1]))
        choice = input('\nTwój wybór: ')

    return choice
