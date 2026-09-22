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
            elif choice==3:
                edit_expense()
            elif choice==4:
                delete_expense()
            elif choice==5:
                search_expense()
            elif choice==6:
                summary()
            elif choice==7:
                print('you quit the program')
                break        
    except ValueError:
        print('you exited the program due to a invalid input')
        return
    return
def add_expense():
    try:
        id=int(input("enter a unique id for your expense(id should not equa to 0):"))
        amount=int(input('Enter the amount of expense you want to add:₹'))
        category=input('Enter the category of expense:')
        if category:
            description=input('Enter the description of expense:')
            date=input('Enter the date in YEAR-MON-DATE of expense(type \'Today\' to input today\'s date):')
            if date.lower()=='today':
                date_=datetime.date.today()
            else:
                date_=datetime.date.fromisoformat(date)
            dict={'id':id,'amount':amount,'category':category,'description':description,'date':str(date_)}
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
            flag=False
            id_in=int(input('enter id of the expense (if you foget id enter 0):'))
            if id_in==0:
                
                date_in=input('Enter the date of expense(YEAR-MON-DATE):')
                date_in = datetime.date.fromisoformat(date_in)
                category_in=input("enter the catogory of expense:")
                category_in.lower()
                for _ in data:
                    if _['date']==str(date_in) and _['category']==category_in:
                        print(json.dumps(_,indent=4))
                        flag=True
                if not flag:
                    print('expense not found')
            else:
                for _ in data:
                    if _['id']==id_in:
                        print(json.dumps(_,indent=4))
                        flag=True
                if not flag:
                    print('id not found try again')

def edit_expense():
    id_in=int(input('enter the id of expense(0 to quit):'))
    if id_in==0:
        return
    else:
        with open(file,'r') as File:
            data=json.load(File)
        flag=True
        for _ in data:
            if _['id']==id_in:
                flag=False
        if flag:
            print(f'----------id {id_in} not found!----------')
            edit_expense()
        while True:
            choice=int(input("what data you want to change\n1.amount\n2.category\n3.description\n4.date\n0 to exit\n:"))
            if (choice)==0:
                break
            elif choice<0 or choice>4:
                print('please enter a valid chioce!')
            else:
                if choice==1:
                    choice1='amount'
                    change=int(input('Enter the new amount:'))
                elif choice==4:
                    choice1='date'
                    change=input('Enter the new date:')
                    change=datetime.date.fromisoformat(change)
                elif choice==3:
                    choice1='description'
                    change=input('Enter the new description:')
                else:
                    choice1='category'
                    change=(input('Enter the new category:'))
                choice2=choice1
                with open(file,'w') as File:
                    for _ in data:
                        if _['id']==id_in:
                            _[choice2]=change
                    json.dump(data,File,indent=4)
                    print('-----------date changed succesfully-----------')
                

def delete_expense():
    id_in=int(input('Enter the id of the expense you want to delete:'))
    with open(file,'r') as File:
        data=json.load(File)
    flag=True
    with open(file,'w') as File:
        for d in data:
            if d['id']==id_in:
                data.remove(d)
                flag=False
                break
        if flag:
            print('data deletion failed ,id not found')
        else:
            print('------------data deletion successfull------------')
        json.dump(data,File,indent=4)
        

def search_expense():
    choice=(input('Enter the choice,on what basis do you want to search the expenses(amount,category,description,date):'))
    with open(file,'r') as File:
        data=json.load(File)
    
    sort_=int(input('in what order do you want your output\n1.increasing\n2.decreasing\n:'))
    new_data=sorted(data,key=lambda expense:expense[choice],reverse=(sort_==2))
    print(json.dumps(new_data,indent=4))
def summary():
    with open(file,'r') as File:
        data=json.load(File)
    print('---------------Here is the summary---------------')
    max_amm=data[0]['amount']
    min_amm=data[0]['amount']
    tot=0
    month=0
    date=str(datetime.date.today())
    dates=[]
    dates_month=[]
    category=set()
    for i in data:
        tot+=i['amount']
        if i['amount']>max_amm:
            max_amm=i['amount']
        if i['amount']<min_amm:
            min_amm=i['amount']
        if date[:4]==i['date'][:4]:
            month+=i['amount']
            dates_month.append(i['date'])
        dates.append(i['date'])
        category.add(i['category'])
    print('Total expenses : ₹',tot)
    print('Max expense ever: ₹',max_amm)
    print('Min expense ever: ₹',min_amm)
    print('Dates of every expenses: ',dates)
    print('Total expense of this month: ₹',month)
    print('dates of expenses this month:',dates_month)
    print('Every category of expense:',category)
    

            

if __name__=='__main__':
    main()