# The Declared Supported Cospan Misses Exactly Two T7 Directions

At the frozen generic fiber \((x,y)=(2,3)\), combine the three logarithmic
extension classes with the three Cut-nearby classes in the ordered supported
block

\[
\langle e_2,e_3,e_4,e_5,e_6,v_{\rm alg}\rangle.
\]

Each image has rank three, their intersection is the \(e_6\) line, and their
combined rank is five.  Consequently their image in rank-seven \(T_7\) has
codimension two.

One missing direction is the entire \(e_1\) summand.  Inside the supported
six-dimensional block, the remaining quotient line is detected in the frozen
normalization by

\[
e_2^\vee-e_4^\vee+180v_{\rm alg}^\vee.
\]

The scalar 180 depends on the independent integral representatives used in the
source certificate; the one-dimensional quotient does not.  The unique
relation between the six displayed source columns is

\[
2g_{111}-\Theta_{101}-\Theta_{110}-2\Theta_{111}=0.
\]

Thus completing the physical readout calculus requires exactly two additional
supported resources: one detecting \(e_1\), and one detecting the intrinsic
quotient of the existing six-dimensional supported block.  Adding more copies
of the present logarithmic or Cut-nearby maps cannot supply either direction.

The source representative of \(e_1\) is the unique odd--odd master,
\(ab/\sqrt K\).  Algebraically it could be isolated by the odd--odd deck
projection of a bulk chain.  That projection is not presently physical:
existing source audits state that the selected positive chamber is not a deck
eigenvector and that its deck character is unselected.  Hence \(e_1\) requires
either a source-derived deck trace/continuation of the bulk chain or a different
bulk pairing; a formal character projector is not admissible evidence.

The second residual line is genuinely supported.  Its next test is the
Betti/Stokes comparison for the \(g_{101}\) and \(g_{110}\) extension lines.
The current weighted-tangency packet proves their pairings are generically
regular and nonzero, but does not identify ordinary global covectors on
\(T_7\); they must remain in the supported totalization.

The obstruction to specializing that packet is now explicit.  Along
\(z=E-x-y\), the exact resultant ratios for the two side walls have orders

\[
\operatorname{ord}_E(g_1)=\operatorname{ord}_E(g_2)=-2,
\]

with normalized leading coefficients

\[
\frac1{32x^4y^2},\qquad \frac1{32x^2y^4}.
\]

The top-wall ratio has order zero and leading coefficient

\[
\frac1{64x^4y^4(x+y)^2}.
\]

Thus the side-wall Stokes functionals require a derived \(E^2\) Rees
normalization before they can participate in the total-energy supported
pairing.  Naive restriction to \(E=0\) is undefined; generic nonvanishing does
not provide the missing comparison.

At the normalized coefficient level, however, the three leading values form a
perfect diagonal pairing on \(W_3\).  The two side entries exchange under
\(x\leftrightarrow y\), and the determinant is

\[
\frac{1}{65536x^{10}y^{10}(x+y)^2},
\]

which is nonzero on the frozen generic locus.  Hence the wall quotient itself
is no longer the blocker.  The remaining construction is the mixed
boundary-to-bulk connecting totalization carrying this perfect \(W_3\) pairing
through the rank-three extension image inside \(T_7\).

The canonical sewn occurrence/Kummer period does not provide an additional
absolute direction.  Entries 333--337 establish a horizontal sewn period line
but also prove that its endpoint mapping cone has no canonical horizontal
morphism into \(\langle e_6,v_{\rm alg}\rangle\subset T_7\).  Importing that
relative line into the residual absolute quotient would therefore repeat the
forbidden splitting error.

After this exclusion, the only declared source object capable of detecting the
two-dimensional quotient is the unsplit bulk physical period together with its
Gauss--Manin derivatives.  The sharp remaining test is to restrict that
source-normalized bulk covector and its first independent derivatives to

\[
T_7/(\operatorname{im}_{\log}+\operatorname{im}_{\rm Cut})
\]

and compute their rank.  Rank two completes the readout calculus; rank at most
one falsifies the currently declared physical family.  A deck-character
projection or an endpoint-cone lift may not be substituted for this test.

The repository-wide source audit shows that this test cannot yet be evaluated
from the connection packets alone.  The published two-site bubble boundary
values live in a different six-master family and do not define a covector on
this three-site (T_7).  In the three-site presentation, the literal
post-residue source form is canonical only in the unsplit localization fiber;
the source supplies no retraction to the absolute nine-master module and no
canonical (T_7) lift.  This does not invalidate evaluation of absolute
(T_7) forms on the literal bulk chain, but the required seven period values
have not been materialized.

Accordingly the minimal missing Betti packet is now explicit.  At one generic
source-normalized point it must provide

[
left(
int_{Gamma_{m BD}}e_1,ldots,
int_{Gamma_{m BD}}e_6,
int_{Gamma_{m BD}}v_{m alg}
ight),
]

together with the orientation, square-root sheet, regulator prescription, and
enough numerical or exact certification to distinguish rank one from rank two
after restriction to the residual quotient.  Gauss--Manin derivatives may
then be generated by the already certified bivariate connection.  Supplying a
generic seven-vector, importing the two-site boundary vector, or projecting
the unsplit source form through a chosen localization splitting would all
change the question.
