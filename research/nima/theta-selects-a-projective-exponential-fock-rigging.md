# Theta selects a projective exponential Fock rigging, not one polynomial Banach weight

## Correction

A polynomially weighted Beurling algebra is a coherent abstract carrier, but it is not the topology already selected by the theta/Tate source. The existing arithmetic test packets use every positive exponential weight in the logarithmic scale.

The correct object is therefore a projective rigging, not one Banach space.

## Typed valuation test algebra

Let \(\mathcal M\) be the finite valuation monoid, let

\[
\ell(\nu)=\sum_p\nu_p\log p,
\]

and retain the type fiber \(T_\nu\) over every valuation label.

For each \(\delta>0\), define

\[
q_\delta(c)
=
\sum_{\nu}
e^{\delta\ell(\nu)}
\lVert c_\nu\rVert_{T_\nu}.
\]

The source test algebra is

\[
\mathcal A_{\exp}
=
\bigcap_{\delta>0}
\ell^1\!\left(\mathcal M,e^{\delta\ell};T\right)
\]

with its projective locally convex topology.

Because

\[
e^{\delta\ell(\nu+\mu)}
=
e^{\delta\ell(\nu)}
e^{\delta\ell(\mu)},
\]

typed convolution satisfies

\[
q_\delta(c*d)\le q_\delta(c)q_\delta(d)
\]

for every \(\delta\). Thus \(\mathcal A_{\exp}\) is a complete typed topological algebra after projective completion.

## Adams continuity is seminorm transport

For the Adams operation \(\psi^r:\nu\mapsto r\nu\),

\[
q_\delta(\psi^r c)=q_{r\delta}(c)
\]

up to the norm of the declared fiber map \(T_\nu\to T_{r\nu}\).

Hence \(\psi^r\) is continuous on the projective limit even though it need not be bounded on any one fixed weighted Banach rung. This is the correct typing: Adams transport moves control from seminorm \(\delta\) to seminorm \(r\delta\).

## Hilbert observation and Fourier-Bohr presentation

The unweighted coefficient Hilbert module is

\[
\mathcal H_0=\ell^2(\mathcal M;T).
\]

Finite packets are dense, and \(\mathcal A_{\exp}\) embeds continuously into \(\mathcal H_0\). Fourier-Bohr synthesis is isometric on \(\mathcal H_0\) when the invariant mean and the discrete type fibers are authorized.

Thus the rigging is

\[
\mathcal A_{\exp}
\subset
\mathcal H_0
\subset
\mathcal A_{\exp}'.
\]

The middle rung controls coefficient observability. It does not carry every constructor or boundary row as a bounded Hilbert operator.

## Boundary dual

The strong dual contains coefficient rows of some finite exponential order:

\[
\mathcal A_{\exp}'
\supset
\bigcup_{\delta>0}
\ell^\infty\!\left(\mathcal M,e^{-\delta\ell};T^*\right).
\]

This includes:

- the constant augmentation and seam rows;
- the primitive coefficient \((\log p)p^{-1/2}\);
- the square coefficient \((\log p)p^{-1}\);
- every fixed polynomial in \(\log p\) times a fixed exponential order.

The primitive current remains a covector, not a Hilbert state. The projective topology makes it continuous without applying a Riesz identification.

## Grade separation

The connected \(k\ge3\) Euler tail already converges absolutely and uniformly in its Bohr presentation, together with every fixed Mellin derivative. It occupies a smoother algebraic subrung.

The low grades remain distinct:

- primitive: dual boundary current;
- square: tempered or Hilbert-level counterterm, but not trace class;
- connected tail: smooth uniformly almost-periodic element;
- seam and endpoint: dual evaluations;
- archimedean channel: separately attached boundary current.

One common projective rigging can host these roles, but it does not identify them.

## Why this is stronger than the polynomial proposal

A single polynomial weight asks every constructor to be bounded in one norm. The source instead supplies a family of seminorms and permits a constructor to move between them. This is exactly the categorical behavior expected of a rigged functor.

The polynomial proposal remains a useful hostile control. If a claimed theorem needs only one \(s\), it factors through a Banach subrung. The actual theta/Tate object should not be reduced to that rung without proof.

## Remaining gate

The coefficient carrier and arithmetic constructor algebra are now compatible at the topological level. The unresolved source-specific construction is the common graph domain

\[
\mathcal A_{\exp}
\subset
D
\subset
\mathcal A_{\exp}'
\]

on which all of the following are simultaneously defined and continuous:

- the doubled Clark–Green operator;
- seam and endpoint traces;
- primitive and square currents;
- the connected tail;
- the archimedean current;
- reciprocal sewing;
- the determinant-line pairing.

The decisive falsifier is a channel or Green cross-term whose coefficient growth has no finite exponential order, or an Adams fiber map that fails the seminorm-transport law.

## Verdict

Theta/Tate does select the arithmetic side of the hybrid: a typed projective exponential Fock rigging. The frontier is no longer choosing a coefficient topology. It is constructing the common graph domain and the dual-valued Green identity without collapsing distinct grades or promoting covectors to states.
