from typing import Union, List, Dict

from src.insights.jobs import read


def get_max_salary(path: str) -> int:

    salary_data = read(path)
    all_salary = set()

    for i in salary_data:
        salary = i["max_salary"]
        if salary.isdigit():
            all_salary.add(int(salary))

    return max(all_salary)


def get_min_salary(path: str) -> int:

    salary_data = read(path)
    all_salary = set()

    for i in salary_data:
        salary = i["min_salary"]
        if salary.isdigit():
            all_salary.add(int(salary))

    return min(all_salary)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:

    try:
        min_salary = job["min_salary"]
        max_min_salary = job["max_salary"]
        if int(min_salary) > int(max_min_salary):
            raise ValueError

        return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])

    except TypeError:
        raise ValueError

    except KeyError:
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
