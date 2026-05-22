first_name = "Prapti"
last_name = "Sinha"
full_name = first_name + " " + last_name 
city = "Patna"
curr_salary = 500000
target_salary = 1500000
months_until_goal = 8

#Ways to write 
# 1. 
print(f"My Name is {full_name}. I live in {city}. I earn {curr_salary} now and want to earn {target_salary} in {months_until_goal} months.")

# 2.
print("My Name is {}. I live in {}. I earn {} now and want to earn {} in {} months."
      .format(full_name, city, curr_salary, target_salary, months_until_goal))

# 3. Old formatting
print("My Name is %s. I live in %s. I earn %d now and want to earn %d in %d months."
      % (full_name, city, curr_salary, target_salary, months_until_goal))