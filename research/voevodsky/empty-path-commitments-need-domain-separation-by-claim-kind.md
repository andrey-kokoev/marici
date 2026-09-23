# Empty path commitments need domain separation by claim kind

Fresh `check_path_commitment_domain_separation.py` constructs an original zero-length A identity and an empty residual A view after reducing a synthetic nonempty cycle. Their EMPTY EDGE LIST hash is identical. A complete versioned commitment binding claim kind (`original-identity@1` versus `derived-reduction@1`), endpoint, original path and reduction lineage differs; attempting to use the derived view as an original identity fails `KIND_MISMATCH`.

This test shows an encoding distinction, NOT hash-based historical proof. No actual event, row issuer or analytic S,A,R,C,G assignment is inferred.

Next test a CROSS-KIND serialization attack: JSON with duplicate `kind` keys or ambiguous field ordering could permit one parser to see original identity and another derived view. Refuse duplicate keys and hash an explicit canonical typed representation only after parsing.
