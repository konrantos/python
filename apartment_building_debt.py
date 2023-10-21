from datetime import datetime
import csv
import matplotlib.pyplot as plt



# Για υλοποίηση σε οποιοδήποτε υπολογιστή χρειάζεται αντικατάσταση του "D:/1-ΣΧΟΛΗ/2-ΕΡΓΑΣΙΑ-ΑΡΧΕΣ/data.csv" με το αντίστοιχο path που βρίσκεται το αρχείο data.csv.



def show_data(start_date,end_date):
# Άνοιγμα του αρχείου CSV και ανάγνωση των περιεχομένων του ως λίστα.
 with open ("D:/1-ΣΧΟΛΗ/2-ΕΡΓΑΣΙΑ-ΑΡΧΕΣ/data.csv","r", encoding='utf-8') as file:
  data = list(csv.DictReader(file, delimiter=","))
  # Επανάληψη για κάθε γραμμή στα δεδομένα.
  for x in data:
    # Μετατροπή του πεδίου date_created σε αντικείμενο datetime.
    date_created = datetime.strptime(x['date_created'], "%Y-%m-%d %H:%M:%S.%f %z")
    # Εξαγωγή μόνο της ημερομηνίας από το αντικείμενο datetime.
    date = datetime.combine(date_created.date(), datetime.min.time())
    # Έλεγχος αν η ημερομηνία βρίσκεται εντός του καθορισμένου εύρους. 
    if start_date <= date <=end_date:
     print(x) 
  
  
  
  
     
     
     
def statistics(start_date, end_date):
  # Κενή λίστα για την αποθήκευση των δεδομένων που πληρούν τα κριτήρια.
    data_list = []
    with open ("D:/1-ΣΧΟΛΗ/2-ΕΡΓΑΣΙΑ-ΑΡΧΕΣ/data.csv","r", encoding='utf-8') as file:
        data = list(csv.DictReader(file, delimiter=","))
        # Επανάληψη για κάθε γραμμή στα δεδομένα.
        for x in data:
            date_created = datetime.strptime(x['date_created'], "%Y-%m-%d %H:%M:%S.%f %z")
            date_obj = datetime.combine(date_created.date(), datetime.min.time())
            payment_date_str = x['plirothike']
            payment_date_obj = payment_date_str
            if start_date and date_obj < start_date:
                continue
            if end_date and date_obj > end_date:
                continue
            data_list.append({
                'building_id': x['buildingID'],
                'date': date_obj,
                'provider': x['title'],
                'amount': float(x['poso']),
                'payment_date': payment_date_obj,
            })    
             # Υπολογισμός των στατιστικών δεδομένων.
        amounts = [x['amount'] for x in data_list]
        total = sum(amounts)
        count = len(amounts)
        minimum = min(amounts)
        maximum= max(amounts)
        mean = total / count
        var = sum((x - mean)**2 for x in amounts) / count
        std_dev = var**0.5
        # Εκτύπωση των στατιστικών δεδομένων.
        print("\nΜέγιστο: {:.2f}".format(maximum))
        print("Ελάχιστο: {:.2f}".format(minimum))
        print("Μέσος όρος: {:.2f}".format(mean))
        print("Τυπική απόκλιση: {:.2f}".format(std_dev))
        print("Διακύμανση: {:.2f} \n".format(var))
        
  
  
  
  
  
  
        
def sum_bills(start_date,end_date):
# Κενή λίστα για την αποθήκευση των δεδομένων που πληρούν τα κριτήρια.
 data_list1=[]
 # Λίστα για την αποθήκευση των αναγνωριστικών των κτηρίων.
 building_ids=[]
 # Λίστα για τον υπολογισμό του συνολικού ποσού οφειλών ανά κτήριο.
 total=[]
 with open ("D:/1-ΣΧΟΛΗ/2-ΕΡΓΑΣΙΑ-ΑΡΧΕΣ/data.csv","r", encoding='utf-8') as file:
  data = list(csv.DictReader(file, delimiter=","))
  # Επανάληψη για κάθε γραμμή στα δεδομένα.
  for x in data:
    date_created = datetime.strptime(x['date_created'], "%Y-%m-%d %H:%M:%S.%f %z")
    date = datetime.combine(date_created.date(), datetime.min.time())
    if start_date <= date <= end_date:
     data_list1.append(x)
  # Υπολογισμός συνολικών οφειλών ανά πολυκατοικία.   
  for x in data_list1:
    check="n"
    sumary=0.0
    if  x["plirothike"]=="false":
      if x["buildingID"] not in building_ids: 
       for y in data_list1:
        if  y["plirothike"]=="false":
         if x["buildingID"]==y["buildingID"]:
          sumary=sumary+float(y["poso"])
          check="y"
    if check=="y":
     total.append([x["buildingID"],["{:.2f}".format(sumary)]])
     building_ids.append(x["buildingID"])   
  print(total)
  return(total)  








