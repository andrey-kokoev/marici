# One extra history still cannot complete the amplitude

Fresh test: append the previously identified [9,1,2,3,4][9,5,6,7,8] cell and examine chi2^4 chi3^4. All four original cells have zero coefficient because one column is absent. In the added cell, columns2 and3 are parallel, so minor23 vanishes identically. Thus ANY scalar combination of these five tensors has zero coefficient, regardless of signs, frame factors, or target-dependent weights.

The complete sourced tree coefficient is NONZERO at both existing common targets. At e=1/2 it is14103947093626598447974040681/27494180857397686999854566723697990696960. The other exact value and every nonzero history contribution are saved in results/nine-point-five-cell-support-gap.json. Exactly25 of the50 authored terms contribute at each target. This is a roster of nonzero source contributions, NOT a lower bound of25 additional cells: identities and alternative decompositions could reorganize them.

The first contributing history is outer(2,4), inner(4,6), right-nested, with the lower spinor replacement at4. Unlike the previous missing history, it requires a transported boundary point. A natural next construction is its positive8-parameter representative

C1=(a1,a2,a3,a4,0,0,0,0,-1),
C2=(0,0,b3*a3,b3*a4+b4,b5,b6,0,0,1).

This is a CANDIDATE, not yet checked: the boundary intersection follows from a3*Z3+a4*Z4=Z9-a1*Z1-a2*Z2 on C1*Z=0. All ordered minors appear subtraction-free and minor23=a2*b3*a3 is nonzero. Next directly audit those minors, inverse coordinates, the dlog Jacobian, and full tensor normalization against the sourced boundary-updated R product. Do not add it to any contour before that check.

Fresh command: uv run --with sympy python research/voevodsky/checkers/check_nine_point_five_cell_support_gap.py. Check passes and records the nonzero tree/structural-zero discrepancy. This turns the next missing contribution into a concrete boundary-cell construction task rather than another fit of existing weights.
