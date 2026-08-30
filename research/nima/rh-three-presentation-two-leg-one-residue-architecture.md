# Three presentations, two legs, and one residue law

## Interpreting the proposed structure

The useful categorical reading of

\[
3(3+2+1)+2+1
\]

is not three independent copies of the same scalar construction.  It is three
complete source presentations:

1. \(\mathcal S_+\), the direct-sector presentation;
2. \(\mathcal S_-\), the reciprocal-sector presentation;
3. \(\mathcal M\), the mixed or seam-residue presentation.

Each presentation retains its own arithmetic grades, boundary carriers, and
completion law.  The additional two are source-derived incidence functors

\[
L_+:\mathcal S_+\longrightarrow\mathcal M,
\qquad
L_-:\mathcal S_-\longrightarrow\mathcal M.
\]

The final one is, by the established tower convention, a dynamical higher
constructor governing the residue of the two images.  A static declaration
that the legs are comparable would not count as a \(+1\) at all.

## Why three presentations and two legs still do not suffice

Let the comparison differential be

\[
\delta=L_+\oplus(-L_-):
\mathcal S_+\oplus\mathcal S_-\longrightarrow\mathcal M
\]

and let the scalar readout be

\[
\rho:\mathcal M\longrightarrow\mathcal O.
\]

A scalar zero says only

\[
\rho\delta(x_+,x_-)=0.
\]

It does not imply \(\delta(x_+,x_-)=0\).  Therefore it does not produce an
equalizer state.

The smallest hostile takes

\[
L_+(a)=(a,0),
\qquad
L_-(b)=(0,b),
\qquad
\rho(x,y)=x+y.
\]

For \((a,b)=(1,1)\), the comparison residue is \((1,-1)\ne0\), but its scalar
readout is zero.  The ordinary pullback of the two legs is still trivial.

## The boundary shadow of the final dynamic law

The final dynamic constructor must have, as its boundary shadow, a classifier
of the entire kernel of the readout.  Introduce a residue object \(\mathcal R\)
and the induced source-derived map

\[
h:\mathcal R\longrightarrow\mathcal M
\]

such that

\[
\operatorname{im}h=\ker\rho.
\]

Then every scalar zero has a typed lift:

\[
\rho\delta(x_+,x_-)=0
\quad\Longrightarrow\quad
\delta(x_+,x_-)=h(r)
\]

for some residue state \(r\).

The natural controlled object is no longer the strict equalizer.  It is the
mapping-cone or homotopy-fiber equation

\[
\delta(x_+,x_-)-h(r)=0.
\]

This repairs the zero-to-state typing gap.  Scalar cancellation becomes a
state in an augmented complex rather than an unjustified equality of the two
sector states.

## RH-bearing form

The architecture becomes relevant to RH only if all of the following are
source-derived:

- the three complete presentations \(\mathcal S_+\), \(\mathcal S_-\), and
  \(\mathcal M\);
- both incidence legs \(L_+\) and \(L_-\);
- the dynamical residue constructor whose boundary map is \(h\);
- exactness \(\operatorname{im}h=\ker\rho\);
- a completion-stable contraction on the augmented mapping cone away from the
  seam.

The earlier labelled equalizer estimate controls only the special case
\(r=0\).  The new problem is to control all residue lifts without suppressing
the genuine tangential spectrum at \(z=1/2\).

## DPC verdict

The proposed count identifies a plausible missing rung, but only when the
three terms mean three complete presentations, two incidence legs, and one
dynamical residue coherencer with an exact boundary classifier.

If the final one is weakened to a static comparison cell, the architecture is
mistyped and the two-coordinate cancellation hostile remains.  When its
dynamic action induces an exact residue classifier, the architecture supplies
the missing zero-to-state bridge and moves the RH frontier to acyclicity of the
augmented mapping cone.

Hostile symmetric multipliers remain decisive.  They must either fail to lift
through the source-derived residue object or create an augmented off-seam
cohomology class.  If neither happens, the residue law contains no information
beyond the scalar divisor.

## Verification

`check_rh_three_presentation_residue_law.py` verifies the strict-pullback
hostile, constructs the exact boundary classifier required of the dynamic
coherencer, and checks that scalar zeros lift to the augmented mapping-cone
kernel while nonzeros do not.
