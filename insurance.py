import csv
from collections import Counter

filename = 'insurance.csv'

def calculate_average_age(filename):
    total_age = 0
    count = 0
    lower_age_count = 0
    higher_age_count = 0
    lower_age_cost = 0
    higher_age_cost = 0

    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            total_age += int(row['age'])
            count += 1

    if count == 0:
        return 0, 0, 0

    average_age = total_age / count

    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            age = int(row['age'])
            charges = float(row['charges'])
            if age < average_age:
                lower_age_cost += charges
                lower_age_count += 1
            elif age > average_age:
                higher_age_cost += charges
                higher_age_count += 1

    if lower_age_count == 0:
        lower_age_avg = 0
    else:
        lower_age_avg = round(lower_age_cost / lower_age_count, 1)

    if higher_age_count == 0:
        higher_age_avg = 0
    else:
        higher_age_avg = round(higher_age_cost / higher_age_count, 1)

    return round(average_age, 2), lower_age_avg, higher_age_avg

def calculate_region(filename):
    region_counter = Counter()

    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            region = row['region']
            region_counter[region] += 1

    return region_counter

def average_cost_by_sex(filename):
    male_total_cost = 0
    female_total_cost = 0
    male_count = 0
    female_count = 0
    sex_counter = Counter()

    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            sex = row['sex']
            sex_counter[sex] += 1
            if sex == 'male':
                male_total_cost += float(row['charges'])
                male_count += 1
            else:
                female_total_cost += float(row['charges'])
                female_count += 1

    if male_count == 0:
        male_average_cost = 0
    else:
        male_average_cost = round(male_total_cost / male_count, 1)

    if female_count == 0:
        female_average_cost = 0
    else:
        female_average_cost = round(female_total_cost / female_count, 1)

    return male_average_cost, female_average_cost, sex_counter['male'], sex_counter['female']

def smoker_average(filename):
    smoker_total_cost = 0
    non_smoker_total_cost = 0
    smoker_count = 0
    non_smoker_count = 0
    smoker_counter = Counter()

    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            smoker = row['smoker']
            smoker_counter[smoker] += 1
            if smoker == 'yes':
                smoker_total_cost += float(row['charges'])
                smoker_count += 1
            else:
                non_smoker_total_cost += float(row['charges'])
                non_smoker_count += 1

    if smoker_count == 0:
        smoker_average_cost = 0
    else:
        smoker_average_cost = round(smoker_total_cost / smoker_count, 1)

    if non_smoker_count == 0:
        non_smoker_average_cost = 0
    else:
        non_smoker_average_cost = round(non_smoker_total_cost / non_smoker_count, 1)

    return smoker_average_cost, non_smoker_average_cost, smoker_counter['yes'], smoker_counter['no']

def range_cost(filename):
    insurance_costs = []
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            insurance_costs.append(float(row['charges']))

    if not insurance_costs:
        return 0  # Handle the case where there are no insurance costs

    insurance_costs_range = max(insurance_costs) - min(insurance_costs)
    return  max(insurance_costs), min(insurance_costs), round(insurance_costs_range,1)

def calculate_average_cost(filename):
    total_cost = 0
    count = 0
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            total_cost += float(row['charges'])
            count += 1

    if count == 0:
        return 0

    average_cost = round(total_cost / count, 1)
    return average_cost

def average_cost_parents(filename):
    parent_total_cost = 0
    non_parent_total_cost = 0
    parent_count = 0
    non_parent_count = 0
    parent_counter = Counter()

    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            parent = int(row['children'])
            parent_counter[parent] += 1
            if parent != 0:
                parent_total_cost += float(row['charges'])
                parent_count += 1
            if parent == 0:
                non_parent_total_cost+= float(row['charges'])
                non_parent_count += 1

    if parent_count == 0:
        parent_average_cost = 0
    elif non_parent_count == 0:
        non_parent_average_cost = 0
    else:
        parent_average_cost = round(parent_total_cost/ parent_count, 1)
        non_parent_average_cost = round(non_parent_total_cost/ non_parent_count, 1)

    return parent_average_cost, non_parent_average_cost

def bmi_average(filename):
    total_bmi = 0
    count = 0
    lower_bmi_count = 0
    higher_bmi_count = 0
    lower_bmi_cost = 0
    higher_bmi_cost = 0

    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            total_bmi += float(row['bmi'])
            count += 1

    if count == 0:
        return 0, 0, 0

    average_bmi = total_bmi / count

    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            bmi = float(row['bmi'])
            charges = float(row['charges'])
            if bmi < average_bmi:
                lower_bmi_cost += charges
                lower_bmi_count += 1
            elif bmi > average_bmi:
                higher_bmi_cost += charges
                higher_bmi_count += 1

    if lower_bmi_count == 0:
        lower_bmi_avg = 0
    else:
        lower_bmi_avg = round(lower_bmi_cost / lower_bmi_count, 1)

    if higher_bmi_count == 0:
        higher_bmi_avg = 0
    else:
        higher_bmi_avg = round(higher_bmi_cost / higher_bmi_count, 1)

    return round(average_bmi,2), lower_bmi_avg, higher_bmi_avg



# Printing out the number of people belonging to male and female
average_cost_male, average_cost_female, num_male, num_female = average_cost_by_sex(filename)
print(f"Average cost of insurance for males: {average_cost_male}")
print(f"Average cost of insurance for females: {average_cost_female}")
print(f"Number of males: {num_male}")
print(f"Number of females: {num_female}")

# Printing out the number of people belonging to each region
region_counts = calculate_region(filename)
for region, count in region_counts.items():
    print(f"{region}: {count}")

# Printing out total average age
avg_age, lower_age_avg_cost, higher_age_avg_cost = calculate_average_age(filename)
print(f"The average age is: {avg_age}")
print(f"The insurance cost for people younger than the average is: {lower_age_avg_cost}")
print(f"The insurance cost for people older than the average is: {higher_age_avg_cost}")



# Average smoker age and number of smokers and non-smokers
average_cost_smoker, average_cost_non_smoker, num_smokers, num_non_smokers = smoker_average(filename)
print(f"Average cost of insurance for smokers: {average_cost_smoker}")
print(f"Average cost of insurance for non-smokers: {average_cost_non_smoker}")
print(f"Number of smokers: {num_smokers}")
print(f"Number of non-smokers: {num_non_smokers}")

# Range in insurance costs
max_insurance, min_insurance, insurance_value = range_cost(filename)
print(f"The highest insurance cost is: {max_insurance}")
print(f"The lowest insurance cost is: {min_insurance}")
print(f"Range in insurance: {insurance_value}")
#average insurance cost
print(f"The average insurance charge is {calculate_average_cost(filename)}")

#average cost for parents
average_cost_parent, average_cost_non_parent = average_cost_parents(filename)
print(f"Average cost of insurance for parents is: {average_cost_parent}")
print(f"Average cost of insurance for non-parents is: {average_cost_non_parent}")

#average cost based on average bmi
avg_bmi, lower_bmi_avg_cost, higher_bmi_avg_cost = bmi_average(filename)
print(f"The average bmi is: {avg_bmi}")
print(f"The lower bmi average is: {lower_bmi_avg_cost}")
print(f"The higher bmi average is: {higher_bmi_avg_cost}")
