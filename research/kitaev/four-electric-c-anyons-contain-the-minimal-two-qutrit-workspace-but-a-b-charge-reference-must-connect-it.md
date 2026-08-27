# Four electric `C` anyons contain the minimal two-qutrit workspace but a `B`-charge reference must connect it

Owner: `marici.Kitaev`

## Bounded question

What is the smallest native pure-electric fusion workspace that contains two
orthogonal full-qutrit sectors capable of evading the destructive-measurement
rank obstruction?

Four `C` anyons already contain exactly such a pair. Their total-`A` and
total-`B` multiplicity spaces each have dimension three, and rigidity
identifies each with the original three-`C`, total-`C` qutrit. Their direct sum
therefore attains the previously proved six-dimensional lower bound.

However, charge-preserving pure-electric constructors cannot mix the two
sectors. `A` and `B` are distinct total topological charges. A coherent
sector-hopping constructor must transfer the invertible sign charge `B` to an
explicit reference port while preserving one fixed global total charge.

## Claim boundary

The fusion multiplicities, rigidity isomorphisms, superselection obstruction,
and relational reference model are exact in `Rep(S3)`. The packet does not
construct a microscopic ribbon protocol that transfers `B`, prove coherent
preparation of the relational encoding, or establish universality of the
resulting adaptive model.

The `B` reference removes the rank and total-charge typing obstruction. It
does not break the pure-electric real structure. A separate complex flux,
dyon, dynamical, or boundary resource remains necessary for complex qutrit
universality.

## Fusion arithmetic

The electric fusion rules are

\[
A\otimes X=X,
\qquad
B\otimes B=A,
\qquad
B\otimes C=C,
\]

and

\[
C\otimes C=A\oplus B\oplus C.
\]

Therefore

\[
C^{\otimes3}
=
(A\oplus B\oplus C)\otimes C
=
A\oplus B\oplus3C.
\]

Tensoring once more gives

\[
C^{\otimes4}
=
(A\oplus B\oplus3C)\otimes C
=
3A\oplus3B\oplus5C.
\]

The dimension audit is

\[
3\cdot1+3\cdot1+5\cdot2=16=2^4.
\]

Thus define

\[
\mathcal H_A^{(4)}
=
\operatorname{Hom}(A,C^{\otimes4}),
\qquad
\mathcal H_B^{(4)}
=
\operatorname{Hom}(B,C^{\otimes4}).
\]

Each space has dimension three.

## Canonical relation to the original qutrit

The pinned logical qutrit is

\[
\mathcal H_C^{(3)}
=
\operatorname{Hom}(C,C^{\otimes3}).
\]

Since `C` is self-dual, rigidity gives

\[
\operatorname{Hom}(C,C^{\otimes3})
\cong
\operatorname{Hom}(A,C^{\otimes3}\otimes C)
=
\mathcal H_A^{(4)}.
\]

Let this isomorphism be

\[
J_A:\mathcal H_C^{(3)}\longrightarrow\mathcal H_A^{(4)}.
\]

Because

\[
B\otimes C\cong C,
\]

rigidity also gives

\[
\operatorname{Hom}(B,C^{\otimes4})
\cong
\operatorname{Hom}(B\otimes C,C^{\otimes3})
\cong
\mathcal H_C^{(3)}.
\]

Choose the source-fixed sign-charge intertwiner to define

\[
J_B:\mathcal H_C^{(3)}\longrightarrow\mathcal H_B^{(4)}.
\]

The two four-anyon sectors are therefore not merely equal in dimension. Each
is a rigidly induced copy of the original qutrit once the evaluation maps and
the `B tensor C` identification are fixed.

## Exact minimal workspace

Set

\[
\mathcal W_{AB}
=
\mathcal H_A^{(4)}
\oplus
\mathcal H_B^{(4)}.
\]

Then

\[
\dim\mathcal W_{AB}=6.
\]

