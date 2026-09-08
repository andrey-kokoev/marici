https://stacks.math.columbia.edu/tag/0A8H

15.73 Hom complexes

Let R be a ring. Let L∙ and M∙ be two complexes of R-modules. We construct a complex Hom∙(L∙,M∙). Namely, for each n we set
Homn(L∙,M∙)=∏n=p+qHomR(L−q,Mp)

It is a good idea to think of Homn as the R-module of all R-linear maps from L∙ to M∙ (viewed as graded modules) which are homogeneous of degree n. In this terminology, we define the differential by the rule
d(f)=dM∘f−(−1)nf∘dL

for f∈Homn(L∙,M∙). We omit the verification that d2=0. See Section 15.74 for sign rules. This construction is a special case of Differential Graded Algebra, Example 22.26.6. It follows immediately from the construction that we have
15.73.0.1
Hn(Hom∙(L∙,M∙))=HomK(R)(L∙,M∙[n])

for all n∈Z.

Lemma 15.73.1. Let R be a ring. Given complexes K∙,L∙,M∙ of R-modules there is a canonical isomorphism
Hom∙(K∙,Hom∙(L∙,M∙))=Hom∙(Tot(K∙⊗RL∙),M∙)

of complexes of R-modules.

Proof. Let α be an element of degree n on the left hand side. Thus

α=(αp,q)∈∏p+q=nHomR(K−q,Homp(L∙,M∙))

Each αp,q is an element

αp,q=(αr,s,q)∈∏r+s+q=nHomR(K−q,HomR(L−s,Mr))

If we make the identifications

15.73.1.1
HomR(K−q,HomR(L−s,Mr))=HomR(K−q⊗RL−s,Mr)

then by our sign rules we get

d(αr,s,q)=dHom∙(L∙,M∙)∘αr,s,q−(−1)nαr,s,q∘dK=dM∘αr,s,q−(−1)r+sαr,s,q∘dL−(−1)r+s+qαr,s,q∘dK

On the other hand, if β is an element of degree n of the right hand side, then

β=(βr,s,q)∈∏r+s+q=nHomR(K−q⊗RL−s,Mr)

and by our sign rule (Homology, Definition 12.18.3) we get

d(βr,s,q)=dM∘βr,s,q−(−1)nβr,s,q∘dTot(K∙⊗L∙)=dM∘βr,s,q−(−1)r+s+q(βr,s,q∘dK+(−1)−qβr,s,q∘dL)

Thus we see that the map induced by the identifications (15.73.1.1) indeed is a morphism of complexes. □

Remark 15.73.2. Let R be a ring. The category Comp(R) of complexes of R-modules is a symmetric monoidal category with tensor product given by Tot(−⊗R−), see Lemma 15.59.1. Given L∙ and M∙ in Comp(R) an element f∈Hom0(L∙,M∙) defines a map of complexes f:L∙→M∙ if and only if d(f)=0. Hence Lemma 15.73.1 also tells us that
MorComp(R)(K∙,Hom∙(L∙,M∙))=MorComp(R)(Tot(K∙⊗RL∙),M∙)

functorially in K∙,L∙,M∙ in Comp(R). This means that Hom∙(−,−) is an internal hom for the symmetric monoidal category Comp(R) as discussed in Categories, Remark 4.43.16.

Lemma 15.73.3. Let R be a ring. Given complexes K∙,L∙,M∙ of R-modules there is a canonical morphism
Tot(Hom∙(L∙,M∙)⊗RHom∙(K∙,L∙))⟶Hom∙(K∙,M∙)

of complexes of R-modules.

Proof. Via the discussion in Remark 15.73.2 the existence of such a canonical map follows from Categories, Remark 4.43.16. We also give a direct construction.

An element α of degree n of the left hand side is

α=(αp,q)∈⨁p+q=nHomp(L∙,M∙)⊗RHomq(K∙,L∙)

The element αp,q is a finite sum αp,q=∑βpi⊗γqi with

βpi=(βr,si)∈∏r+s=pHomR(L−s,Mr)

and

γqi=(γu,vi)∈∏u+v=qHomR(K−v,Lu)

The map is given by sending α to δ=(δr,v) with

δr,v=∑i,sβr,si∘γ−s,vi∈HomR(K−v,Mr)

For given r+v=n this sum is finite as there are only finitely many nonzero αp,q, hence only finitely many nonzero βpi and γqi. By our sign rules we have

