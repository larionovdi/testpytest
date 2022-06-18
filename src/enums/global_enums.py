from enum import Enum


class GlobalErrorMessages(Enum):
    wrong_status_code = 'Recieved status unexpected'
    wrong_element_count = "Numer of item is not equal to  expected"