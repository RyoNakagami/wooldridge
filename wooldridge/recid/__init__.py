def load():
    """name of dataset: recid
    no of variables: 18
    no of observations: 1445

    +----------+--------------------------------+
    | variable | label                          |
    +----------+--------------------------------+
    | black    | =1 if black                    |
    | alcohol  | =1 if alcohol problems         |
    | drugs    | =1 if drug history             |
    | super    | =1 if release supervised       |
    | married  | =1 if married when incarc.     |
    | felon    | =1 if felony sentence          |
    | workprg  | =1 if in N.C. pris. work prg.  |
    | property | =1 if property crime           |
    | person   | =1 if crime against person     |
    | priors   | # prior convictions            |
    | educ     | years of schooling             |
    | rules    | # rules violations in prison   |
    | age      | in months                      |
    | tserved  | time served, rounded to months |
    | follow   | length follow period, months   |
    | durat    | min(time until return, follow) |
    | cens     | =1 if duration right censored  |
    | ldurat   | log(durat)                     |
    +----------+--------------------------------+

    C.-F. Chung, P. Schmidt, and A.D. Witte (1991), “Survival Analysis: A
    Survey,” Journal of Quantitative Criminology 7, 59-98. Professor Chung
    kindly provided the data."""

    import wooldridge
    return wooldridge.load(__file__, "recid.csv.bz2")


def wooldridge():
    import wooldridge
    return wooldridge.dataset_list()