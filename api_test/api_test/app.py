from datetime import date

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    day = str(date.today()).split('-', 2)[2]
    month = str(date.today()).split('-', 2)[1]
    year = str(date.today()).split('-', 2)[0]
    return {'Month': month, 'Day': day, 'Year': year}
