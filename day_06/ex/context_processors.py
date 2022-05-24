import random

from day_06.settings import USER_NAMES


def get_names(request):
    rand_name = random.randint(0, 9)

    context = {
        'names_list': USER_NAMES,
        'first_name': USER_NAMES[rand_name],
    }
    return context
