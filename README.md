# fastapi_demo

create virtual environment:-
python3 -m venv env
 
start virtualenv:-

for windows : => env\Scripts\activate 
for ubuntu : => source env/bin/activate

install all dependency from requirements.txt file.- => pip install -r requirements.txt

for the start our api 
=> fastapi_demo\app>python main.py 


Apis:
---------------------------------------------------------------------
---For user register:-

API = http://127.0.0.1:8000/user/register
Method = POST

Request : 
{
  "first_name": "Lucas anderson",
  "last_name": "anderson",
  "email": "anderson@gmail.com",
  "password": "Lucas@123"
}

response:
{
    "data": [
        {
            "id": "627cf79d979114a140f76c7b",
            "first_name": "Lucas anderson",
            "last_name": "anderson",
            "email": "anderson@gmail.com",
            "password": "$2b$12$SwnoqEOLpkUUJKJJytfJ3ezyajI9sBtO6KrgDRywLu4at1P.x.03i"
        }
    ],
    "code": 200,
    "message": "User added successfully."
}


----------------------------------------------------------------------
---For user login :-

API = http://127.0.0.1:8000/user/login
Method = POST

Request : 
{
  "email": "anderson@gmail.com",
  "password": "Lucas@123"
}

REsponse:
{
    "data": [
        {
            "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIM1NzEyMCwic2NvcGUiOiJhY2Nlc3NfdG9rZW4iLCJzdWIiOiJhbmRlcnNvbkBnbWFpbC5jb20ifQ.iBKT8G6TwcxF0YHnnX5oN71WMswiaId94R1m0-opQRU",
            "refresh_token": "eyJ0eXAiOiJKV1QiLCsImlhdCI6MTY1MjM1NzEyMCwic2NvcGUiOiJyZWZyZXNoX3Rva2VuIiwic3ViIjoiYW5kZXJzb25AZ21haWwuY29tIn0.ZCDLFYKPlrn7LqzMu57Zeqtl7kCw12Wm2avkiN-oxy0"
        }
    ],
    "code": 200,
    "message": "Successfully login"
}

Not:  this token is jwt Token

----------------------------------------------------------------------------
---For get all users:-

API = http://127.0.0.1:8000/user/get_user
Method = GET

Request : 
{
  "email": "anderson@gmail.com",
  "password": "Lucas@123"
}

bearer Token = eyJ0eXAiOiJKV1QiLCJhbGciOiJIM1NzEyMCwic2NvcGUiOiJhY2Nlc3NfdG9rZW4iLCJzdWIiOiJhbmRlcnNvbkBnbWFpbC5jb20ifQ.iBKT8G6TwcxF0YHnnX5oN71WMswiaId94R1m0-opQRU

note: request send with jwt access token with bearer token

Response:
 
{
    "data": [
        [
          {
                "id": "627cf79d979114a140f76c7b",
                "first_name": "Lucas anderson",
                "last_name": "anderson",
                "email": "anderson@gmail.com",
                "password": "$2b$12$SwnoqEOLpkUUJKJJytfJ3ezyajI9sBtO6KrgDRywLu4at1P.x.03i"
            }
        ]
    ],
    "code": 200,
    "message": "User data retrieved successfully"
}
 
           
-------------------------------------------------------------
---For get all users:-

API = http://127.0.0.1:8000/student/
Method = POST

Request : 
{
  "fullname": "Adams smith",
  "email": "smith@gmail.com",
  "course_of_study": "Water resources engineering",
  "year": 2,
  "gpa": "3.0"
}

bearer Token = eyJ0eXAiOiJKV1QiLCJhbGciOiJIM1NzEyMCwic2NvcGUiOiJhY2Nlc3NfdG9rZW4iLCJzdWIiOiJhbmRlcnNvbkBnbWFpbC5jb20ifQ.iBKT8G6TwcxF0YHnnX5oN71WMswiaId94R1m0-opQRU

note: request send with jwt access token with bearer token

REsponse
{
    "data": [
        {
            "id": "627cf9aa979114a140f76c7c",
            "fullname": "Adams smith",
            "email": "smith@gmail.com",
            "course_of_study": "Water resources engineering",
            "year": 2,
            "GPA": 3.0
        }
    ],
    "code": 200,
    "message": "Student added successfully."
}

-----------------------------------------------------------------------------
---For get all students :-

API = http://127.0.0.1:8000/student/
Method = GET

Note : request send with bearee token

Response:
{
    "data": [
        [

          {
            "id": "627cf9aa979114a140f76c7c",
            "fullname": "Adams smith",
            "email": "smith@gmail.com",
            "course_of_study": "Water resources engineering",
            "year": 2,
            "GPA": 3.0
        }
      
        ]
    ],
    "code": 200,
    "message": "Students data retrieved successfully"
}

-------------------------------------------------------------
---For get student by id:-

API = http://127.0.0.1:8000/student/627cf9aa979114a140f76c7c
Method = GET

627cf9aa979114a140f76c7c is student id

Note : request send with bearee token

Response :-

{
    "data": [
        {
            "id": "627cf9aa979114a140f76c7c",
            "fullname": "Adams smith",
            "email": "smith@gmail.com",
            "course_of_study": "Water resources engineering",
            "year": 2,
            "GPA": 3.0
        }
    ],
    "code": 200,
    "message": "Student data retrieved successfully"
}

----------------------------------------------------------------

---For delete student :-

API = http://127.0.0.1:8000/student/627cf9aa979114a140f76c7c
Method = DELETE

627cf9aa979114a140f76c7c is student id

Note : request send with bearee token

Response:-
{
    "data": [
        "Student with ID: 627cf9aa979114a140f76c7c removed"
    ],
    "code": 200,
    "message": "Student deleted successfully"
}

----------------------------------------------------------------
---For delete student :-

API = http://127.0.0.1:8000/student/627cf9aa979114a140f76c7c
Method = PUT

627cf9aa979114a140f76c7c is student id

Note : request send with bearee token

Request:-

{
  "fullname": "Allen martin",
  "email": "smith@gmail.com",
  "course_of_study": "Water resources and environmental engineering",
  "year": 4,
  "gpa": "4.0"
}

Response:-

{
    "data": [
        "Student with ID: 624d7ced3ef8cdf6f5a3ba56 name update is successful"
    ],
    "code": 200,
    "message": "Student dsta updated successfully"
}



