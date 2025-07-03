from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Optional: enable CORS for browser requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/domestic/Account")
def get_account():
    return {
        "accountNumber": 5,
        "name": "Robert H. Reyes",
        "email": "RobertHReyes@armyspy.com",
        "phone": "250-563-2041",
        "address1": "Line 1",
        "address2": "Line 2",
        "address3": "Line 3",
        "address4": "Line 4",
        "eirCode": "D09KK66",
        "mobileNumber": "839999999",
        "creditStatus": "Active",
        "balance": -135.98,
        "nextInvoiceDate": "2021-08-09"
    }