def matplot_lib(start_date,end_date):
 import matplotlib.pyplot as plt
 with open ("D:/1-ΣΧΟΛΗ/2-ΕΡΓΑΣΙΑ-ΑΡΧΕΣ/data.csv","r", encoding='utf-8') as file:
  data = list(csv.DictReader(file, delimiter=","))
  data_list2 = []
  for x in data:
        date_created = datetime.strptime(x["date_created"], "%Y-%m-%d %H:%M:%S.%f %z")
        date = datetime.combine(date_created.date(), datetime.min.time())
        # Έλεγχος αν η ημερομηνία βρίσκεται εντός του καθορισμένου εύρους.
        if start_date <= date <= end_date:
            data_list2.append(x)
     
            
  # Σχεδιασμός γραφήματος για το συνολικό χρέος ανά πολυκατοικία.       
  building_data = {}
  total=[]
  building_ids=[]
  for x in data_list2:
        if x["buildingID"] not in building_data:
            building_data[x["buildingID"]] = []
        building_data[x["buildingID"]].append(float(x["poso"]))
  total = sorted([(building_id, sum(debts)) for building_id, debts in building_data.items()], key=lambda x: x[1])
  fig, ax = plt.subplots(figsize=(10, 12))
  ax.set_xlabel("ID πολυκατοικίας")
  ax.set_ylabel("Συνολικές οφειλές")
  for x in total:
    ax.bar(x[0],x[1] , label=f"Building {x[0]}")
  ax.legend()
  plt.title('Συνολικό χρέος ανά πολυκατοικία')
  plt.tight_layout()
  plt.show()
  
  
  # Σχεδιασμός γραφήματος για το μηνιαίο χρέος.
  amounts=[]         
  for x in data_list2:
          if x["plirothike"]=="false":
            amounts.append(float(x['poso']))
            dates = [datetime.strptime(x['date_created'], "%Y-%m-%d %H:%M:%S.%f %z").strftime('%Y-%m') for x in data_list2]
  monthly_data = {}
  for i in range(len(amounts)):
    if dates[i] not in monthly_data:
        monthly_data[dates[i]] = []
    monthly_data[dates[i]].append(amounts[i])
  for month in monthly_data:
    monthly_data[month] = sum(monthly_data[month])
  sorted_dates = sorted(monthly_data.keys())
  sorted_amounts = [monthly_data[date] for date in sorted_dates]
  plt.bar(sorted_dates, sorted_amounts, color='skyblue')
  plt.title('Οφειλές ανά μήνα')
  plt.xlabel('Μήνας')
  plt.ylabel('Ποσό')
  plt.tight_layout()
  plt.show() 
  
  
  # Σχεδιασμός γραφήματος για το πλήθος των δαπανών ανά πολυκατοικία.
  building_ids=[]
  total=[]
  for x in data_list2:
    check="n"
    sumary=0
    if  x["plirothike"]=="true":
      if x["buildingID"] not in building_ids: 
       for y in data_list2:
        if  y["plirothike"]=="true":
         if x["buildingID"]==y["buildingID"]:
          sumary=sumary+1
          check="y"
    if check=="y":
     total.append([x["buildingID"],[sumary]])
     building_ids.append(x["buildingID"])
     total = sorted(total, key=lambda x: x[1])
  for x in total:
   plt.bar(x[0],x[1])
  plt.title('Πλήθος δαπανών ανά πολυκατοικία')
  plt.xlabel('ID πολυκατοικίας')
  plt.ylabel('Πλήθος δαπανών')
  plt.tight_layout()
  plt.show()


  # Σχεδιασμός γραφήματος για το χρέος ανά πολυκατοικία ανά μήνα.
  monthly_data = {}
  for x in data_list2:
    building_id = x["buildingID"]
    if building_id not in monthly_data:
        monthly_data[building_id] = {}
    year_month = datetime.strftime(datetime.strptime(x["date_created"], "%Y-%m-%d %H:%M:%S.%f %z"), "%Y-%m")
    if year_month not in monthly_data[building_id]:
        monthly_data[building_id][year_month] = 0.0
    if x["plirothike"] == "false":
        monthly_data[building_id][year_month] += float(x["poso"])
  merged_data = {}
  for building_id, monthly_values in monthly_data.items():
    for year_month, value in monthly_values.items():
        if year_month not in merged_data:
            merged_data[year_month] = {}
        merged_data[year_month][building_id] = value       
 sorted_data = sorted(merged_data.items(), key=lambda x: (x[0], sum(x[1].values())))
 sorted_building_values = {
            month: dict(sorted(building_values.items(), key=lambda x: x[1], reverse=True))
            for month, building_values in sorted_data
        }
 for year_month, building_values in sorted_building_values.items():
            plt.bar(building_values.keys(), building_values.values(), label=year_month)
 plt.legend()
 plt.xlabel("ID πολυκατοικίας")
 plt.ylabel("Ποσό οφειλής")
 plt.title("Σύνολο οφειλών ανά πολυκατικοία ανά μήνα")
 plt.tight_layout()
 plt.show()
  
  
  
  
  
  
  
  
