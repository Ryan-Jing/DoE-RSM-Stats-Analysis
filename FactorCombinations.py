import csv

def generate_combinations():
    values = [-1, 0, 1]
    combinations = []

    for value1 in values:
        for value2 in values:
            for value3 in values:
                combinations.append([value1, value2, value3])

    return combinations

def write_to_csv(combinations):
    with open('213_Project2_Chart.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Column 1', 'Column 2', 'Column 3'])
        for combination in combinations:
            writer.writerow(combination)

if __name__ == "__main__":
    all_combinations = generate_combinations()
    write_to_csv(all_combinations)
    print("Combinations written to 213_Project2_Chart.csv successfully!")
