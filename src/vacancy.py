import json
import os
import logging
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(BASE_DIR, "logs", "vacancy.log")
file_handler = logging.FileHandler(path, encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

class Vacancy:
    def __init__(self, title: str, url: str, salary: Optional[float], description: str, company: str):
        self.title = title
        self.url = url
        self.salary = salary if salary else "Зарплата не указана"
        self.description = description
        self.company = company

    def __repr__(self):

