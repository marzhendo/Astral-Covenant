import random

def artoria_skill(servant, player, enemies, calc_damage, log):

    for e in enemies:
        if not e.is_alive():
            continue

        dmg = int(calc_damage(servant, e) * 1.4)
        e.hp -= dmg
        log(f"{servant.name} unleashes Excalibur! {e.name} takes {dmg}!")

        # 30% defense down
        if random.random() < 0.3:
            e.add_status("Defense Down", 2)
            log(f"{e.name} is affected by Defense Down!")
def emiya_skill(servant, player, enemies, calc_damage, log):

    hits = random.randint(2,4)

    for _ in range(hits):
        alive = [e for e in enemies if e.is_alive()]
        if not alive:
            return

        target = random.choice(alive)

        dmg = int(calc_damage(servant, target) * 0.9)
        target.hp -= dmg
        log(f"{servant.name} fires Broken Phantasm! {target.name} takes {dmg}!")

        # 25% burn
        if random.random() < 0.25:
            target.add_status("Burn", 2)
            log(f"{target.name} is affected by Burn!")

def mash_skill(servant, player, enemies, calc_damage, log):

    log(f"{servant.name} raises Lord Chaldeas!")

    # reduce damage via Astral Mark removal / defensive buff simulation
    if player.has_status("Defense Down"):
        player.status_effects = [
            s for s in player.status_effects if s["name"] != "Defense Down"
        ]
        log("Defense restored!")

    heal = int(player.max_hp * 0.25)
    player.hp = min(player.max_hp, player.hp + heal)

    log(f"{player.name} recovers {heal} HP!")