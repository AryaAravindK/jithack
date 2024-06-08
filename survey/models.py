from django.db import models
from typing import List
# Create your models here.


class questions:
    question:str
    answer:str
    tofQuesiton:str
    tofAnswer:bool
    multiChoiceQuestion:str
    multiChoiceAnswer:List[str]
    
    
    
    
    