import random as rand
from PIL import Image
import time


PUNK_HANDS_SET = set()

# [NAILS, SLEEVE, BRACELET, WATCH, GLOVE, HALF GLOVE, RING]
NAILS, SLEEVE, BRACELET, WATCH, GLOVE, HALF_GLOVE, RING = 0, 0, 0, 0, 0, 0, 0


def universal_picker(n, chances, options):
    sum_chances = 0
    pick_number = rand.uniform(0, 100)

    for x in range(n):
        sum_chances += chances[x]

        if pick_number < sum_chances:
            return options[x]

    return options[n - 1]


def pick_background():
    options = ['BLUE', 'RED', 'PURPLE']
    n = len(options)
    chances = [50, 35, 15]

    return rand.choices(options, weights=chances, cum_weights=None, k=1)


def pick_skin():
    options = ['LIGHT', 'MEDIUM', 'DARK', 'ALBINO']
    n = len(options)
    chances = [30, 30, 30, 10]

    return rand.choices(options, weights=chances, cum_weights=None, k=1)


def pick_nails():
    options = ['NAILS01', 'NAILS02', 'NAILS03', 'NAILS04',
               'NAILS05', 'NAILS06', 'NAILS07', 'NAILS08', 'NAILS09']
    n = len(options)
    chances = [2, 12.25, 12.25, 12.25, 12.25, 12.25, 12.25, 12.25, 12.25]

    return rand.choices(options, weights=chances, cum_weights=None, k=1)


def pick_sleeve():
    options = ['SLEEVE01', 'SLEEVE02', 'SLEEVE03', 'SLEEVE04', 'SLEEVE05',
               'SLEEVE06', 'SLEEVE07', 'SLEEVE08', 'SLEEVE09', 'SLEEVE10',
               'SLEEVE11', 'SLEEVE12', 'SLEEVE13', 'SLEEVE14', 'SLEEVE15']
    n = len(options)
    chances = [6.66, 6.66, 6.66, 6.66, 6.66, 6.66, 6.66,
               6.66, 6.66, 6.66, 6.66, 6.66, 6.66, 6.66, 6.66, ]

    return rand.choices(options, weights=chances, cum_weights=None, k=1)


def pick_bracelet():
    options = ['BRACELET01', 'BRACELET02', 'BRACELET03', 'BRACELET04', 'BRACELET05',
               'BRACELET06', 'BRACELET07', 'BRACELET08', 'BRACELET09', 'BRACELET10',
               'BRACELET11', 'BRACELET12']
    n = len(options)
    chances = [8.33, 8.33, 8.33, 8.33, 8.33,
               8.33, 8.33, 8.33, 8.33, 8.33, 8.33, 8.33]

    return rand.choices(options, weights=chances, cum_weights=None, k=1)


def pick_watch():
    options = ['WATCH01', 'WATCH02', 'WATCH03', 'WATCH04', 'WATCH05',
               'WATCH06', 'WATCH07', 'WATCH08', 'WATCH09', 'WATCH10',
               'WATCH11', 'WATCH12', 'WATCH13', 'WATCH14', 'WATCH15',
               'WATCH16', 'WATCH17', 'WATCH18']
    n = len(options)
    chances = [5.55, 5.55, 5.55, 5.55, 5.55, 5.55, 5.55, 5.55,
               5.55, 5.55, 5.55, 5.55, 5.55, 5.55, 5.55, 5.55, 5.55, 5.55]

    return rand.choices(options, weights=chances, cum_weights=None, k=1)


def pick_glove():
    options = ['GLOVE01', 'GLOVE02', 'GLOVE03']
    n = len(options)
    chances = [33.33, 33.33, 33.33]

    return rand.choices(options, weights=chances, cum_weights=None, k=1)


def pick_half_glove():
    options = ['HALFGLOVE01', 'HALFGLOVE02', 'HALFGLOVE03']
    n = len(options)
    chances = [33.33, 33.33, 33.33]

    return rand.choices(options, weights=chances, cum_weights=None, k=1)


def pick_ring():
    options = ['RING01', 'RING02', 'RING03', 'RING04', 'RING05',
               'RING06', 'RING07', 'RING08', 'RING09', 'RING10',
               'RING11', 'RING12', 'RING13', 'RING14']
    n = len(options)
    chances = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 2.5, 2.5, 2.5, 2.5]

    return rand.choices(options, weights=chances, cum_weights=None, k=1)


