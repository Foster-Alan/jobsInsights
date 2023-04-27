from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:

    with open(path, "r") as file:
        job_list = list(csv.DictReader(file))
        return job_list


def get_unique_job_types(path: str) -> List[str]:
    jobs_type = read(path)
    all_job = set()

    for i in jobs_type:
        jobs = i["job_type"]
        all_job.add(jobs)

    return all_job


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:

    all_job = []

    for i in jobs:
        if i["job_type"] == job_type:
            all_job.append(i)

    return all_job
