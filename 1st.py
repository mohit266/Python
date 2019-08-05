
import csv

def get_length(file_path):
    with open(file_path,"r") as csvfile:
        data_reader = csv.reader(csvfile)
        data_reader_list = list(data_reader)
        #print(data_reader_list)
    return len(data_reader_list)

def append_data(file_path,name1,email1):

    next_id = get_length(file_path)
    with open(file_path,"a") as csvfile:
        data_write = csv.DictWriter(csvfile,fieldnames=['id','name','email'])
        #data_write.writeheader()
        data_write.writerow({
            "id" :  next_id,
            "name": name1,
            "email": email1
        })


append_data("mohit.csv","Anurag","anu@gmail.com")
