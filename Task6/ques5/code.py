def find_highest_scorer(input_file,output_file):
    highest_scorer = ""
    highest_marks =-1
    with open(input_file, "r") as file:
        for line in file:
            parts = line.strip().split()
            name = " ".join(parts[:-1])  
            marks = int(parts[-1])  
            if marks > highest_marks:
                highest_marks = marks
                highest_scorer = name
    with open(output_file, "w") as file:
        file.write(highest_scorer)
input_filename = "students.txt"
output_filename = "high_score.txt"
find_highest_scorer(input_filename,output_filename)
print("Highest scorer's name has been written to", output_filename)