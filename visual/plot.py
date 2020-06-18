import matplotlib.pyplot as plt

def plot_CDG(df, logy=False):
    """
    Plot Cas confirmes, Deces, Gueris
    """
    return df[["cas_confirmes", "deces", "gueris"]].plot(logy=logy)


def plot_SCDG(df, logy=False):
    """
    Plot Susceptible, Infected, Recovered and cummulative died
    """
    return df[["susceptible", "cas_confirmes", "deces", "gueris"]].plot(logy=logy)


def plot_SIR(S, I, R, t, logy=False):
    # Plot the data on three separate curves for S(t), I(t) and R(t)
    fig = plt.figure(facecolor='w')
    ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)

    if not S is None:
        ax.plot(t, S, 'b', alpha=0.5, lw=2, label='Susceptible')

    if not I is None:
        ax.plot(t, I, 'r', alpha=0.5, lw=2, label='Infected')

    if not R is None:
        ax.plot(t, R, 'g', alpha=0.5, lw=2, label='Recovered with immunity')

    ax.set_xlabel('Time /days')
    ax.set_ylabel('Number (1000s)')

    ax.yaxis.set_tick_params(length=0)
    ax.xaxis.set_tick_params(length=0)
    ax.grid(b=True, which='major', c='w', lw=2, ls='-')
    legend = ax.legend()
    legend.get_frame().set_alpha(0.5)
    for spine in ('top', 'right', 'bottom', 'left'):
        ax.spines[spine].set_visible(False)

    return ax


def plot_SEIR(S, E, I, R, t, logy=False):
    # Plot the data on three separate curves for S(t), I(t) and R(t)
    fig = plt.figure(facecolor='w')
    ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)

    if not S is None:
        ax.plot(t, S, 'b', alpha=0.5, lw=2, label='Susceptible')

    if not E is None:
        ax.plot(t, E, 'm', alpha=0.5, lw=2, label='Exposed')

    if not I is None:
        ax.plot(t, I, 'r', alpha=0.5, lw=2, label='Infected')

    if not R is None:
        ax.plot(t, R, 'g', alpha=0.5, lw=2, label='Recovered with immunity')

    ax.set_xlabel('Time /days')
    ax.set_ylabel('Number (1000s)')

    ax.yaxis.set_tick_params(length=0)
    ax.xaxis.set_tick_params(length=0)
    ax.grid(b=True, which='major', c='w', lw=2, ls='-')
    legend = ax.legend()
    legend.get_frame().set_alpha(0.5)
    for spine in ('top', 'right', 'bottom', 'left'):
        ax.spines[spine].set_visible(False)

    return ax
