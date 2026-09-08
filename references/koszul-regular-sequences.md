15.31 Koszul regular sequences

Please take a look at Algebra, Sections 10.68, 10.69, and 10.72 before looking at this one.

Definition 15.31.1. Let R be a ring. Let r≥0 and let f1,…,fr∈R be a sequence of elements. Let M be an R-module. The sequence f1,…,fr is called

    M-Koszul-regular if Hi(K∙(f1,…,fr)⊗RM)=0 for all i≠0,

    M-H1-regular if H1(K∙(f1,…,fr)⊗RM)=0,

    Koszul-regular if Hi(K∙(f1,…,fr))=0 for all i≠0, and

    H1-regular if H1(K∙(f1,…,fr))=0.

We will see in Lemmas 15.31.2, 15.31.3, and 15.31.6 that for elements f1,…,fr of a ring R we have the following implications
f1,…,fr is a regular sequence⇒f1,…,fr is a Koszul-regular sequence⇒f1,…,fr is an H1-regular sequence⇒f1,…,fr is a quasi-regular sequence.

In general none of these implications can be reversed, but if R is a Noetherian local ring and f1,…,fr∈mR, then the four conditions are all equivalent (Lemma 15.31.7). If f=f1∈R is a length 1 sequence and f is not a unit of R then it is clear that the following are all equivalent

    f is a regular sequence of length one,

    f is a Koszul-regular sequence of length one, and

    f is a H1-regular sequence of length one.

It is also clear that these imply that f is a quasi-regular sequence of length one. But there do exist quasi-regular sequences of length 1 which are not regular sequences. Namely, let
R=k[x,y0,y1,…]/(xy0,xy1−y0,xy2−y1,…)

and let f be the image of x in R. Then f is a zerodivisor, but ⨁n≥0(fn)/(fn+1)≅k[x] is a polynomial ring.

Lemma 15.31.2. Let R be a ring, M an R-module, and f1,…,fr∈R such that for i=1,…,r multiplication by fi is injective on M/(f1,…,fi−1)M. Then f1,…,fr is M-Koszul regular. In particular, an M-regular sequence is M-Koszul-regular and any regular sequence is Koszul-regular.

Proof. Let R, M, f1,…,fr be as in the first sentence of the lemma. If r=1, it is immediate that f1 is M-Koszul-regular. Assume r>1. Since f1 is a nonzerodivisor on M, we obtain a short exact sequence of complexes:

0→K∙(f2,…,fr)⊗M−→f1K∙(f2,…,fr)⊗M→K∙(f¯¯¯2,…,f¯¯¯r)⊗M/f1M→0

Here f¯¯¯i is the image of fi in R/(f1). By Lemma 15.29.8 the complex K∙(f1,…,fr) is isomorphic to the cone of multiplication by f1 on K∙(f2,…,fr). Thus K∙(R,f1,…,fr)⊗M is isomorphic to the cone on the first map. Hence K∙(f¯¯¯2,…,f¯¯¯r)⊗M/f1M is quasi-isomorphic to K∙(f1,…,fr)⊗M. As R/(f1), M/f1M, f¯¯¯2,…,f¯¯¯r satisfy the conditions of the lemma, by induction we conclude this complex is acyclic in postive degrees. This finishes the proof of the first statement. The second statement immediately follows from the first. □

Lemma 15.31.3. A M-Koszul-regular sequence is M-H1-regular. A Koszul-regular sequence is H1-regular.

Proof. This is immediate from the definition. □

Lemma 15.31.4. Let f1,…,fr−1∈R be a sequence and f,g∈R. Let M be an R-module.

    If f1,…,fr−1,f and f1,…,fr−1,g are M-H1-regular then f1,…,fr−1,fg is M-H1-regular too.

    If f1,…,fr−1,f and f1,…,fr−1,g are M-Koszul-regular then f1,…,fr−1,fg is M-Koszul-regular too.

Proof. By Lemma 15.29.11 we have exact sequences

Hi(K∙(f1,…,fr−1,f)⊗M)→Hi(K∙(f1,…,fr−1,fg)⊗M)→Hi(K∙(f1,…,fr−1,g)⊗M)

for all i. □

