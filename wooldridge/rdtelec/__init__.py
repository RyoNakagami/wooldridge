def load():
    """name of dataset: rdtelec
    no of variables: 6
    no of observations: 29

    +----------+--------------------------+
    | variable | label                    |
    +----------+--------------------------+
    | rd       | R&D spending, millions $ |
    | sales    | firm sales, millions $   |
    | rdintens | rd as percent of sales   |
    | lrd      | log(rd)                  |
    | lsales   | log(sales)               |
    | salessq  | sales^2                  |
    +----------+--------------------------+

    See RDCHEM.RAW"""

    import wooldridge
    return wooldridge.load(__file__, "rdtelec.csv.bz2")


def wooldridge():
    import wooldridge
    return wooldridge.dataset_list()