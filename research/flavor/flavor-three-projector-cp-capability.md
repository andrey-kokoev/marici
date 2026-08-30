# Three-projector CP capability (WP326)

## Exact witness

WP326 adds a third rank-one projector whose ray is proportional to
((1,i,1)^T). Together with rays proportional to (e_1) and ((1,1,0)^T), the
three rays span the full generation space. There is no common invariant line
of the type that obstructed WP325.

For the fixed affine lifts

\[
Y_u=I+P+2Q+3R,
\qquad
Y_d=2I+4P+Q+5R,
\]

the exact spectrum discriminants are (257) and (172636/27). The Hermitian
commutator is nonsingular, and

\[
\operatorname{Tr}\left([H_u,H_d]^3\right)
=-10900883i.
\]

Thus three complex relational projectors are sufficient for nondegenerate
three-family mixing and CP capability.

## Hostile conjugate

Complex conjugation preserves both sector characteristic polynomials but flips
the CP-odd invariant. The conjugate pair is therefore an exact witness that
CP-even spectral information cannot choose a CP orientation.

## Authority disposition

This is a capability theorem, not a numerical selector. The three rays, their
complex orientation, and all affine coefficients were stipulated. A physical
selector must derive them from a source action before flavor readout and must
provide a calibrated CP-sensitive instrument.

Run `uv run --with sympy python
research/flavor/checkers/wp326_three_projector_cp_capability.py` to regenerate
the exact witness.
