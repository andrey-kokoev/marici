# All15 right-nested histories now have explicit positive dlog representatives

Freshly generalized the two checked examples to EVERY right-nested history in the sourced n=9 formula. There are15:10 lower-boundary-updated and5 unshifted. `check_nine_point_right_history_cells.py` builds all matrices and retains them in results/nine-point-right-history-cells.json.

Construction: for outer pair(A,B), set row1 entries at(A-1,A,B-1,B) to(x1,x2,x3,x4), and row1 at9 to-1. Row2 at9 is+1. For inner pair(a,b), normally place(y1,y2,y3,y4) at(a-1,a,b-1,b). If a=B, replace the y1 entry by y1*x3 at B-1 and y1*x4 at B, adding the latter to the existing y2 entry. Always ADD overlapping entries rather than overwriting them. The coordinate order is(x1,x2,x3,x4,y1,y2,y3,y4).

Checks passed:

* All36 ordered maximal minors of each of the15 matrices are identically zero or polynomials with positive coefficients.
* All15 histories reproduce the full fermionic wedge and sourced bosonic normalization at BOTH existing common quotient targets.
* Each history has a separately constructed positive-image target from6D positive moment-curve data, recovering exactly the chosen positive eight coordinates with nonzero Jacobian.
* Total45 exact full-tensor/prefactor comparisons; orientation ratio is+1 with the recorded dlog order.

These are regular localized checks, not symbolic all-kinematics normalization proofs. Original common targets need not lie inside each positive cell image; their inverse-coordinate signs are recorded. The15 cells alone are not the full tree sum. No channel or net infrastructure was changed.

Remaining executable work: construct the35 left-nested representatives, including20 upper-boundary updates, calibrate their orientations/fermionic rows in the same convention, then compare the complete50-cell rational sum to the already cyclic-tested source expression. A geometric completeness/no-overlap or contour argument remains distinct from this termwise rational normalization. The fork's original four zero-column channels cannot be repaired merely by choosing family coefficients, as the durable support-obstruction artifacts show.

This finishes the tenth requested iteration with substantive progress, but the amplitude/contour objective remains open; there is a nonredundant continuation.
