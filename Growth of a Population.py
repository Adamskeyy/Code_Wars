# Examples:
# nb_year(1500, 0.05, 100, 5000) -> 15
# nb_year(1500000, 0.025, 10000, 2000000) -> 10


def nb_year(p0, percent, aug, p):
    percent /= 100
    years = 0
    while p0 < p:
        p0 = p0 + (p0 * percent + aug)
        years += 1
    return years


print(nb_year(1500, 5, 100, 5000))