import requests

def get_data_from_api():
    url = "http://www.career.go.kr/cnet/openapi/getOpenApi?apiKey=631411887293319c018c3eeeb7413e40&svcType=api&svcCode=JOB&contentType=json&gubun=job_dic_list"
    response = requests.get(url)
    response.raise_for_status()  # Check for HTTP errors
    data = response.json()
    return data