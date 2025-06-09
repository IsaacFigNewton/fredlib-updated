import os
import sys
import rdflib
from rdflib import plugin
from rdflib.serializer import Serializer

from fredlib_updated.utils.TextPreprocessor import TextPreprocessor
from fredlib_updated.FredGraph import FredGraph

__author__ = 'Misael Mongiovi, Andrea Giovanni Nuzzolese'

plugin.register('application/rdf+xml', Serializer, 'rdflib.plugins.serializers.rdfxml', 'XMLSerializer')
plugin.register('xml', Serializer, 'rdflib.plugins.serializers.rdfxml', 'XMLSerializer')


def getFredGraph(text:str,
                 key:str,
                 filename:str,
                 prefix:str = "fred:",
                 namespace:str = "http://www.ontologydesignpatterns.org/ont/fred/domain.owl#",
                 wsd:bool = False,
                 wfd:bool = False,
                 wfd_profile:str = 'b',
                 tense:bool = False,
                 roles:bool = False,
                 textannotation:str = "earmark",
                 semantic_subgraph:bool = False,
                 response_format:str = "application/rdf+xml"
                 ):

    # keyword validation
    if wfd_profile not in {'b', 'd', 't'}:
        raise KeyError(f"ERROR: Invalid wfd_profile: {wfd_profile} not in ['b', 'd', 't'].")
    if textannotation not in {"earmark", "nif"}:
        raise KeyError(f"ERROR: Invalid textannotation: {textannotation} not in ['earmark', 'nif'].")

    valid_response_formats = {
        "application/rdf+xml",
        "text/turtle",
        "application/rdf+json",
        "text/rdf+n3",
        "text/rdf+nt",
        "image/png",
    }
    if response_format not in valid_response_formats:
        raise KeyError(f"ERROR: Invalid response_format: {response_format} not in {valid_response_formats}.")

    # preprocess the text
    processed_text = TextPreprocessor(text)\
                        .preprocess_text()\
                        .processed_text

    command_to_exec = [
        "curl -G -X GET",
        f"-H \"Accept: {response_format}\"",
        f"-H \"Authorization: Bearer {key}\"",
        f"--data-urlencode text=\"{processed_text}\"",
        f"-d prefix=\"{prefix}\"",
        f"--data-urlencode namespace=\"{namespace}\"",
        f"-d wsd=\"{(str(wsd)).lower()}\"",
        f"-d wfd=\"{(str(wfd)).lower()}\"",
        f"-d wfd-profile=\"{wfd_profile}\"",
        f"-d tense=\"{(str(tense)).lower()}\"",
        f"-d roles=\"{(str(roles)).lower()}\"",
        f"-d textannotation=\"{textannotation}\"",
        f"-d semantic-subgraph=\"{(str(semantic_subgraph)).lower()}\"",
        "http://wit.istc.cnr.it/stlab-tools/fred >",
        filename
    ]
    try:
        os.system(" ".join(command_to_exec))
    except:
        print("error os running curl FRED")
        sys.exit(1)

    return openFredGraph(filename)

def openFredGraph(filename):
    rdf = rdflib.Graph()
    rdf.parse(filename)
    return FredGraph(rdf)