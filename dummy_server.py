from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
# from fastapi.middleware.cors import CORSMiddleware
# from starlette.middleware import Middleware
# from starlette.middleware.cors import CORSMiddleware
from fastapi.middleware.cors import CORSMiddleware

from Priorities import CS_IT_Count, Non_CS_IT_Count, Total_count, unique_list, final_answer_as_tuple, \
    list_with_subject_count_greater_than_five, final_weightage_as_tuple, final_time_period_as_tuple

# origins = ["http://localhost:7800/"]

# middleware = [
#     Middleware(CORSMiddleware, allow_origins=origins)
# ]

# app = FastAPI(middleware=middleware)
app = FastAPI()  # an instance of the imported FastAPI.Through this instance, we can use multiple
# methods associated with FastAPI.

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

Tutors = {1:
              {"username": "pranay",
               "password": "root"
               }
          }


class Tutor(BaseModel):
    username: str
    password: str


@app.get("/Count")
def get_count():
    # return {"The no. of students belonging to CS/IT background is": CS_IT_Count}
    return ["CS_IT_Count", CS_IT_Count], ["Non_CS_IT_Count", Non_CS_IT_Count], ["Total_Count", Total_count]


@app.get("/Get-Tutor/{tutor_id}")
def get_tutor(tutor_id: int = Path(None, description="Enter the ID of the Tutor:", gt=0)):
    if tutor_id in Tutors:
        return Tutors[tutor_id]
    return {"Error": "Tutor does not exist"}


# @app.post("/Create-Tutor/{tutor_name, tutor_id}")
# def create_tutor(tutor_name: str, tutor_id: int tutor_obj: Tutor):
#     if tutor_name in Tutors:
#         return {"Error": "Tutor already exists"}
#
#     Tutors[tutor_name] = tutor_obj
#     return Tutors[tutor_name]


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

@app.get("/Tech_Stack_Certifications")
def get_tech_stack_certifications():
    return {"The following list displays the tech-stack known by students": unique_list}


@app.get("/Tech_Stack_Certifications_Known_By_Students")
def get_tech_stack_certifications():
    # return {"The following list displays Languages/Tools and no. of students who have previously learned the same"
    #         : final_answer_as_tuple}
    return {"subject_count": final_answer_as_tuple}


@app.get("/Shortlisting_the_subjects")
def get_tech_stack_certifications():
    # return {"The following list displays the subjects which are known to five or more than five students"
    #         : list_with_subject_count_greater_than_five}
    return {"shortlist"
            : list_with_subject_count_greater_than_five}


@app.get("/Weightage_per_Subject")
def get_tech_stack_certifications():
    #     return {"The following list displays subjects and their corresponding weightage"
    #             : final_weightage_as_tuple}
    return {"weightage"
            : final_weightage_as_tuple}


@app.get("/Time_Period_per_Subject")
def get_tech_stack_certifications():
    # return {"The following list displays subjects and corresponding time alloted to each subject"
    #         : final_time_period_as_tuple}
    return {"Time"
            : final_time_period_as_tuple}