d(αp,q)=dHom∙(L∙,M∙)(αp,q)+(−1)pdHom∙(K∙,L∙)(αp,q)=∑(dM∘βpi∘γqi−(−1)pβpi∘dL∘γqi)+(−1)p∑(βpi∘dL∘γqi−(−1)qβpi∘γqi∘dK)=∑(dM∘βpi∘γqi−(−1)nβpi∘γqi∘dK)

It follows that the rules α↦δ is compatible with differentials and the lemma is proved. □

Lemma 15.73.4. Let R be a ring. Given complexes K∙,L∙,M∙ of R-modules there is a canonical morphism
Tot(K∙⊗RHom∙(M∙,L∙))⟶Hom∙(M∙,Tot(K∙⊗RL∙))

of complexes of R-modules functorial in all three complexes.

Proof. Via the discussion in Remark 15.73.2 the existence of such a canonical map follows from Categories, Remark 4.43.16. We also give a direct construction.

Let α be an element of degree n of the right hand side. Thus

α=(αp,q)∈∏p+q=nHomR(M−q,Totp(K∙⊗RL∙))

Each αp,q is an element

αp,q=(αr,s,q)∈HomR(M−q,⨁r+s+q=nKr⊗RLs)

where we think of αr,s,q as a family of maps such that for every x∈M−q only a finite number of αr,s,q(x) are nonzero. By our sign rules we get

d(αr,s,q)=dTot(K∙⊗RL∙)∘αr,s,q−(−1)nαr,s,q∘dM=dK∘αr,s,q+(−1)rdL∘αr,s,q−(−1)nαr,s,q∘dM

On the other hand, if β is an element of degree n of the left hand side, then

β=(βp,q)∈⨁p+q=nKp⊗RHomq(M∙,L∙)

and we can write βp,q=∑γpi⊗δqi with γpi∈Kp and

δqi=(δr,si)∈∏r+s=qHomR(M−s,Lr)

By our sign rules we have

d(βp,q)=dK(βp,q)+(−1)pdHom∙(M∙,L∙)(βp,q)=∑dK(γpi)⊗δqi+(−1)p∑γpi⊗(dL∘δqi−(−1)qδqi∘dM)

We send the element β to α with

αr,s,q=cr,s,q(∑γri⊗δs,qi)

where cr,s,q:Kr⊗RHomR(M−q,Ls)→HomR(M−q,Kr⊗RLs) is the canonical map. For a given β and r there are only finitely many nonzero γri hence only finitely many nonzero αr,s,q are nonzero (for a given r). Thus this family of maps satisfies the conditions above and the map is well defined. Comparing signs we see that this is compatible with differentials. □

Lemma 15.73.5. Let R be a ring. Given complexes K∙,L∙ of R-modules there is a canonical morphism
K∙⟶Hom∙(L∙,Tot(K∙⊗RL∙))

of complexes of R-modules functorial in both complexes.

Proof. Via the discussion in Remark 15.73.2 the existence of such a canonical map follows from Categories, Remark 4.43.16. We also give a direct construction.

Let α be an element of degree n of the right hand side. Thus

α=(αp,q)∈∏p+q=nHomR(L−q,Totp(K∙⊗RL∙))

Each αp,q is an element

αp,q=(αr,s,q)∈HomR(L−q,⨁r+s+q=nKr⊗RLs)

where we think of αr,s,q as a family of maps such that for every x∈L−q only a finite number of αr,s,q(x) are nonzero. By our sign rules we get

d(αr,s,q)=dTot(K∙⊗RL∙)∘αr,s,q−(−1)nαr,s,q∘dL=dK∘αr,s,q+(−1)rdL∘αr,s,q−(−1)nαr,s,q∘dL

Now an element β∈Kn we send to α with αn,−q,q=β⊗idL−q and αr,s,q=0 if r≠n. This is indeed an element as above, as for fixed q there is only one nonzero αr,s,q. The description of the differential shows this is compatible with differentials. □

Lemma 15.73.6. Let R be a ring. Given complexes K∙,L∙,M∙ of R-modules there is a canonical morphism
Tot(Hom∙(L∙,M∙)⊗RK∙)⟶Hom∙(Hom∙(K∙,L∙),M∙)

of complexes of R-modules functorial in all three complexes.

Proof. Via the discussion in Remark 15.73.2 the existence of such a canonical map follows from Categories, Remark 4.43.16. We also give a direct construction.

