from fastapi import FastAPI, Path, Request, File, UploadFile, Form
from typing import Optional
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse


from Priorities import CS_IT_Count, Non_CS_IT_Count, Total_count, unique_list, final_answer_as_tuple, \
    list_with_subject_count_greater_than_five, final_weightage_as_tuple, final_time_period_as_tuple

app = FastAPI()  # an instance of the imported FastAPI.Through this instance, we can use multiple
# methods associated with FastAPI.

list_of_usernames = []
list_of_passwords = []
combined_list = []
templates = Jinja2Templates(directory="Front_end")

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:7800",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Tutors = {1:
#               {"username": "pranay",
#                "password": "root"
#                }
#           }

#
# class Tutor(BaseModel):
#     username: str
#     password: str
#
#
# @app.post("/Add_Tutor")
# async def add_tutor(tutor_name: str = Form(...), password: str = Form(...)):
#     print(tutor_name)
#     list_of_usernames.append(tutor_name)
#     list_of_passwords.append(password)
#
#
# for elements in zip(list_of_usernames, list_of_passwords):
#     combined_list.append(elements)
#
#
# @app.post("/Get-file")
# async def get_file(data_file: UploadFile = File(...)):
#     print(data_file.content_type)
#     contents = await data_file.read()
#     save_file(data_file.filename, contents)
#     return {"Filename": data_file.filename}


@app.get("/Count")
async def get_count():
    # return {"The no. of students belonging to CS/IT background is": CS_IT_Count}
    return ["CS_IT_Count", CS_IT_Count], ["Non_CS_IT_Count", Non_CS_IT_Count], ["Total_Count", Total_count]


# @app.get("/CS_IT_Count")
# def get_cs_it_count():
#     # return {"The no. of students belonging to CS/IT background is": CS_IT_Count}
#     return {"CS_IT_Count": CS_IT_Count}
#
#
# @app.get("/Non_CS_IT_Count")
# def get_non_cs_it_count():
#     return {"The no. of students belonging to Non-CS/IT background is ": Non_CS_IT_Count}
#
#
# @app.get("/Total_Count")
# def get_total_count():
#     return {"The total count of students is ": Total_count}


@app.get("/index")
def index():
    return templates.TemplateResponse('welcome.html')

@app.get("/Tech_Stack_Certifications")
async def get_tech_stack_certifications():
    return {"The following list displays the tech-stack known by students": unique_list}


@app.get("/Tech_Stack_Certifications_Known_By_Students")
async def get_tech_stack_certifications():
    # return {"The following list displays Languages/Tools and no. of students who have previously learned the same"
    #         : final_answer_as_tuple}
    return {"subject_count": final_answer_as_tuple}


@app.get("/Shortlisting_the_subjects")
async def get_tech_stack_certifications():
    # return {"The following list displays the subjects which are known to five or more than five students"
    #         : list_with_subject_count_greater_than_five}
    return {"shortlist"
            : list_with_subject_count_greater_than_five}


@app.get("/Weightage_per_Subject")
async def get_tech_stack_certifications():
    #     return {"The following list displays subjects and their corresponding weightage"
    #             : final_weightage_as_tuple}
    return {"weightage"
            : final_weightage_as_tuple}


@app.get("/Time_Period_per_Subject")
async def get_tech_stack_certifications():
    # return {"The following list displays subjects and corresponding time alloted to each subject"
    #         : final_time_period_as_tuple}
    return {"Time"
            : final_time_period_as_tuple}