while True:
    try:
        # Ζητάμε από τον χρήστη να εισαγάγει την αρχική ημερομηνία.
        start_date = input("Αρχική ημερομηνία:\n")
        # Μετατροπή την εισαγωγή του χρήστη σε αντικείμενο τύπου datetime.
        start_date = datetime.strptime(start_date, "%d/%m/%Y")
        # Ζητάμε από τον χρήστη να εισαγάγει την τελική ημερομηνία.
        end_date = input("Τελική ημερομηνία:\n")
        # Μετατροπή την εισαγωγή του χρήστη σε αντικείμενο τύπου datetime.
        end_date = datetime.strptime(end_date, "%d/%m/%Y")
         # Ελέγχοςεάν η αρχική ημερομηνία είναι πριν ή ίση με την τελική ημερομηνία
        if start_date <= end_date:
          # Έξοδος από την επανάληψη αν οι ημερομηνίες είναι έγκυρες.
            break
        else:
            print("Η αρχική ημερομηνία πρέπει να είναι πριν την τελική ημερομηνία.\nΠαρακαλώ εισαγάγετε ξανά τις ημερομηνίες.\n")
    except ValueError:
        print("Λανθασμένη μορφή ημερομηνίας!\nΠαρακαλώ εισαγάγετε ξανά τις ημερομηνίες.\n")
while True:
    # Εμφάνιση μενού.
    print("\nMenu\n1.Εμφάνιση δεδομένων σε κατάλογο.\n2.Εμφάνιση στατιστικών στοιχείων.\n3.Εμφάνιση οφειλών ανά πολυκατοικία.\n4.Εμφάνιση γραφικών παραστάσεων.\n5.Αλλαγή ημερομηνιών.\n6.Έξοδος.\n")
    # Ζητάμε από τον χρήστη να εισαγάγει την επιλογή του.
    choice = input("Επιλογή: ")
    # Καλούμε την αντίστοιχη συνάρτηση σε περίπτωση που ο χρήστης εισάγει 1-4.
    if choice == "1":
        show_data(start_date, end_date)
    elif choice == "2":
        statistics(start_date, end_date)
    elif choice == "3":
        sum_bills(start_date, end_date)
    elif choice == "4":
        matplot_lib(start_date, end_date)
    # Αν εισαχυεί η τιμή '5΄, ζητάμε από τον χρήστη να εισαγάγει νέες αρχικές και τελικές ημερομηνίες και εφαρμόζονται οι ίδιοι ελέγχοι.
    elif choice == "5":
        while True:
            try:
                start_date = input("Αρχική ημερομηνία:\n")
                start_date = datetime.strptime(start_date, "%d/%m/%Y")
                end_date = input("Τελική ημερομηνία:\n")
                end_date = datetime.strptime(end_date, "%d/%m/%Y")
                if start_date <= end_date:
                    break
                else:
                    print("Η αρχική ημερομηνία πρέπει να είναι πριν την τελική ημερομηνία.\nΠαρακαλώ εισαγάγετε ξανά τις ημερομηνίες.\n")
            except ValueError:
                print("Λανθασμένη μορφή ημερομηνίας!\nΠαρακαλώ εισαγάγετε ξανά τις ημερομηνίες.\n")
    # Αν εισαχυεί η τιμή '6΄, το πρόγραμμα τερματίζεται.
    elif choice == "6":
        break
    else:
        print("Μη έγκυρη επιλογή. Παρακαλώ επιλέξτε ξανά.")