import sys
class Node:
     def __init__(self,data):
          
        self.item=data
        self.nref=None
        self.pref=None
class Phonebook:
    def __init__(self):
         self.head=None
    def traverse_list(self):
        if self.head is None:
            print("There are no contacts")
            return
        else:
            n = self.head
            while n is not None:
               if(len(n.item[0])>6):
                    print(n.item[0],"\t",n.item[1])
               else:
                    print(n.item[0],"\t\t",n.item[1])
               n = n.nref         
    def menu(self):
        s=input("Enter your name:")
        if s.isspace==True or s.isalpha()!=True:
             sys.exit("Name is a mandatory field.Process exiting due to blank field or entered other than name...")
        print("********************************************************************")
        print("\t\tLet's create your phonebook",s )
        print("********************************************************************")
        print("\tYou can now perform the following operations on this phonebook\n")
        print("1. Add a new contact")
        print("2. Remove an existing contact")
        print("3. Update a contact")
        print("4. Search for a contact")
        print("5. Display all contacts")
        print("6. Exit phonebook")
    def choice(self,g):
        if q==1:
             ans="y"
             while(ans=="y"):
                    h1=[]
                    print("********************************************************************")
                    a1=input("Enter contact name:")
                    if a1.isspace()==True or a1.isnumeric()==True:
                         sys.exit("Name is a mandatory field.Process exiting due to blank field or entered other than name...")
                    b1=int(input("Enter phone number:"))
                    if b1=="" or b1==" ":
                         sys.exit("Phone number is a mandatory field.Process exiting due to blank field or entered other than name...")
                    h1.append(a1)
                    h1.append(b1)
                    g.add_contact(h1)
                    print("Contact is successfully added")
                    print("********************************************************************")
                    ans=input("Do you want to continue operations click y otherwise click any key:")
        elif q==2:
            ans2="y"
            while(ans2=="y"):
                 print("********************************************************************")
                 z2=input(" Enter contact name:")
                 if z2.isspace()==True or z2.isnumeric()==True:
                      sys.exit("Contact name is mandatory.Process exiting due to blank field or entered other than numbers...")
                 g.delete_contacts(z2)
                 print("********************************************************************")
                 ans2=input("Do you want to continue operations click y otherwise click any key:")
        elif q==3:
              ans3="y"
              while(ans3=="y"):
                 print("********************************************************************")
                 x=[]
                 t1=input("Enter old contact name:")
                 if t1.isspace()==True or t1.isnumeric()==True:
                      sys.exit("The old contact name is mandatory.Process exiting due to blank field or entered other than name...")
                 t2=int(input("Enter old phone number:"))
                 if t2=="" or t2==" ":
                      sys.exit("The new phone number is mandatory.Process exiting due to blank field or entered other than numbers...")
                 x.append(t1)
                 x.append(t2)
                 print("********************************************************************")
                 y=[]
                 t3=input("Enter new contact name:")
                 if t3.isspace()==True or t3.isnumeric()==True:
                      sys.exit("The new contact name  is mandatory.Process exiting due to blank field or entered other than name...")
                 t4=int(input("Enter new phone number:"))
                 if t4==" " or t4=="":
                      sys.exit("The new phone number is mandatory.Process exiting due to blank field or entered other than numbers...")
                 y.append(t3)
                 y.append(t4)
                 g.update_contact(x,y)
                 print("********************************************************************")
                 ans3=input("Do you want to continue operations click y otherwise click any key:")
        elif q==4:
            ans4="y"
            while(ans4=="y"):
                 print("********************************************************************")
                 print("You can perform the following operations to search a contact")
                 print("1.Contact name ")
                 print("2.Phone number")
                 y2=int(input("Enter your choice:"))
                 g.search_contact(y2)
                 print("********************************************************************")
                 ans4=input("Do you want to continue operations click y otherwise click any key:")
        elif q==5:     
            g.display_contacts()
        elif q==6:
            print("********************************************************************")
            print("\t\tThank you for using our Phonebook system.")
            print("\t\tPlease visit again!")
            print("********************************************************************")
            print("\t\tGoodbye, have a nice day ahead!")
        else:
            print("Invalid Input")

    def add_contact(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.nref is not None:
            n = n.nref
        
        n.nref = new_node
        new_node.pref = n
    
    def delete_contacts(self,z2):
          if self.head is None:
               print("There are no contacts to delete")
               return 
          if self.head.nref is None:
               if self.head.item[0] == z2:
                    self.head = None
                    print("Your contact is successfully deleted")
               else:
                    print("Contact name not found")
                    return 

          else:
               if self.head.item[0] == z2:
                    self.head = self.head.nref
                    self.head.pref = None
                    print("Your contact is successfully deleted")
                    return

          n = self.head
          while n.nref is not None:
               if n.item[0] == z2:
                    break;
               n = n.nref
          if n.nref is not None:
               n.pref.nref = n.nref
               n.nref.pref = n.pref
               print("Your contact is successfully deleted")
               
          else:
               if n.item[0] == z2:
                    n.pref.nref = None
                    print("Your contact is successfully deleted")
               else:
                    print("Contact name not found")
    def update_contact(self,x,y):
        if self.head is None:
            print("There are no contacts to update")
            return
        new_node=Node(y)
        if self.head.item == x:
            new_node.nref=self.head.nref
            self.head=new_node
            print("Contact number is updated successfully")
            return
        n = self.head
        while n.nref is not None:
            if n.item == x:
                break;
            n = n.nref
        if n.nref is not None:
            new_node.pref=n.pref     
            new_node.nref=n.nref
            n.pref.nref=new_node
            n.nref.pref=new_node
            print("Contact number is updated successfully")
        else:
            if n.item == x:
                n.pref.nref = new_node
                new_node.pref=n.pref
                print("Contact number is updated successfully")
            else:
                print("Contact not found")
            
    def search_contact(self,y2):
         
         if(y2==1):
              wf=0
              data=input("Search:")
              if data.isspace()==True or data.isnumeric()==True:
                   sys.exit("The contact name  is mandatory for searching.Process exiting due to blank field or entered other than name...")
              k=len(data)
              if self.head is None:
                    print("There are no contacts to search")
                    return
              else:
                    n = self.head
                    while n is not None:
                         if(n.item[0][0:k].upper()==data.upper()):
                              print("Contact name:",n.item[0])
                              print("Phone number:",n.item[1])
                              wf=wf+1
                         n = n.nref
                    if(wf==0):
                         print("Contact not found")
                         
                         
         elif(y2==2):
              we=0
              data=input("Search:")
              if data.isspace()==True or data.isnumeric()!=True:
                   sys.exit("The phone number is mandatory for searching.Process exiting due to blank field or entered other than numbers...")
              kq=len(data)
              if self.head is None:
                    print("There are no contacts to search")
                    return
              else:
                    n = self.head
                    while n is not None:
                         if(str(n.item[1])[0:kq]==data):
                              print("Contact name:",n.item[0])
                              print("Phone number:",n.item[1])
                              we=we+1
                         n = n.nref
                    if(we==0):
                         print("Contact not found")

         else:
               print("Invalid Input")
    def display_contacts(self):
         print("********************************************************************")
         print("Contact_name\tPhone number")
         ch.traverse_list()
ch=Phonebook()
ch.menu()
LL=[["Nitish",8623472708],["Harshit",8834272709],["Ramesh",8995472710],["Jagadeesh",9682372711],
    ["Karthik",9112372712],["Swaraj",9216572713],["Suresh",9389072714],["Himavath",9488972715],
    ["Anasudha",9588972716],["Anasurya",9788972717],["Sampanth",9989972718],["Ruchita",8988972719],
    ["Amurtha",6388972720],["Venkat",6488972721],["Manesh",9088972722],["Mukesh",7988972721],
    ["William",7587906570],["Michael",7487906570],["Jackson",7323487907],["Lincoln",7278906578]]
LL.sort()
for i in range(len(LL)):
     value = LL[i]
     ch.add_contact(value)
while(True):
     print("********************************************************************")
     q=int(input("Enter your choice:"))
     if(q==6):
          ch.choice(ch)
          break
     else:
          ch.choice(ch)

