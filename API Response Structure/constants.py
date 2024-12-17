# result info constants
RESULT_INFO = {
    # Error codes
    "BAD_REQUEST": {"code_id": "E100", "code": "BAD_REQUEST", "message": "Bad Request", "status": False},
    "SYSTEM_ERROR": {"code_id": "E101", "code": "SYSTEM_ERROR", "message": "Internal Server Error", "status": False},
    "NOT_FOUND": {"code_id": "E102", "code": "NOT_FOUND", "message": "Not Found", "status": False},
    "IDEM_ERROR": {"code_id": "E103", "code": "IDEM_ERROR", "message": "Idempotenancy Error", "status": False},
    "REQUEST_TIMEOUT": {"code_id": "E104", "code": "REQUEST_TIMEOUT", "message": "Request Timeout Error", "status": False},
    "FORBIDDEN": {"code_id": "E105", "code": "FORBIDDEN", "message": "Access Denied", "status": False},
    "SERVICE_UNAVAILABLE": {"code_id": "E106", "code": "SERVICE_UNAVAILABLE", "message": "Service Unavailable", "status": False},

    # Success code
    "SUCCESS": {"code_id": "S100", "code": "SUCCESS", "message": "Success", "status": True},
    "RECORD_CREATED": {"code_id": "S101", "code": "RECORD_CREATED", "message": "Record Created Succesfully", "status": True},
    "RECORD_UPDATED": {"code_id": "S102", "code": "RECORD_UPDATED", "message": "Record Updated Succesfully", "status": True},
    "RECORD_DELETED": {"code_id": "S103", "code": "RECORD_DELETED", "message": "Record Deleted Succesfully", "status": True},
}
