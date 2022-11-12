import csv

mib_dictionary = {}
object_list = []
mibs = []
oids = []
data_types = []
object_classes = []
object_node_types = []
line_count = []
mib_entry_objects = []

class mib_entry:
    def __init__(self, mib, oid, data_type, object_class, object_node_type):
        self.mib = mib
        self.oid = oid
        self.data_type = data_type
        self.object_class = object_class
        self.object_node_type = object_node_type

    def __str__(self) -> str:
        return '{},{},{},{},{}'.format(self.mib,self.oid,self.data_type,self.object_class,self.object_node_type)


def parse_csv(csv_to_analyize):
    with open(csv_to_analyize, mode='r') as csv_file:
        csv_file_opened = csv.reader(csv_file, delimiter=',')

        
        for row in csv_file_opened:       
           for column in row:
                if column == row[0]:
                    mibs.append(column)
                elif column == row[1]:
                    if column != '':
                        oids.append(column)
                    else:
                        oid = ''
                        oids.append(oid)
                        pass
                elif column == row[2]:
                    if column != '':
                        data_types.append(column)
                    elif column == '':
                        data_types.append(column)
                        pass            
                elif column == row[3]:
                    if column != '':
                        pass
                elif column == row[4]:
                    object_classes.append(column)
                    if column == '':
                        object_classes.append(column)
                        pass
                
                elif column == row[5]:
                    object_node_types.append(column)
                else:
                    object_node_type = ''
                    object_node_types.append(object_node_type)
                    pass  
                line_count.append(1) 

parse_csv('file_to_analyize.csv')

def extract_list(list_to_extract):
    i = 0
    while i < len(list_to_extract):
        obj = mib_entry(mibs[i], oids[i], data_types[i], object_classes[i], object_node_types[i])
        mib_entry_objects.append(obj)
        i += 1
   

extract_list(mibs)
print(str(mib_entry_objects[0]))


