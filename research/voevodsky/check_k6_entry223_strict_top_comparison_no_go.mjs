
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
if (vars.length !== 24) throw Error("variable census");
if (rank(A) !== 21 || rank(aug) !== 21) throw Error("supported system ranks");
if (rank(Ar) !== 23 || rank(augr) !== 23) throw Error("rotation system ranks");
if (rank(Arr) !== 24 || rank(augrr) !== 24) throw Error("D3 rational ranks");
if (rankMod2(Arr) !== 23 || rankMod2(augrr) !== 24) throw Error("mod-2 obstruction");
if (selectedDet !== 2n && selectedDet !== -2n) throw Error("maximal minor");
if (sol.some(x=>x.d!==1n&&x.d!==2n) || sol.every(x=>x.d===1n)) throw Error("half-integral solution");
if (sol.filter(x=>!x.zero()).length !== 12) throw Error("solution support");
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
  strict_top_map:{top:1,long_facets:"identity_with_cellular_sign",short_facets:0},
  literal_support_rule:"an edge may map only to the two target pair rows incident to its unique long-road label",
  general_derived_correspondence_no_go:false,
  minimal_additional_datum:"one reflection-odd pair/corridor homotopy generator with independently derived unit boundary into the mod-2 defect row",
  endpoint_Q_mapping_fiber_instantiated:false
}));
