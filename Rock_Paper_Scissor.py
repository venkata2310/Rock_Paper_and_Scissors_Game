import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Welcome to Rock paper scissors game\n1 for rock, 2 for paper and 3 for scissors")
x=int(input("Please choose: "))
y=random.randint(1,3)
if x==1 and y==1:
    print(f"you choose \n {rock}")
    print(f"computer choose \n {rock}")
    print("It's a draw")
if x==2 and y==2:
    print(f"you choose \n {paper}")
    print(f"computer choose \n {paper}")
    print("It's a draw")
if x==3 and y==3:
    print(f"you choose \n {scissors}")
    print(f"computer choose \n {scissors}")
    print("It's a draw")
if x==1 and y==2:
    print(f"you choose \n {rock}")
    print(f"computer choose \n {paper}")
    print("you lose")
if x==1 and y==3:
    print(f"you choose \n {rock}")
    print(f"computer choose \n {scissors}")
    print("you won")
if x==2 and y==1:
    print(f"you choose \n {paper}")
    print(f"computer choose \n {rock}")
    print("you won")
if x==2 and y==3:
    print(f"you choose \n {paper}")
    print(f"computer choose \n {scissors}")
    print("you lose")
if x==3 and y==1:
    print(f"you choose \n {scissors}")
    print(f"computer choose \n {rock}")
    print("you lose")
if x==3 and y==2:
    print(f"you choose \n {scissors}")
    print(f"computer choose \n {paper}")
    print("you won")
