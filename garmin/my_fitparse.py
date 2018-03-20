
import fitparse


filepath = 'C:/Users/dgarciagarci/Google Drive/Formacion/Python for Data Science/Garmin Files/fit files from device'
filename = '6A2J5808.FIT'
fileurl = filepath +"/"+ filename

print ("hello fitparse")
print(fileurl)

fitfile = fitparse.FitFile(fileurl)

# Get all data messages that are of type record
for record in fitfile.get_messages('record'):

    # Go through all the data entries in this record
    for record_data in record:

        # Print the records name and value (and units if it has any)
        if record_data.units:
            print (record_data.name + " "+ str(record_data.value) +" "+ str(record_data.units))
        else:
            print (record_data.name +","+ str(record_data.value))
    print()
