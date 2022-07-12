from fastapi import FastAPI, Path, Request, File, UploadFile, Form, Depends, HTTPException, status
from typing import Optional, Union
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import sqlalchemy
import databases

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


#
# users_db = {
#     "pranay": {
#         "username": "pranay",
#         "hashed_password": "fakehashedsecret",
#         "disabled": False,
#     },
#     "manav": {
#         "username": "manav",
#         "hashed_password": "fakehashedsecret_2",
#         "disabled": True,
#     },
# }
#
#
# def fake_hash_password(password: str):
#     return "fakehashed" + password
#
#
class Admin(BaseModel):
    username: str
    password: str


class UserType(BaseModel):
    tutor: str
    student: str
    username: Union[str, None] = None
    birthdate: Union[str, None] = None


#
#
# class UserInDB(User):
#     hashed_password: str
#
#
# def get_user(db, username: str):
#     if username in db:
#         user_dict = db[username]
#         return UserInDB(**user_dict)
#
#
# def fake_decode_token(token):
#     # This doesn't provide any security at all
#     # Check the next version
#     user = get_user(users_db, token)
#     return user
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
# async def login(request: Request, form_data: OAuth2PasswordRequestForm = Depends()):
#     user_dict = users_db.get(form_data.username)
#     if not user_dict:
#         raise HTTPException(status_code=400, detail="Incorrect username or password")
#     user = UserInDB(**user_dict)
#     hashed_password = fake_hash_password(form_data.password)
#     if not hashed_password == user.hashed_password:
#         raise HTTPException(status_code=400, detail="Incorrect username or password")
#
#     return templates.TemplateResponse('welcome.html', context={"request": request})
#     # return {"access_token": user.username, "token_type": "bearer"}


# @app.get("/users/me")
# async def read_users_me(current_user: User = Depends(get_current_active_user)):
#     return current_user


@app.get("/")
async def index(request: Request, response_class: HTMLResponse):
    return templates.TemplateResponse('input_validation.html', context={"request": request})


@app.post("/input_details")
def index(request: Request, tutor_name: str = Form(...), password: str = Form(...)):
    if tutor_name == 'admin' and password == 'password':
        # return templates.TemplateResponse('batch_details_one.html', context={"request": request})
        return templates.TemplateResponse('output_selection.html', context={"request": request})
    else:
        return {"Access Denied": "Enter Admin as user-name and 'password' as password"}


# @app.post("/admin_login")
# async def check_admin(admin: Admin):
#     return admin

# @app.post("/user_type")
# async def return_user_type(user_type: UserType):
#     return user_type

# @app.post("/output_selection")
# def selection(request:Request, individual_details: str = Form(...), batch_details: str = Form(...)):
#     if individual_details:
#         return templates.TemplateResponse('individual_student_entry.html', context={"request": request})
#     else:
#         return templates.TemplateResponse('batch_details_one.html', context={"request": request})

#
# @app.get("/individual_student_records")
# def individual_records(request:Request, individual_username: str = Form(...), birthdate: str = Form(...)):
#     for student_records in individual_student_data:
#         for details in student_records: # try to get the output by commenting this line
#             if individual_username and birthdate in details:
#                 return templates.TemplateResponse('individual_student_details.html', context={"request": request})
#             else:
#                 return {"Error 404": "Student Details not found"}


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
