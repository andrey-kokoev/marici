# Prime Resegmentation Is Not Equicontinuous in the Entire-Germ Topology

## Question

The finite prime-translation squares commute after canonical interval
resegmentation. Does that finite coherence pass automatically to the Euler
completion?

It does not in the ordinary Fréchet topology of entire source germs.

## Natural topology

Let the seminorms on entire functions be

\[
p_{R,n}(f)=\sup_{|y|\le R}|f^{(n)}(y)|,
\qquad R>0,\quad n\ge0.
\]

Prime transport through total logarithmic length \(L\) uses the translation

\[
(T_Lf)(y)=f(y+L).
\]

For every fixed \(L\), this map is continuous because

\[
p_{R,n}(T_Lf)\le p_{R+L,n}(f).
\]

The bound changes its controlling seminorm with \(L\). It supplies no
equicontinuity as the Euler cutoff grows.

## Exact obstruction

Take the single entire germ \(f(y)=e^y\). Then

\[
p_{R,0}(f)=e^R,
\qquad
p_{R,0}(T_Lf)=e^{R+L}.
\]

Thus the translation family \(\{T_L:L\ge0\}\) is not pointwise bounded and
hence not equicontinuous in this Fréchet space. Restricting \(L\) to sums of
prime logarithms does not help: those lengths are unbounded.

The same obstruction affects wall jets. Evaluation at the moving wall is

\[
f\longmapsto f^{(n)}(L),
\]

and the family of these evaluation functionals is not equicontinuous as
\(L\to\infty\).

## Meaning

Finite cocycle coherence is exact, but the most obvious completion topology
does not carry it uniformly. Therefore completion cannot be justified merely
by saying that every finite prime square commutes.

This is a genuine topology-selection gate. A viable completed carrier must
derive from the source one of the following:

1. weights that compensate logarithmic translation;
2. a moving family of seminorms covariant under prime transport;
3. a restricted orbit space smaller than all entire germs;
4. an explicit boundary-current completion in which the lost evaluations
   remain independent coordinates.

Choosing weights solely to make translation bounded would be circular. Their
normalization must come from the Mellin character, theta decay, the primitive
and square currents, or finite Euler reconstruction.

## Sharp next test

For a proposed source seminorm family \(P_\alpha\), compute the exact transport
ratio

\[
C_\alpha(L)=
\sup_{f\ne0}\frac{P_\alpha(T_Lf)}{P_{\beta(\alpha)}(f)}.
\]

The completion route survives only if the source supplies a controlling index
\(\beta(\alpha)\) and a bound compatible with arbitrary Euler cutoffs. The
hostile witness is any source-authorized orbit whose translated wall values
grow faster than that bound.

## Status

This does not disprove completion-stable coherence for the theta source. It
proves that the ordinary entire-germ completion is insufficient and locates
the first real obstruction after the finite cocycle theorem.
