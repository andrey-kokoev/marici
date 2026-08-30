# Raw Theta-Tail Coherency Crosses Sheets Off the Seam

## Hostile test of the new DPC

For the raw half-line theta transforms

\[
U(x,y)=\int_0^\infty\Phi(u)e^{yu}e^{ixu}\,du,
\qquad
V(x,y)=\int_0^\infty\Phi(u)e^{-yu}e^{ixu}\,du,
\]

the light-cone orientation coordinate is

\[
S_3(x,y)=|U(x,y)|^2-|V(x,y)|^2.
\]

The first hostile test asks whether (S_3) keeps one sign for fixed positive (y).

It does not.

At (y=0.2), five Simpson quadratures with independently varied mesh and endpoint all give

\[
S_3(15.7,0.2)>4.2\times10^{-7},
\]

and

\[
S_3(15.8,0.2)<-5.3\times10^{-7}.
\]

The raw coherency state therefore crosses (S_3=0) inside the open sector. A broader scan finds repeated crossings at larger (x).

## Scope correction

The rank-one coherency theorem remains exact. Completion plus complex seam still reduces the hidden fiber to two signs. What fails is the conjecture that the raw tail transport preserves one sign.

Thus the raw matrix

\[
H_{mathrm{tail}}=
\begin{pmatrix}
|U|^2 & UV\\
\overline{UV} & |V|^2
\end{pmatrix}
\]

is not yet the physical RH-bearing coherency object.

The missing dynamics must enter before the sheet claim through at least one of:

1. Clark differentiation and its odd quadrature;
2. the primitive and prime-square boundary currents;
3. the completed endpoint term;
4. a source-authorized change from raw tail power to a conserved flux coordinate.

Any corrected coherency matrix must reduce to the exact tail/seam factorization while altering the transported orientation coordinate for a source-derived reason. Fitting a positive correction after locating the crossings is prohibited.

## Meaning

The geometric-algebra picture survives but moves one level upward. The raw tail state travels on the coherency sphere and crosses its equator. RH, if captured by this architecture, must concern a completed connection or conserved section whose hemisphere is protected even while the raw presentation crosses.

This is closely analogous to the distinction between a moving coordinate presentation and a fixed physical object: sheet crossing of the raw chart is not yet loss of the completed relationship.

## Verification boundary

The exploration `research/grothendieck/explorations/raw_theta_stokes_sheet_crossing.py` reproduces the bracket with five refinements and writes `research/grothendieck/results/raw_theta_stokes_sheet_crossing.json`.

This is stable numerical reconnaissance, not directed interval certification. It is sufficient to reject the raw route as a research strategy; an exact analytic crossing theorem remains optional because the RH programme no longer depends on raw sheet preservation.