def pick_traits():
    # [NAILS, SLEEVE, BRACELET, WATCH, GLOVE, HALF GLOVE, RING]
    chosen_traits = [False, False, False, False, False, False, False]

    num_trait_options = [2, 3, 4, 5]
    num_trait_chances = [24.475, 48.515, 24.485, 2.535]

    num_traits = rand.choices(
        num_trait_options, weights=num_trait_chances, cum_weights=None, k=1)[0]

    while num_traits > 0:
        trait_picker = rand.uniform(0, 100)

        # NAILS 0
        if trait_picker <= 15:
            if chosen_traits[GLOVE] == False:
                chosen_traits[NAILS] = True
                num_traits -= 1
        # SLEEVE 1
        elif trait_picker <= 50:
            chosen_traits[SLEEVE] = True
            num_traits -= 1
        # BRACELET 2
        elif trait_picker <= 60:
            if chosen_traits[WATCH] == False:
                chosen_traits[BRACELET] = True
                num_traits -= 1
        # WATCH 3
        elif trait_picker <= 80:
            if chosen_traits[BRACELET] == False:
                chosen_traits[WATCH] = True
                num_traits -= 1
        # GLOVE 4
        elif trait_picker <= 85:
            if chosen_traits[NAILS] == False and chosen_traits[HALF_GLOVE] == False:
                chosen_traits[4] = True
                num_traits -= 1
        # HALF GLOVE 5
        elif trait_picker <= 90:
            if chosen_traits[GLOVE] == False and chosen_traits[RING] == False:
                chosen_traits[HALF_GLOVE] = True
            num_traits -= 1
        # RING 6
        else:
            if chosen_traits[GLOVE] == False and chosen_traits[HALF_GLOVE] == False:
                chosen_traits[RING] = True
                num_traits -= 1

    return chosen_traits


def make_hand(path):
    punk_hand_id = ""

    background = pick_background()[0]
    skin_tone = pick_skin()[0]

    punk_hand_id = punk_hand_id + background + skin_tone

    final_image = Image.open('../assets/backgrounds/' + background + '.png')
    skin_tone_image = Image.open('../assets/skintones/' + skin_tone + '.png')

    final_image.paste(skin_tone_image, (0, 0), skin_tone_image)

    chosen_traits = pick_traits()

    if chosen_traits[2] == True:
        bracelet = pick_bracelet()[0]
        image = Image.open('../assets/bracelets/' + bracelet + '.png')
        final_image.paste(image, (0, 0), image)
        punk_hand_id += bracelet

    if chosen_traits[3] == True:
        watch = pick_watch()[0]
        image = Image.open('../assets/watches/' + watch + '.png')
        final_image.paste(image, (0, 0), image)
        punk_hand_id += watch

    if chosen_traits[1] == True:
        sleeve = pick_sleeve()[0]
        image = Image.open('../assets/sleeves/' + sleeve + '.png')
        final_image.paste(image, (0, 0), image)
        punk_hand_id += sleeve

    if chosen_traits[6] == True:
        ring = pick_ring()[0]
        image = Image.open('../assets/rings/' + ring + '.png')
        final_image.paste(image, (0, 0), image)
        punk_hand_id += ring

    if chosen_traits[0] == True:
        nails = pick_nails()[0]
        image = Image.open('../assets/nails/' + nails + '.png')
        final_image.paste(image, (0, 0), image)
        punk_hand_id += nails

    if chosen_traits[4] == True:
        glove = pick_glove()[0]
        image = Image.open('../assets/gloves/' + glove + '.png')
        final_image.paste(image, (0, 0), image)
        punk_hand_id += glove

    if chosen_traits[5] == True:
        half_glove = pick_half_glove()[0]
        image = Image.open('../assets/half_gloves/' + half_glove + '.png')
        final_image.paste(image, (0, 0), image)
        punk_hand_id += half_glove

    if punk_hand_id not in PUNK_HANDS_SET:
        final_image.save(path)
        PUNK_HANDS_SET.add(punk_hand_id)


start_time = time.time()

for x in range(100):
    make_hand('../test_output/punk_hand_' + str(x + 1) + '.png')

print("--- %s seconds ---" % (time.time() - start_time))
