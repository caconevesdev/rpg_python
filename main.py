from random import randint

lista_npcs = []

player = {
    "name": "Caio",
    "level": 1,
    "exp": 0,
    "exp_max": 30,
    "hp": 100,
    "hp_max": 100,
    "damage": 25,
}


def create_npc(level):
    novo_npc = {
        "name": f"Monster #{level}",
        "level": level,
        "damage": 5 * level,
        "hp": 100 * level,
        "hp_max": 100 * level,
        "exp": 7 * level
    }

    return novo_npc


def generate_npcs(n_npcs):
    for x in range(n_npcs):
        npc = create_npc(x + 1)
        lista_npcs.append(npc)


def show_npcs():
    for npc in lista_npcs:
        show_npc(npc)


def show_npc(npc):
    print(
        f"Name: {npc['name']} // Level: {npc['level']} // Damage: {npc['damage']} // HP: {npc['hp']} // EXP: {npc['exp']}"
    )


def show_player():
    print(
        f"Name: {player['name']} // Level: {player['level']} // Damage: {player['damage']} // HP: {player['hp']}/{player['hp_max']} // EXP: {player['exp']}/{player['exp_max']}"
    )


def reset_player():
    player['hp'] = player['hp_max']


def reset_npc(npc):
    npc['hp'] = npc['hp_max']


def level_up():
    if player['exp'] >= player['exp_max']:
        player['level'] += 1
        player['exp'] = 0
        player['exp_max'] = player['exp_max'] * 2
        player['hp_max'] += 20


def start_battle(npc):

    while player['hp'] > 0 and npc['hp'] > 0:
        attack_npc(npc)
        attack_player(npc)
        show_info_battle(npc)

    if player['hp'] > 0:
        print(f"The {player['name']} won and gained {npc['exp']} EXP!")
        player['exp'] += npc['exp']
        show_player()
    else:
        print(f"The {npc['name']} killed the player {player['name']}!")
        show_npc(npc)

    level_up()
    reset_player()
    reset_npc(npc)


def attack_npc(npc):
    npc['hp'] -= player['damage']


def attack_player(npc):
    player['hp'] -= npc['damage']


def show_info_battle(npc):
    print(f"Player: {player['hp']}/{player['hp_max']}")
    print(f"NPC: {npc['name']}: {npc['hp']}/{npc['hp_max']}")
    print("-------------------\n")


generate_npcs(5)

npc_selected = lista_npcs[0]
start_battle(npc_selected)
start_battle(npc_selected)
start_battle(npc_selected)
start_battle(npc_selected)
start_battle(npc_selected)

show_player()