# This program show how many rainfall in the year
MOUTH = 12


def main():
    rainfall_year = []
    all_fall = 0
    for m in range(MOUTH):
        print('Enter rainfall in', m+1, 'mouth')
        fall = int(input())
        rainfall_year.append(fall)
    for emty in rainfall_year:
        all_fall += emty
    min_rainfall = min(rainfall_year)
    max_rainfall = max(rainfall_year)
    print('All rainfall in the year', all_fall)
    print('Min rainfall in the year', min_rainfall)
    print('Max rainfall in the year', max_rainfall)
    print('Mean rainfall in the year', all_fall/12)


main()
