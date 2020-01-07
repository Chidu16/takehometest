# Function to print the given list of customers in a sorted way bbased on their User ID

def print_cust(customer_list,file_name,invite_dist, out_file_name):

    #fetching the size argument to sort the list based customer ID
    size = lambda customer_list: customer_list[0]
    customer_list.sort(key=size)

    try:
        #opening the output file in write more to print the output. If the same file is given multiple times the file is overwritten
        with open(out_file_name,'w') as fp:

            #checking if there are any customers in the list
            if len(customer_list) == 0:
                print("There are no Customers in the file {} who are within the {} KM radius of the company".format(file_name,invite_dist), file=fp)

            else:

                #printing the Customer List who is to be invited, in ascending order of their ID
                for cust in customer_list:
                        print(cust[0],cust[1],  file=fp) #Printing only the customer ID and customer name

    except (OSError, IOError):
        print("unable to writ the output to the file {}".format(out_file_name))

    else:
        fp.close