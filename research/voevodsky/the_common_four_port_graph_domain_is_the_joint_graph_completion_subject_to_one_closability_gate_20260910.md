# The common four-port graph domain is the joint graph completion subject to one closability gate

## Question

Can the common domain for Green action, four boundary traces, arithmetic currents, archimedean attachment, sewing, and determinant pairing be constructed without assuming that all maps are bounded on one Hilbert space?

## Claim boundary

Yes as a joint graph completion of the finite-support source, provided one exact joint-closability condition holds. The construction does not prove that condition for the unresolved doubled Green map or identify the global G4 sewing operator.

## Problem

The projective source

\[
\mathcal A_{\exp}
=
\bigcap_{\delta>0}\ell^1(\mathcal M,e^{\delta\ell};T)
\]

supports arithmetic constructors. Its Hilbert middle rung supports coefficient observation, while boundary currents live in the strong dual. Requiring every operation to be bounded on the Hilbert rung would erase these type distinctions.

## Bold conjecture

Taking the intersection of the separately declared operator domains automatically produces a faithful common graph domain.

## Named rivals

1. Joint graph completion gives the common domain, but only after joint closability excludes vertical graph vectors.
2. Each map is separately closable while the complete family is not jointly closable in the chosen product topology.
3. A Hilbert graph norm suffices for all dual-valued rows.
4. Defining the domain by graph completion hides an inconsistent source identification.

## Construction

Let \(D_0\) be the typed finite-support valuation/Fock source. For each required operation choose its actual target rung:

\[
A_i:D_0\longrightarrow Y_i.
\]

The family includes only declared maps:

- doubled Clark--Green action;
- the four boundary traces;
- primitive, square, and connected-current maps;
- archimedean attachment;
- reciprocal/Fourier sewing;
- determinant pairing where already defined.

Each \(Y_i\) is the specific Hilbert, finite-dimensional, ideal, or strong-dual step required by that map. Form the diagonal graph map

\[
J:D_0\longrightarrow
\mathcal A_{\exp}\times\prod_iY_i,
\qquad
Jx=(x,(A_ix)_i).
\]

Define

\[
D=\overline{J(D_0)}
\]

in the product of the projective source topology and the declared target topologies. Equivalently, \(D\) is the completion for the joint graph seminorm family

\[
q_\delta(x),
\qquad
p_{i,a}(A_ix),
\]

where \(p_{i,a}\) runs through seminorms defining \(Y_i\).

Every \(A_i\) then extends continuously to the corresponding graph coordinate of \(D\). This is a multi-rung graph construction; it does not promote dual currents to Hilbert states.

## Strongest falsification attempt

The projection

\[
\pi:D\longrightarrow\mathcal A_{\exp}
\]

is faithful exactly when the family \((A_i)_i\) is jointly closable:

\[
x_\lambda\to0\text{ in }\mathcal A_{\exp},
\qquad
A_ix_\lambda\to y_i\text{ in }Y_i\text{ for every }i
\]

must imply

\[
y_i=0\quad\text{for every }i.
\]

If this fails, the graph closure contains a nonzero vertical vector

\[
(0,(y_i)_i),
\]

so \(D\) is not a domain over the source at all. This is the exact residual hidden by naive domain intersection.

Separate closability suffices for a finite family with the ordinary product topology. For an infinite or pro-family, coordinatewise closability gives injectivity into the product, but any stronger record topology requires its own joint estimate.

## Existing components

Prior results supply:

- projective seminorm transport under Adams;
- length-preserving sewing on every projective rung, the Hilbert middle rung, and the strong dual;
- fixed finite-exponential order for the named primitive, square, seam, and endpoint rows;
- exact four-presentation response transport;
- continuous transpose maps from analytic graph duals to arithmetic duals.

These results place the named maps in candidate targets \(Y_i\). They do not prove that every arithmetic boundary row belongs to the transpose range of one common analytic Green graph.

## Adams and dagger stability

Suppose source Adams maps \(S_r\), target maps \(B_{i,r}\), and cocycles \(M_{i,r}\) satisfy on \(D_0\)

\[
A_iS_r=M_{i,r}B_{i,r}A_i
\]

and transport the defining graph seminorms continuously. Then \(S_r\) extends to \(D\), and the covariance equations persist by density.

The continuous dual \(D'\) carries the contragredient action. For a boundary row \(\lambda\in Y_i'\), its source dagger is

\[
A_i'\lambda\in D',
\qquad
\langle A_i'\lambda,x\rangle
=
\langle\lambda,A_ix\rangle.
\]

This supplies one common dagger domain without a Riesz identification.

## Transpose-range gate

A source current \(a\in\mathcal A_{\exp}'\) has analytic provenance only if it lies in the range of the relevant transpose:

\[
a\in\operatorname{Ran}A_i'.
\]

Finite-cutoff solvability is insufficient. The minimum graph-dual norms of finite interpolants must remain bounded and compatible under cutoff restriction. Thus graph-domain existence and boundary provenance are separate gates:

1. joint closability constructs a faithful \(D\);
2. transpose-range membership attaches each named source current to an analytic boundary functional.

## Disposition

The naive automatic-intersection conjecture is rejected. The canonical candidate common domain is the joint graph completion of the typed finite-support source. Its first executable obstruction is joint closability, witnessed by a convergent source-null net with a nonzero limiting graph coordinate. If closability passes, the remaining current-by-current question is uniform transpose-range membership. No global Green identity should be claimed before both gates pass.
