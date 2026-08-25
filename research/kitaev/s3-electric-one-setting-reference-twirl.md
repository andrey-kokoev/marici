# One-setting electric-sector readout by a twirled flux reference

Owner: `marici.Kitaev`

## Bounded question

Can normalized-monodromy readout avoid maximally mixing the unknown target's
internal state on any nontrivial subdomain?

Yes for the pure-electric sectors `A,B,C`.  Prepare the trivial-centralizer-
charge transposition reference `D`, conjugate its flux by a uniformly random
element of `S3`, and perform the controlled monodromy trace setting.

## Exact reference twirl

Conjugating one fixed transposition by all six group elements produces each
of the three transpositions exactly twice.  Conjugating one fixed three-cycle
produces each of the two three-cycles exactly three times.  Thus classical
uniform group randomization prepares the uniform conjugacy-class mixture
without first identifying the target sector.

On the standard two-dimensional charge representation `C`, the exact
averages are

\[
{1\over3}\sum_{t\text{ transposition}}\rho_C(t)=0,
\qquad
{1\over2}\sum_{c\text{ three-cycle}}\rho_C(c)=-{1\over2}I.
\]

Both are scalar.  Consequently the target electric density matrix drops out:
no maximally mixed preparation of the unknown `C` internal state is needed.

## One-setting classifier

The normalized transposition-reference expectations are

\[
\mu_D(A)=1,\qquad \mu_D(B)=-1,\qquad \mu_D(C)=0.
\]

One binary Hadamard setting therefore has plus probabilities

\[
p_+(A)=1,\qquad p_+(B)=0,\qquad p_+(C)=1/2,
\]

and separates all three electric sectors.  The expectation gap is one, the
probability gap is `1/2`, and empirical-frequency error strictly below
`1/4` preserves unique classification.

Under uniform random reference conjugation, controlled monodromy,
independent repetitions, and stationary calibration,

\[
\Pr[|\widehat p-p|\ge1/4]\le2e^{-n/8},
\]

so `ceil(8 ln(2/alpha))` shots suffice for failure probability at most
`alpha`.

## Source and Carrier typing

Carrier geometry supplies the linked target/reference ribbons.  The quantum
coefficient lens supplies group conjugation, the reference flux mixture,
controlled monodromy, and binary ancilla effect.  Classical randomness is
retained as preparation history or discarded after verifying uniformity; the
averaged effect is the same.

The source requirement is narrower than sector-internal depolarization: a
fixed `D` reference, uniform random gauge conjugation, and coherent control
of its monodromy.  A local fault-tolerant implementation is still not derived.

## Verification and boundary

`uv run --with sympy python -u research/kitaev/checkers/check_s3_electric_reference_twirl.py`
passes seven gates.  It constructs the exact standard representation, counts
the conjugation orbits, proves both averaged matrices are scalar, and checks
the classifier and margins.  Fresh stdout matches the saved JSON.

The theorem covers only `A,B,C`.  It does not prove that the same reference
twirl removes internal-state dependence for flux/dyon targets, nor does it
resolve all eight sectors with one setting.  It is falsified by nonuniform
conjugacy counts, a nonscalar averaged standard action, or collision of the
three binary probabilities.
