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
    url = f"https://www.career.go.kr/cnet/front/openapi/job.json?apiKey={api_key}&seq={seq}"
    url_info = f"https://www.career.go.kr/cnet/front/base/job/jobView.do?SEQ={seq}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    work_data = [item['work'] for item in data.get('workList', []) if 'work' in item]
    rel_job_data = [item['rel_job_nm'] for item in data.get('searchJobCd', []) if 'rel_job_nm' in item]
    depart_data = [item['depart_name'] for item in data.get('departList', []) if 'depart_name' in item]
    certi_data = [item['certi'] for item in data.get('certiList', []) if 'certi' in item]
    forcast_data = [item['forecast'] for item in data.get('forecastList', []) if 'forecast' in item]

    return {
        "job_nm" : data['baseInfo']['job_nm'],
        "work_data": work_data,
        "rel_job_data": rel_job_data,
        "depart_data": depart_data,
        "certi_data": certi_data,
        "forcast_data": forcast_data,
        "url_info": url_info
    }