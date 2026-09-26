# Path generation fields must reject JSON Boolean true

Fresh `check_path_generation_boolean_confusion.py` confirms that Python regards `True == 1` and `isinstance(True,int)` as true. A path-commitment generation field parsed from JSON `true` therefore must use EXACT integer type validation, not ordinary equality or `isinstance`. The fixture admits positive integer `1` as structural scope only; rejects Boolean `true`, float `1.0`, string `"1"`, zero and negative integers.

This is a local type check, not observed event or owner-issued source authentication. Analytic S,A,R,C,G remains deferred.

The bounded path commitment encoding branch now covers kind separation, duplicate/unknown keys and exact integer type. A separate successor should test CANONICAL REPRESENTATION of source-row manifest digests across JSON integer encodings: JSON `1` versus `1.0` must not silently alias in a row-bound commitment; require exact integer/rational schema and canonicalization.
