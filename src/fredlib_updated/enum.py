from flufl.enum import Enum

class FredType(Enum):
    Situation = 1
    Event = 2
    NamedEntity = 3
    SkolemizedEntity = 4
    Quality = 5
    Concept = 6

class NodeType(Enum):
    Class = 1
    Instance = 0

class ResourceType(Enum):
    Fred = 0
    Dbpedia = 1
    Verbnet = 2

class EdgeMotif(Enum):
    Identity = 1
    Type = 2
    SubClass = 3
    Equivalence = 4
    Role = 5
    Modality = 6
    Negation = 7
    Property = 8

class NaryMotif(Enum):
    Event = 1
    Situation = 2
    OtherEvent = 3
    Concept = 4

class PathMotif(Enum):
    Type = 1
    SubClass = 2

class ClusterMotif(Enum):
    Identity = 1
    Equivalence = 2
    IdentityEquivalence = 3 #all concepts tied by a sequence of sameAs and equivalentClass in any direction

class Role(Enum):
    Agent = 1
    Patient = 2
    Theme = 3
    Location = 4
    Time = 5
    Involve = 6
    Declared = 7
    VNOblique = 8
    LocOblique = 9
    ConjOblique = 10
    Extended = 11
    Associated = 12