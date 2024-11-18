def read_txt_file():
    with open("lesson.txt","r") as file:
        contents=file.read()
        print(contents)
    
def write_txt_file():
    with open("lesson.txt","w")as file:
        file.write("Hello this is the new line")
def append_txt_file():
    with open("lesson.txt","a") as file:
        file.write("this is new line")
def delete_a_line(line_num):
    with open("lesson.txt","r") as file:
        lines = file.readlines()
    del lines[line_num-1]
    with open("lesson.txt","w") as file:
        file.writelines(lines)
def edit_txt_file(line_num,new_line):
    with open("lesson.txt","r") as file:
        lines = file.readlines()
    lines[line_num-1] = new_line
    with open("lesson.txt","w") as file:
        file.writelines(lines)
edit_txt_file(1,"this is the new line\n")    
# delete_a_line(2)