import pandas as pd
from sqlalchemy import create_engine
import mysql.connector
# from sample_test import importing_data_into_db as function_1

# Here, Pandas library is imported which is required for reading the Excel file that consists the input data
# of students through its function 'read_excel'. from sqlalchemy package, 'create_engine' function is imported in order
# to create an engine using necessary fields like user_name,password,host,dbname. (Required for auto table creation)
# Lastly, mysql.connector is imported for establishing a connectivity between Python and the database.
# So, that sql queries could be executed(fired) using Python.


# Run pip install openpyxl in terminal.
# openpyxl is a Necessary dependency for opening Excel files through pandas.


# df = pd.read_excel('Fynd_Batch3.xlsx')  # read_excel function of pandas to read Excel files through Python
# print(df.head())   # For reading the first 5 rows of the data to cross-check if
#                      the previous command is executed properly.
# print("Executed!")


# engine = create_engine("mysql://root:root@localhost/Test_2")  # for SQL engine Creation
# Syntax -> create_engine('database://user:password@host/database')

# df.to_sql('test_3', con=engine, if_exists='append', index=False)  # Table creation statement
# index=False # prevents pandas to add its own index
# if_exists='append' # if the table already exists, the data from the Excel sheet is added to it.
# print("Executed!")

# function_1() # to be executed only once for importing the data from excel into DB

# connector.commit() # Commit statement -> to push the data into tables, so that it gets saved and can't be rolled back
# print("Committed Successfully")

connector = mysql.connector.connect(host='bncm4psrmotblosp6jbg-mysql.services.clever-cloud.com', database='bncm4psrmotblosp6jbg', user='up2ocb1hrji2ux0d', password='KEuBHlyXcanciLh2Dtgz')
# connector = mysql.connector.connect(host='localhost', database='Test_2', user='root', password='root')
# print(connector)

cursor = connector.cursor()
# print("Done!") # Acknowledgement

# Executing SQL statements through Python and reading the data through cursor.

# cursor.execute("select * from test_3 limit 5")
# print(cursor)
# test_list = []
# for data in cursor:
#     print(data)
#     test_list.append(data)
# print(test_list)


############################################_____PRIORITY_1_____########################################################

# Logic for extracting Graduation streams from the table stored inside the Database.
# cursor.execute() performs or executes the sql query mentioned inside it and for displaying the data post execution,
# a for loop is defined, which is also used to transfer the data extracted from the table through cursor,
# to another empty list, and at the same time, the data is type-casted into list form,
# as the data we get from the table (i.e. rows) is in tuple form.

cursor.execute("Select Graduation_Stream from test_3")

Graduation_Stream_List = []
for data in cursor:
    #    print(data)        # for printing cursor contents
    #    print(type(data))  # prints the default type of data which is <class 'tuple'>
    Graduation_Stream_List.append(list(data))

# print(Graduation_Stream_List)

# Logic for getting a count of CS/IT and Non CS/IT students.
# So that a tutor could get an idea of how diverse a batch is and decide the topics to be selected accordingly.

# Two variables for counting the no. of students from CS/IT background and Non-CS/IT Background.
CS_IT_Count = 0
Non_CS_IT_Count = 0

# Two for loops taken for traversing through a couple of lists,
# First for loop is to traverse through the main list containing multiple sub lists
# Second for loop is to traverse through the contents of each sub-list which are in string from.
# if the desired sub-strings('Computer','Information Technology') are present in any of the strings,
# the count of that sub-string is increased by 1. Thus, when all the records from the input data are checked,
# we would get a specific count of students belonging to CS/IT and Non-CS/it backgrounds respectively.
# using AND, OR will not give the same output hence, if..elif..else
for sub_lists in Graduation_Stream_List:
    for streams in sub_lists:
        if 'Computer' in streams:
            CS_IT_Count += 1
        elif 'Information Technology' in streams:
            CS_IT_Count += 1
        else:
            Non_CS_IT_Count += 1

print(f'The Number of Students belonging to CS/IT background is : {CS_IT_Count}')
print(f'The Number of Students belonging to Non-CS/IT background is : {Non_CS_IT_Count}')

# Here, we get a count of students who belong to CS/IT background,
# as well as students belonging to different backgrounds.


Total_count = CS_IT_Count + Non_CS_IT_Count
print(f'The total count of students is : {Total_count}')

# The above statement gives a total count of students in the batch(i.e. 30 in this case)


# Logic for extracting Tech-Stack/certifications from the table stored inside the Database.
# cursor.execute() performs or executes the sql query mentioned inside it and for displaying the data post execution,
# a for loop is defined, which is also used to transfer the data extracted from the table through cursor,
# to another empty list, and at the same time, the data is type-casted into list form,
# as the data we get from the table (i.e. rows) is in tuple form.

