import json
import xmltodict


def xml_to_json(xml_data):
    
    xml_data_dictionary = xmltodict.parse(xml_data)
    json_data = json.dumps(xml_data_dictionary, indent=4)
    return json_data

def json_to_xml(json_data_dictionary):
    # wrap the xmltodict function
    xml_data = xmltodict.unparse(json_data_dictionary, pretty=True)
    return xml_data

def load_file(filename, type):
    file = open('./' + filename)
    if type == 'xml':
        data = file.read()
        file.close()
        return data

    elif type == 'json':
        data = json.load(file)
        file.close()
        return data

def write_json(filename, data):
    new_file = open(filename + '.json', 'w+')
    new_file.write(data)
    new_file.close()
    return 

def write_xml(filename, data):
    
    new_file = open(filename + '.xml', 'w+')
    new_file.write(data)
    


def menu():
    print('Enter the file to convert: ')
    print('Type Q! + Enter to quit')
    file_name = input()
    return file_name



    print(f'file type of {filename} not recognised')
    file.close()
    return
      
def main():
    print("Welcome to Tom's JSON - XML - JSON converter")
    
    while(True):
        filename =  menu()
        split_filename = filename.split('.')
        name = split_filename[0]
        extension = split_filename[1]

        if extension == 'xml' or extension == 'XML':
            data = load_file(filename, 'xml')
            # do xml to json conversion
            converted_data = xml_to_json(data)
            write_json(name, converted_data)
            break

        elif extension == 'json' or extension == 'JSON':
            data = load_file(filename, 'json')
            # Do json conversion
            converted_data = json_to_xml(data)
            write_xml(name, converted_data)
            break

        elif filename == 'Q!':
            print('Goodbye! Adieu! Ciao! Sayounara!')
            break

        
    
if __name__ == "__main__":
    main()