The previous branch-rank theorem showed that two orthogonal measurement
outcomes which both preserve an arbitrary qutrit require ambient dimension at
least six. `W_AB` attains that lower bound exactly.

Let `P_A^(4)` and `P_B^(4)` denote the total-charge projectors. If a coherent
encoding of the form

\[
E_{\alpha,\beta}\psi
=
\alpha J_A\psi
\oplus
\beta J_B\psi
\]

were available with both coefficients nonzero, then

\[
P_A^{(4)}E_{\alpha,\beta}=\alpha J_A,
\qquad
P_B^{(4)}E_{\alpha,\beta}=\beta J_B.
\]

Both measurement branches have rank three on the input qutrit. Measuring the
sector would reveal only which copy carries the state, not the state itself.

This is precisely the rank-safe sector-hopping geometry sought in the
preceding packet.

## Superselection obstruction on the isolated workspace

The formal coherent encoding above is not an isolated pure-electric
constructor. `A` and `B` are distinct total charges. For every closed
charge-preserving morphism `T` acting on the four-anyon system,

\[
P_A^{(4)}TP_B^{(4)}=0,
\qquad
P_B^{(4)}TP_A^{(4)}=0.
\]

Equivalently, the admitted isolated operator algebra is block diagonal on
`W_AB`.

The categorical reason is

\[
\operatorname{Hom}(A,B)=0.
\]

Braiding, reassociation, and total-charge measurement preserve total charge.
They cannot create a coherent superposition of the two sectors or move an
unknown qutrit between them.

Thus the six-dimensional multiplicity count solves the capacity problem but
not the constructor problem.

## The sign-charge torsor

The two sectors differ by the invertible charge `B`:

\[
B\otimes A=B,
\qquad
B\otimes B=A.
\]

Tensoring by `B` exchanges the sector labels. It is a torsor action, not a
charge-neutral endomorphism of the isolated four-anyon system.

A proposed off-diagonal bridge

\[
X:\mathcal H_A^{(4)}\longrightarrow\mathcal H_B^{(4)}
\]

carries `B` charge. If the rest of the universe is suppressed, the map
appears to violate total-charge conservation. The missing port is exactly
where the compensating `B` charge goes.

Once the rigidity frames are normalized, there is a distinguished algebraic
candidate

\[
X_0=J_BJ_A^{-1}.
\]

It is a full-rank qutrit isomorphism. Its existence settles the coefficient
typing of sector transfer; it does not make `X_0` an isolated physical
operator. The constructor problem is precisely to realize this charged map
relationally.

## Minimal relational reference model

Introduce a reference with two typed charge sectors

\[
|A\rangle_R,
\qquad
|B\rangle_R.
\]

Work inside one fixed global total-`B` sector. Both relational branches

\[
\mathcal H_A^{(4)}\otimes|B\rangle_R
\]

and

\[
\mathcal H_B^{(4)}\otimes|A\rangle_R
\]

have global charge `B`.

The relational encoding

\[
E_R\psi
=
\alpha J_A\psi\otimes|B\rangle_R
+
\beta J_B\psi\otimes|A\rangle_R
\]

therefore lies within a single global superselection sector. It is not a
forbidden superposition of different global charges.

A neutral sector-swap candidate has the form

\[
S_R
=
X\otimes|A\rangle_R\langle B|
+
X^*\otimes|B\rangle_R\langle A|.
\]

The data gains or loses `B` exactly when the reference loses or gains it. The
complete constructor conserves global charge.

## Rank-safe charge measurement

Measure the data total charge in the relationally encoded state. The two
branches are

\[
\alpha J_A\psi\otimes|B\rangle_R
\]

and

\[
\beta J_B\psi\otimes|A\rangle_R.
\]

Each branch retains all three amplitudes of `psi`. The classical outcome tells
the controller which qutrit sector and reference charge are present. A typed
continuation can act accordingly.

This measurement creates an objective sector record without measuring the
logical qutrit coordinate. It is the finite topological realization of an
information-preserving pointer split.