cursor.execute("Select Tech_Stack_Certifications from test_3")

Tech_Stack_Certifications = []

for data in cursor:
    #    print(data)  # for printing cursor contents
    #    print(type(data))  # prints the default type of data which is <class 'tuple'>
    Tech_Stack_Certifications.append(list(data))

# print(Tech_Stack_Certifications)


# The output obtained after extracting the tech-stack table from the database is a list containing multiple
# sub-lists, which contain one string each, which tells the languages/tools that are known by students.
# so, in order to get each language/tool known by each student individually, the string inside each sub-list
# is split on the bases of a ',' separator using the split() which can be used with a python string,
# which returns a list. And, to access each string in each sub-list, two for loops are used. First for loop is to
# traverse through the sub-lists inside the tech-stack-certifications, the second for loop is to get the string
# in each sublist, and append it to another empty list which is defined just before the for loops. So, the output of
# these two for loops would be a list containing sub-lists, but inside each sub-list, individual tools/languages known
# by each student would be present. This step turned out to be unskippable since the split() method itself
# returns the output in a list format.

subjects_list = []
for sub_lists in Tech_Stack_Certifications:
    for subjects in sub_lists:
        subjects_list.append(subjects.split(','))

# print(subjects_list)

# The above statements could be written using 'List Comprehension' method (shown below)
# for reducing the length of code and in an understandable manner.

# temp_list = [subjects.split(',') for sub_lists_1 in Tech_Stack_Certifications for subjects in sub_lists_1]
# print(temp_list)

# After executing the above step, a list containing sub-lists with each language/tool known by every student
# individually is obtained. To extract each language/tool from each sub-list, two for loop are used. and to store
# the same, one empty list is defined just before the for loops. First for loop traverses through all the sub-lists
# in the Parent list, and the second for loop traverses through every sub-list, so that, each element of every sub-list
# can be accessed and appended to the empty list.

repetitive_subjects_list = []
for each_sub_list in subjects_list:
    for each_subject in each_sub_list:
        repetitive_subjects_list.append(each_subject)

# print(repetitive_subjects_list)

# The above statements could be written using 'List Comprehension' method (shown below)
# for reducing the length of code, in an understandable manner.

# another_temp_list = [each_subject for each_sub_list in subjects_list for each_subject in each_sub_list]
# print(another_temp_list)

# At this stage, a list with all the languages/tools known by each student is obtained as output of previous stage
# In this list, there are repeated elements since topics could be common, and it is possible that multiple students
# may have learned the same tool/language. Thus, to get a list where each topic is mentioned only once,
# below logic is written. An empty list is defined to which, each element is added only once using a for loop,
# inside which, an if statement checks if the topic exists in the unique list. if it is present, the loop continues
# and if it is absent, that topic is appended to the unique list.

unique_list = []

for every_element in repetitive_subjects_list:
    if every_element in unique_list:
        continue
    else:
        unique_list.append(every_element)

print(f'The following list displays the tech-stack known by students :\n{unique_list}')

# To get a count of each element in the list of unique elements, another empty list is defined. To get a count of
# each element, it is necessary to count the number of times that element is repeated in the repetitive_subjects_list.
# for this purpose, a for loop is used to get the count of each element in the unique list,
# from the repetitive_subjects_list, which is then appended to the empty list defined just before the for loop.

count_unique_list = []
for each_element in unique_list:
    #    print(each_element)
    #    print(repetitive_subjects_list.count(each_element))
    count_unique_list.append(repetitive_subjects_list.count(each_element))

# print(count_unique_list)

# Finally, to bind together the outputs, i.e. to display each subject and no. of students who have studied
# the subject before, 'list comprehension' is used along with zip function which binds together, corresponding elements
# of two lists and returns a list of tuples. Here, an option to convert that list of tuples into a
# list of lists is also given.

final_answer_as_list = [[subject, count] for subject, count in zip(unique_list, count_unique_list)]
final_answer_as_tuple = [(subject, count) for subject, count in zip(unique_list, count_unique_list)]

# print(final_answer_as_list)
print(
    f'The following list displays Languages/Tools and no. of students \nwho have previously learned the same:\n{final_answer_as_tuple}')

# A tutor can design the flow of syllabus on these two factors:
# A) A Count of CS/IT and Non-CS/IT Students
# B) A list of subjects along with the count of students who have studied the subject before.

############################################_____PRIORITY_2_____########################################################

