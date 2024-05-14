import requests, os

def get_data_from_api(career_id: int):
    api_key = os.getenv('career_api_key')
    url = f"https://www.career.go.kr/cnet/front/openapi/jobs.json?apiKey={api_key}&searchAptdCodes={career_id}&searchJobNm="
    response = requests.get(url)
    response.raise_for_status()  # Check for HTTP errors
    data = response.json()
    print(data)
    return data