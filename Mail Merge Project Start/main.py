#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
place_holder='[name]'

with open("Input/Names/invited_names.txt") as letter_names:
    names=letter_names.readlines()

with open("Input/Letters/starting_letter.txt") as letter:
    letter_contents=letter.read()
for name in names:
    striped_name=name.strip()
    new_contents= letter_contents.replace(place_holder,striped_name)
    with open(f'Output/ReadyToSend/send_for_{striped_name}.txt','w',encoding='utf-8') as completed:
        completed.write(new_contents)