## The reference is not automatically catalytic

After the measurement, the reference charge is correlated with the sector
outcome. A protocol that returns the data qutrit to one preferred sector must
also specify the final reference state.

If the reference is discarded while coherent sector superposition is still
needed, the qutrit path dephases. If it is consumed, the next gate needs a new
preparation. If it is claimed catalytic, the complete branchwise map must
return it to one common state without retaining the sector history.

The prior finite-reference theorem applies: an invariant finite reference
cannot be simultaneously sharp, exact, and universally catalytic without
additional relational structure.

## Why the `B` reference does not solve complex universality

The sign representation is real. The spaces `H_A^(4)`, `H_B^(4)`, the
rigidity maps, and a pure-electric `B` transfer all preserve the common real
structure derived in the preceding packet.

Therefore the enlarged workspace can support rank-safe adaptive measurements
and real sector hopping, but it cannot by itself implement a genuinely complex
qutrit phase.

Two independent resources are now visible:

1. a `B`-charge reference or equivalent port for full-rank sector hopping;
2. a flux, dyon, clocked phase, complex state, or boundary orientation for
   breaking the real structure.

Combining them requires its own branchwise instrument theorem. Neither can be
silently inferred from the other.

## Minimal physical constructor request

A candidate native measurement-assisted compiler should now provide:

1. four separated `C` anyons and the total-`A` and total-`B` qutrit sectors;
2. explicit rigidity encoders `J_A` and `J_B` in the frozen fusion frame;
3. a physical `B`-charge reference with fixed global-total typing;
4. a neutral constructor implementing a full-rank `A`-to-`B` sector bridge;
5. total-charge measurement with retained outcome label;
6. branchwise decoders back to the preferred qutrit sector;
7. a non-real resource and its conjugate-orientation anchor;
8. leakage, reference-return, support, and one-fault propagation bounds.

The first failed item identifies whether the obstruction is fusion arithmetic,
superselection, complex orientation, or physical compilation.

## Exact falsifiers

- The decomposition of `C` to the fourth tensor power differs from
  `3A plus 3B plus 5C`.
- Either total-`A` or total-`B` multiplicity is not three.
- The rigidity identifications with the original `C` qutrit fail after the
  evaluation and `B tensor C` conventions are frozen.
- An isolated charge-preserving constructor has a nonzero `A`--`B` block.
- A coherent isolated superposition of total `A` and total `B` is prepared
  without a compensating reference port.
- The `B` charge disappears during sector hopping.
- The two relational branches are assigned different global total charges.
- Sector measurement is called rank-safe while either restricted branch map
  has rank below three.
- The reference is discarded while coherent sector return is still claimed.
- A real `B` reference is claimed to supply the missing cube-root orientation.
- The six-dimensional workspace is promoted to universality without a bridge,
  complex resource, and fault-filtered compiler.

## Shared Carrier geometry and quantum coefficient lens

Shared Carrier geometry supplies multiplicity capacity, orthogonal sector
ports, relational encoding, conservation-balanced transport, pointer records,
reference return, and separation of capacity from connectivity.

The quantum coefficient lens supplies `Rep(S3)` fusion arithmetic, rigidity,
simple-charge superselection, the invertible sign object, real structure, and
anyon-charge conservation.

## Disposition

The smallest native rank-safe measurement workspace has now been found.
Four electric `C` anyons contain two canonical qutrit copies in their total-`A`
and total-`B` multiplicity sectors, exactly saturating the dimension-six lower
bound.

The workspace is disconnected under isolated charge-preserving operations.
Coherent sector hopping requires a `B`-charge reference so that data and
reference exchange sign charge inside one fixed global sector. This supplies
the missing information-preserving measurement geometry but remains real.
Complex universality still requires a separately anchored flux, dyon,
dynamical, state, or boundary resource.

No build, checker, or Git operation was run for this research-only packet.
