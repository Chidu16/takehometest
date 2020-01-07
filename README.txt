The Intercom project is intended to calculated the distance between a given list of customers and the company by considering respective
latitudes and longitudes.

There are 3 Functions namely distance, invite_customer and print_cust in 3 different files Distance.py, Invite_Customer.py and Print.py
respectively.

The first function, distance() take 2 arguments as input which are the latitude and longitude of any given customer and returns the distance
between Intercom office and the customer in KM

The second function, invite_customer() takes 2 arguments as input, the file containing the customer list and the radial distance threshold
respective and returns a list of customers containg their name ID and distance between Intercom and the customer, who are with in the given
threshold distance.

The Third Function, print_cust() takes 4 arguments as input, the list of customers returned from the 2nd function, the input file, the threshold distance
and the outputfile where final output is to e printed, respectively. This function will print the final output in the provided output file.

To run the entire program successfully, we need to run the invite_customer() first which will inturn call the distance() finction and later
we need to run print_cust() with the list returned by the first execution. A sample execution is given in Run.txt file.

===============================================================================================================================================================

The unit testing is done using the Unittest package. The Unittest.py file contains the Test class which inturn contains 3 methods namely
test_distance, test_invite_customer, test_print.

The test_distance method tests if the distance calculated by the distance() function is proper or not. The values in the test case is
checked in online tool.
The test_invite_customer method tests if the customers considered for invite are all with in the threshold range.
The test_print method tests if the list set to it is properly sorted or not.

To run the unittest we just have to run the Unitest.py file and it will execute all the test cases.


