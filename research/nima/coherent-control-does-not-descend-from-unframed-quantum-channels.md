# Coherent control does not descend from unframed quantum channels

## Question

Can the missing optical route-control operation be constructed from the two
completed channels alone?

## Claim boundary

No. A completed unitary channel forgets global phase, while a controlled
unitary makes that phase relative and observable. Consequently there is no
representative-independent constructor from an unframed unitary channel to its
controlled implementation.

## Channel quotient

A unitary \(U\) induces the channel

\[
\mathcal U(\rho)=U\rho U^\dagger.
\]

For every phase \(\omega\in U(1)\),

\[
\mathcal U=\mathcal{\omega U}.
\]

The channel object therefore identifies \(U\) and \(\omega U\).

## Controlled lift

The usual controlled implementation is

\[
C_U
=
|0\rangle\langle0|\otimes I
+
|1\rangle\langle1|\otimes U.
\]

Replacing \(U\) by \(\omega U\) gives

\[
C_{\omega U}
=
|0\rangle\langle0|\otimes I
+
\omega|1\rangle\langle1|\otimes U.
\]

The two controlled operators differ by a relative control phase, not a global
phase. They can produce different control-port records.

Thus the assignment \(\mathcal U\mapsto C_U\) is not defined on the channel
quotient. It requires a lift choosing a phase-framed representative of
\(\mathcal U\).

## Minimal exact witness

Take a one-dimensional target. The operators \(U=1\) and \(U=-1\) induce the
same identity channel. Their controlled lifts on the control qubit are

\[
C_1=I,
\qquad
C_{-1}=Z.
\]

Applied to the control state \(|+\rangle\), they produce \(|+\rangle\) and
\(|-\rangle\), which are perfectly distinguished by complementary ports.

Therefore the proposed coherent-control measurement does not reveal a hidden
property of the completed channel. It reveals which controlled lift the source
implemented.

## Consequence for the optical associator

Aspect’s current left and right routes are typed as completed observable
transformations. If they differ only by a global phase, they are the same
channel. No downstream operation on those channel objects can recover the
phase.

A coherent associator experiment must begin with stronger source objects:

1. phase-framed isometries, scattering amplitudes, or dilation operators;
2. a controlled constructor defined before quotienting by global phase;
3. a common phase standard relating the two controlled branches;
4. environment and hardware erasure preserving that standard;
5. final control-port interference.

The controlled constructor cannot be synthesized afterward from channel
tomography or equality of observable route maps.

## Categorical formulation

Let

\[
\pi:U(\mathcal H)\longrightarrow PU(\mathcal H)
\]

be the quotient by scalar phase. Controlled implementation is defined on
\(U(\mathcal H)\), not on \(PU(\mathcal H)\). A section of \(\pi\), or an
equivalent phase-framed source lift, is additional structure.

The failed square is the attempted factorization of controlled implementation
through \(\pi\). The two representatives \(U\) and \(-U\) have one image under
\(\pi\) and distinct controlled images.

## DPC

For every controlled-route proposal:

1. identify whether the input object is an amplitude, isometry, dilation,
   unitary modulo phase, or CPTP channel;
2. test invariance under \(U\mapsto\omega U\);
3. reject controlled construction from a phase-quotiented object;
4. require a source-derived phase-framed lift;
5. record the controlled lift as part of the experimental source, not as a
   property reconstructed from channel outputs;
6. delete the lift and confirm that associator phase becomes unobservable.

## Disposition

The missing optical constructor cannot be derived from the existing completed
channel equality tester. A positive experiment must move the source boundary
earlier, to phase-framed amplitude-level operations with native coherent
control. Otherwise the global associator phase is not an observable of the
declared object.

## Verification

The checker check_controlled_channel_phase_descent.py verifies that \(1\) and
\(-1\) induce the same target channel, their controlled lifts are distinct,
and the \(|+\rangle\) control input exits opposite ports.
