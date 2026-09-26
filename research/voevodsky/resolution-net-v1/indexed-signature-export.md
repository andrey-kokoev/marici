# Concrete certificates now retain heterogeneous package indices

The indexed exporter replaces the single Unit package and unrestricted numeric rule types with finite inductive declarations:

* one Pkg constructor per distinct complete Python package record;
* U constructors with their exact input/output Pkg indices;
* V constructors with their exact two ordered input indices and output;
* Evidence constructors at the exact admitted package, retaining distinct witnesses even when their packages agree.

A resource fixture consumes token a and token b independently and joins the spent footprints. Its five actual wire rewrites are serialized and replayed exactly. The generated Agda module has5 package constructors,2 unary rules,1 binary rule and3 seed-witness constructors (including an alternate witness at the same initial package). Every RepresentedStep certificate passes a fresh ignore-interfaces check.

Negative tests are rejected BY AGDA, specifically with UnequalTerms:

1. Apply the consume-a constructor to seed evidence belonging to the b-world.
2. Replace one seed witness by the alternate witness at the SAME package while claiming pure compression via identity.

Thus the proof checker now sees genuine finite endpoint indices and witness distinctions, not merely a one-package surrogate. Files: indexed_port_certificates.py, check_indexed_port_certificates.py, agda/ResolutionNetIndexedPortCertificates.agda, results/indexed-port-packet.json and results/indexed-port-certificates.json. Reproduce via python research/voevodsky/resolution-net-v1/check_indexed_port_certificates.py.

Trust boundary remains precise: the exporter DECLARES the finite U/V/Evidence signature. Agda checks that terms use that signature correctly, but does not thereby prove every declared domain rule is valid resource consumption. The Python resource validator checks the fixture's intended transitions, while the generic formal footprint theorem concerns its own semantic Change/Separate relations. Those two signatures have not yet been formally connected. Serialization, reification and package-table assignment also remain trusted.

Next emit an interpretation of the generated Pkg/U/V/Evidence declarations into the checked resource-world signature, with actual Change/Separate/Fresh witnesses for each constructor. This would make an endpoint-correct but semantically invalid revival rule fail formal domain admission, rather than simply becoming another generated constructor. It is a narrower and more useful next trust reduction than claiming the entire Python compiler verified.
