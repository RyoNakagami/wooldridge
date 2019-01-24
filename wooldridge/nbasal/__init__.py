def load():
    """name of dataset: nbasal
    no of variables: 22
    no of observations: 269

    +----------+------------------------------+
    | variable | label                        |
    +----------+------------------------------+
    | marr     | =1 if married                |
    | wage     | annual salary, thousands $   |
    | exper    | years as professional player |
    | age      | age in years                 |
    | coll     | years played in college      |
    | games    | average games per year       |
    | minutes  | average minutes per year     |
    | guard    | =1 if guard                  |
    | forward  | =1 if forward                |
    | center   | =1 if center                 |
    | points   | points per game              |
    | rebounds | rebounds per game            |
    | assists  | assists per game             |
    | draft    | draft number                 |
    | allstar  | =1 if ever all star          |
    | avgmin   | minutes per game             |
    | lwage    | log(wage)                    |
    | black    | =1 if black                  |
    | children | =1 if has children           |
    | expersq  | exper^2                      |
    | agesq    | age^2                        |
    | marrblck | marr*black                   |
    +----------+------------------------------+

    Collected by Christopher Torrente, a former MSU undergraduate, for a
    term project. He obtained the salary data and the career statistics
    from The Complete Handbook of Pro Basketball, 1995, edited by Zander
    Hollander. New York: Signet. The demographic information (marital
    status, number of children, and so on) was obtained from the teams’
    1994-1995 media guides."""

    import wooldridge
    return wooldridge.load(__file__, "nbasal.csv.bz2")


def wooldridge():
    import wooldridge
    return wooldridge.dataset_list()