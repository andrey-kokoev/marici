# An exact signed row equation is not a Farkas implication

On the fixed unit square, multiplier -1 on the x-lower row has an exact equation for x<=0 but an inadmissible negative multiplier. Multiplier +1 on x-upper with surplus -1 likewise has an exact equation for x<=0 but negative surplus. Fresh `check_nonnegative_farkas_gate.py` refuses both as implication packets.

In contrast, two DIFFERENT valid nonnegative proofs of x<=2 are P=(0,1,0,0),c=1 and Q=(1,2,0,0),c=0. The exact signed vector P-Q=(-1,-1,0,0) is a legitimate comparison difference between these separately validated endpoint packets, but cannot be installed as a standalone nonnegative implication proof. Algebraic equality, admissibility of a proof, and admissibility of a signed comparison occupy separate checks. No source issuer or analytic S,A,R,C,G assignment is inferred.

Next test a comparison delta whose parent ENDPOINT packet is negative while the delta itself reconstructs correctly and even vanishes. Require endpoint validation before accepting any signed comparison as history.
