
__version__ = '1.0.1'
__authors__ = 'Misael Mongiovi, Andrea Giovanni Nuzzolese, Isaac Rudnick'

"""
FRED (Framework for RDF Extraction from Documents) Library
A Python library for working with FRED semantic graphs and RDF data.
"""

# Import main classes from fredlib
from .fredlib import (
    FredGraph,
    FredNode, 
    FredEdge
)

# Import enums from fredlib
from .fredlib import (
    FredType,
    NodeType,
    ResourceType,
    EdgeMotif,
    NaryMotif,
    PathMotif,
    ClusterMotif,
    Role
)

# Import functions from fredlib
from .fredlib import (
    getFredGraph,
    openFredGraph
)

# Import utility functions
from .utils import (
    preprocessText,
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
    'preprocessText',
    'clean_uri',
    'get_simplified_nx_graph',
    'plot_graph',
    'load_rdf_as_nx'
]