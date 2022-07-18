from fastapi import FastAPI, Path, Request, File, UploadFile, Form, Depends, HTTPException, status
from typing import Optional, Union
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from Priorities import CS_IT_Count, Non_CS_IT_Count, Total_count, unique_list, final_answer_as_tuple, \
    list_with_subject_count_greater_than_five, final_weightage_as_tuple, final_time_period_as_tuple, \
    individual_student_data

app = FastAPI()  # an instance of the imported FastAPI. Through this instance, we can use multiple
# methods associated with FastAPI.

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

templates = Jinja2Templates(directory="templates")

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


@app.get("/")
async def index(request: Request, response_class: HTMLResponse):
    # return templates.TemplateResponse('input_validation.html', context={"request": request})
    return templates.TemplateResponse('index.html', context={"request": request})


@app.post("/token")
async def received_data(form_data: OAuth2PasswordRequestForm = Depends()):
    return {"access_token": form_data.username + "token"}


@app.post("/input_details")
async def index(request: Request, token: str = Depends(oauth2_scheme)):
    if token:
        return templates.TemplateResponse('output_selection.html', context={"request": request})
    else:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

# @app.post("/input_details")
# def index(request: Request, username: str = Form(...), password: str = Form(...)):
#     if username == 'admin' and password == 'password':
#         # return templates.TemplateResponse('batch_details_one.html', context={"request": request})
#         return templates.TemplateResponse('output_selection.html', context={"request": request})
#     else:
#         # return {"Access Denied": "Enter Admin as user-name and 'password' as password"}
#         raise HTTPException(status_code=400, detail="Incorrect username or password")


@app.post("/output_selection")
def selection(request: Request, details: str = Form(...)):
    if details == "individual":
        return templates.TemplateResponse('individual_student_entry.html', context={"request": request})
    else:
        return templates.TemplateResponse('batch_details_one.html', context={"request": request})


def check_student(request: Request, individual_username: str = Form(...), birthdate: str = Form(...)):
    for student_records in individual_student_data:
        # for details in student_records:  # try to get the output by commenting this line
        if individual_username and birthdate in student_records:
            return student_records
        else:
            continue


@app.api_route("/individual_student_records", methods=["GET", "POST"])
def individual_records(request: Request, individual_username: str = Form(...), birthdate: str = Form(...),
                       student: dict = Depends(check_student)):
    # for student_records in individual_student_data:
    #     if individual_username and birthdate in student_records:
    #         return {"details": student}
    #     else:
    #         continue

    if student:
        return {"details"
                : student}
    else:
        return {"Error 404": "Student Details not found"}


@app.get("/output")
async def index(request: Request, response_class: HTMLResponse):
    return templates.TemplateResponse('batch_details_two.html', context={"request": request})


@app.get("/previous_output")
async def index(request: Request, response_class: HTMLResponse):
    return templates.TemplateResponse('batch_details_one.html', context={"request": request})


@app.get("/selection_page")
async def index(request: Request, response_class: HTMLResponse):
    return templates.TemplateResponse('output_selection.html', context={"request": request})


@app.get("/individual_entry")
async def index(request: Request, response_class: HTMLResponse):
    return templates.TemplateResponse('individual_student_entry.html', context={"request": request})


@app.get("/Count")
async def get_count():
    # return {"The no. of students belonging to CS/IT background is": CS_IT_Count}
    # return ["CS_IT_Count", CS_IT_Count], ["Non_CS_IT_Count", Non_CS_IT_Count], ["Total_Count", Total_count]
    return {"count": [CS_IT_Count, Non_CS_IT_Count]}


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

# if __name__ == '__main__':
#     uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
#   uvicorn.run("https://morning-eyrie-65331.herokuapp.com/", host="127.0.0.1", port=8000, log_level="info")
#   uvicorn.run("example:app", host="127.0.0.1", port=8000, log_level="info")
