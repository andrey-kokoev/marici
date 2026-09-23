# Exact rational packet hashes require normalization, not floating input

Fresh `check_canonical_rational_packet.py` parses only exact integer or integer-fraction strings, reduces each rational and hashes the normalized sequence. Thus `1` and `1/1` (and zero lexemes `0`, `00`, `-0`, `0/1`) identify the same mathematical coefficient packet; `-2/4` becomes `-1/2`. Floating values, decimal and exponent syntax, whitespace, signed `+1` and zero denominator are refused rather than silently rounded or ambiguously hashed.

This normalization concerns LOCAL proof-packet equality only. A source event's signed canonical BYTES, if ever available, could have a different encoding policy and would require independently specified versioning. Neither a canonical math digest nor an occurrence ID authenticates a Farkas row issuer or analytic S,A,R,C,G correspondence.

The packet-versus-occurrence branch now has separate exact math content, generation-scoped cache keys and historical occurrence identities. A nonredundant successor should test a rational PACKET TRANSFORM with negative multipliers: an algebraically correct normal/bound equation is not a valid Farkas proof unless all source multipliers and surplus are nonnegative. Keep owner and analytic boundaries intact.
