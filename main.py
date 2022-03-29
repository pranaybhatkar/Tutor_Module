# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# from fastapi import FastAPI
# from typing import Optional
# from pydantic import BaseModel
# from Priorities import CS_IT_Count, Non_CS_IT_Count, Total_count, unique_list, final_answer_as_tuple, \
#     list_with_subject_count_greater_than_five, final_weightage_as_tuple, final_time_period_as_tuple
#
# app = FastAPI()  # an instance of the imported FastAPI.Through this instance, we can use multiple
#                  # methods associated with FastAPI.
#
#
# @app.get("/CS_IT_Count")
# def get_cs_it_count():
#     return {"The no. of students belonging to CS/IT background is :": CS_IT_Count}
#
#
# @app.get("/Non_CS_IT_Count")
# def get_non_cs_it_count():
#     return {"The no. of students belonging to Non-CS/IT background is :": Non_CS_IT_Count}
#
#
# @app.get("/Total_Count")
# def get_total_count():
#     return {"The total count of students is ": Total_count}
#
#
# @app.get("/Tech_Stack_Certifications")
# def get_tech_stack_certifications():
#     return {"The following list displays the tech-stack known by students :": unique_list}
#
#
# @app.get("/Tech_Stack_Certifications_Known_By_Students")
# def get_tech_stack_certifications():
#     return {"The following list displays Languages/Tools and no. of students who have previously learned the same:"
#             : final_answer_as_tuple}
#
#
# @app.get("/Shortlisting_the subjects")
# def get_tech_stack_certifications():
#     return {"The following list displays the subjects which are known to five or more than five students:"
#             : list_with_subject_count_greater_than_five}
#
#
# @app.get("/Weightage_per_Subject")
# def get_tech_stack_certifications():
#     return {"The following list displays subjects and their corresponding weightage:"
#             : final_weightage_as_tuple}
#
#
# @app.get("/Time_Period_per_Subject")
# def get_tech_stack_certifications():
#     return {"The following list displays subjects and corresponding time alloted to each subject:"
#             : final_time_period_as_tuple}