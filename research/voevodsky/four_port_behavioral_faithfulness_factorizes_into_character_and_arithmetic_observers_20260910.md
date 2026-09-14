# Four-port behavioral faithfulness factorizes into character and arithmetic observers

## Question

What is the analytic four-port analogue of the finite shift-defect theorem that constructor-word records recover every hidden coefficient?

## Claim boundary

Prior research supplies the finite factorization theorem and a passing three-label fixture. It proves finite separation by source-derived Fourier-character and arithmetic-cylinder probes. It does not establish joint separation after completion by any fixed finite family.

## Boundary character observer

Let the universal boundary quotient be

\[
W=W_1\oplus W_{-1}\oplus W_i\oplus W_{-i},
\]

with \(F^4=I\). The four source projectors \(P_\lambda\) separate \(W\). Equivalently, one source-authorized cyclic covector \(\ell\) generates the orbit observer

\[
\mathcal O_\ell(w)
=
\bigl(\ell(w),\ell(Fw),\ell(F^2w),\ell(F^3w)\bigr),
\]

provided its restriction to every character line is nonzero.

In the real wall--tail frame \((1,\delta_0,K,V)\), a covector \((a,b,c,d)\) is cyclic precisely when

\[
a+b\ne0,
\qquad
a-b\ne0,
\qquad(c,d)\ne(0,0).
\]

Thus the seed must mix a one-sided wall incidence with an oriented causal-tail incidence. A wall-only or tail-only observer remains trapped in one invariant plane.

## Arithmetic multiplicity

After adjoining a finite arithmetic packet \(C_X\), the state carrier is

\[
W\otimes C_X.
\]

Every Fourier character then occurs with multiplicity \(\dim C_X\). Fourier transport cannot separate that multiplicity by itself. Let \(A_F\) be the four-character observer and \(A_X\) a source-derived valuation/Fock cylinder family. The combined observer is

\[
A_F\otimes A_X,
\]

and

\[
\operatorname{rank}(A_F\otimes A_X)
=
\operatorname{rank}(A_F)\operatorname{rank}(A_X).
\]

This is the four-port counterpart of probing matrix coefficients with native shift-defect words: the fixed character factor separates boundary type, while the arithmetic constructor family separates copies within each type.

## Fresh finite verification

The existing checker

`research/nima/checkers/check_rh_boundary_separation_tensor_product.py`

was rerun. On its three-label fixture it reports:

\[
\dim(W\otimes C_X)=12,
\]

\[
\operatorname{rank}A_F=4,
\qquad
\operatorname{rank}A_X=3,
\]

and

\[
\operatorname{rank}(A_F\otimes A_X)=12.
\]

Thus the source tensor observer is faithful on that finite packet.

Four character rows paired with only one arithmetic scalar have rank four and leave an eight-dimensional kernel. A terminal total scalar has rank one.

## Behavioral interpretation

Let \(C\) be the bounded constructor category and

\[
\beta(x)=\bigl(O(T_wx)\bigr)_w
\]

its behavior map. On finite packets, the character-by-cylinder probes are a finite subfamily of behavior coordinates. Their full rank proves that this subfamily already separates the tested state carrier.

The separation is source-shaped:

- powers of Fourier generate the four character directions;
- valuation/Fock constructor words generate the arithmetic cylinder directions;
- their tensor pairing preserves which arithmetic occurrence belongs to which boundary character.

No backward reconstruction from the scalar readout is used.

## Completion boundary

As cutoff grows, character multiplicity grows. The finite theorem does not imply that one fixed finite probe set separates the completion. The completed behavior observer must satisfy one of the following:

1. retain a natural continuous function-valued arithmetic probe family jointly separating every character sector;
2. prove a source recurrence making a bounded probe family complete;
3. retain the pro-observer over finite character-by-cylinder packets.

A normalized sequence escaping every fixed finite arithmetic probe family is the decisive hostile. A nonzero commutator between cutoff bonding and a character-by-cylinder probe is the transport hostile.

## Disposition

Finite behavioral faithfulness of the analytic four-port packet is constructed after tensoring the four Fourier-character observer with the source valuation/Fock probe family. The three-label exact rank is twelve. The completed observer remains function-valued or pro-finite unless a source-derived finite-determination theorem is supplied.
