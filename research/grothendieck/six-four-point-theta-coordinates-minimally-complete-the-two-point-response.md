# Six four-point theta coordinates minimally complete the two-point response

## Constructed

On the fixed four-prime full-route source, eighteen independent two-point interval coordinates plus six explicit four-point coordinates reconstruct all twenty-four route coefficients. The square measurement matrix has determinant one. Six additional scalar linear measurements are necessary by rank-nullity, and the displayed construction attains this bound.

This is output minimality relative to the existing rank-eighteen two-point observation, not a minimal-state theorem. It is also not minimality over arbitrary nonlinear encodings.

## Coordinates

Use the fifteen consecutive arithmetic interval atoms, numbered zero through fourteen, with endpoints obtained by sorting n_S=2 product_(j in S) p_j for p=(2,3,5,7).

The six additional ordered tensor coordinates are:

- (0,1,4,10)
- (0,1,6,10)
- (0,1,7,12)
- (0,2,8,10)
- (0,2,9,12)
- (0,3,11,13)

The eighteen selected two-point coordinates, exact 24-by-24 inverse, and route order are recorded in `results/minimal-theta-four-point-completion.json`.

For K_d=sum_(i_1<...<i_d) v_ei1 tensor ... tensor v_eid, the joint readout is (P_2 K_2, P_4 K_4)=M c. The exact inverse reconstructs c, and any source correlation Bc is consequently B M^{-1} applied to that readout. This makes the connection to the six previously selected labelled edge-pair probes explicit without treating interval coefficients as edge labels.

## Compositional implementation

`theta_interval_signature.py` implements sparse event signatures through degree four, route validation, linear source mixtures, and concatenation. A new edge multiplies the signature by (1+v_e); no same-event higher tensor powers are inserted. General composition uses

K_d(XY)=sum_(a+b=d) K_a(X) tensor K_b(Y).

The degree-zero coordinate carries total coefficient mass, which need not be one for signed mixtures. Omitting it breaks bilinear composition. The implementation retains all intermediate tensor coordinates; the minimal selected output alone is not asserted to be closed under streaming updates. Endpoint types must still be respected by the caller when concatenating formal mixtures; tensor multiplication itself also makes sense for noncomposable words.

The exact checker verifies every cut of all 168 admissible paths, a signed rational full-route reconstruction, and a bilinear composition of source mixtures. It rejects repeated-prime paths.

## Analytical readout

Import the theta atom map H and its finite left inverse L from the preceding packet. For Theta_d=H^{tensor d}K_d, the readout is

c=M^{-1}(P_2 L^{tensor 2} Theta_2, P_4 L^{tensor 4} Theta_4).

Each selected coordinate is a bounded product of dual atom functionals. It need not be obtained by measuring the entire continuum tensor first. With the direct-sum Hilbert norm, perturbations eta_2,eta_4 obey

||error|| <= ||M^{-1}|| sqrt(||L||^4 ||eta_2||^2 + ||L||^8 ||eta_4||^2).

This is a finite analytical bound conditional on the recorded atom independence; it is not a certified numerical condition number. Unimodularity in the coefficient basis does not imply well-conditioning in the physical theta metric.

## What remains

The source must supply event-segmented, route-conditioned two- and four-point responses. The construction does not create them from the averaged one-point history. No assertion is made that the independent physical source already admits these operations.

The next gate is now precise: either exhibit that physical source adapter, or prove it cannot preserve the retained route segmentation. A second independent task is bounding the finite theta Gram inverse in the actual measurement norm. Additional finite rank computations alone will not close either gate.

## Verification

Run `uv run --with sympy python research/grothendieck/checkers/check_minimal_theta_four_point_completion.py`.

All checks passed. The analytic input and preceding rank obstruction are documented in `four-point-theta-interval-signatures-recover-the-four-prime-route-mixture.md`. No positivity or confinement conclusion is drawn.
