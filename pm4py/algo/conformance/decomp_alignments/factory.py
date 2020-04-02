from pm4py.algo.conformance.decomp_alignments.versions import recompos_maximal

RECOMPOS_MAXIMAL = "recompos_maximal"

VERSIONS = {RECOMPOS_MAXIMAL: recompos_maximal.apply}


def apply(log, net, im, fm, variant=RECOMPOS_MAXIMAL, parameters=None):
    """
    Apply the recomposition alignment approach
    to a log and a Petri net performing decomposition

    Parameters
    --------------
    log
        Event log
    net
        Petri net
    im
        Initial marking
    fm
        Final marking
    variant
        Variant of the algorithm, possible values: recompos_maximal
    parameters
        Parameters of the algorithm

    Returns
    --------------
    aligned_traces
        For each trace, return its alignment
    """
    return VERSIONS[variant](log, net, im, fm, parameters=parameters)
