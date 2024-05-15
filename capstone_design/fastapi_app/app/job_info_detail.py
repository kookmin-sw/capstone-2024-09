import requests, os

api_key = os.getenv('career_api_key')
def get_list(searchJobNm, searchAptdCodes):
    page_index = 1
    job_dict = {}

    while True:
        url = f"https://www.career.go.kr/cnet/front/openapi/jobs.json?apiKey={api_key}&searchAptdCodes={searchAptdCodes}&searchJobNm={searchJobNm}&pageIndex={page_index}"
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


def get_data_from_api(searchAptdCodes: int, words):
    job_dict = {}
    for word in words:
        job_dict.update(get_list(searchAptdCodes, word))
    return job_dict