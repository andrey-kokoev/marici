# Zero-length reflexive paths are identity, not derivation witnesses

Fresh `check_zero_length_identity_path.py` explicitly admits an empty path from a known fictional occurrence P to itself as `STRUCTURAL_IDENTITY_NOT_OBSERVED`. The same empty sequence labelled nonempty derivation fails `MISSING_DERIVATION_EDGE`; empty identity on different IDs or unknown IDs also fails. Identity composition is a structural convenience, not a witnessed transition or proof of observed source occurrence.

The fixture's known-ID registry is synthetic. It establishes no actual event, owner-issued row set or analytic S,A,R,C,G map.

Next test the UNIT LAW for path concatenation: composing identity at start/end with a typed nonempty edge preserves its edge sequence and occurrence endpoints, but cannot introduce or erase audit events; reject identity labels on the wrong middle occurrence.
