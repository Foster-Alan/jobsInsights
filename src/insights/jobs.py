from functools import lru_cache
from typing import List, Dict
import csv

@lru_cache
def read(path: str) -> List[Dict]:
 
     with open(path, "r") as file:
        jobList = list(csv.DictReader(file))
        return jobList


def get_unique_job_types(path: str) -> List[str]:
    jobs_type = read(path)
    all_job_type = set()

    for item in jobs_type:
        jobs = item['job_type']
        all_job_type.add(jobs)

    return all_job_type


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
