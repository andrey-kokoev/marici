# The Bunch–Davies total-energy loop preserves the symmetric mixed line

## Question

Does the physical total-energy continuation select the single-wall root swap that sends the canonical mixed residue to the antisymmetric \(v_{\rm alg}\)-detecting class?

## Claim boundary

This packet compares the established local Bunch–Davies collision orientation with the existing two-wall monodromy matrices. It does not exclude a separately sourced physical path around one discriminant wall.

## Physical loop action

The Bunch–Davies approach to \(E=0\) gives same-sense half-twists at both doubled nodes. Therefore the total-energy loop acts by the product of the two commuting wall swaps,

\[
T_{\rm BD}=T_1T_2,
\]

rather than by either \(T_1\) or \(T_2\) separately.

On the mixed basis,

\[
T_1(g_{101})=-g_{101},\qquad T_1(g_{110})=g_{110},
\]

and

\[
T_2(g_{101})=g_{101},\qquad T_2(g_{110})=-g_{110}.
\]

Hence

\[
T_{\rm BD}(g_{101})=-g_{101},
\qquad
T_{\rm BD}(g_{110})=-g_{110}.
\]

For the canonical symmetric residue \(s_+=g_{101}+g_{110}\),

\[
T_{\rm BD}(s_+)=-s_+.
\]

The line remains symmetric; only its overall orientation changes. Its \(v_{\rm alg}\) projection therefore remains zero.

## Distinction of available operations

A labelled single-wall transport does algebraically produce

\[
T_2(s_+)=s_-,
\]

but the current physical total-energy prescription does not select that path. The carrier contains the operation; the admitted Bunch–Davies continuation selects the diagonal product instead.

Thus the four-vertex flow must not replace the physical path by an arbitrary generator of the monodromy group. To obtain the second detector from wall monodromy, information must enter through a source-derived path that encircles one discriminant wall without simultaneously encircling its paired wall, together with its orientation and physical readout authority.

## Disposition

The algebraic antisymmetric detector exists, but the established total-energy Bunch–Davies flow does not reach it. The missing role is physical path selection: route the canonical mixed state through one labelled wall generator rather than through the diagonal two-wall loop. Without that selection, the physical mixed readout remains rank one.

Verification:

- `research/voevodsky/checkers/check_BD_two_wall_mixed_action.py`
- `research/voevodsky/results/BD_two_wall_mixed_action.json`
