# import json

input_file = 'food_pair_train.jsonl'
output_file = 'train_food_pairings.jsonl'

# # Open the input and output files
# with open(input_file, 'r', encoding='utf-8') as f_in, open(output_file, 'w', encoding='utf-8') as f_out:
#     for line in f_in:
#         line = line.replace("'", '"')  # Replace single quotes with double quotes
#         f_out.write(line)

# print("Conversion complete. Output saved to", output_file)

import json

with open("train_wine_bible.jsonl", 'r') as f:
    with open("food_pair_train.jsonl", 'w') as j:
        new_lines = []
        for line in f.readlines():
            print(line[8:])
            new_lines.append(json.load(str(line)))
        print(new_lines[-1])
        
        j.writelines(add + new_lines)