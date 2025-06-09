
__version__ = '1.0.1'
__authors__ = 'Misael Mongiovi, Andrea Giovanni Nuzzolese, Isaac Rudnick'

"""
FRED (Framework for RDF Extraction from Documents) Library
A Python library for working with FRED semantic graphs and RDF data.
"""

# Import enums
from fredlib_updated.enum import (
    FredType,
    NodeType,
    ResourceType,
    EdgeMotif,
    NaryMotif,
    PathMotif,
    ClusterMotif,
    Role,
)

# Import main classes
from fredlib_updated.FredEdge import FredEdge
from fredlib_updated.FredNode import FredNode
from fredlib_updated.FredGraph import FredGraph

# Import functions from fredlib
from fredlib_updated.fredlib import (
    getFredGraph,
    openFredGraph,
)

# Import utility functions
from fredlib_updated.utils.TextPreprocessor import (
    TextPreprocessor,
)

# Import visualization functions
from fredlib_updated.utils.visualization import (
    clean_uri,
    get_simplified_nx_graph,
    plot_graph,
    load_rdf_as_nx
)

# Define what gets imported with "from package import *"
__all__ = [
    # Main classes
    'FredGraph',
    'FredNode',
    'FredEdge',
    
    # Enums
    'FredType',
    'NodeType', 
    'ResourceType',
    'EdgeMotif',
    'NaryMotif',
    'PathMotif',
    'ClusterMotif',
    'Role',
    
    # FRED functions
    'getFredGraph',
    'openFredGraph',
    
    # Utility functions
    'TextPreprocessor',
    'clean_uri',
    'get_simplified_nx_graph',
    'plot_graph',
    'load_rdf_as_nx'
]