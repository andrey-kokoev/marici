#!/usr/bin/env python3
"""Bounded constructor synthesis from explicit SCC obstruction signatures."""
from __future__ import annotations

import re

RULES = [
    {
        "id": "rh-prime-shell-adjoint-jet-family",
        "terms": {"prime", "shell", "adjoint", "residual", "family", "jet"},
        "required_terms": {"prime", "shell", "adjoint"},
        "exclusive": True,
        "constructor": "source-normalized five-port adjoint cancellation for every prime shell and every parameter-root jet below Xi multiplicity",
        "hostile": "isolate the eventually sign-definite ordinary component and require the declared wall, reciprocal, derivative, and ordered-linking compensators to cancel it shellwise for each jet",
        "forbids": "promoting arithmetic summability, scalar Evans matching, or the zeroth jet to the complete adjoint kernel family",
    },
    {
        "id": "rh-global-fourier-poisson-intertwining",
        "terms": {"global", "fourier", "poisson", "response", "intertwining", "sewing"},
        "required_terms": {"global", "fourier", "poisson", "intertwining"},
        "exclusive": True,
        "constructor": "global Fourier-Poisson response intertwiner into the declared maximal-isotropic sewing relation",
        "hostile": "preserve every local Evans-domain and five-port summability estimate while perturbing one global response phase; reject sewing unless the full response relation remains invariant",
        "forbids": "substituting local graph-domain membership or arithmetic summability for the global response theorem",
    },
    {
        "id": "block-elimination-first-jet",
        "terms": {"determinant", "block", "retained", "incidence", "cutoff", "extension", "trace"},
        "constructor": "exact complement first jet of the eliminated/retained block decomposition, including retained-state transport and both incidence directions",
        "hostile": "add one labelled block, compare the full complement first jet with the proposed increment, then add a second block and require telescoping",
        "forbids": "using only the new block diagonal trace",
    },
    {
        "id": "reduction-order",
        "terms": {"quotient", "serialized", "reduced", "equivariant", "involution", "liftable"},
        "constructor": "compare complete ambient exact structures before applying the nonfaithful reduction or serialization functor",
        "hostile": "verify ambient mutual containment and generator naturality, then vary quotient frames; classify mismatches appearing only after reduction as serialization artifacts",
        "forbids": "promoting quotient-coordinate mismatch to source noncovariance",
    },
    {
        "id": "relative-normalization",
        "terms": {"normalization", "scale", "torsor", "pairing"},
        "constructor": "source-derived comparison or pairing between independently framed target lines",
        "hostile": "apply independent nonzero target-frame rescalings; accept only a comparison invariant under the simultaneous source-derived transport",
        "forbids": "observer calibration presented as source selection",
    },
    {
        "id": "transport-completion",
        "terms": {"transport", "inversion", "pivot", "permutation", "jacobian", "residue"},
        "constructor": "one functorial transport witness carrying occurrence, residue/Jacobian, inversion, and retained-pivot data",
        "hostile": "change every admitted frame independently and require the complete square to commute without post-hoc alignment",
        "forbids": "diagonal-block or incidence-only transport",
    },
    {
        "id": "differentiated-square",
        "terms": {"jet", "derivative", "differentiated", "normal", "tangent"},
        "constructor": "separated wall blocks with source-derived normal and tangent first jets",
        "hostile": "require zero tangent residual and the preregistered normal differentiated chain equation over two finite fields",
        "forbids": "reconstructing separated blocks from an assembled cone after seeing the residual",
    },
    {
        "id": "rank-stratification",
        "terms": {"fitting", "stratification", "rank", "locus", "stratum"},
        "constructor": "source-derived Fitting atlas with constant-rank transition certificates",
        "hostile": "cross the nearest rank-jump boundary while preserving the declared local packet and reject any transported bundle claim",
        "forbids": "forming a connection across fibers of changing type",
    },
    {
        "id": "joint-source-operation",
        "terms": {"mixed", "joint", "coupled", "prime", "labelled"},
        "constructor": "nonlinear joint source operation before marginalization or sewing",
        "hostile": "hold every marginal fixed while varying only cross-label coupling; reject any scalar additive surrogate",
        "forbids": "repairing missing source coupling by increasing observer rank",
    },
    {
        "id": "higher-coherence-extension",
        "terms": {"cocycle", "degree", "descent", "coherence", "face"},
        "constructor": "source-derived next-degree coherence cell whose complete boundary is the frozen lower cocycle profile",
        "hostile": "hold every proper face and every lower-degree cocycle fixed while varying the top cell; reject extension when the top boundary remains nontrivial",
        "forbids": "declaring higher coherence from the closure of lower faces alone",
    },
    {
        "id": "typed-connecting-map",
        "terms": {"map", "morphism", "gysin", "costalk", "connecting", "tate", "shifted"},
        "constructor": "degree- and twist-typed connecting morphism at the declared boundary",
        "hostile": "erase the shift or twist and require the resulting degree-zero shortcut to fail",
        "forbids": "untyped rank matching treated as factorization",
    },
]


def tokens(text):
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def synthesize(model):
    blockers = list(model.get("missing_constructors", []))
    if model.get("next_falsifier"):
        blockers.append(model["next_falsifier"])
    candidates = []
    for rule in RULES:
        hits = []
        score = 0
        for blocker in blockers:
            overlap = tokens(blocker) & rule["terms"]
            required = rule.get("required_terms", set())
            if overlap and required <= tokens(blocker):
                hits.append({"text": blocker, "matched_terms": sorted(overlap)})
                score += len(overlap)
        if hits:
            candidates.append({
                "rule": rule["id"],
                "score": score,
                "triggering_obligations": hits,
                "candidate_constructor": rule["constructor"],
                "discriminating_hostile": rule["hostile"],
                "forbidden_substitute": rule["forbids"],
                "epistemic_status": "candidate_requires_source_derivation",
                "exclusive": rule.get("exclusive", False),
            })
    if any(x["exclusive"] for x in candidates):
        candidates = [x for x in candidates if x["exclusive"]]
    for candidate in candidates:
        candidate.pop("exclusive", None)
    candidates.sort(key=lambda x: (-x["score"], x["rule"]))
    return {
        "schema": "marici.scc.constructor-synthesis.v1",
        "model": model["id"],
        "source_obligations": blockers,
        "candidates": candidates,
        "candidate_count": len(candidates),
        "status": "candidate_menu_not_truth_certificate" if candidates else "no_rule_match",
        "next": "derive the highest-ranked constructor from source data, freeze its receiver, then run the attached hostile" if candidates else "add a typed obstruction signature; do not infer a constructor from vocabulary-free failure",
    }