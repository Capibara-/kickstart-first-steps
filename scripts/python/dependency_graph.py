import pydot
import sys
import fnmatch
import os


# ________                                   .___                             ________                                   __
# \______ \   ____ ______   ____   ____    __| _/____   ____   ____ ___.__.  /  _____/  ____   ____   ________________ _/  |_  ___________
#  |    |  \_/ __ \\____ \_/ __ \ /    \  / __ |/ __ \ /    \_/ ___<   |  | /   \  ____/ __ \ /    \_/ __ \_  __ \__  \\   __\/  _ \_  __ \
#  |    `   \  ___/|  |_> >  ___/|   |  \/ /_/ \  ___/|   |  \  \___\___  | \    \_\  \  ___/|   |  \  ___/|  | \// __ \|  | (  <_> )  | \/
# /_______  /\___  >   __/ \___  >___|  /\____ |\___  >___|  /\___  > ____|  \______  /\___  >___|  /\___  >__|  (____  /__|  \____/|__|
#         \/     \/|__|        \/     \/      \/    \/     \/     \/\/              \/     \/     \/     \/           \/
#
# This script will generate a dependency tree png via maven given a few search terms for the graph nodes, it works
# by generating a graph for each module and then aggregating only the nodes (and consequently edges) that contain
# the given search terms.


DOT_FILENAME = "dependency.dot"
INCLUDED_PACKAGES = "com.wix.*,com.wixpress.*"
OUTPUT_IMAGE_NAME = "graph.png"

def main():
    if len(sys.argv) != 3:
        print "Usage: {} <main_module_dir> <comma_separated_search_strings>".format(sys.argv[0])
        return


    graph = pydot.Dot(graph_type='digraph')
    project_dir = sys.argv[1]


    os.chdir(project_dir)
    print "[+] Generating dependency graphs via maven from directory {}.".format(os.getcwd())

    # Generate dependency tree for each module using maven:
    os.system("mvn dependency:tree -DoutputType=dot -DoutputFile={} -Dincludes={}".
              format(DOT_FILENAME, INCLUDED_PACKAGES))

    # Iterate over all .dot files and generate a big graph that is the aggregate of all of them given some restrictions:
    for root, dirnames, filenames in os.walk(project_dir):
        for filename in fnmatch.filter(filenames, '*.dot'):
            filePath = os.path.join(root, filename)
            if os.stat(filePath).st_size > 0:
                add_file_to_graph(filePath, graph)
            os.remove(filePath)

    # Save created graph to png:
    output_path = os.path.join(os.getcwd(), OUTPUT_IMAGE_NAME)
    print "[+] Saving graph image to {}".format(output_path)
    graph.write_png(output_path)


def is_relevant_nodes(edge):
    search_terms = sys.argv[2].split(',')
    return reduce(lambda (x,y), (w,z): (x or w, y or z),
                  map(lambda x: (x in edge.get_source(), x in edge.get_destination()),
                      search_terms))

def add_file_to_graph(file_path, final_graph):
    print "[+] Loading graph from: {}.".format(file_path)

    graph = pydot.graph_from_dot_file(file_path)
    node_names = map(lambda node: node.get_name(), final_graph.get_nodes())
    edge_names = map(lambda edge: (edge.get_source(), edge.get_destination()),
                     final_graph.get_edges())

    for edge in graph.get_edges():
        (src_relevant, dst_relevant) = is_relevant_nodes(edge)

        if src_relevant and (edge.get_source() not in node_names):
            final_graph.add_node(pydot.Node(edge.get_source()))

        if dst_relevant and (edge.get_destination() not in node_names):
            final_graph.add_node(pydot.Node(edge.get_destination()))

        if src_relevant and dst_relevant and (edge.get_source(), edge.get_destination()) not in edge_names:
            final_graph.add_edge(pydot.Edge(edge.get_source(), edge.get_destination()))


if __name__ == "__main__":
    main()