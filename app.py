import pandas as pd


url_for_data = "https://covid.ourworldindata.org/data/owid-covid-data.csv"

data = pd.read_csv(url_for_data)

data = data[data.location == "Nepal"]
data = pd.DataFrame(data)
data = data[
    [
        "date",
        "total_cases",
        "new_cases",
        "total_deaths",
        "new_deaths",
        "icu_patients",
        "hosp_patients",
        "total_tests",
        "new_tests",
        "positive_rate",
        "tests_per_case",
        "tests_units",
        "total_vaccinations",
        "people_vaccinated",
        "new_vaccinations",
    ]
]

data.to_csv("covidNepal.csv", index=True)