Lemma 15.31.5. Let φ:R→S be a flat ring map. Let f1,…,fr∈R. Let M be an R-module and set N=M⊗RS.

    If f1,…,fr in R is an M-H1-regular sequence, then φ(f1),…,φ(fr) is an N-H1-regular sequence in S.

    If f1,…,fr is an M-Koszul-regular sequence in R, then φ(f1),…,φ(fr) is an N-Koszul-regular sequence in S.

Proof. This is true because K∙(f1,…,fr)⊗RS=K∙(φ(f1),…,φ(fr)) and therefore (K∙(f1,…,fr)⊗RM)⊗RS=K∙(φ(f1),…,φ(fr))⊗SN. □

Lemma 15.31.6. An M-H1-regular sequence is M-quasi-regular.

Proof. Let R be a ring and let M be an R-module. Let f1,…,fr be an M-H1-regular sequence. Denote J=(f1,…,fr). The assumption means that we have an exact sequence

∧2(Rr)⊗M→R⊕r⊗M→JM→0

where the first arrow is given by ei∧ej⊗m↦(fiej−fjei)⊗m. Tensoring the sequence with R/J we see that

JM/J2M=(R/J)⊕r⊗RM=(M/JM)⊕r

is a finite free module. To finish the proof we have to prove for every n≥2 the following: if

ξ=∑|I|=n,I=(i1,…,ir)mIfi11…firr∈Jn+1M

then mI∈JM for all I. In the next paragraph, we prove mI∈JM for I=(0,…,0,n) and in the last paragraph we deduce the general case from this special case.

Let I=(0,…,0,n). Let ξ be as above. We can write ξ=m1f1+…+mr−1fr−1+mIfnr. As we have assumed ξ∈Jn+1M, we can also write ξ=∑1≤i≤j≤r−1mijfifj+∑1≤i≤r−1m′ififnr+m′′fn+1r. Then we see that

(m1−m11f1−m′1fnr)f1+(m2−m12f1−m22f2−m′2fnr)f2+…+(mr−1−m1r−1f1−…−mr−1r−1fr−1−m′r−1fnr)fr−1+(mI−m′′fr)fnr=0

Since f1,…,fr−1,fnr is M-H1-regular by Lemma 15.31.4 we see that mI−m′′fr is in the submodule f1M+…+fr−1M+fnrM. Thus mI∈f1M+…+frM.

Let S=R[x1,x2,…,xr,1/xr]. The ring map R→S is faithfully flat, hence f1,…,fr is an M-H1-regular sequence in S, see Lemma 15.31.5. By Lemma 15.29.4 we see that

g1=f1−x1xrfr, …, gr−1=fr−1−xr−1xrfr, gr=1xrfr

is an M-H1-regular sequence in S. Finally, note that our element ξ can be rewritten

ξ=∑|I|=n,I=(i1,…,ir)mI(g1+x1gr)i1…(gr−1+xr−1gr)ir−1(xrgr)ir

and the coefficient of gnr in this expression is

∑mIxi11…xirr

By the case discussed in the previous paragraph this sum is in J(M⊗RS). Since the monomials xi11…xirr form part of an R-basis of S over R we conclude that mI∈J for all I as desired. □

For nonzero finite modules over Noetherian local rings all of the types of regular sequences introduced so far are equivalent.

Lemma 15.31.7. Let (R,m) be a Noetherian local ring. Let M be a nonzero finite R-module. Let f1,…,fr∈m. The following are equivalent

    f1,…,fr is an M-regular sequence,

    f1,…,fr is a M-Koszul-regular sequence,

    f1,…,fr is an M-H1-regular sequence,

    f1,…,fr is an M-quasi-regular sequence.

In particular the sequence f1,…,fr is a regular sequence in R if and only if it is a Koszul regular sequence, if and only if it is a H1-regular sequence, if and only if it is a quasi-regular sequence.

Proof. The implication (1) ⇒ (2) is Lemma 15.31.2. The implication (2) ⇒ (3) is Lemma 15.31.3. The implication (3) ⇒ (4) is Lemma 15.31.6. The implication (4) ⇒ (1) is Algebra, Lemma 10.69.6. □

