import math

# Function definitions
def binomial_coefficient(n, k):
    return math.comb(n, k)

def probability_of_hit_in_slot(p_cost, remaining_copies, total_pool_size, total_same_cost_units):
    return (p_cost / total_same_cost_units) * (remaining_copies / total_pool_size)

def probability_of_hit_in_one_roll(p_slot):
    return 1 - (1 - p_slot) ** 5

def binomial_probability(n, k, p_hit):
    return binomial_coefficient(n, k) * (p_hit ** k) * ((1 - p_hit) ** (n - k))

def cumulative_probability(n, k, p_hit):
    total_prob = 0
    for i in range(k, n + 1):
        total_prob += binomial_probability(n, i, p_hit)
    return total_prob

def tft_probability_to_3_star(level, unit_cost, remaining_copies, total_rolls, copies_needed, units_bought, champion_costs):
    shop_odds = {
        1: [100, 0, 0, 0, 0],
        2: [100, 0, 0, 0, 0],
        3: [75, 25, 0, 0, 0],
        4: [55, 30, 15, 0, 0],
        5: [45, 33, 20, 2, 0],
        6: [30, 40, 25, 5, 0],
        7: [19, 30, 40, 10, 1],
        8: [18, 25, 32, 22, 3],
        9: [15, 20, 25, 30, 10],
        10: [5, 10, 20, 40, 25],
        11: [1, 2, 12, 50, 35],
    }

    pool_size = {
        1: 30,
        2: 25,
        3: 18,
        4: 12,
        5: 9
    }

    p_cost = shop_odds[level][unit_cost - 1] / 100.0
    total_pool_size = pool_size[unit_cost]
    total_same_cost_units = len(champion_costs[unit_cost])

    copies_remaining = copies_needed - units_bought
    p_slot = probability_of_hit_in_slot(p_cost, remaining_copies, total_pool_size, total_same_cost_units)
    p_hit_in_roll = probability_of_hit_in_one_roll(p_slot)
    
    return cumulative_probability(total_rolls, copies_remaining, p_hit_in_roll)

# Champion cost mapping
champion_costs = {
    1: ["Twitch", "Zoe", "Ziggs", "Blitzcrank", "Elise", "Warwick", "Nomsy", "Jayce", "Ashe", "Soraka", "Jax", "Poppy", "Lillia", "Seraphine"],
    2: ["Zilean", "Kog'Maw", "Nilah", "Ahri", "Rumble", "Syndra", "Cassiopeia", "Galio", "Kassadin", "Nunu", "Akali", "Shyvana", "Tristana"],
    3: ["Bard", "Ezreal", "Jinx", "Mordekaiser", "Hecarim", "Wukong", "Shen", "Hwei", "Katarina", "Swain", "Veigar", "Neeko", "Vex"],
    4: ["Nami", "Tahm Kench", "Olaf", "Rakan", "Fiora", "Gwen", "Taric", "Ryze", "Varus", "Karma", "Nasus", "Kalista"],
    5: ["Morganna", "Norra & Yuumi", "Briar", "Camille", "Xerath", "Milio", "Diana", "Smolder"]
}
