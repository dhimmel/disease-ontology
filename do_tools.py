import networkx

import IGS_scripts.oboparser as oboparser

def load_do(path):
    """path is location of obo file"""
    return oboparser.parse(path, ['is_a'])

def do_to_networkx(do):
    """Return a networkx representation of do"""
    terms = do.get_terms()
    dox = networkx.MultiDiGraph()
    dox.add_nodes_from(term for term in terms if not term.obsolete)
    for term in dox:
        for typedef, id_, name in term.relationships:
            dox.add_edge(term, do.get_term(id_), key = typedef)

    assert networkx.is_directed_acyclic_graph(dox)
    return dox
