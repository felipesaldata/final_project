import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def covid_time_series(df):
        sns.lineplot(
            data=df,
            x="date",
            y="value",
            hue="country_region"
        )

        plt.xticks(rotation=15)
        plt.xlabel("Date")
        plt.ylabel("Value")
        plt.title("Latam covid time series")

def covid_bar_chart(df):
    sns.barplot(
        data=df,
        x="value",
        y="country_region"
    )

    plt.xlabel("Value")
    plt.ylabel("Country Region")
    plt.title("Latam countries in a global context")

def top_countries(df, countries, n):
    """Permite obtener la tabla de paises con su valor y color de acuerdo con el 
    dataframe ingresado countries y el número de elementos n que se quiere visualizar"""
    top_countries_df = (
    df
    .select_columns(["country_region", "value"])
    .groupby(["country_region"])
    .aggregate("sum")
    .sort_values("value", ascending=False)
    .reset_index()
    .head(20)
    .transform_column(
        column_name="country_region",
        function=lambda x: "red" if x in countries else "lightblue",
        dest_column_name="color"
        )
    )
    return top_countries_df.head(n)


