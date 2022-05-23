# Populates letter template with names from a list and outputs into txt files

with open("Input/Letters/starting_letter.txt") as start_file:
    start_text = start_file.read()

with open("Input/Names/invited_names.txt") as start_file:
    # start_text = start_file.read()
    name_list = start_file.readlines()

for name in name_list:
    formatted_name = name.strip()
    with open(f"Output/ReadyToSend/{formatted_name}.txt", mode="w") as new_file:
        new_file.write(start_text.replace("[name]", formatted_name))