Consider an element β of degree n of the right hand side. Then

β=(βp,s)∈∏p+s=nHomR(Hom−s(K∙,L∙),Mp)

Our sign rules tell us that

d(βp,s)=dM∘βp,s−(−1)nβp,s∘dHom∙(K∙,L∙)

We can describe the last term as follows

(βp,s∘dHom∙(K∙,L∙))(f)=βp,s(dL∘f−(−1)s+1f∘dK)

if f∈Hom−s−1(K∙,L∙). We conclude that in some unspecified sense d(βp,s) is a sum of three terms with signs as follows

15.73.6.1
d(βp,s)=dM(βp,s)−(−1)ndL(βp,s)+(−1)p+1dK(βp,s)

Next, we consider an element α of degree n of the left hand side. We can write it like so

α=(αt,r)∈⨁t+r=nHomt(L∙,M∙)⊗Kr

Each αt,r maps to an element

αt,r↦(αp,q,r)∈∏p+q=tHomR(L−q,Mp)⊗RKr

Our sign rules tell us that

d(αp,q,r)=dHom∙(L∙,M∙)(αp,q,r)+(−1)p+qdK(αp,q,r)

where if we further write αp,q,r=∑gp,qi⊗kri then we have

dHom∙(L∙,M∙)(αp,q,r)=∑(dM∘gp,qi)⊗kri−(−1)p+q∑(gp,qi∘dL)⊗kri

We conclude that in some unspecified sense d(αp,q,r) is a sum of three terms with signs as follows

15.73.6.2
d(αp,q,r)=dM(αp,q,r)−(−1)p+qdL(αp,q,r)+(−1)p+qdK(αp,q,r)

To define our map we will use the canonical maps

cp,q,r:HomR(L−q,Mp)⊗RKr⟶HomR(HomR(Kr,L−q),Mp)

which sends φ⊗k to the map ψ↦φ(ψ(k)). This is functorial in all three variables. With s=q+r there is an inclusion

HomR(HomR(Kr,L−q),Mp)⊂HomR(Hom−s(K∙,L∙),Mp)

coming from the projection Hom−s(K∙,L∙)→HomR(Kr,L−q). Since αp,q,r is nonzero only for a finite number of r we see that for a given s there is only a finite number of q,r with q+r=s. Thus we can send α to the element β with

βp,s=∑q+r=sϵp,q,rcp,q,r(αp,q,r)

where where the sum uses the inclusions given above and where ϵp,q,r∈{±1}. Comparing signs in the equations (15.73.6.1) and (15.73.6.2) we see that

    ϵp,q,r=ϵp+1,q,r

    −(−1)nϵp,q,r=−(−1)p+qϵp,q−1,r or equivalently ϵp,q,r=(−1)rϵp,q−1,r

    (−1)p+1ϵp,q,r=(−1)p+qϵp,q,r+1 or equivalently (−1)q+1ϵp,q,r=ϵp,q,r+1.

A good solution is to take

ϵp,r,s=(−1)r+qr

The choice of this sign is explained in the remark following the proof. □

Remark 15.73.7. Let us explain why the sign used in the direct construction in the proof of Lemma 15.73.6 agrees with the sign we get from the construction using the discussion in Remark 15.73.2 and Categories, Remark 4.43.16. Denote −⊗−=Tot(−⊗R−) and hom(−,−)=Hom∙(−,−). The construction using monoidal category language tells us to use the arrow
hom(L∙,M∙)⊗K∙⟶hom(hom(K∙,L∙),M∙)

in Comp(R) corresponding to the arrow
hom(L∙,M∙)⊗K∙⊗hom(K∙,L∙)⟶M∙

gotten by swapping the order of the last two tensor products and then using the evaluation maps hom(K∙,L∙)⊗K∙→L∙ and hom(L∙,K∙)⊗L∙→M∙. Only in swapping does a sign intervene. Namely, in the isomorphism
K∙⊗hom(K∙,L∙)→hom(K∙,L∙)⊗K∙

there is a sign (−1)r(q+r′) on Kr⊗RHomR(K−r′,Lq), see Section 15.74 item (9). The reader can convince themselves that, because of the correspondence we are using to describe maps into an internal hom, this sign only matters if r=r′ and in this case we obtain (−1)r(q+r)=(−1)r+qr as in the direct proof.
