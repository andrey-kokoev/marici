# v114: soft D1 integral Smith audit

A new independent checker reconstructs the plus-defect columns over the
integers and computes exact Smith normal forms at cutoff `D=12`.

The target rank is 91. The original image has rank 89 and the image augmented
by its `a^2` products has rank 90, confirming the rank-one defect integrally at
this cutoff. However, the original and completed matrices have respectively 20
and 21 nonunit Smith factors. The proposed completion is therefore not
saturated over the integers.

This sharpens the modular result: the L2 transition supplies the missing
rational rank but does not by itself produce the required integral physical
extension. An integral saturation or torsion-aware derived replacement is
needed.

Evidence is in `results/soft-axis-plus-defect-smith.json`; the checker is
`checkers/check_soft_axis_plus_defect_smith.py`. The Rzk summary passes all six
declarations without assumptions. This is a bounded cutoff audit, not an
all-degree theorem or global chain map.