Lemma 15.31.8. Let A be a ring. Let I⊂A be an ideal. Let g1,…,gm be a sequence in A whose image in A/I is H1-regular. Then I∩(g1,…,gm)=I(g1,…,gm).

Proof. Consider the exact sequence of complexes

0→I⊗AK∙(A,g1,…,gm)→K∙(A,g1,…,gm)→K∙(A/I,g1,…,gm)→0

Since the complex on the right has H1=0 by assumption we see that

Coker(I⊕m→I)⟶Coker(A⊕m→A)

is injective. This is equivalent to the assertion of the lemma. □

Lemma 15.31.9. Let A be a ring. Let I⊂J⊂A be ideals. Assume that J/I⊂A/I is generated by an H1-regular sequence. Then I∩J2=IJ.

Proof. To prove this choose g1,…,gm∈J whose images in A/I form a H1-regular sequence which generates J/I. In particular J=I+(g1,…,gm). Suppose that x∈I∩J2. Because x∈J2 can write

x=∑aijgigj+∑ajgj+a

with aij∈A, aj∈I and a∈I2. Then ∑aijgigj∈I∩(g1,…,gm) hence by Lemma 15.31.8 we see that ∑aijgigj∈I(g1,…,gm). Thus x∈IJ as desired. □

Lemma 15.31.10. Let A be a ring. Let I be an ideal generated by a quasi-regular sequence f1,…,fn in A. Let g1,…,gm∈A be elements whose images g¯¯¯1,…,g¯¯¯m form an H1-regular sequence in A/I. Then f1,…,fn,g1,…,gm is a quasi-regular sequence in A.

Proof. We claim that g1,…,gm forms an H1-regular sequence in A/Id for every d. By induction assume that this holds in A/Id−1. We have a short exact sequence of complexes

0→K∙(A,g∙)⊗AId−1/Id→K∙(A/Id,g∙)→K∙(A/Id−1,g∙)→0

Since f1,…,fn is quasi-regular we see that the first complex is a direct sum of copies of K∙(A/I,g1,…,gm) hence acyclic in degree 1. By induction hypothesis the last complex is acyclic in degree 1. Hence also the middle complex is. In particular, the sequence g1,…,gm forms a quasi-regular sequence in A/Id for every d≥1, see Lemma 15.31.6. Now we are ready to prove that f1,…,fn,g1,…,gm is a quasi-regular sequence in A. Namely, set J=(f1,…,fn,g1,…,gm) and suppose that (with multinomial notation)

∑|N|+|M|=daN,MfNgM∈Jd+1

for some aN,M∈A. We have to show that aN,M∈J for all N,M. Let e∈{0,1,…,d}. Then

∑|N|=d−e, |M|=eaN,MfNgM∈(g1,…,gm)e+1+Id−e+1

Because g1,…,gm is a quasi-regular sequence in A/Id−e+1 we deduce

∑|N|=d−eaN,MfN∈(g1,…,gm)+Id−e+1

for each M with |M|=e. By Lemma 15.31.8 applied to Id−e/Id−e+1 in the ring A/Id−e+1 this implies ∑|N|=d−eaN,MfN∈Id−e(g1,…,gm). Since f1,…,fn is quasi-regular in A this implies that aN,M∈J for each N,M with |N|=d−e and |M|=e. This proves the lemma. □

Lemma 15.31.11. Let A be a ring. Let I be an ideal generated by an H1-regular sequence f1,…,fn in A. Let g1,…,gm∈A be elements whose images g¯¯¯1,…,g¯¯¯m form an H1-regular sequence in A/I. Then f1,…,fn,g1,…,gm is an H1-regular sequence in A.

Proof. We have to show that H1(A,f1,…,fn,g1,…,gm)=0. To do this consider the commutative diagram

∧2(A⊕n+m)A⊕n+mA0∧2(A/I⊕m)A/I⊕mA/I0

Consider an element (a1,…,an+m)∈A⊕n+m which maps to zero in A. Because g¯¯¯1,…,g¯¯¯m form an H1-regular sequence in A/I we see that (a¯¯¯n+1,…,a¯¯¯n+m) is the image of some element α¯¯¯ of ∧2(A/I⊕m). We can lift α¯¯¯ to an element α∈∧2(A⊕n+m) and subtract the image of it in A⊕n+m from our element (a1,…,an+m). Thus we may assume that an+1,…,an+m∈I. Since I=(f1,…,fn) we can modify our element (a1,…,an+m) by linear combinations of the elements

