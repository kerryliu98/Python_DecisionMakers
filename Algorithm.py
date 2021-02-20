# Keeps track of the point total during questions
score = 0

# A header to start the program
print("------------------------------------")
print("      HOUSING SCORE CALCULATOR      ")
print("------------------------------------")
print()

# I am using while loop with "break" and "continue" for every factor.
# so that users don't have to start over if there's a typo in the middle.
# I am trying to be "user-centered", although it makes my program harder to read. 

# Deciding Housing Type Depending on Marriage or Parenthood
while True:
    q1 = input(
        'Do you have any legally-dependent children living with you? (y/n) \n> ')
    # Students with children regardless of marriage status 
    # should apply for “Students with Children Housing”.
    if q1.lower() == 'y':
        housing_type = 'Students with Children'
    
    # For students without children:  
    elif q1.lower() == 'n':
        q1_1 = input('Do you have a spouse living with you? (y/n) \n> ')
        # married students will be considered “Couples without Children Housing”.
        if q1_1.lower() == 'y':
            housing_type = 'Couples without Children'
        # single students will be considered “Single Students Housing”, 
        elif q1_1.lower() == 'n':
            housing_type = 'Single Student Housing'
        else:
            print("Please enter 'y' or 'n'.")
            continue
    else:
        print("Please enter 'y' or 'n'.")
        continue
    break

# Enrollment Status (Matriculated / Non-matriculated)
while True:
    q2 = input('Are you a matriculated student? (y/n) \n> ')
    if q2.lower() == 'y':
        # class year (only applies for Matriculated)
        q2_1 = input('What year are you? (1/2/3/4/...) \n> ')
        # used "try" to test whether the input is a number 
        try:
            q2_1 = int(q2_1)
        except:
            print("Please enter a number.")
            continue
        else:
            if q2_1 == 1:
                score += 4
            elif q2_1 in [2, 3, 4]:
                score += q2_1 - 1
        # full time / part time (only applies for Matriculated)
        q2_2 = input('Do you study full-time? (y/n) \n> ')
        if q2_2.lower() == 'y':
            score += 4
        elif q2_2.lower() == 'n':
            score += 2
        else:
            print("Please enter 'y' or 'n'.")
            continue

    elif q2.lower() == 'n':
        # Academic Suspension (only applies for Non-matriculated)
        q2_3 = input('Are you on Academic Suspension? (y/n) \n> ')
        if q2_3.lower() == 'y':
            score -= 4
        elif q2_3.lower() == 'n':
            pass
        else:
            print("Please enter 'y' or 'n'.")
            continue
    else:
        print("Please enter 'y' or 'n'.")
        continue
    break

# Student Source
while True:
    q3 = input(
        'Are you an out-of-province student or international student? (y/n) \n> ')
    if q3.lower() == 'y':
        score += 1
    elif q3.lower() == 'n':
        pass
    else:
        print("Please answer 'y' or 'n'.")
        continue
    break


# for people who might need special care
# a note will appear at the end
special_care = False

# Age
while True:
    q4 = input('Are you a senior citizen? (y/n) \n> ')
    if q4.lower() == 'y':
        score += 5
        special_care = True
    elif q4.lower() == 'n':
        pass
    else:
        print("Please enter 'y' or 'n'.")
        continue
    break
    
# Disabilities
while True:
    q5 = input(
        'Do you identify as a person with a visible or non-visible disability? (y/n) \n> ')
    if q5.lower() == 'y':
        score += 5
        special_care = True
    elif q5.lower() == 'n':
        pass
    else:
        print("Please enter 'y' or 'n'.")
        continue
    break

# Academic Integrity
while True:
    q6 = input('Have you ever violated Academic Integrity? (y/n) \n> ')
    if q6.lower() == 'y':
        score -= 4
    elif q6.lower() == 'n':
        pass
    else:
        print("Please answer 'y' or 'n'.")
        continue
    break

# Conviction
while True:
    q7 = input('Have you ever been convicted of a crime? (y/n) \n> ')
    if q7.lower() == 'y':
        score -= 4
    elif q7.lower() == 'n':
        pass
    else:
        print("Please enter 'y' or 'n'.")
        continue
    break


# At the end of the program, tell the user their housing type and score
print()
print("---------------RESULT---------------")
print('Housing Type:', housing_type)
print('Housing Points Score:', score)
print("------------------------------------")

# a note for senior citizens and those with disabilities
if special_care:
    print('*Please contact us as soon as possible so we can best meet your needs.')
