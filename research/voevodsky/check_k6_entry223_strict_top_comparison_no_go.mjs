
const N=6;
const diag=(a,b)=>a<b?[a,b]:[b,a];
const keyD=d=>d.join("");
const edge=(d)=>d[1]-d[0]===1||(d[0]===0&&d[1]===5);
const between=(v,a,b)=>{const span=(b+N-a)%N,pos=(v+N-a)%N;return pos>0&&pos<span};
const crosses=(x,y)=>{if(x.includes(y[0])||x.includes(y[1]))return false;return between(y[0],x[0],x[1])!==between(y[1],x[0],x[1])&&between(x[0],y[0],y[1])!==between(x[1],y[0],y[1])};
const ds=[];for(let a=0;a<N;a++)for(let b=a+1;b<N;b++){let d=[a,b];if(!edge(d))ds.push(d)}
const faceKey=f=>[...f].sort().join(",");
const parse=s=>s?new Set(s.split(",").map(x=>ds.findIndex(d=>keyD(d)===x))):new Set();
const faces=[[],[],[],[]];
for(let m=0;m<(1<<ds.length);m++){if(pop(m)>3)continue;const f=[];for(let i=0;i<ds.length;i++)if(m>>i&1)f.push(i);let ok=true;for(let i=0;i<f.length;i++)for(let j=i+1;j<f.length;j++)if(crosses(ds[f[i]],ds[f[j]]))ok=false;if(ok)faces[f.length].push(f)}
faces.forEach(x=>x.sort((a,b)=>faceKey(a.map(i=>keyD(ds[i]))).localeCompare(faceKey(b.map(i=>keyD(ds[i]))))));
function pop(x){let n=0;while(x){n+=x&1;x>>=1}return n}
const raw=(f,a)=>f.filter(x=>x<a).length%2===0?1:-1;
// vertex gauges
const gauges=new Map([[faceKey(faces[3][0].map(i=>keyD(ds[i]))),1]]);
let changed=true;
while(changed){changed=false;for(const e of faces[2]){const ends=[];for(let a=0;a<ds.length;a++)if(!e.includes(a)&&e.every(x=>!crosses(ds[x],ds[a]))){const t=[...e,a].sort((x,y)=>x-y);ends.push([t,raw(e,a)])}if(ends.length!==2)throw Error("ends");const k0=faceKey(ends[0][0].map(i=>keyD(ds[i]))),k1=faceKey(ends[1][0].map(i=>keyD(ds[i]))),rel=-ends[0][1]*ends[1][1];if(gauges.has(k0)&&!gauges.has(k1)){gauges.set(k1,rel*gauges.get(k0));changed=true}else if(!gauges.has(k0)&&gauges.has(k1)){gauges.set(k0,rel*gauges.get(k1));changed=true}}}
const inc=(f,t,a)=> {
  const gf=gauges.get(faceKey(f.map(i=>keyD(ds[i])))) ?? 1;
  const gt=gauges.get(faceKey(t.map(i=>keyD(ds[i])))) ?? 1;
  return raw(f,a)*gf*gt;
};
const d3=faces[1].map(f=>inc([],f,f[0]));
const d2=Array.from({length:faces[2].length},()=>Array(faces[1].length).fill(0));
for(let j=0;j<faces[1].length;j++)for(let i=0;i<faces[2].length;i++)if(faces[1][j].every(x=>faces[2][i].includes(x))){const a=faces[2][i].find(x=>!faces[1][j].includes(x));d2[i][j]=inc(faces[1][j],faces[2][i],a)}
const isShort=i=>{const [a,b]=ds[i];for(let v=0;v<6;v++)if(keyD(diag(v,(v+2)%6))===keyD(ds[i]))return true;return false};
const longs=faces[1].map((f,j)=>[f[0],j]).filter(([i])=>!isShort(i));
const B=[[-1,0,1],[1,-1,0],[0,1,-1]];
const F2=Array.from({length:3},()=>Array(9).fill(0));
longs.forEach(([i,j],r)=>F2[r][j]=d3[j]);
const rhs=Array.from({length:3},(_,r)=>Array.from({length:9},(_,j)=>B[r].reduce((s,b,k)=>s+b*F2[k][j],0)));
// vars only edge contains long, target row supported in nonzero B column
const vars=[];
for(let e=0;e<faces[2].length;e++){const li=faces[2][e].find(i=>!isShort(i));if(li!==undefined){const road=longs.findIndex(([i])=>i===li);for(let r=0;r<3;r++)if(B[r][road]!==0)vars.push([r,e]);}}
const A=[],bb=[];
for(let r=0;r<3;r++)for(let j=0;j<9;j++){const row=vars.map(([rr,e])=>rr===r?d2[e][j]:0);A.push(row);bb.push(rhs[r][j]);}
function rank(M){M=M.map(r=>r.map(BigInt));let rr=0;for(let c=0;c<(M[0]?.length??0)&&rr<M.length;c++){let p=rr;while(p<M.length&&M[p][c]===0n)p++;if(p===M.length)continue;[M[rr],M[p]]=[M[p],M[rr]];for(let i=rr+1;i<M.length;i++)if(M[i][c]!==0n){const a=M[rr][c],b=M[i][c];for(let j=c;j<M[i].length;j++)M[i][j]=a*M[i][j]-b*M[rr][j];}rr++;}return rr}
const aug=A.map((r,i)=>[...r,bb[i]]);
// Add strict C3 covariance on the supported edge map.
const rotV=v=>(v+2)%6;
const permDiag=(i,act)=>ds.findIndex(d=>keyD(d)===keyD(diag(act(ds[i][0]),act(ds[i][1]))));
const permFace=(f,act)=>f.map(i=>permDiag(i,act)).sort((a,b)=>a-b);
function actionSigns(act,topSign){
  const signs=[new Map(),new Map(),new Map(),new Map()];
  signs[0].set(faceKey([]),topSign);
  for(let sz=0;sz<3;sz++)for(const f of faces[sz]){
    const sf=signs[sz].get(faceKey(f.map(i=>keyD(ds[i]))));
    const imf=permFace(f,act);
    for(let a=0;a<ds.length;a++)if(!f.includes(a)&&f.every(x=>!crosses(ds[x],ds[a]))){
      const t=[...f,a].sort((x,y)=>x-y),imt=permFace(t,act),ima=permDiag(a,act);
      const val=sf*inc(f,t,a)*inc(imf,imt,ima);
      const k=faceKey(t.map(i=>keyD(ds[i])));
      if(signs[sz+1].has(k)&&signs[sz+1].get(k)!==val)throw Error("action sign");
      signs[sz+1].set(k,val);
    }
  }
  return signs;
}
const rs=actionSigns(rotV,1);
const longPerm=longs.map(([i])=>longs.findIndex(([j])=>j===permDiag(i,rotV)));
const varIndex=new Map(vars.map((v,i)=>[v.join(","),i]));
const Ar=A.map(r=>[...r]), bbr=[...bb];
for(let e=0;e<faces[2].length;e++){
  const ep=faces[2].findIndex(f=>faceKey(f.map(i=>keyD(ds[i])))===faceKey(permFace(faces[2][e],rotV).map(i=>keyD(ds[i]))));
  const s=rs[2].get(faceKey(faces[2][e].map(i=>keyD(ds[i]))));
  for(let r=0;r<3;r++){
    const row=Array(vars.length).fill(0);
    const i1=varIndex.get([r,ep].join(","));
    const pre=longPerm.findIndex(x=>x===r);
    const i2=varIndex.get([pre,e].join(","));
    if(i1!==undefined)row[i1]+=s;
    if(i2!==undefined)row[i2]-=1;
    if(row.some(Boolean)){Ar.push(row);bbr.push(0)}
  }
}
const augr=Ar.map((r,i)=>[...r,bbr[i]]);
const reflV=v=>(9-v)%6;
const ss=actionSigns(reflV,-1);
const reflLongPerm=longs.map(([i])=>longs.findIndex(([j])=>j===permDiag(i,reflV)));
const permMat=(perm,sgn)=>Array.from({length:3},(_,r)=>Array.from({length:3},(_,c)=>perm[c]===r?sgn:0));
const mul=(X,Y)=>X.map((row)=>Y[0].map((_,j)=>row.reduce((s,x,k)=>s+x*Y[k][j],0)));
const eqM=(X,Y)=>JSON.stringify(X)===JSON.stringify(Y);
const facetRefl=permMat(reflLongPerm,-1);
let pairReflSign=0,pairReflPerm=null;
const perms=[[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]];
for(const perm of perms)for(const sgn of [1,-1])if(eqM(mul(permMat(perm,sgn),B),mul(B,facetRefl))){pairReflSign=sgn;pairReflPerm=perm}
if(pairReflSign===0)throw Error("no pair reflection");
const Arr=Ar.map(r=>[...r]), bbrr=[...bbr];
for(let e=0;e<faces[2].length;e++){
  const ep=faces[2].findIndex(f=>faceKey(f.map(i=>keyD(ds[i])))===faceKey(permFace(faces[2][e],reflV).map(i=>keyD(ds[i]))));
  const s=ss[2].get(faceKey(faces[2][e].map(i=>keyD(ds[i]))));
  for(let r=0;r<3;r++){
    const row=Array(vars.length).fill(0);
    const i1=varIndex.get([r,ep].join(","));
    const pre=pairReflPerm.findIndex(x=>x===r);
    const i2=varIndex.get([pre,e].join(","));
    if(i1!==undefined)row[i1]+=s;
    if(i2!==undefined)row[i2]-=pairReflSign;
    if(row.some(Boolean)){Arr.push(row);bbrr.push(0)}
  }
}
const augrr=Arr.map((r,i)=>[...r,bbrr[i]]);
const bgcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b]}return a||1n};
class Q{constructor(n,d=1n){if(d<0n){n=-n;d=-d}const g=bgcd(n,d);this.n=n/g;this.d=d/g}add(o){return new Q(this.n*o.d+o.n*this.d,this.d*o.d)}sub(o){return new Q(this.n*o.d-o.n*this.d,this.d*o.d)}mul(o){return new Q(this.n*o.n,this.d*o.d)}div(o){return new Q(this.n*o.d,this.d*o.n)}zero(){return this.n===0n}toString(){return this.d===1n?String(this.n):this.n+"/"+this.d}}
function solveUnique(A,b){
 const M=A.map((r,i)=>[...r,b[i]].map(x=>new Q(BigInt(x))));
 let rr=0;const piv=[];
 for(let c=0;c<A[0].length;c++){let p=rr;while(p<M.length&&M[p][c].zero())p++;if(p===M.length)continue;[M[rr],M[p]]=[M[p],M[rr]];const q=M[rr][c];M[rr]=M[rr].map(x=>x.div(q));for(let i=0;i<M.length;i++)if(i!==rr&&!M[i][c].zero()){const z=M[i][c];M[i]=M[i].map((x,j)=>x.sub(z.mul(M[rr][j])))}piv.push(c);rr++}
 if(piv.length!==A[0].length)throw Error("not unique");
 const x=Array(A[0].length);for(let i=0;i<piv.length;i++)x[piv[i]]=M[i][A[0].length];
 return x;
}
const sol=solveUnique(Arr,bbrr);
function rankMod2(M){M=M.map(r=>r.map(x=>((x%2)+2)%2));let rr=0;for(let c=0;c<(M[0]?.length??0)&&rr<M.length;c++){let p=rr;while(p<M.length&&M[p][c]===0)p++;if(p===M.length)continue;[M[rr],M[p]]=[M[p],M[rr]];for(let i=0;i<M.length;i++)if(i!==rr&&M[i][c])for(let j=c;j<M[i].length;j++)M[i][j]^=M[rr][j];rr++}return rr}
const selectedRows=[];let current=[];
for(let i=0;i<Arr.length&&selectedRows.length<24;i++){const trial=[...current,Arr[i]];if(rank(trial)>current.length){current=trial;selectedRows.push(i)}}
function detBareiss(M){M=M.map(r=>r.map(BigInt));let sign=1n,prev=1n;for(let k=0;k<M.length-1;k++){let p=k;while(p<M.length&&M[p][k]===0n)p++;if(p===M.length)return 0n;if(p!==k){[M[p],M[k]]=[M[k],M[p]];sign=-sign}const pivot=M[k][k];for(let i=k+1;i<M.length;i++)for(let j=k+1;j<M.length;j++)M[i][j]=(M[i][j]*pivot-M[i][k]*M[k][j])/prev;prev=pivot}return sign*M[M.length-1][M.length-1]}
const selectedDet=detBareiss(selectedRows.map(i=>Arr[i]));
function solveAffineMod2(M,b){
 const X=M.map((r,i)=>[...r.map(x=>((x%2)+2)%2),((b[i]%2)+2)%2]);let rr=0;const piv=[];
 for(let c=0;c<M[0].length&&rr<X.length;c++){let p=rr;while(p<X.length&&!X[p][c])p++;if(p===X.length)continue;[X[rr],X[p]]=[X[p],X[rr]];for(let i=0;i<X.length;i++)if(i!==rr&&X[i][c])for(let j=c;j<=M[0].length;j++)X[i][j]^=X[rr][j];piv.push(c);rr++;}
 for(const row of X)if(row.slice(0,-1).every(x=>x===0)&&row.at(-1))return null;
 const n=M[0].length,ps=new Set(piv),x=Array(n).fill(0);for(let i=0;i<piv.length;i++)x[piv[i]]=X[i][n];
 const basis=[];for(let f=0;f<n;f++)if(!ps.has(f)){const v=Array(n).fill(0);v[f]=1;for(let i=piv.length-1;i>=0;i--){const c=piv[i];let z=0;for(let j=c+1;j<n;j++)z^=(X[i][j]&v[j]);v[c]=z;}basis.push(v);}
 return{x,basis};
}
const nonreflectionSolution=solveAffineMod2(Ar,bbr);
if(!nonreflectionSolution)throw Error("nonreflection system");
const correctionVectors=[];
for(let mask=0;mask<(1<<nonreflectionSolution.basis.length);mask++){
 const x=[...nonreflectionSolution.x];
 for(let k=0;k<nonreflectionSolution.basis.length;k++)if(mask>>k&1)for(let j=0;j<x.length;j++)x[j]^=nonreflectionSolution.basis[k][j];
 correctionVectors.push(Arr.slice(Ar.length).map(row=>row.reduce((z,a,j)=>z^((((a%2)+2)%2)&x[j]),0)));
}
const correction=correctionVectors[0];
if(!correctionVectors.every(value=>JSON.stringify(value)===JSON.stringify(correction)))throw Error("correction orbit not unique");
const correctionWeight=correction.reduce((sum,value)=>sum+value,0);
// Entry245 constructs the required correction in homological degree -1:
// every odd reflection row has its own primitive facet-homotopy boundary.
// Unlike the same-degree scalar column below, these are mapping-cone columns.
const oddRows=correction.map((value,index)=>value?index:-1).filter(index=>index>=0);
const shiftedExtended=Arr.map((row,index)=>[
 ...row,
 ...oddRows.map(oddRow=>index-Ar.length===oddRow?1:0)
]);
const shiftedAugmented=shiftedExtended.map((row,index)=>[...row,bbrr[index]]);
const shiftedRank=rank(shiftedExtended);
const shiftedAugmentedRank=rank(shiftedAugmented);
const shiftedMod2Rank=rankMod2(shiftedExtended);
const shiftedMod2AugmentedRank=rankMod2(shiftedAugmented);
const shiftedOddRows=[];let shiftedOddRowMatrix=[];
for(let i=0;i<shiftedExtended.length&&shiftedOddRows.length<shiftedMod2Rank;i++){
 const trial=[...shiftedOddRowMatrix,shiftedExtended[i]];
 if(rankMod2(trial)>shiftedOddRows.length){shiftedOddRowMatrix=trial;shiftedOddRows.push(i)}
}
const shiftedOddColumns=[];let shiftedOddSquare=shiftedOddRows.map(()=>[]);
for(let c=0;c<shiftedExtended[0].length&&shiftedOddColumns.length<shiftedMod2Rank;c++){
 const trial=shiftedOddRows.map((row,i)=>[...shiftedOddSquare[i],shiftedExtended[row][c]]);
 if(rankMod2(trial)>shiftedOddColumns.length){shiftedOddSquare=trial;shiftedOddColumns.push(c)}
}
const shiftedOddDet=detBareiss(shiftedOddSquare);
const shiftedFreeColumns=Array.from({length:shiftedExtended[0].length},(_,i)=>i).filter(i=>!shiftedOddColumns.includes(i));
const topNormalizationRow=Array(shiftedExtended[0].length).fill(0);
if(shiftedFreeColumns.length===1)topNormalizationRow[shiftedFreeColumns[0]]=1;
const topNormalizedSquare=[...shiftedOddRows.map(i=>shiftedExtended[i]),topNormalizationRow];
const topNormalizedDet=detBareiss(topNormalizedSquare);
const topNormalizedMatrix=[...shiftedExtended,topNormalizationRow];
const topNormalizedRhs=[...bbrr,1];
const topNormalizedAugmented=topNormalizedMatrix.map((row,index)=>[...row,topNormalizedRhs[index]]);
const shiftedRows=[];let shiftedCurrent=[];
for(let i=0;i<shiftedExtended.length&&shiftedRows.length<shiftedRank;i++){
 const trial=[...shiftedCurrent,shiftedExtended[i]];
 if(rank(trial)>shiftedCurrent.length){shiftedCurrent=trial;shiftedRows.push(i)}
}
const shiftedPivotColumns=[];let shiftedColumnMatrix=shiftedRows.map(()=>[]);
for(let c=0;c<shiftedExtended[0].length&&shiftedPivotColumns.length<shiftedRank;c++){
 const trial=shiftedRows.map((row,i)=>[...shiftedColumnMatrix[i],shiftedExtended[row][c]]);
 if(rank(trial)>shiftedPivotColumns.length){shiftedColumnMatrix=trial;shiftedPivotColumns.push(c)}
}
const shiftedDet=detBareiss(shiftedColumnMatrix);
const naiveExtended=Arr.map((row,index)=>[...row,index<Ar.length?0:correction[index-Ar.length]]);
const naiveExtendedAugmented=naiveExtended.map((row,index)=>[...row,bbrr[index]]);
const naiveSolution=solveUnique(naiveExtended,bbrr);
const naiveRows=[];let naiveCurrent=[];
for(let i=0;i<naiveExtended.length&&naiveRows.length<25;i++){const trial=[...naiveCurrent,naiveExtended[i]];if(rank(trial)>naiveCurrent.length){naiveCurrent=trial;naiveRows.push(i)}}
const naiveDet=detBareiss(naiveRows.map(index=>naiveExtended[index]));
if (vars.length !== 24) throw Error("variable census");
if (rank(A) !== 21 || rank(aug) !== 21) throw Error("supported system ranks");
if (rank(Ar) !== 23 || rank(augr) !== 23) throw Error("rotation system ranks");
if (rank(Arr) !== 24 || rank(augrr) !== 24) throw Error("D3 rational ranks");
if (rankMod2(Arr) !== 23 || rankMod2(augrr) !== 24) throw Error("mod-2 obstruction");
if (selectedDet !== 2n && selectedDet !== -2n) throw Error("maximal minor");
if (sol.some(x=>x.d!==1n&&x.d!==2n) || sol.every(x=>x.d===1n)) throw Error("half-integral solution");
if (sol.filter(x=>!x.zero()).length !== 12) throw Error("solution support");
if (correctionWeight !== 12) throw Error("odd-orbit correction support");
if(oddRows.length!==12||shiftedRank!==35||shiftedAugmentedRank!==35)throw Error(`shifted cone ranks ${oddRows.length}/${shiftedRank}/${shiftedAugmentedRank}`);
if(shiftedMod2Rank!==35||shiftedMod2AugmentedRank!==35)throw Error(`shifted cone mod2 ${shiftedMod2Rank}/${shiftedMod2AugmentedRank}`);
if(shiftedOddDet%2n===0n)throw Error(`shifted cone odd minor ${shiftedOddDet}`);
if(shiftedFreeColumns.length!==1||rank(topNormalizedMatrix)!==36||rank(topNormalizedAugmented)!==36)throw Error("top normalization ranks");
if(topNormalizedDet!==1n&&topNormalizedDet!==-1n)throw Error(`top normalization minor ${topNormalizedDet}`);
if (rank(naiveExtended)!==25||rank(naiveExtendedAugmented)!==25)throw Error("naive extension ranks");
if (naiveSolution[24].toString()!=="0"||naiveSolution.every(x=>x.d===1n))throw Error("naive same-degree repair");
if (naiveDet!==4n&&naiveDet!==-4n)throw Error("naive extension minor");
console.log(JSON.stringify({
  status:"falsified_scoped_strict_integral_K6_to_entry223_top_comparison",
  source_face_ranks:[1,9,21,14],
  target_ranks:[1,3,3],
  support_variables:24,
  supported_rank:21,
  supported_affine_rank:3,
  rotation_equivariant_rank:23,
  rotation_equivariant_affine_rank:1,
  D3_equivariant_rank:24,
  D3_equivariant_augmented_rank:24,
  D3_equivariant_affine_rank:0,
  unique_rational_solution:true,
  unique_solution_nonzero_coefficients:12,
  unique_solution_denominators:[2],
  integral_solution:false,
  mod2_coefficient_rank:23,
  mod2_augmented_rank:24,
  selected_maximal_minor_determinant:Number(selectedDet),
  smith_factors:[...Array(23).fill(1),2],
  obstruction_group:"Z/2",
  minimal_mod2_reflection_correction_rows:12,
  minimal_mod2_reflection_correction_unique:true,
  shifted_mapping_cone_columns:12,
  shifted_mapping_cone_rank:shiftedRank,
  shifted_mapping_cone_augmented_rank:shiftedAugmentedRank,
  shifted_mapping_cone_affine_rank:shiftedExtended[0].length-shiftedRank,
  shifted_mapping_cone_mod2_rank:shiftedMod2Rank,
  shifted_mapping_cone_mod2_augmented_rank:shiftedMod2AugmentedRank,
  shifted_mapping_cone_selected_minor:Number(shiftedDet),
  shifted_mapping_cone_selected_odd_minor:Number(shiftedOddDet),
  shifted_mapping_cone_smith_nonzero_all_ones:true,
  shifted_mapping_cone_integral_obstruction:false,
  external_top_normalization:{free_classes:1,coefficient:1,rank:36,augmented_rank:36,unimodular_minor:Number(topNormalizedDet),integral_unique:true},
  naive_same_degree_odd_column_rank:25,
  naive_same_degree_odd_column_scalar:0,
  naive_same_degree_integral_solution:false,
  naive_same_degree_selected_minor_determinant:Number(naiveDet),
  shifted_mapping_cone_required:true,
  strict_top_map:{top:1,long_facets:"identity_with_cellular_sign",short_facets:0},
  literal_support_rule:"an edge may map only to the two target pair rows incident to its unique long-road label",
  general_derived_correspondence_no_go:false,
  derived_pair_facet_repair_constructed:true,
  finite_W012_qSigma_top_normalization_constructed:true,
  remaining_geometric_datum:"normalization-provenanced six-functor realization into the literal entry143 BM-Cech complex",
  endpoint_Q_mapping_fiber_instantiated:false
}));
