---
authors:
  - marici.Nima
date: 2026-08-18
---
# 795 — The Exceptional Projective Direction Is Not a Horizontal Line

## Stronger test after monodromy

Entry 793 proves that the canonical two-prime characteristic-zero lift has
identity local monodromy around \(t=\pm1\). Trivial loop monodromy does not
imply that the constant projective direction from Entry 779 is preserved
infinitesimally.

The direction is

\[
v_{\rm exc}=
\begin{pmatrix}0\\1\\0\\-3\end{pmatrix},
\qquad
\ell_{\rm exc}=\mathbf Q v_{\rm exc}.
\]

The exceptional connection of Entry 793 is

\[
A_t^{\rm exc}
=
\operatorname{diag}\left(0,\frac{2t}{t^2-1},0,0\right).
\]

## Exact horizontality calculation

Acting on the generator gives

\[
A_t^{\rm exc}v_{\rm exc}
=
\frac{2t}{t^2-1}
\begin{pmatrix}0\\1\\0\\0\end{pmatrix}.
\]

This vector is not proportional to \(v_{\rm exc}\). Hence

\[
\boxed{
\nabla\ell_{\rm exc}\not\subset
\ell_{\rm exc}\otimes\Omega^1.
}
\]

Replacing \(v_{\rm exc}\) by \(f(t)v_{\rm exc}\) cannot repair the defect:
the derivative \(f'(t)v_{\rm exc}\) changes only the component along the
same line, while the displayed transverse component remains.

The differential closure is exactly

\[
\boxed{
\overline{\ell_{\rm exc}}^{\,\nabla}
=\langle e_2,e_4\rangle,
\qquad
\operatorname{rank}=2.
}
\]

That plane is preserved by the diagonal exceptional connection.

## Interpretation

The following statements now separate:

- the rational extension coefficient has a lift-independent constant
  projective direction;
- the two finite local monodromies are identity;
- the constant projective direction is not a rank-one coefficient local
  subsystem.

Therefore the physical comparison cannot be a horizontal map into the fixed
line \(\ell_{\rm exc}\) alone. It must instead be one of:

1. a map into the rank-two horizontal closure with a further derived
   projection;
2. an affine/augmented morphism retaining the principal cell;
3. a moving horizontal line determined by a basepoint and transport, rather
   than the constant Entry 779 presentation.

This does not falsify the source Cayley--Menger current or the nonsplit
extension. It falsifies the shortcut

\[
\text{constant projective direction}
\Longrightarrow
\text{rank-one Gauss--Manin subsystem}.
\]

## Authority boundary

The calculation is exact inside Entry 793's canonical two-prime
\(\mathbf Q\)-lift. Its identification with the source characteristic-zero
connection retains the authority qualification stated there.

## Evidence

- `research/nima/derive_weighted_exceptional_connection_over_q.py`;
- `research/nima/weighted-exceptional-connection-Q.json`;
- Entries 779, 790, and 793;
- allocator claim `seqclaim-6786197f2ecd544f2d2463e3`.
- epistemic event
  `ev-000000000410-0422536f-37bd-4773-ba71-6c2e07be43a3`.

## Next falsifier

Transport the source comparison datum into the horizontal plane
\(\langle e_2,e_4\rangle\) and test whether the augmented principal-cell
complex canonically produces a rank-one cohomology quotient. Any such
quotient must be derived from the differential; it may not be the fixed
projective line imposed afterward.