# Logic written below is to shortlist the topics from the available list of Languages/tools known by the students.
# To do so, any language/tool known by more than 5 students is shortlisted, and for obtaining the same result,
# an empty list is defined, a for loop is used to traverse through all the sub-lists in the list of languages/tools
# known. The count of each subject in each sub-list is checked, if it is greater than five, the whole sub-list is
# appended to the empty list defined just before the for loop.


# subjects_with_count_greater_than_five = []
# for every_count in count_unique_list:
#     if every_count >= 5:
#         subjects_with_count_greater_than_five.append(every_count)
#     else:
#         continue
#
# print(subjects_with_count_greater_than_five)

list_with_subject_count_greater_than_five = []
for all_sub_lists in final_answer_as_list:
    if all_sub_lists[1] >= 5:
        # list_with_subject_count_greater_than_five.append(all_sub_lists)
        list_with_subject_count_greater_than_five.append(tuple(all_sub_lists))  # to get the answers in tuple form,
    # comment the above line before running this one

print(f'The following list displays the subjects which are known to five or more than five students:'
      f'\n{list_with_subject_count_greater_than_five}')

############################################_____PRIORITY_3_____########################################################

# For calculating and assigning the weightage per subject, below logic is written. Depending on the type of
# subjects and their count, weightage is assigned to these subjects. For doing the same, a list containing
# multiple sub-lists where each sub-list has a weightage and the range for which that weightage is applicable,
# is defined. Along with this list, two more empty lists are defined to store the subjects and their
# weightages individually. Two for loops are defined, first, to access each sub-list in the list with subject
# count greater than five, and second, to access each sub-list in the list with weightages and their range,
# defined earlier.

weightage_list_corresponding_to_student_count = [['5%', 5, 7], ['10%', 10, 13], ['30%', 15, 18],
                                                 ['45%', 19, 21], ['50%', 22, 23]]

subjects = []
weightages = []
for all_lists in list_with_subject_count_greater_than_five:
    for each_list in weightage_list_corresponding_to_student_count:
        if each_list[1] <= all_lists[1] <= each_list[2]:
            subjects.append(all_lists[0])
            weightages.append(each_list[0])

# print(subjects)
# print(weightages)

# The above logic could have been written using an if - elif - else ladder,
# but it would have increased the length of the code as well.

# Finally, to bind together the outputs, i.e. subjects and their corresponding weightages
# "list comprehension" is used along with zip function which binds together, corresponding elements
# of the two lists and returns a list of tuples. Here, an option to convert that list of tuples into a
# list of lists is also given.


final_weightage_as_list = [[subject, weightage] for subject, weightage in zip(subjects, weightages)]
final_weightage_as_tuple = [(subject, weightage) for subject, weightage in zip(subjects, weightages)]

# print(final_weightage_as_list)
print(f'The following list displays subjects and their corresponding weightage:\n{final_weightage_as_tuple}')

############################################_____PRIORITY_4_____########################################################

# For calculating and assigning time per subject, the below logic is written. A list containing the weightages obtained
# from earlier stage and designated time period for each value of the calculated weightages is defined. Also,
# two empty lists are defined for storing subjects and their corresponding time periods. To obtain the same, Two for
# loops are defined, first, to traverse through all the sub-lists in the list containing subjects and their weightages
# and second, to traverse through the list defined earlier, containing weightages and corresponding time periods.


list_with_weightage_and_corresponding_time_period = [['5%', '3_Days'], ['10%', '1_Week'], ['30%', '2_Weeks'],
                                                     ['45%', '3_Weeks'], ['50%', '4_Weeks']]
another_subjects_list = []
time_period = []
for lists in final_weightage_as_list:
    for elements in list_with_weightage_and_corresponding_time_period:
        if elements[0] == lists[1]:
            another_subjects_list.append(lists[0])
            time_period.append(elements[1])

# print(another_subjects_list)
# print(time_period)

# Finally, to bind together the outputs, i.e. subjects and the corresponding time period allocated to them
# "list comprehension" is used along with zip function which binds together, corresponding elements
# of the two lists and returns a list of tuples. Here, an option to convert that list of tuples into a
# list of lists is also given.

final_time_period_as_list = [[topic, time] for topic, time in zip(another_subjects_list, time_period)]
final_time_period_as_tuple = [(topic, time) for topic, time in zip(another_subjects_list, time_period)]

# print(final_time_period_as_list)
print(
    f'The following list displays subjects and corresponding time alloted to each subject:\n{final_time_period_as_tuple}')


############################################_____PRIORITY_5_____########################################################

# For displaying individual records of a student, following logic is written.

cursor.execute("Select * from test_3")
individual_student_data = []

for data in cursor:
    individual_student_data.append(data)

# print(individual_student_data)



########################################################################################################################
