# The all-place charge spinor exists algebraically, but its Fourier image escapes the current space

## 1. Algebraic all-place current space

Let

\[
  V=\bigoplus_v\mathbb C e_v
\]

be the finite-support place-current space over all places, and let \(V^*\) be
its full algebraic dual. The global charge covector

\[
  \varepsilon=\sum_ve_v^*
\]

is a well-defined element of \(V^*\): it evaluates on each finite-support
current by a finite sum.

Form

\[
  \mathbb H=V\oplus V^*
\]

with the evaluation pairing

\[
  B(x+\alpha,y+\beta)=\alpha(y)+\beta(x).
\]

## 2. Exact global maximal isotropic

Define

\[
  L=\ker\varepsilon\oplus\mathbb C\varepsilon.
\]

If \(y+\beta\in L^{\perp_B}\), then:

1. pairing with \(\varepsilon\) gives \(\varepsilon(y)=0\), so
   \(y\in\ker\varepsilon\);
2. pairing with every \(x\in\ker\varepsilon\) gives \(\beta(x)=0\), hence
   \(\beta\) is proportional to \(\varepsilon\).

Therefore

\[
  \boxed{L=L^{\perp_B}.}
\]

The global charge spinor \(\varepsilon\in\Lambda^1V^*\) has annihilator
exactly \(L\), by the same contraction/wedge calculation as at finite place
sets.

Thus the compatible finite-place charge spinors possess a canonical
algebraic inverse limit. No prime ordering or metric is required.

## 3. Failure of the Fourier quarter-turn

At a finite place set \(S\), a coordinate Fourier quarter-turn exchanges

\[
  e_v\longleftrightarrow e_v^*
\]

up to orientation. It sends

\[
  \varepsilon_S=\sum_{v\in S}e_v^*
\]

to the finite all-ones current

\[
  \mathbf1_S=\sum_{v\in S}e_v.
\]

In the all-place limit,

\[
  \mathbf1_\infty=\sum_ve_v
\]

does not belong to the finite-support current space \(V\).

Hence the algebraic hyperbolic double retaining the global charge is not
closed under the reciprocal quarter-turn:

\[
\boxed{
\varepsilon\in V^*,
\qquad
J\varepsilon\notin V.}
\]

## 4. The same obstruction in Fisher topology

The all-ones current also fails to lie in the raw critical Fisher completion
when its squared norm is

\[
  \sum_pc_p
\]

with \(c_p\sim p^{-1/2}\). This sum diverges.

Thus neither the finite-support algebraic topology nor the positive Fisher
topology contains both the global charge spinor and its Fourier-rotated
partner.

## 5. Required rigged Clifford space

The completed source needs a rigging

\[
  V_{\mathrm{test}}
  \subset
  V_{\mathrm{energy}}
  \subset
  V_{\mathrm{dist}}
\]

such that:

1. \(\varepsilon\) and \(J\varepsilon\) exist as distributional boundary
   spinors;
2. the Clifford evaluation pairing extends between the test and
   distributional sectors;
3. the Fourier rotor acts continuously on the rigging;
4. the product-formula annihilator remains closed in the appropriate graph
   topology; and
5. the spinor pairing is renormalized without choosing a prime ordering.

This is the geometric-algebra version of the theta comb living in
\(\mathcal S'\) rather than \(L^2\).

## 6. Meaning of the two sectors

The two complementary sectors are now exact but topologically asymmetric:

\[
  V=\text{finite source currents},
\qquad
  V^*=\text{global charge observations}.
\]

Fourier reciprocity demands a completion in which each can be rotated into
the other. The half-planes are scalar shadows of the two distributional
polarizations of this rigged hyperbolic space.

## 7. Falsifier

The programme fails if no source-selected rigging simultaneously admits:

\[
  \varepsilon,\quad J\varepsilon,\quad
  \text{the prime Fock vacuum},\quad
  \text{and the completed spinor pairing}.
\]

It also fails if several inequivalent riggings satisfy all visible
finite-place restrictions and yield different divisors.

## 8. Scope

The global algebraic maximal-isotropic relation, pure-spinor annihilator, and
escape of the Fourier-rotated all-ones current are exact. No Fourier-stable
rigged Clifford completion, renormalized spinor pairing, identity with \(X\),
or RH theorem is constructed.

Successor correction: a single Fourier-stable rigging is not required.
The paired-chart packet replaces it by two oppositely typed riggings exchanged
by the quarter-turn.
