# The local five-cube blind class is a rank-one residue polynomial

## Question

Does the five-cube itself realize the one-dimensional interpolation kernel found globally at grade 165165, and what is the exact form of its shell residue?

## Claim boundary

The claim concerns the isolated 32-vertex, 80-edge Boolean five-cube with the five declared shell directions. It does not identify the local class with the global class without an inclusion-and-uniqueness argument, and it does not identify the residue polynomial with an augmentation-graded class without a comparison map.

## Predicted factorization

Use the four total evaluations

\[
T_4=\left\{1,\frac56,\frac34,\frac7{10}\right\}.
\]

A residue polynomial supported in shell degrees 1 through 5 and vanishing on \(T_4\) must be a vertex-vector multiple of

\[
q(z)=z(z-1)\left(z-\frac56\right)
\left(z-\frac34\right)\left(z-\frac7{10}\right).
\]

Therefore any local blind class \(x\) satisfies

\[
R_x(z)=q(z)v
\]

for some \(v\in V\), provided the four-setting evaluation matrix has its expected rank. This is tensor rank one across shell degree and vertex residue.

The fifth setting \(z=2/3\) detects the class exactly when

\[
q\left(\frac23\right)v\neq0.
\]

## Exact local test

Construct all 80 directed edges of the Boolean five-cube. Stack shell-weighted incidence at prefixes of

\[
1,\quad\frac56,\quad\frac34,\quad\frac7{10},\quad\frac23.
\]

Exact rational row reduction must establish:

- the preregistered terminal ranks 79 and 80 after four and five evaluations;
- the full computed rank sequence, with any intermediate mismatch retained;
- a unique blind direction after four evaluations;
- a nonzero fifth evaluation;
- coefficientwise factorization \(R_x(z)=q(z)v\);
- full four-evaluation rank after deleting the final edge \(12705\to15015\).

## Significance

The blind object is not merely counted by a rank defect. It is a route assignment whose five shell divergences are locked into the single coefficient vector of \(q\). The completed cube supplies a lift of the one-dimensional polynomial interpolation kernel through the shell-divergence map

\[
\Phi:E_{\square^5}\longrightarrow V\otimes k^5.
\]

The next character evaluation separates that coefficient direction because it lies outside the four prescribed roots.

## Strongest falsification attempt

The local explanation fails if the isolated cube has additional blind dimensions, if its residue does not factor through \(q\), if the fifth setting also vanishes, or if removal of the final edge leaves a blind class. Exact rational arithmetic tests every condition without modular lifting assumptions.

## Computed result

The exact local ranks are

\[
31,\quad57,\quad73,\quad79,\quad80,
\]

with nullities

\[
49,\quad23,\quad7,\quad1,\quad0.
\]

The initially anticipated intermediate ranks 56 and 74 were wrong; the terminal one-dimensional and zero-dimensional predictions survive. The unique four-evaluation kernel vector uses all 80 cube edges, while its vertex factor \(v\) uses all 32 vertices. Its shell polynomial is

\[
q(z)=\frac7{16}z-\frac{521}{240}z^2
+\frac{241}{60}z^3-\frac{197}{60}z^4+z^5.
\]

This equals the declared product polynomial. Evaluation at \(2/3\) is nonzero at all 32 vertices. Deleting the final edge restores full four-evaluation rank.

## Disposition

The local mechanism survives with a corrected intermediate rank profile. Five-cube completion lifts the unique four-root interpolation polynomial to a full-support edge route. The augmentation comparison remains a distinct open gate.
