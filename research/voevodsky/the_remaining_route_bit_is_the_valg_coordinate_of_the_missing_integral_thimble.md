# The remaining route bit is the v_alg coordinate of the missing integral thimble

## Comparison with prior obstruction theory

Prior research identifies the integral cusp-extension ambiguity as

\[
\operatorname{Ext}^1_{\mathbb Z}
(\mathbb Z/2,\mathbb Z\langle e_6,v_{\rm alg}\rangle)
\cong(\mathbb Z/2)^2.
\]

A source-normalized lift \(m\) is classified by

\[
2m=a e_6+bv_{\rm alg}
\pmod{2\langle e_6,v_{\rm alg}\rangle}.
\]

Entries 1153 and 1751 state that selecting \((a,b)\) requires an integral Picard--Lefschetz thimble and a lift through the primitive infinity-Gysin sequence.

## Reduction supplied by the pyramid analysis

The pyramid calculation independently fixes the decomposition of the source geometry:

- the normal-jet/common-pencil direction is the primitive \(e_6\) axis \(\alpha_{12}\);
- the unresolved route plane is \(\langle\alpha_{13},\alpha_{14}\rangle\);
- the relative wall detector has primitive \(v_{\rm alg}\) covector \((-1,+1)\).

Thus the missing signed Gysin column

\[
J(w_{110})\in\langle\alpha_{13},\alpha_{14}\rangle
\]

is exactly the geometric datum needed to determine the \(v_{\rm alg}\) coordinate of the integral lift. The final sum-versus-difference route bit is not a new independent ambiguity: it is the route presentation of the already-known unresolved \(v_{\rm alg}\) extension coordinate.

This does **not** compute the value of that bit. It identifies its obstruction-theoretic home.

## Why existing pairings do not decide it

The prior audit records that the known physical Cut pairing maps to zero in the elliptic coinvariants. The present analysis also shows that:

- absolute physical-chamber Picard transport is identity;
- site exchange preserves the ordered vertex labels;
- conductor \(A_2\) incidence has the wrong discriminant lattice;
- ordinary boundary residues are incorrectly typed for absolute Picard classes.

Therefore repeating any of those calculations cannot produce \(J(w_{110})\).

## Minimal constructor

A successful packet must provide all of:

1. a source-normalized integral Lefschetz thimble \(m\);
2. its primitive infinity-Gysin lift;
3. the coefficient of \(v_{\rm alg}\) in \(2m\) modulo two;
4. a label matching that coefficient to one oriented fixed-pencil route axis.

This single object simultaneously resolves the cusp-extension bit and the pyramid kernel-orientation bit.

## Status

The role and flow of the missing comparison are determined. Its value is not derivable from the currently serialized algebraic matrices; it requires the geometric integral thimble already identified as absent by prior research.

Verification:

- `research/voevodsky/checkers/check_route_bit_thimble_obstruction_alignment.py`
- `research/voevodsky/results/route_bit_thimble_obstruction_alignment.json`