(0,…,gj,0,…,0,fi,0,…,0)

in the image of the top left horizontal arrow to reduce to the case that an+1,…,an+m are zero. In this case (a1,…,an,0,…,0) defines an element of H1(A,f1,…,fn) which we assumed to be zero. □

Lemma 15.31.12. Let A be a ring. Let f1,…,fn,g1,…,gm∈A be an H1-regular sequence. Then the images g¯¯¯1,…,g¯¯¯m in A/(f1,…,fn) form an H1-regular sequence.

Proof. Set I=(f1,…,fn). We have to show that any relation ∑j=1,…,ma¯¯¯jg¯¯¯j in A/I is a linear combination of trivial relations. Because I=(f1,…,fn) we can lift this relation to a relation

∑j=1,…,majgj+∑i=1,…,nbifi=0

in A. By assumption this relation in A is a linear combination of trivial relations. Taking the image in A/I we obtain what we want. □

Lemma 15.31.13. Let A be a ring. Let I be an ideal generated by a Koszul-regular sequence f1,…,fn in A. Let g1,…,gm∈A be elements whose images g¯¯¯1,…,g¯¯¯m form a Koszul-regular sequence in A/I. Then f1,…,fn,g1,…,gm is a Koszul-regular sequence in A.

Proof. Our assumptions say that K∙(A,f1,…,fn) is a finite free resolution of A/I and K∙(A/I,g¯¯¯1,…,g¯¯¯m) is a finite free resolution of A/(fi,gj) over A/I. Then

K∙(A,f1,…,fn,g1,…,gm)=Tot(K∙(A,f1,…,fn)⊗AK∙(A,g1,…,gm))≅A/I⊗AK∙(A,g1,…,gm)=K∙(A/I,g¯¯¯1,…,g¯¯¯m)≅A/(fi,gj)

The first equality by Lemma 15.29.12. The first quasi-isomorphism ≅ by (the dual of) Homology, Lemma 12.25.4 as the qth row of the double complex K∙(A,f1,…,fn)⊗AK∙(A,g1,…,gm) is a resolution of A/I⊗AKq(A,g1,…,gm). The second equality is clear. The last quasi-isomorphism by assumption. Hence we win. □

To conclude in the following lemma it is necessary to assume that both f1,…,fn and f1,…,fn,g1,…,gm are Koszul-regular. A counter example to dropping the assumption that f1,…,fn is Koszul-regular is Examples, Lemma 110.15.1.

Lemma 15.31.14. Let A be a ring. Let f1,…,fn,g1,…,gm∈A. If both f1,…,fn and f1,…,fn,g1,…,gm are Koszul-regular sequences in A, then g¯¯¯1,…,g¯¯¯m in A/(f1,…,fn) form a Koszul-regular sequence.

Proof. Set I=(f1,…,fn). Our assumptions say that K∙(A,f1,…,fn) is a finite free resolution of A/I and K∙(A,f1,…,fn,g1,…,gm) is a finite free resolution of A/(fi,gj) over A. Then

A/(fi,gj)≅K∙(A,f1,…,fn,g1,…,gm)=Tot(K∙(A,f1,…,fn)⊗AK∙(A,g1,…,gm))≅A/I⊗AK∙(A,g1,…,gm)=K∙(A/I,g¯¯¯1,…,g¯¯¯m)

The first quasi-isomorphism ≅ by assumption. The first equality by Lemma 15.29.12. The second quasi-isomorphism by (the dual of) Homology, Lemma 12.25.4 as the qth row of the double complex K∙(A,f1,…,fn)⊗AK∙(A,g1,…,gm) is a resolution of A/I⊗AKq(A,g1,…,gm). The second equality is clear. Hence we win. □

Lemma 15.31.15. Let R be a ring. Let I be an ideal generated by f1,…,fr∈R.

    If I can be generated by a quasi-regular sequence of length r, then f1,…,fr is a quasi-regular sequence.

    If I can be generated by an H1-regular sequence of length r, then f1,…,fr is an H1-regular sequence.

    If I can be generated by a Koszul-regular sequence of length r, then f1,…,fr is a Koszul-regular sequence.

