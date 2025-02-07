import csv
ages = []
sexes = []
bmis = []
num_children = []
smoker_statuses = []
regions = []
insurance_charges = []
category_to_num = {'male': 0, 'female': 1}


def update_list (lst, column_name):
    with open('C:\python-portfolio-project-starter-files\insurance.csv',mode='r') as insurance_csv: 
        csv_reader = csv.DictReader(insurance_csv)
        for row in csv_reader:
            lst.append(row[column_name])
            
update_list(ages,'age')
update_list(sexes, 'sex')
update_list(bmis,'bmi')
update_list(num_children, 'children')
update_list(smoker_statuses,'smoker')
update_list(regions,  'region')
update_list(insurance_charges, 'charges')

class PatientsInfo:
    def __init__ (self, patients_ages, patients_sexes, patients_bmis, patients_num_children,patients_smoker_statuses, patients_regions, patients_charges):
        self.patients_ages = patients_ages
        self.patients_sexes = patients_sexes
        self.patients_bmis = patients_bmis
        self.patients_num_children = patients_num_children
        self.patients_smoker_statuses = patients_smoker_statuses
        self.patients_regions = patients_regions
        self.patients_charges = patients_charges
    
    def analyze_ages(self):
        total_ages = 0
        for age in self.patients_ages: 
            total_ages += int(age)
        average_ages = round(total_ages / len(self.patients_ages))
        return('The Average Patient Age is: {average} years old'.format(average = average_ages))
    
    def average_charges(self):
        total_charge = 0
        for charge in self.patients_charges:
            total_charge += float(charge)
        average_charge = round(total_charge/len(self.patients_charges),2)
        return('The Average Patient Insurance charge is: {c} dollars'.format(c = average_charge))
    
    def regions (self):
        regions = []
        for region in self.patients_regions:
            if region not in regions:
                regions.append(region)
        return regions
    def analyze_sex (self):
        male = 0
        female = 0
        for sex in self.patients_sexes:
            if sex == 'male':
                male += 1
            else:
                female +=1
        print("Count for female: {f}".format(f = female))
        print("Count for male: {m}".format(m = male))
        
    def analyze_smoker(self):
        smoker=0
        nonsmoker=0
        for smoker_status in self.patients_smoker_statuses:
            if(smoker_status=='smoker'):
                smoker+=1
            else:
                nonsmoker+=1
            
        print("Count for smoker: {f}".format(f = smoker))
        print("Count for nonsmoker: {m}".format(m = nonsmoker))
        
    def create_dictionary(self):
        self.patients_dictionary = {}
        self.patients_dictionary["age"] = [int(age) for age in self.patients_ages]
        self.patients_dictionary["sexes_new"] = [category_to_num[category] for category in self.patients_sexes]
        self.patients_dictionary["bmi"] = self.patients_bmis
        self.patients_dictionary["children"] = self.patients_num_children
        self.patients_dictionary["smoker"] = self.patients_smoker_statuses
        self.patients_dictionary["regions"] = self.patients_regions
        self.patients_dictionary["charges"] = self.patients_charges
        return self.patients_dictionary    

if __name__ == '__main__':
    avg_cost_category = []
    total_sum_for_men=0
    total_sum_for_women=0
    c=0
    b=0
    # category_to_num = {'male': 0, 'female': 1}
    
    patient_info = PatientsInfo(ages,sexes,bmis,num_children,smoker_statuses,regions,insurance_charges)
    patient_info.analyze_ages()
    patient_info.average_charges()
    patient_info.analyze_sex()
    patient_info.analyze_smoker()

    zipped_charges=list(zip(ages,insurance_charges))
    cost_by_age=[[int(age), float(charge)] for age, charge in zipped_charges]
    categories = ['-25 years', '26-40 years', '41-60 years', '+60 years']
    patients_per_category = [i * 0 for i in range(len(categories))]
    cost_per_category = [i * 0 for i in range(len(categories))]
    for index in range(len(cost_by_age)):
        
        if cost_by_age[index][0] <= 25:
            patients_per_category[0] += 1
            cost_per_category[0] += cost_by_age[index][1]
            
        elif cost_by_age[index][0] >= 26 and cost_by_age[index][0] <= 40:
            patients_per_category[1] += 1
            cost_per_category[1] += cost_by_age[index][1]
            
        elif cost_by_age[index][0] >= 41 and cost_by_age[index][0] <= 60:
            patients_per_category[2] += 1
            cost_per_category[2] += cost_by_age[index][1]
            
        else:
            patients_per_category[-1] += 1
            cost_per_category[-1] += cost_by_age[index][1]

    for index in range(len(categories)):
        average_cost = round((cost_per_category[index] / patients_per_category[index]),2)
        avg_cost_category.append([categories[index], average_cost])
        print('The average insurance cost for people in category "{c}" is: {d} dollaras'. format(
            c = avg_cost_category[index][0], d = avg_cost_category[index][1]))

    sexes_new = [category_to_num[category] for category in sexes]
    print(sexes_new)
    cost_by_sex = [[sex, float(charge)] for sex, charge in list(zip(sexes_new,insurance_charges))]
    for i in range(len(cost_by_sex)):
        for j in range(len(cost_by_sex[i])):
            if cost_by_sex[i][j]==0:
                c=c+1
                total_sum_for_men=total_sum_for_men+cost_by_sex[i][j+1]
            elif cost_by_sex[i][j]==1:
                b=b+1
                total_sum_for_women=total_sum_for_women+cost_by_sex[i][j+1]

    print("Total charge for men" + str(total_sum_for_men))
    print("Total charge for women" + str(total_sum_for_women))
    avarage_cost_for_women=total_sum_for_women/b
    average_cost_for_men=total_sum_for_men/c
    print("Average cost for Men " + str(average_cost_for_men))
    print("Average cost for Women" + str(avarage_cost_for_women))

    print (patient_info.create_dictionary())
