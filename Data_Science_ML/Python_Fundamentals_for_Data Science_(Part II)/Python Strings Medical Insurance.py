medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

#print(medical_data)
update_medical_data = medical_data.replace("#", "$")
#print(update_medical_data)

num_records = 0
for record in update_medical_data:
    if record == "$":
        num_records += 1
print("There are {num_records} medical records in the data.".format(num_records = num_records))
medical_data_split = update_medical_data.split(";")
#print(medical_data_split)
medical_records = []
medical_records = [rec_splitted.split(",") for rec_splitted in medical_data_split]
print(medical_records)
medical_records_clean = []

#for med_rec in medical_records:
#    record_clean = []
#    for item in med_rec:
#        record_clean.append(item.strip())
#    medical_records_clean.append(record_clean)

#List Comprenhension
medical_records_clean = [[item.strip() for item in med_rec] for med_rec in medical_records]
#print(medical_records_clean)
for record in medical_records_clean:
    print(record[0])

for record in medical_records_clean:
    names_upper = record[0].upper()    
    print(names_upper)

#names = []
#ages = []
#bmis = []
#insurance_costs = []

names = [record[0] for record in medical_records_clean]
ages = [record[1] for record in medical_records_clean]
bmis = [record[2] for record in medical_records_clean]
insurance_costs = [record[3] for record in medical_records_clean]

print(names)
print(ages)
print(bmis)
print(insurance_costs)

total_bmi = 0
for bmi in bmis:
    total_bmi += float(bmi)
#print(total_bmi)
average_bmi = total_bmi/len(bmis)
print("Average BMI: {average_bmi}".format(average_bmi = average_bmi))

total_insurance_cost = 0 

#Using list slicing to removing "$"

for cost in insurance_costs:
    total_insurance_cost += float(cost[1:])

avg_insurance_cost = total_insurance_cost/len(insurance_costs)
print(avg_insurance_cost)

#first_name uses split method to return the first index after the method occurs, since we have just 1 name and 1 last name, we can divide using the space as a separator

for full_name, age, bmi, ins_cost in medical_records_clean:
    first_name = full_name.split(" ")[0]
    print("{name} is {age} years old with a BMI of {bmi} and an insurance cost of {ins_cost}.".format(name=first_name, age=age, bmi=bmi, ins_cost=ins_cost))