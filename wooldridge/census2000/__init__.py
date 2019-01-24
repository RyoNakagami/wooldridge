def load():
    """name of dataset: census2000
    no of variables: 6
    no of observations: 29501

    +----------+----------------------------+
    | variable | label                      |
    +----------+----------------------------+
    | state    | State (ICPSR code)         |
    | puma     | Public Use Microdata Area  |
    | educ     | educational attainment     |
    | lweekinc | log(weekly income)         |
    | exper    | years workforce experience |
    | expersq  | exper^2                    |
    +----------+----------------------------+

    Obtained from the United States Census Bureau by Professor Alberto
    Abadie of the Harvard Kennedy School of Government. Professor Abadie
    kindly provided the data."""

    import wooldridge
    return wooldridge.load(__file__, "census2000.csv.bz2")


def wooldridge():
    import wooldridge
    return wooldridge.dataset_list()