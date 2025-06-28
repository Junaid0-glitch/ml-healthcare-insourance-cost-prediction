from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Annotated, Literal
from prediction_helper import predict

class ModelInput(BaseModel):
    gender: Annotated[Literal["male", "female"], Field(description="Enter your gender")]
    marital_status: Annotated[Literal["married", "unmarried"], Field(description="Enter your marital status")]
    age: Annotated[int, Field(gt=0, lt=110, description="Enter your age")]
    number_of_dependants: Annotated[int, Field(gt=0, lt=8)]
    income_lakhs: Annotated[float, Field(gt=10000, description="Enter your annual income in lakhs")]
    genetical_risk: Annotated[int, Field(gt=0, lt=6)]
    insurance_plan: Annotated[Literal['Bronze', 'Silver', 'Gold'], Field(description="Choose one of the given plans")]
    employment_status: Annotated[Literal['Salaried', 'Self-Employed', 'Freelancer'], Field()]
    bmi_category: Annotated[Literal['Normal', 'Obesity', 'Overweight', 'Underweight'], Field()]
    smoking_status: Annotated[Literal['No Smoking', 'Regular', 'Occasional'], Field()]
    region: Annotated[Literal['Northwest', 'Southeast', 'Northeast', 'Southwest'], Field()]
    medical_history: Annotated[
        Literal[
            'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
            'Thyroid', 'Heart disease', 'High blood pressure & Heart disease',
            'Diabetes & Thyroid', 'Diabetes & Heart disease'
        ],
        Field()
    ]

app = FastAPI()

@app.get("/")
def greetings():
    return {"message": "Hello!"}

@app.get("/home")
def home():
    return {"message": "Welcome! The API is live"}

@app.post("/predict")
def predict_output(input_data: ModelInput):
    try:
        data = input_data.model_dump()

        converted_data = {
            "Gender": data["gender"].title(),
            "Marital Status": data["marital_status"].title(),
            "Age": data["age"],
            "Number of Dependants": data["number_of_dependants"],
            "Income in Lakhs": data["income_lakhs"],
            "Genetical Risk": data["genetical_risk"],
            "Insurance Plan": data["insurance_plan"].title(),
            "Employment Status": data["employment_status"],
            "BMI Category": data["bmi_category"],
            "Smoking Status": data["smoking_status"],
            "Region": data["region"],
            "Medical History": data["medical_history"]
        }

        prediction = predict(converted_data)
        return {"prediction": prediction}

    except KeyError as ke:
        raise HTTPException(status_code=400, detail=f"Missing field: {str(ke)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
