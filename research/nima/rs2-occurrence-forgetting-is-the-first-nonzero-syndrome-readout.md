# RS-2 occurrence forgetting is the first nonzero syndrome readout

## Source map

Entry 356 defines the saturated occurrence-forgetting map

\[
F:\mathbb Z^6\longrightarrow\mathbb Z^3,
\]

which forgets the lower denominator while retaining the marked Cut. The six
occurrences are two regular \(C_3\)-orbits, while the three marked Cuts form
one regular orbit.

At the equal-energy cyclic fixed locus, let \(N_2\) be the direct sum of the
two occurrence norms and \(N_1\) the marked-Cut norm. Exact multiplication
gives

\[
\boxed{FN_2=N_1F}.
\]

Thus \(F\) is a source-derived chain map after reduction modulo three.

## Induced map

The norm homologies have dimensions

\[
\dim H(N_2)=2,\qquad \dim H(N_1)=1.
\]

The induced map has rank one:

\[
\boxed{\bar F:H(N_2)\twoheadrightarrow H(N_1)}.
\]

It identifies the two orbit-syndrome generators and leaves their difference
as a one-dimensional kernel.

By contrast, the all-positive scalar readout still induces zero on
\(H(N_2)\). Therefore \(\bar F\) is not yet a numerical period. It is the
first nonzero source-derived *coefficient/relative readout* of the
nonsemisimple syndrome.

## Meaning

The architecture is now visibly layered:

\[
\text{six source occurrences}
\xrightarrow{\text{forget lower denominator}}
\text{three marked Cuts}
\xrightarrow{\text{all-positive period}}
\text{scalar}.
\]

The first arrow sees the mod-three syndrome; the second does not. Information
can therefore survive at an intermediate relative/coefficient interface while
being invisible to the final scalar readout.

This is precisely the distinction between a coefficient lens and a physical
readout that the cross-sector programme has repeatedly required.

## Remaining gate

The one-dimensional target \(H(N_1)\) has the same field and dimension as the
string road class

\[
H^1(C_3,A_2)\cong\mathbb F_3.
\]

No identification is admitted yet. The next theorem must derive a Bockstein,
Tate, Kato, or other source kernel relating the marked-Cut norm quotient to
the road extension class. Uniqueness of a one-dimensional vector-space
isomorphism up to scalar is not naturality.

## Durable evidence

- Entries 356, 410, 436, 1552, and 1553;
- research/nima/checkers/check_rs2_occurrence_forgetting_on_norm_homology.py;
- research/nima/results/rs2-occurrence-forgetting-norm-homology.json.
