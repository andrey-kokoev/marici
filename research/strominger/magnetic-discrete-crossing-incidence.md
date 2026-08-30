# Rational magnetic crossings have a discrete lattice incidence

The oriented crossing data does not require a continuous depth state.

At grade six, evaluate the scalar route augmentation

\[
S(d)=A(d)+B(d)
\]

only on admitted odd excess labels \(d=q-g\). Among adjacent labels through
\(d=31\), exactly two reverse sign:

\[
S(5)<0<S(7),
\]

and

\[
S(11)>0>S(13).
\]

The exact endpoint values are

\[
S(5)=-116807107608576000,
\]

\[
S(7)=2402889070804992000,
\]

\[
S(11)=105282139657863168000,
\]

\[
S(13)=-309772449377943552000.
\]

The rational analytic roots lie strictly inside these edges:

\[
5<\frac{17}{3}<7,
\qquad
11<\frac{37}{3}<13.
\]

## Discrete labelled incidence

For an oriented adjacent pair \(e:d_-\to d_+\), define

\[
\iota(e)=
\frac{\operatorname{sgn}S(d_+)-\operatorname{sgn}S(d_-)}{2}.
\]

Then

\[
\iota(5\to7)=+1,
\qquad
\iota(11\to13)=-1.
\]

These incidence numbers agree with the orientations of the analytically
continued scalar crossings. Both route coordinates and the complementary
difference character remain nonzero at all four endpoints, so the sign changes
are not caused by endpoint route loss.

The grade-two exception is different. At \(d=5\), both routes vanish at the
lattice vertex. It carries no nonzero interference-edge incidence.

## What this removes

No fractional configuration and no continuous evolution are needed to retain
the crossing orientation. The datum lives on ordered pairs of adjacent
admissible configurations:

\[
\text{vertex signs}
\longrightarrow
\text{oriented edge incidence}.
\]

This is a combinatorial sign-crossing shadow of the excluded rational zeros.
It is not yet a wall-crossing morphism.

## Remaining authority boundary

The odd excess labels possess a canonical numerical order and spacing by two.
That does not make every adjacent pair a source-authorized correspondence.
Indeed, the presently proved transfer law does not supply one:

\[
d=q-g,
\qquad
d\longmapsto d+2
\quad\Longleftrightarrow\quad
q\longmapsto q+2
\]

at fixed grade. By contrast, the determinant transfer extends the pole-depth
cutoff \(k\mapsto k+1\) inside a fixed component \(q\). It preserves both
\(q\) and \(d\). Therefore it cannot be used as authority for the adjacent
\(d\)-pair.

Three levels must be kept distinct:

- labelled incidence: established from the admitted labels and scalar
  evaluations;
- cutoff transfer: source-derived, but internal to fixed \(q\);
- component incidence: would require a new source operation relating \(q\) to
  \(q+2\).

No such inter-component constructor has been derived in the current magnetic
packet. The two incidence numbers are therefore exact comparisons between
labelled configurations, not source-derived crossing charges.

The next authority-bearing theorem would have to construct an inter-component
correspondence and prove naturality of the route packet under it. The existing
cutoff transfer cannot be repurposed for that job.

Replay:

\`python research/strominger/checkers/magnetic_discrete_crossing_incidence_checks.py\`
