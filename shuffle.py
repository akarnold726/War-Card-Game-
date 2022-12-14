import random 

def shuffle(cards): 
    shuffled_cards = []
    used_ids = []
    while len(shuffled_cards) < len(cards): 
        card_id = random.radnint(0, len(cards)-1)
        if card_id not in used_ids:
            used_ids.append(card_id)
            shuffled_cards.append([cards[card_id]])
    return shuffled_cards 