import pandas as pd

# share of female in a management/senior position
management_position_df = pd.read_csv("management-positions/management-positions.csv")
management_position_df.rename(columns={'Pacific Island Countries and territories':'island'}, inplace=True)
management_position_df = management_position_df[["island", "TIME_PERIOD", "OBS_VALUE", "Age"]]
management_position_df.columns = ["island", "year", "share_female_lead", "age"]
management_position_df["categories"] = management_position_df["island"]+" "+management_position_df["age"]
management_position_df.sort_values(by=["island", "year", "age"], inplace=True, ascending=False)
management_position_df.to_csv("data/management-position.csv", index=False)

# number of people with a given education level
education_level_df = pd.read_csv("education-level/education-level.csv")
education_level_df.rename(columns={'Pacific Island Countries and territories':'island'}, inplace=True)
education_level_df = education_level_df[["island", "TIME_PERIOD", "OBS_VALUE", "Sex", "Age", "Education level"]]
education_level_df.columns = ["island", "year", "count", "sex", "age", "level"]
education_level_df = education_level_df[~education_level_df["level"].isin(["Level not stated", "All education levels"])]
education_level_df.sort_values(by=["island", "year", "sex", "age", "level"])
education_level_df.to_csv("data/education-level.csv", index=False)

# number of people employed
employment_df = pd.read_csv("employed/employed.csv")
employment_df.rename(columns={'Pacific Island Countries and territories':'island'}, inplace=True)
employment_df = employment_df[["island", "TIME_PERIOD", "OBS_VALUE", "Age", "Sex", "DISABILITY"]]
employment_df.columns = ["island", "year", "count_employed", "age", "sex", "disability"]
employment_df = employment_df[employment_df["age"].isin(["55-64", "25-54"])]
employment_df = employment_df[employment_df["disability"]=="_T"]
employment_df.sort_values(by=["sex", "island", "year", "age"], inplace=True)
employment_df.to_csv("data/employment.csv", index=False)

# gender pay gap
gender_pay_gap_df = pd.read_csv("genderpaygap/genderpaygap.csv").dropna(axis=1)
gender_pay_gap_df = gender_pay_gap_df.loc[:, gender_pay_gap_df.nunique() > 1]
gender_pay_gap_df.drop(columns=['URBANIZATION', 'OCCUPATION'], inplace=True)
gender_pay_gap_df = gender_pay_gap_df.sort_values(by=["TIME_PERIOD", "Pacific Island Countries and territories", "Urbanization"])
gender_pay_gap_df.drop(columns=["GEO_PICT"], inplace=True)
gender_pay_gap_df.to_csv("data/gender-pay-gap.csv", index=False)

# employment rates
chomage_df = pd.read_csv("employment-rates/employment-rates.csv")
chomage_df.rename(columns={'Pacific Island Countries and territories':'island'}, inplace=True)
chomage_df = chomage_df[chomage_df["INDICATOR"]=="UNEMPRATE"]
chomage_df = chomage_df[chomage_df["Sex"].isin(["Male", "Female"])]
chomage_df = chomage_df[chomage_df["Age"].isin(["25-54", "55-64"])]
chomage_df = chomage_df[["island", "TIME_PERIOD", "OBS_VALUE", "Age", "Sex"]]
chomage_df.columns = ["island", "year", "unemployment_rate", "age", "sex"]
chomage_df.sort_values(by=["island", "year", "age", "sex"], inplace=True)
chomage_df.to_csv("data/employment-rates.csv", index=False)
