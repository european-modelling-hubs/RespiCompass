import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def get_country_data(df, country, year=None): 
    """
    Get the data for a given country.
    """
    if year is None:
        return df.loc[df.country == country]
    else:
        return df.loc[(df.country == country) & (df.year == year)]

def compute_absolute_hospitalizations(df_hosp_rates, 
                                      df_population, 
                                      country):
    """
    Compute total annual RSV-associated hospitalizations in different age groups for a given country.
    Args:
        df_hosp_rates: dataframe with annual hospitalization rates (per 1000) in different age groups
        df_population: dataframe with the population data in different age groups
        country: country name
    Returns:
        dataframe with the total annual hospitalization burden of RSV in a given country in different age groups
    """
    df_country = get_country_data(df_hosp_rates, country)
    df_country_pop = get_country_data(df_population, country)
    
    # merge 
    df_country = df_country.merge(df_country_pop, on=["country", "age_group"])
    
    # compute the total burden of RSV in a given country.
    df_country["median_absolute_hospitalizations"] = (df_country["median_hosp_rate"] / 1000 * df_country["population"]).astype(int)
    df_country["lower_absolute_hospitalizations"] = (df_country["lower_hosp_rate"] / 1000 * df_country["population"]).astype(int)
    df_country["upper_absolute_hospitalizations"] = (df_country["upper_hosp_rate"] / 1000 * df_country["population"]).astype(int)

    # sample between lower and upper absolute burden
    df_country["sampled_absolute_hospitalizations"] = np.random.uniform(df_country["lower_absolute_hospitalizations"], df_country["upper_absolute_hospitalizations"])
    df_country["sampled_absolute_hospitalizations"] = df_country["sampled_absolute_hospitalizations"].astype(int)
            
    return df_country


def compute_synthetic_curve(country, 
                            hosp_rates, 
                            population, 
                            reference_season, 
                            hospitalization_column = "median_absolute_hospitalizations", 
                            random_weekly_sample=False):
    
    """
    This function computes the synthetic hospitalization curve for a given country, using the hospitalization rates and population estimates from RESCEU and Eurostat, and the reference season.
    Args:
        country (str): The country to compute the synthetic curve for.
        hosp_rates (pd.DataFrame): The hospitalization rates from RESCEU.
        population (pd.DataFrame): The population estimates from Eurostat.
        reference_season (pd.DataFrame): The reference season to compute the synthetic curve for. Must contain a "week" and a "hospitalizations" column.
        population_year (int): The year of the population data to use.
        hospitalization_column (str): The column in the hospitalization rates to use to compute the synthetic curve. Can be "median_absolute_hospitalizations" or "sampled_absolute_hospitalizations".
        random_weekly_sample (bool): Whether to sample the hospitalizations randomly across the weeks.
    Returns:
        pd.DataFrame: The synthetic hospitalization curve.
    """

    # compute absolute hospitalizations
    df_absolute_hospitalizations = compute_absolute_hospitalizations(hosp_rates, population, country)

    # compute hospitalizations share in reference season 
    reference_season["hospitalizations_share"] = reference_season["hospitalizations"] / reference_season["hospitalizations"].sum()

    # compute synthetic curves 
    age_groups, weeks, hospitalizations = [], [], []

    # iterate over age groups
    for grp in df_absolute_hospitalizations.age_group.unique(): 

        # get absolute hospitalizations for this age group
        abs_hosp = df_absolute_hospitalizations[df_absolute_hospitalizations.age_group == grp][hospitalization_column].values[0]

        # iterate over weeks and spread the hospitalizations evenly across the weeks
        for week in reference_season.week.unique(): 

            # get share of hospitalizations for this week
            share = reference_season.loc[reference_season.week == week]["hospitalizations_share"].values[0]

            # get hospitalizations for this week
            if random_weekly_sample == True:
                hospitalizations.append(np.random.binomial(abs_hosp, share))
            else:
                hospitalizations.append(int(abs_hosp * share))

            age_groups.append(grp)
            weeks.append(week)

    df_hospitalizations_curve = pd.DataFrame({"age_group": age_groups, "week": weeks, "hospitalizations": hospitalizations})
    df_hospitalizations_curve["country"] = country
    return df_hospitalizations_curve

