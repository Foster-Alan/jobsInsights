from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    industry_data = read(path)
    all_indrustries = set()

    for i in industry_data:
        indrustry = i["industry"]
        if indrustry != "":
            all_indrustries.add(indrustry)

    return all_indrustries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:

    all_indrustries = []

    for i in jobs:
        if i["industry"] == industry:
            all_indrustries.append(i)

    return all_indrustries
