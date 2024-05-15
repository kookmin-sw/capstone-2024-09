import requests, os

def get_data_from_api(career_id: int):
    api_key = os.getenv('career_api_key')
    page_index = 1
    job_dict = {}

    while True:
        url = f"https://www.career.go.kr/cnet/front/openapi/jobs.json?apiKey={api_key}&searchAptdCodes={career_id}&searchJobNm=&pageIndex={page_index}"
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        if not data['jobs']:
            break

        for job in data['jobs']:
            job_name = job['job_nm']
            job_code = job['job_cd']
            related_job_name = job['rel_job_nm']
            job_dict[job_name] = (job_code, related_job_name)

        page_index += 1

    return job_dict