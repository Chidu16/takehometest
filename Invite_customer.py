from Distance import distance
import json

#Function to read the file of customers and retur the list of customers with the given distance from the company

def invite_customer(file_name,invite_dist):

    #list that will contain all the customers who would be invited
    customer_list = []

    try:
        #opening the file containing customer list in read mode
        with open(file_name, "r") as fp:
            #fetching the records line by line
            for cust in fp:

                # converting the text into json for easier access
                cust_json = json.loads(cust)

                #calling the distance function to calculate the actual distance by passing the customer positions
                dist = distance(float(cust_json['latitude']), float(cust_json['longitude']))

                if dist < invite_dist:
                    customer_list.append( [cust_json['user_id'], cust_json['name'], dist])

        #Calling the the print function to print the customer list

    except (OSError, IOError):
        print("unable to read the file {}".format(file_name))

    else:
        #closing the file
        fp.close()
        return customer_list


