import requests, os

api_key = os.getenv('career_api_key')
def get_list(searchAptdCodes, searchJobNm):
    page_index = 1
    job_dict = {}

    while True:
        url = f"https://www.career.go.kr/cnet/front/openapi/jobs.json?apiKey={api_key}&searchAptdCodes={searchAptdCodes}&searchJobNm={searchJobNm}&pageIndex={page_index}"
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        print(data)
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

def get_detail(seq):
    url = f"http://www.career.go.kr/cnet/openapi/getOpenApi?apiKey={api_key}&svcType=api&svcCode=JOB_VIEW&contentType=json&gubun=job_dic_list&jobdicSeq={seq}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    work_data = [item['work'] for item in data.get('worklist', []) if 'work' in item]
    rel_job_data = [item['rel_job_nm'] for item in data.get('searchJobCd', []) if 'rel_job_nm' in item]
    depart_data = [item['depart_name'] for item in data.get('departList', []) if 'depart_name' in item]
    depart_data = [item['certi'] for item in data.get('certiList', []) if 'certi' in item]

    return work_data