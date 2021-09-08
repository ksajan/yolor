import glob
image_file = "basic_data/images/test/*"
txt_file_name = "basic_data/test.txt"
list_file = glob.glob(image_file)
f = open(txt_file_name, 'w')
for file in list_file:
    f.write(file+'\n')
f.close()
    
# with open(txt_file_name, "w") as my_output_file:
#     with open(csv_file, "r") as my_input_file:
#         [my_output_file.write(" ".join(row)+'\n')
#          for row in csv.reader(my_input_file)]
#     my_output_file.close()
