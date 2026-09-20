import json
import datetime 
file='storage.txt'
def main():
    try:
        while True:
            print("*******************************************************************************")
            print("===== EXPENSE TRACKER =====\n1. Add Expense\n2. View Expenses\n3. Edit Expense\n4. Delete Expense\n5. Search Expenses\n6. Summary\n7. Exit")
            print("*******************************************************************************")
            choice=int(input('Enter your choice:'))
            if choice>7 or choice<1:
                print(f"{choice} is not valid")
            elif choice==1:
                add_expense()
            elif choice==2:
                view_expense()
            elif choice==7:
                print('you quit the program')
                break        
    except ValueError:
        print('you exited the program due to a invalid input')
        return
    return
def add_expense():
    try:
        amount=int(input('Enter the amount of expense you want to add:₹'))
        category=input('Enter the category of expense:')
        if category:
            description=input('Enter the description of expense:')
            date=input('Enter the date in YEAR-MON-DATE of expense(type \'Today\' to input today\'s date):')
            if date.lower()=='today':
                date_=datetime.date.today()
            else:
                date_=datetime.date.fromisoformat(date)
            dict={'amount':amount,'category':category,'description':description,'date':str(date_)}
            with open(file,'r') as File:
                try:
                    data=json.load(File)
                    data.append(dict)
                except json.decoder.JSONDecodeError:
                    data=[]
                    data.append(dict)
            with open(file,'w') as File:
                json.dump(data,File,indent=4)
                print("-------------------data added :)-------------------")
        else:
            print('category is mandatory')

    except TypeError:
        print("enter the date in correct format")
    
    

def view_expense():
    choice=int(input("enter your choice:\n1.To get all expenses till now\n2.To get a specific expense\n:"))
    if choice==1:
        with open(file,'r') as File:
            data=json.load(File)
            print('************************************************')
            for _ in data:
                print(json.dumps(_,indent=4))
            print('************************************************')

    elif choice==2:
        with open (file,'r') as File:
            data=json.load(File)
            date_in=input('Enter the date of expense(YEAR-MON-DATE):')
            date_in = datetime.date.fromisoformat(date_in)
            category_in=input("enter the catogory of expense:")
            category_in.lower()
            flag=False
            for _ in data:
                if _['date']==str(date_in) and _['category']==category_in:
                    print(json.dumps(_,indent=4))
                    flag=True
            if not flag:
                print('expense not found')

            










if __name__=='__main__':
    main()