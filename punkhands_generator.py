import random as rand
import numpy as np
from PIL import Image
import time

PUNK_HANDS_SET = set()


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

    return universal_picker(n, chances, options)


def pick_skin():
    options = ['LIGHT', 'MEDIUM', 'DARK', 'ALBINO']
    n = len(options)
    chances = [30, 30, 30, 10]

    return universal_picker(n, chances, options)


def pick_nails():
    options = ['NAILS01', 'NAILS02', 'NAILS03', 'NAILS04',
               'NAILS05', 'NAILS06', 'NAILS07', 'NAILS08', 'NAILS09']
    n = len(options)
    chances = [2, 12.25, 12.25, 12.25, 12.25, 12.25, 12.25, 12.25, 12.25]

    return universal_picker(n, chances, options)


def pick_sleeve():
    options = ['SLEEVE01', 'SLEEVE02', 'SLEEVE03', 'SLEEVE04', 'SLEEVE05',
               'SLEEVE06', 'SLEEVE07', 'SLEEVE08', 'SLEEVE09', 'SLEEVE10',
               'SLEEVE11', 'SLEEVE12', 'SLEEVE13', 'SLEEVE14', 'SLEEVE15']
    n = len(options)
    chances = np.full(n, 6.66)

    return universal_picker(n, chances, options)


def pick_bracelet():
    options = ['BRACELET01', 'BRACELET02', 'BRACELET03', 'BRACELET04', 'BRACELET05',
               'BRACELET06', 'BRACELET07', 'BRACELET08', 'BRACELET09', 'BRACELET10',
               'BRACELET11', 'BRACELET12']
    n = len(options)
    chances = np.full(n, 8.33)

    return universal_picker(n, chances, options)


def pick_watch():
    options = ['WATCH01', 'WATCH02', 'WATCH03', 'WATCH04', 'WATCH05',
               'WATCH06', 'WATCH07', 'WATCH08', 'WATCH09', 'WATCH10',
               'WATCH11', 'WATCH12', 'WATCH13', 'WATCH14', 'WATCH15',
               'WATCH16', 'WATCH17', 'WATCH18']
    n = len(options)
    chances = np.full(n, 5.55)

    return universal_picker(n, chances, options)


def pick_glove():
    options = ['GLOVE01', 'GLOVE02', 'GLOVE03']
    n = len(options)
    chances = [33.33, 33.33, 33.33]

    return universal_picker(n, chances, options)


def pick_half_glove():
    options = ['HALFGLOVE01', 'HALFGLOVE02', 'HALFGLOVE03']
    n = len(options)
    chances = [33.33, 33.33, 33.33]

    return universal_picker(n, chances, options)


def pick_ring():
    options = ['RING01', 'RING02', 'RING03', 'RING04', 'RING05',
               'RING06', 'RING07', 'RING08', 'RING09', 'RING10',
               'RING11', 'RING12', 'RING13', 'RING14']
    n = len(options)
    chances = np.append(np.full(10, 9), np.full(4, 2.5))

    return universal_picker(n, chances, options)


def pick_traits():
    # [NAILS, SLEEVE, BRACELET, WATCH, GLOVE, HALF GLOVE, RING]
    chosen_traits = [False, False, False, False, False, False, False]

    num_trait_options = [2, 3, 4, 5]
    num_trait_n = len(num_trait_options)
    num_trait_chances = [24.475, 48.515, 24.485, 2.535]

    num_traits = universal_picker(
        num_trait_n, num_trait_chances, num_trait_options)

    while num_traits > 0:
        trait_picker = rand.uniform(0, 100)

        # NAILS 0
        if trait_picker <= 15:
            if chosen_traits[4] == False:
                chosen_traits[0] = True
                num_traits -= 1
        # SLEEVE 1
        elif trait_picker <= 50:
            chosen_traits[1] = True
            num_traits -= 1
        # BRACELET 2
        elif trait_picker <= 60:
            if chosen_traits[3] == False:
                chosen_traits[2] = True
                num_traits -= 1
        # WATCH 3
        elif trait_picker <= 80:
            if chosen_traits[2] == False:
                chosen_traits[3] = True
                num_traits -= 1
        # GLOVE 4
        elif trait_picker <= 85:
            if chosen_traits[0] == False & chosen_traits[5] == False:
                chosen_traits[4] = True
                num_traits -= 1
        # HALF GLOVE 5
        elif trait_picker <= 90:
            if chosen_traits[4] == False & chosen_traits[6] == False:
                chosen_traits[5] = True
            num_traits -= 1
        # RING 6
        else:
            if chosen_traits[4] == False & chosen_traits[5] == False:
                chosen_traits[6] = True
                num_traits -= 1

    return chosen_traits


def make_hand(path):
    punk_hand_id = ""

    background = pick_background()
    skin_tone = pick_skin()

    punk_hand_id = punk_hand_id + background + skin_tone

    final_image = Image.open('../assets/backgrounds/' + background + '.png')
    skin_tone_image = Image.open('../assets/skintones/' + skin_tone + '.png')

    final_image.paste(skin_tone_image, (0, 0), skin_tone_image)

    chosen_traits = pick_traits()

    if chosen_traits[2] == True:
        bracelet = pick_bracelet()
        image = Image.open('../assets/bracelets/' + bracelet + '.png')
        final_image.paste(image, (0, 0), image)
        punk_hand_id += bracelet

    if chosen_traits[3] == True:
        watch = pick_watch()
        image = Image.open('../assets/watches/' + watch + '.png')
        final_image.paste(image, (0, 0), image)
        punk_hand_id += watch

    if chosen_traits[1] == True:
        sleeve = pick_sleeve()
        image = Image.open('../assets/sleeves/' + sleeve + '.png')
        final_image.paste(image, (0, 0), image)
        punk_hand_id += sleeve

    if chosen_traits[6] == True:
        ring = pick_ring()
        image = Image.open('../assets/rings/' + ring + '.png')
        final_image.paste(image, (0, 0), image)
        punk_hand_id += ring

    if chosen_traits[0] == True:
        nails = pick_nails()
        image = Image.open('../assets/nails/' + nails + '.png')
        final_image.paste(image, (0, 0), image)
        punk_hand_id += nails

    if chosen_traits[4] == True:
        glove = pick_glove()
        image = Image.open('../assets/gloves/' + glove + '.png')
        final_image.paste(image, (0, 0), image)
        punk_hand_id += glove

    if chosen_traits[5] == True:
        half_glove = pick_half_glove()
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
