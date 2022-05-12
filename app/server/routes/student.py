from tkinter import N
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, FastAPI, HTTPException, Security,Depends
from ..crud.database  import (
    add_student,
    delete_student,
    retrieve_student,
    retrieve_students,
    update_student,
)

from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from server.models.student import (
    ErrorResponseModel,
    ResponseModel,
    StudentSchema,
    UpdateStudentModel,
)

from .auth import Auth
auth_handler = Auth()
security = HTTPBearer()
router = APIRouter()


@router.post("/", response_description="Student data added into the database")
async def add_student_data(student: StudentSchema = Body(...),credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials
    if (auth_handler.decode_token(token)):
        student = jsonable_encoder(student)
        refe_no = "1234567890"
        student["ref_no"]=refe_no
        new_student = await add_student(student)
        return ResponseModel(new_student, "Student added successfully.")
    else:
        return ErrorResponseModel("An error occurred.", 404, "Token not valid")
    
    
@router.get("/", response_description="Students retrieved")
async def get_students(credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials
    if (auth_handler.decode_token(token)):
        students = await retrieve_students()
        if students:
            return ResponseModel(students, "Students data retrieved successfully")
        return ResponseModel(students, "Empty list returned")
    else:
        return ErrorResponseModel("An error occurred.", 404, "Token not valid")


@router.get("/{id}", response_description="Student data retrieved")           
async def get_student_data(id,credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials
    if (auth_handler.decode_token(token)):
        student = await retrieve_student(id)
        if student:
            return ResponseModel(student, "Student data retrieved successfully")
        return ErrorResponseModel("An error occurred.", 404, "Student doesn't exist.")
    else:
        return ErrorResponseModel("An error occurred.", 404, "Token not valid")
    
    
@router.put("/{id}")
async def update_student_data(id: str, req: UpdateStudentModel = Body(...),credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials
    if (auth_handler.decode_token(token)):
        req = {k: v for k, v in req.dict().items() if v is not None}
        updated_student = await update_student(id, req)
        if updated_student:
            return ResponseModel(
                "Student with ID: {} name update is successful".format(id),
                "Student data updated successfully",)
        return ErrorResponseModel(
            "An error occurred",
            404,
            "There was an error updating the student data.",
        )
    else:
        return ErrorResponseModel("An error occurred.", 404, "Token not valid")
    
    
@router.delete("/{id}", response_description="Student data deleted from the database")
async def delete_student_data(id: str,credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials
    if (auth_handler.decode_token(token)):
        deleted_student = await delete_student(id)
        if deleted_student:
            return ResponseModel(
                "Student with ID: {} removed".format(id), "Student deleted successfully"
            )
        return ErrorResponseModel(
            "An error occurred", 404, "Student with id {0} doesn't exist".format(id)
        )
    else:
        return ErrorResponseModel("An error occurred.", 404, "Token not valid")


