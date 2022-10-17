from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

from Priorities import CS_IT_Count, Non_CS_IT_Count, Total_count, unique_list, final_answer_as_tuple, \
    list_with_subject_count_greater_than_five, final_weightage_as_tuple, final_time_period_as_tuple, \
    individual_student_data, check_records, individual_student_data_objects

app = FastAPI()  # an instance of the imported FastAPI. Through this instance, we can use multiple

# methods associated with FastAPI.


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


# Index route for rendering the same.
@app.get("/")
async def index(request: Request, response_class: HTMLResponse):
    return templates.TemplateResponse('index.html', context={"request": request})


# For checking the input details.
@app.post("/input_details")
def index(request: Request, username: str = Form(...), password: str = Form(...)):
    if username == 'admin' and password == 'password':
        return templates.TemplateResponse('output_selection.html', context={"request": request})
    else:
        raise HTTPException(status_code=400, detail="Incorrect username or password")


# Route for selecting the type of output to be displayed.
@app.post("/output_selection")
def selection(request: Request, details: str = Form(...)):
    if details == "individual":
        return templates.TemplateResponse('individual_student_entry.html', context={"request": request})
    else:
        return templates.TemplateResponse('batch_details_one.html', context={"request": request})


# Routes for fetching and displaying individual student data.
test = []


@app.post("/individual_student_records")
def individual_records(request: Request, individual_username: str = Form(...), birthdate: str = Form(...)):
    for student_records in individual_student_data:
        if individual_username and birthdate in student_records:
            test.clear()
            test.append(individual_username)
            test.append(birthdate)
            return templates.TemplateResponse('individual_student_details.html', context={"request": request})
        else:
            raise HTTPException(status_code=400, detail="Incorrect username or password")


Fields = ['Serial_no', 'Name', 'DOB', 'Graduation_Stream', 'Institute/University', 'Post_Graduation_Stream',
          'Institute/University', 'Tech_Stack_Certifications']


@app.get("/individual_student_details")
def check_student():
    for student_records in individual_student_data:
        for element in test:
            if element in student_records:
                final_record_as_list = [[var_1, objects] for var_1, objects in zip(Fields, student_records)]
                return {"details": final_record_as_list}
            else:
                raise HTTPException(status_code=400, detail="Incorrect username or password")


# Written for Navigation Purpose(Renders on button press)

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


# Basic Routes for returning the desired data output(Batch details).

@app.get("/Count")
async def get_count():
    return {"count": [CS_IT_Count, Non_CS_IT_Count]}


@app.get("/Tech_Stack_Certifications")
async def get_tech_stack_certifications():
    return {"The following list displays the tech-stack known by students": unique_list}


@app.get("/Tech_Stack_Certifications_Known_By_Students")
async def get_tech_stack_certifications():
    return {"subject_count": final_answer_as_tuple}


@app.get("/Shortlisting_the_subjects")
async def get_tech_stack_certifications():
    return {"shortlist"
            : list_with_subject_count_greater_than_five}


@app.get("/Weightage_per_Subject")
async def get_tech_stack_certifications():
    return {"weightage"
            : final_weightage_as_tuple}


@app.get("/Time_Period_per_Subject")
async def get_tech_stack_certifications():
    return {"Time"
            : final_time_period_as_tuple}

# if __name__ == '__main__':
#     uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
#   uvicorn.run("https://morning-eyrie-65331.herokuapp.com/", host="127.0.0.1", port=8000, log_level="info")
#   uvicorn.run("example:app", host="127.0.0.1", port=8000, log_level="info")
