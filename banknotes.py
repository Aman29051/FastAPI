from pydantic import BaseModel


class Banknote(BaseModel):
    variance : float
    skewness : float
    kurtosis : float
    entropy : float
