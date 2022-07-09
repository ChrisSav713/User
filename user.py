class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        print(f'''\nFirst Name : {self.first_name}
Last Name : {self.last_name}
Email : {self.email}
Age: {self.age}''')
        if self.is_rewards_member:
            print(f'''Is a rewards card member with {self.gold_card_points} points\n''')
        else:
            print(f'''Not a rewards card member\n''')

    def enroll(self):
        if(self.is_rewards_member == True):
            print("User is already a member")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 250
            return True
    
    def spend_points(self, amount):
        if(self.gold_card_points > amount):
            self.gold_card_points -= amount
            return True
        else:
            print("Not enough points to spend")
            return False

users = []
users.append(User("Joe", "Smith", "Smith@yahoo.com", 24))
users[0].display_info()

users[0].enroll()
users[0].display_info()

users.append(User("Mary", "Jones", "Jones@gmail.com", 36))
users.append(User("Mike", "Winger", "Winger@outlook.com", 32))

users[0].spend_points(50)

users[1].enroll()

users[1].spend_points(80)
for user in users:
    user.display_info()

users[0].enroll()

users[2].spend_points(40)
