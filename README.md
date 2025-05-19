# abac-policy-evaluator
Project from CST412


Instructions:

Make sure that before you run the Python file, you have your input acm entry file or equivalent, requests, update acm file, and an access request (to evalauate perms).

With that, the file has file access, so it crucial that you have all the files in the same directory with the Python file.

Run the Python file in either Visual Code or run it in a terminal or cmd. Do:
py assignment3_312.py 
or
python assignment3_312.py

When loading the py file, you will then see a menu:

1. Load input ACM
2. Print ACM
3. Update ACM
4. Evalauate access requests from file
5. Exit

Option 1: 
enter the file name with the ACM entries, then the program will load the entries into memory
If file DNE, then you will receive "file not found" message.

Option 2:
prints current ACM.
shows all users/objects/perms 

Option 3:
enter filename containing update
it will then apply/remove updates and display a message for each added perm, removed, and invalid update 

Option 4: 
enter the filename containing access requests, then the program will check each request and print either permit or deny

Option 5:
ends


Notes:
can use any input file that follows the ACM format 
(see sample files, input-acm-entries, sample-requests, 
sample-update-acm-entries))