Proof. If I can be generated by a quasi-regular sequence of length r, then I/I2 is free of rank r over R/I. Since f1,…,fr generate by assumption we see that the images f¯¯¯i form a basis of I/I2 over R/I. It follows that f1,…,fr is a quasi-regular sequence as all this means, besides the freeness of I/I2, is that the maps SymnR/I(I/I2)→In/In+1 are isomorphisms.

We continue to assume that I can be generated by a quasi-regular sequence, say g1,…,gr. Write gj=∑aijfi. As f1,…,fr is quasi-regular according to the previous paragraph, we see that det(aij) is invertible mod I. The matrix aij gives a map R⊕r→R⊕r which induces a map of Koszul complexes α:K∙(R,f1,…,fr)→K∙(R,g1,…,gr), see Lemma 15.29.3. This map becomes an isomorphism on inverting det(aij). Since the cohomology modules of both K∙(R,f1,…,fr) and K∙(R,g1,…,gr) are annihilated by I, see Lemma 15.29.6, we see that α is a quasi-isomorphism.

Now assume that g1,…,gr is a H1-regular sequence generating I. Then g1,…,gr is a quasi-regular sequence by Lemma 15.31.6. By the previous paragraph we conclude that f1,…,fr is a H1-regular sequence. Similarly for Koszul-regular sequences. □

Lemma 15.31.16. Let R be a ring. Let a1,…,an∈R be elements such that R→R⊕n, x↦(xa1,…,xan) is injective. Then the element ∑aiti of the polynomial ring R[t1,…,tn] is a nonzerodivisor.

Proof. If one of the ai is a unit this is just the statement that any element of the form t1+a2t2+…+antn is a nonzerodivisor in the polynomial ring over R.

Case I: R is Noetherian. Let qj, j=1,…,m be the associated primes of R. We have to show that each of the maps

∑aiti:Symd(R⊕n)⟶Symd+1(R⊕n)

is injective. As Symd(R⊕n) is a free R-module its associated primes are qj, j=1,…,m. For each j there exists an i=i(j) such that ai∉qj because there exists an x∈R with qjx=0 but aix≠0 for some i by assumption. Hence ai is a unit in Rqj and the map is injective after localizing at qj. Thus the map is injective, see Algebra, Lemma 10.63.19.

Case II: R general. We can write R as the union of Noetherian rings Rλ with a1,…,an∈Rλ. For each Rλ the result holds, hence the result holds for R. □

Lemma 15.31.17. Let R be a ring. Let f1,…,fn be a Koszul-regular sequence in R such that (f1,…,fn)≠R. Consider the faithfully flat, smooth ring map
R⟶S=R[{tij}i≤j,t−111,t−122,…,t−1nn]

For 1≤i≤n set
gi=∑i≤jtijfj∈S.

Then g1,…,gn is a regular sequence in S and (f1,…,fn)S=(g1,…,gn).

Proof. The equality of ideals is obvious as the matrix

⎛⎝⎜⎜⎜t1100…t12t220…t13t23t33……………⎞⎠⎟⎟⎟

is invertible in S. Because f1,…,fn is a Koszul-regular sequence we see that the kernel of R→R⊕n, x↦(xf1,…,xfn) is zero (as it computes the nthe Koszul homology of R w.r.t. f1,…,fn). Hence by Lemma 15.31.16 we see that g1=f1t11+…+fnt1n is a nonzerodivisor in S′=R[t11,t12,…,t1n,t−111]. We see that g1,f2,…,fn is a Koszul-sequence in S′ by Lemma 15.31.5 and 15.31.15. We conclude that f¯¯¯2,…,f¯¯¯n is a Koszul-regular sequence in S′/(g1) by Lemma 15.31.14. Hence by induction on n we see that the images g¯¯¯2,…,g¯¯¯n of g2,…,gn in S′/(g1)[{tij}2≤i≤j,t−122,…,t−1nn] form a regular sequence. This in turn means that g1,…,gn forms a regular sequence in S.