'''
wimbledon task
estimated time: 1 hour
actual time: 1h 45 minutes
'''


def main():
    filename = 'wimbledon.csv'
    champions, countries = read_data(filename)
    champion_count = count_champions(champions)

    print("Wimbledon Champions:")
    for champion, count in sorted(champion_count.items(), key=lambda item: item[0]):
        print(f"{champion} {count}")

    formatted_countries = format_countries(countries)
    print(f"\nThese {len(countries)} countries have won Wimbledon: \n{formatted_countries}")

def read_data(filename):
    champions = []
    countries = set()
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        header = in_file.readline()
        for line in in_file:
            parts = line.strip().split(',')
            if len(parts) < 3:
                continue
            country = parts[1]
            champion = parts[2]
            champions.append((champion, country))
            countries.add(country)
    return champions, countries

def count_champions(champions):
    champion_count = {}
    for champion, country in champions:
        if champion in champion_count:
            champion_count[champion] += 1
        else:
            champion_count[champion] = 1
    return champion_count

def format_countries(countries):
    return ', '.join(sorted(countries))

main()
