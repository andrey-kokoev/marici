# Adjacent correction words do not form a naive source syzygy

The degree-12-to-14 correction word was translated by `(0,2)` into the
degree-16 source module and the degree-14-to-16 word was subtracted. Independent
replay gives nonzero differences:

- K pole 0: 30 translated and 30 target terms, residual support 39;
- K pole 1: 50 translated and 50 target terms, residual support 57.

Thus adjacent correction words are not equal modulo a zero source relation
under naive subtraction. This condition is stronger than compositional
coherence because the two cells have different q-representative boundaries.
The admissible next comparison requires a direct degree-12-to-16 correction
and the composite of both adjacent corrections; only those have matching
boundary.
