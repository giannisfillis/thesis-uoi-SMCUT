import numpy as np
from mudpod.projections import View, IdentityProjector, JohnsonLindenstrauss
from mudpod.observer import RandomObserver, PercentileObserver
from mudpod.unimodality import UnimodalityTest, MonteCarloUnimodalityTest

def get_view(arguments: dict) -> View:
    """Get a view based on the config parameters existing in arguments.

    Args:
        arguments: a dict containing the config parameters.
    Returns:
        The parametrized view.
    """
    pt = str(arguments['<pj>'])
    if pt == 'jl':
        p = JohnsonLindenstrauss()
    elif pt == 'i':
        p = IdentityProjector()
    else:
       raise ValueError(f'The projection type: {pt} is not supported!')
    

    dt = str(arguments['--dist'])
    ot = str(arguments['--obs'])
    if ot == 'percentile':
        o = PercentileObserver(0.99, dt)
    elif ot == 'random':
        o = RandomObserver()
    else:
       raise ValueError(f'The observer type: {ot} is not supported!')

    v = View(p, o, dt)

    return v


def get_monte_carlo_test(arguments: dict, workers_num: int = 1) -> MonteCarloUnimodalityTest:
    """Get a Monte Carlo unimodality test.

    Args:
        arguments: a dict containing the config parameters.
        workers_num: an integer indicating the number of workers.
    Returns:
        A parametrized Monte Carlo unimodality test.
    """
    v = get_view(arguments)

    t = UnimodalityTest(v, float(arguments['<pv>']))
    mct = MonteCarloUnimodalityTest(
        t,
        sim_num=int(arguments['<sims>']),
        workers_num=workers_num
    )

    return mct