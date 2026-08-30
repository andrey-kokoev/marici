# Fourier acts between two polarized cyclic towers

## Correction to the single-tower candidate

Let the prime-valuation monoid be

\[
M_+=\bigoplus_p\mathbb N
\]

and let \(M_-=-M_+\). Their common group completion is

\[
M^{\mathrm{gp}}=\bigoplus_p\mathbb Z.
\]

Normalized additive Fourier transport reverses dilation:

\[
\mathcal F U_q=U_{-q}\mathcal F.
\]

Consequently it sends every positive prime valuation to the corresponding negative valuation. It cannot be an endomorphism of the positive Euler tower.

The completed cyclic object must therefore retain two polarizations:

\[
\widehat{\operatorname{Cyc}}(A_+)
\quad\text{and}\quad
\widehat{\operatorname{Cyc}}(A_-),
\]

where, schematically,

\[
\widehat{\operatorname{Cyc}}(A_\pm)
=
\prod_{n\ge1}(A_\pm^{\otimes n})_{C_n}.
\]

The product notation records arity. It does not choose the analytic completion topology.

Fourier has the typed components

\[
\mathcal F_n:
(A_+^{\otimes n})_{C_n}
\longrightarrow
(A_-^{\otimes n})_{C_n},
\qquad
\mathcal F_n=[\mathcal F^{\otimes n}].
\]

It preserves cyclic arity and reverses valuation orientation. Applying Fourier twice returns to the original tower, up to the already declared reflection convention.

## First two grades

At arity one,

\[
\mathcal F_1:A_+\to A_-.
\]

At arity two,

\[
\mathcal F_2:\operatorname{Sym}^2(A_+)\to
\operatorname{Sym}^2(A_-).
\]

The observer grades remain

\[
J_1(\phi)=\operatorname{Tr}(A_\phi)
\]

and

\[
\widetilde J_2(\phi\odot\psi)
=
\frac12\operatorname{Tr}
\left(A_\phi A_\psi+A_\psi A_\phi\right).
\]

Their naturality squares compare different target objects:

\[
J_{1,-}\mathcal F_1
=
T_{1,+-}J_{1,+},
\]

\[
J_{2,-}\mathcal F_2
=
T_{2,+-}J_{2,+}.
\]

A formula such as \(J\mathcal F=\mathcal F_{\mathrm{Euler}}J\) inside one positive target erases the polarization and is therefore ill-typed.

## Relative determinant comparison

The two cyclic towers produce relative determinant-line systems \(L_+\) and \(L_-\). The missing comparison is a line-valued cell

\[
\eta_{\mathcal F}:
\widehat J_-\widehat{\operatorname{Cyc}}(\mathcal F)
\Longrightarrow
\mathcal F_{\det,+-}\widehat J_+.
\]

For cutoffs \(X\subset Y\subset Z\), transition maps must satisfy

\[
\tau_{Z/X}=\tau_{Z/Y}\tau_{Y/X}
\]

and Fourier compatibility must hold at each cutoff inclusion:

\[
\tau^{\mathcal F}_{Y/X}\eta_{\mathcal F,X}
=
\eta_{\mathcal F,Y}\tau_{Y/X}.
\]

These equations do not authorize a scalar origin for either determinant line.

## Boundary meaning

The bilateral group completion is flat under reversal. The boundary defect appears only after choosing the positive polarization

\[
M_+\hookrightarrow M^{\mathrm{gp}}.
\]

Primitive and square currents are the first two cyclic coordinates retained at this polarized interface. They are not extra arithmetic missing from the additive theta source.

This makes the incidence map, rather than Fourier itself, the live constructor:

\[
\partial_\pm:
\widehat{\operatorname{Cyc}}(A_\pm)
\rightharpoonup L_\pm.
\]

The source problem is to construct \(\partial_+\), \(\partial_-\), and \(\eta_{\mathcal F}\) with the required topology and cutoff coherence.

## Finite falsifier

At one prime, let \(e_r\) have valuation \(r\). Fourier requires

\[
e_1\mapsto e_{-1}.
\]

No endomorphism of the positive valuation carrier can realize this image. At arity two the witness is

\[
e_1\odot e_1\mapsto e_{-1}\odot e_{-1}.
\]

More generally, reversal of a cyclic word is well defined on cyclic coinvariants and preserves its length, but changes its polarization whenever the word is non-vacuum.

## DPC

A proposed completed Fourier–cyclic constructor passes only if:

1. positive and negative valuation towers remain distinct;
2. every arity map is induced by tensor power before cyclic quotient;
3. cyclic equivalence is preserved;
4. word length is preserved;
5. valuation orientation is reversed;
6. the two applications of Fourier obey the declared reflection law;
7. determinant comparison is line-valued and cutoff-natural;
8. boundary incidence is constructed separately from bilateral Fourier transport.

The smallest failures are a one-tower image of \(e_1\), an unrecorded projection of \(e_{-1}\) back into \(M_+\), or scalar equality obtained only after identifying the two determinant lines.

## Outcome

SCC has correctly guessed the cyclic arity tower, but its source object must be doubled. The universal algebraic Fourier lift already exists between the two towers. What remains missing is not that lift; it is the polarized boundary incidence and the relative determinant-line comparison that transports its anomaly coordinates without choosing a scalar frame.
