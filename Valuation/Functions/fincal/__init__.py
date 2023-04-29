def pvFunction(r, n, fv):
    return fv / (1 + r) ** n


def pvPerpetuity(r, c):
    return c / r


def pvPerpetuityDue(r, c):
    return c / r * (1 + r)


def pvAnnuity(r, n, c):
    return c / r * (1 - 1 / (1 + r) ** n)


def pvAnnuityDue(r, n, c):
    """
    Objective: estimate present value of annuity due
    :param r: period rate
    :param n: number of periods
    :param c: constant cash flow
    :return:
    """
    return c / r * (1 - 1 / (1 + r) ** n) * (1 + r)


def pvGrowingAnnuity(r, n, c, g):
    """
    Objective: estimate present value of a growting annuity
    :param c: period discount rate
    :param r: number of periods
    :param n: period payment
    :param g: period growth rate (g<r)
    :return:
    """
    return c / (r - g) * (1 - (1 + g) ** n / (1 + r) ** n)


def fvFunction(r, n, pv):
    return pv * (1 + r) ** n


def fvAnnuity(r, n, c):
    return c / r * ((1 + r) ** n - 1)


def fvAnnuitDue(r, n, c):
    """
    Objective: estimate future value of annuity due
    :param r: period rate
    :param n: number of periods
    :param c: constant cash flow
    :return:
    """
    return c / r * ((1 + r) ** n - 1) * (1 + r)


def fvGrowingAnnuity(r, n, c, g):
    """
    Objective: estimate future value of a growting annuity
    :param c: period discount rate
    :param r: number of periods
    :param n: period payment
    :param g: period growth rate (g<r)
    :return:
    """
    return c / (r - g) * ((1 + r) ** n - (1 + g) * n)