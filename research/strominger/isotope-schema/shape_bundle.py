"""Load the complete local shape contract and reject caller-side weakening.

Authority here means these versioned repository files, not a truth certificate.
Byte-keyed caches reparse when any file changes; caller graphs are compared by
RDF graph isomorphism, including all constraints and blank-node structures.
"""
from functools import lru_cache
from pathlib import Path

from rdflib import Graph
from rdflib.compare import isomorphic

BASE = Path(__file__).resolve().parent
SHAPE_FILES = ("shapes.ttl", "profiles.ttl", "structure-shapes.ttl",
               "organization-shapes.ttl", "provenance-shapes.ttl", "identity-shapes.ttl", "reader-shapes.ttl")


@lru_cache(maxsize=4)
def _parse(contents):
    graph = Graph()
    for raw in contents:
        graph.parse(data=raw, format="turtle")
    return frozenset(graph)


def _authoritative_snapshot():
    return _parse(tuple((BASE / name).read_bytes() for name in SHAPE_FILES))


def _graph(triples):
    graph = Graph()
    for triple in triples:
        graph.add(triple)
    return graph


def load_shapes():
    return _graph(_authoritative_snapshot())


@lru_cache(maxsize=32)
def _equivalent(supplied, authoritative):
    return supplied == authoritative or isomorphic(_graph(supplied), _graph(authoritative))


def require_authoritative_shapes(shapes):
    if not _equivalent(frozenset(shapes), _authoritative_snapshot()):
        raise ValueError("Incomplete shape bundle or altered authoritative constraints")
