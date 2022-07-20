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


# class User(BaseModel):
#     username: str
#     disabled: Union[bool, None] = None
#
#
# class UserInDB(User):
#     hashed_password: str
#
#
@app.get("/")
async def index(request: Request, response_class: HTMLResponse):
    # return templates.TemplateResponse('input_validation.html', context={"request": request})
    return templates.TemplateResponse('index.html', context={"request": request})


#
# ------------------------------------------attempt_1-------------------------------------------------#
# fake_users_db = {
#     "manav": {
#         "username": "manav bharatiya",
#         "hashed_password": "fakehashed21021997",
#         "disabled": False,
#     },
#     "pranay": {
#         "username": "pranay bhatkar",
#         "hashed_password": "fakehashed26031994",
#         "disabled": True,
#     },
# }
# def get_user(db, username: str):
#     if username in db:
#         user_dict = db[username]
#         return UserInDB(**user_dict)
#
#
# def fake_decode_token(token):
#     user = get_user(fake_users_db, token)
#     return user
#
#
# def fake_hash_password(password: str):
#     return "fake-hashed" + password
#
#
# async def get_current_user(token: str = Depends(oauth2_scheme)):
#     user = fake_decode_token(token)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid authentication credentials",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     return user
#
#
# async def get_current_active_user(current_user: User = Depends(get_current_user)):
#     if current_user.disabled:
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user
#
#
# @app.post("/token")
# async def login(request: Request, username: str = Form(...), password: str = Form(...)):
#     user_dict = fake_users_db.get(username)
#     if not user_dict:
#         raise HTTPException(status_code=400, detail="Incorrect username or password")
#     user = UserInDB(**user_dict)
#     hashed_password = fake_hash_password(password)
#     if not hashed_password == user.hashed_password:
#         raise HTTPException(status_code=400, detail="Incorrect username or password")
#
#     return {"access_token": user.username, "token_type": "bearer"}
#
#
# @app.get("/input_details")
# async def read_users_me(request: Request, username: str = Form(...), password: str = Form(...),
#                         current_user: User = Depends(get_current_active_user)):
#     if current_user:
#         return templates.TemplateResponse('output_selection.html', context={"request": request})
#     else:
#         raise HTTPException(status_code=400, detail="Incorrect username or password")

# ------------------------------------------attempt_2----------------------------------------------------#
# @app.post("/token")
# async def received_data(form_data: OAuth2PasswordRequestForm = Depends()):
#     return {"access_token": form_data.username + "token"}


# @app.post("/input_details")
# async def index(request: Request, token: str = Depends(oauth2_scheme)):
#     if "access_token" in token:
#         return templates.TemplateResponse('output_selection.html', context={"request": request})
#     else:
#         raise HTTPException(status_code=400, detail="Incorrect username or password")

# -------------------------------------------------------------------------------------------------------#

@app.post("/input_details")
def index(request: Request, username: str = Form(...), password: str = Form(...)):
    if username == 'admin' and password == 'password':
        # return templates.TemplateResponse('batch_details_one.html', context={"request": request})
        return templates.TemplateResponse('output_selection.html', context={"request": request})
    else:
        # return {"Access Denied": "Enter Admin as user-name and 'password' as password"}
        raise HTTPException(status_code=400, detail="Incorrect username or password")


@app.post("/output_selection")
def selection(request: Request, details: str = Form(...)):
    if details == "individual":
        return templates.TemplateResponse('individual_student_entry.html', context={"request": request})
    else:
        return templates.TemplateResponse('batch_details_one.html', context={"request": request})


test = []


@app.post("/individual_student_records")
def individual_records(request: Request, individual_username: str = Form(...), birthdate: str = Form(...)):
    for student_records in individual_student_data:
        if individual_username and birthdate in student_records:
            test.append(individual_username)
            test.append(birthdate)
            return templates.TemplateResponse('individual_student_details.html', context={"request": request})
            # return {"details": student}
        else:
            # continue
            raise HTTPException(status_code=400, detail="Incorrect username or password")

    # if student:
    #     # return {"details": student}
    #     return templates.TemplateResponse('individual_student_details.html', context={"request": request})
    # else:
    #     raise HTTPException(status_code=400, detail="Incorrect username or password")


# @app.get("/individual_student_details")
# def check_student(request: Request, individual_username: str = Form(...), birthdate: str = Form(...)):
#     for student_records in individual_student_data:
#         # for details in student_records:  # try to get the output by commenting this line
#         if individual_username and birthdate in student_records:
#             return student_records
#         else:
#             continue

@app.get("/individual_student_details")
def check_student():
    for student_records in individual_student_data:
        if test[0] and test[1] in student_records:
            return student_records
        else:
            continue


# @app.api_route("/individual_student_records", methods=["GET", "POST"])


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
