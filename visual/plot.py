def plot_CDG(df, logy=False):
    """
    Plot Cas confirmes, Deces, Gueris
    """
    df[["cas_confirmes", "deces", "gueris"]].plot(logy=logy)


def plot_SIR(df, logy=False):
    """
    Plot Susceptible, Infected, Recovered and cummulative died
    """
    df[["susceptible", "cas_confirmes", "deces", "gueris"]].plot(logy=logy)