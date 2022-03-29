import pandas as pd
from sqlalchemy import create_engine
import mysql.connector

# connector = mysql.connector.connect(host='localhost', database='Test_2', user='root', password='root')
# print(connector) # Acknowledgement
# cursor = connector.cursor()
# print("Done!") # Acknowledgement


def importing_data_into_db():
    file_name = input("Enter the file name with .xlsx extension:")
    df = pd.read_excel(file_name)
    engine = create_engine("mysql://root:root@localhost/Test_2")
    df.to_sql('test_3', con=engine, if_exists='append', index=False)
    print("Executed!")

# importing_data_into_db() to be run only once





#
# def all_priorities():
#     cursor.execute("Select Graduation_Stream from test_3")
#
#     graduation_stream_list = []
#     for data in cursor:
#         #    print(data)        # for printing cursor contents
#         #    print(type(data))  # prints the default type of data which is <class 'tuple'>
#         graduation_stream_list.append(list(data))
#
#     # print(graduation_stream_list)
#
#     cs_it_count = 0
#     non_cs_it_count = 0
#
#     for sub_lists in graduation_stream_list:
#         for streams in sub_lists:
#             if 'Computer' in streams:
#                 cs_it_count += 1
#             elif 'Information Technology' in streams:
#                 cs_it_count += 1
#             else:
#                 non_cs_it_count += 1
#
#     print(f'The Number of Students belonging to CS/IT background is : {cs_it_count}')
#     print(f'The Number of Students belonging to Non-CS/IT background is : {non_cs_it_count}')
#
#     total_count = cs_it_count + non_cs_it_count
#     print(f'The total count of students is : {total_count}')
#
#     cursor.execute("Select Tech_Stack_Certifications from test_3")
#     tech_stack_certifications = []
#
#     for data in cursor:
#         #    print(data)  # for printing cursor contents
#         #    print(type(data))  # prints the default type of data which is <class 'tuple'>
#         tech_stack_certifications.append(list(data))
#
#     # print(tech_stack_certifications)
#
#     subjects_list = []
#     for sub_lists in tech_stack_certifications:
#         for subjects in sub_lists:
#             subjects_list.append(subjects.split(','))
#
#     # print(subjects_list)
#
#     repetitive_subjects_list = []
#     for each_sub_list in subjects_list:
#         for each_subject in each_sub_list:
#             repetitive_subjects_list.append(each_subject)
#
#     # print(repetitive_subjects_list)
#
#     unique_list = []
#
#     for every_element in repetitive_subjects_list:
#         if every_element in unique_list:
#             continue
#         else:
#             unique_list.append(every_element)
#
#     print(f'The following list displays the tech-stack known by students :\n{unique_list}')
#
#     count_unique_list = []
#     for each_element in unique_list:
#         #    print(each_element)
#         #    print(repetitive_subjects_list.count(each_element))
#         count_unique_list.append(repetitive_subjects_list.count(each_element))
#
#     # print(count_unique_list)
#
#     final_answer_as_list = [[subject, count] for subject, count in zip(unique_list, count_unique_list)]
#     final_answer_as_tuple = [(subject, count) for subject, count in zip(unique_list, count_unique_list)]
#
#     # print(final_answer_as_list)
#     print(
#         f'The following list displays Languages/Tools and no. of students \nwho have previously learned the same:\n{final_answer_as_tuple}')
#
#     list_with_subject_count_greater_than_five = []
#     for all_sub_lists in final_answer_as_list:
#         if all_sub_lists[1] >= 5:
#             # list_with_subject_count_greater_than_five.append(all_sub_lists)
#             list_with_subject_count_greater_than_five.append(tuple(all_sub_lists))  # to get the answers in tuple form,
#         # comment the above line before running this one
#
#     print(f'The following list displays the subjects which are known to five or more than five students:'
#           f'\n{list_with_subject_count_greater_than_five}')
#
#     weightage_list_corresponding_to_student_count = [['5%', 5, 7], ['10%', 10, 13], ['30%', 15, 18],
#                                                      ['45%', 19, 21], ['50%', 22, 23]]
#
#     subjects = []
#     weightages = []
#     for all_lists in list_with_subject_count_greater_than_five:
#         for each_list in weightage_list_corresponding_to_student_count:
#             if each_list[1] <= all_lists[1] <= each_list[2]:
#                 subjects.append(all_lists[0])
#                 weightages.append(each_list[0])
#
#     # print(subjects)
#     # print(weightages)
#
#     final_weightage_as_list = [[subject, weightage] for subject, weightage in zip(subjects, weightages)]
#     final_weightage_as_tuple = [(subject, weightage) for subject, weightage in zip(subjects, weightages)]
#
#     # print(final_weightage_as_list)
#     print(f'The following list displays subjects and their corresponding weightage:\n{final_weightage_as_tuple}')
#
#     list_with_weightage_and_corresponding_time_period = [['5%', '3_Days'], ['10%', '1_Week'], ['30%', '2_Weeks'],
#                                                          ['45%', '3_Weeks'], ['50%', '4_Weeks']]
#     another_subjects_list = []
#     time_period = []
#     for lists in final_weightage_as_list:
#         for elements in list_with_weightage_and_corresponding_time_period:
#             if elements[0] == lists[1]:
#                 another_subjects_list.append(lists[0])
#                 time_period.append(elements[1])
#
#     # print(another_subjects_list)
#     # print(time_period)
#
#     # final_time_period_as_list = [[topic, time] for topic, time in zip(another_subjects_list, time_period)]
#     final_time_period_as_tuple = [(topic, time) for topic, time in zip(another_subjects_list, time_period)]
#
#     # print(final_time_period_as_list)
#     print(
#         f'The following list displays subjects and corresponding time alloted to each subject:\n{final_time_period_as_tuple}')
#
#
# all_priorities()
