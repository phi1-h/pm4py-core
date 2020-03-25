from pm4py.objects.log.importer.xes import factory as xes_importer
from pm4py.algo.discovery.inductive import factory as inductive_miner
from pm4py.algo.enhancement.decision import algorithm
from pm4py.visualization.decisiontree import factory as visualizer
import os


def execute_script():
    # in this case, we obtain a decision tree by alignments on a specific decision point
    log = xes_importer.apply(os.path.join("..", "tests", "input_data", "receipt.xes"))
    net, im, fm = inductive_miner.apply(log)
    # we need to specify a decision point. In this case, the place p_25 is a suitable decision point
    clf, feature_names, classes = algorithm.get_decision_tree(log, net, im, fm, decision_point="p_25")
    # we can visualize the decision tree
    gviz = visualizer.apply(clf, feature_names, classes, parameters={"format": "svg"})
    visualizer.view(gviz)


if __name__ == "__main__":
    execute_script()
