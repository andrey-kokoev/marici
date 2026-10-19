// Unselected geometry/transport probe. helium4-window-model explicitly selects
// a conditional reader rule; the other probe alternatives remain unresolved.
import {createWindowConstruction} from './window-construction-model.mjs';
import {makeLatticeItem,itemKey} from './lattice-items.mjs';
import {transportCarrierCoefficients} from './deuterium-tunnel-model.mjs';
const copy=x=>structuredClone(x),equal=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
const marks=['C0','M0','C1','M1','C2'];
function regularSeed(body){
 const candidates=[];
 for(const inverted of [false,true]){
  const origin=body.center.map(x=>x+(inverted?.25:-.25));if(!origin.every(Number.isInteger))continue;
  const seed=makeLatticeItem('tetrahedron',origin,inverted);if(seed.key===body.key)candidates.push(seed);
 }
 if(candidates.length!==1)throw Error('A uniquely bound regular proton seed is required');return candidates[0];
}
function swap(vector,a,b){const out=copy(vector);[out[a],out[b]]=[out[b],out[a]];return out;}
export function applyHelium4CoreLoop(coefficients,variant,direction=1){
 if(![1,-1].includes(direction)||!Array.isArray(coefficients)||coefficients.length!==5||coefficients.some(z=>!Array.isArray(z)||z.length!==2||z.some(x=>!Number.isFinite(x))))throw Error('Finite five-slot carrier and signed direction required');
 let value=copy(coefficients);const steps=direction===1?variant.steps:[...variant.steps].reverse();
 for(const step of steps)value=applyHelium4CoreStep(value,step,direction);
 return value;
}
export function applyHelium4CoreStep(coefficients,step,direction=1){
 if(![1,-1].includes(direction)||!Array.isArray(coefficients)||coefficients.length!==5||coefficients.some(z=>!Array.isArray(z)||z.length!==2||z.some(x=>!Number.isFinite(x))))throw Error('Finite five-slot carrier and signed direction required');
 if(step.kind==='PN')return transportCarrierCoefficients(coefficients,step.event,step.direction*direction);
 if(step.kind==='shared-neutron')return step.reverseMOrder?swap(coefficients,1,3):copy(coefficients);
 if(step.kind==='proton-reader-hypothesis')return swap(coefficients,0,2);
 throw Error('Unknown core-loop comparison');
}
export function deriveHelium4Core(helium3){
 if(helium3.atomTrial!=='helium3'||helium3.status!=='complete'||helium3.items.length!==5||!equal(helium3.counts,{proton:2,neutron:1,electron:2}))throw Error('A completed retained helium-3 trial is required');
 const {items,bindings:b}=helium3,protons=[items[0],items[3]],neutron=items[1],names=new Map(Object.entries(b).map(([n,p])=>[itemKey([p]),n]));
 if(protons.some(p=>p.species!=='proton')||neutron.species!=='neutron')throw Error('Unexpected retained carrier roles');
 const oldPackets=[],alternatives=[];
 for(const [pIndex,p] of protons.entries()){
  const seed=regularSeed(p),[c0,m0,c1]=p.window,m1=p.continuation;
  if(![c0,c1].every(n=>n.startsWith('C'))||![m0,m1].every(n=>n.startsWith('M')))throw Error('Proton must retain its marked CMC/M context');
  const old=createWindowConstruction({seed,identity:helium3.identity,bindings:Object.fromEntries(['C0','M0','C1','M1'].map((n,i)=>[n,b[[c0,m0,c1,m1][i]]]))});const oldN=old.step();
  const oldE=old.step(),expectedElectron=items[pIndex===0?2:4];
  if(oldN.items[1].key!==neutron.key||expectedElectron.species!=='electron'||oldE.items[2].key!==expectedElectron.key)throw Error('Retained proton does not bind its original neutron/electron packet');oldPackets.push(oldE);
  const available=p.faces.filter(f=>{const ns=f.map(q=>names.get(itemKey([q])));return ns.every(Boolean)&&ns.filter(n=>n.startsWith('M')).length===2&&itemKey(f)!==itemKey(oldN.events[0].face);});
  if(available.length!==1)throw Error('Expected one unused MCM face per proton');
  const choices=[];
  for(const exchangeMiddleM of [false,true]){
   // Both frames reach the same unused MCM face. Geometry alone does not pick
   // between re-reading the old CMC face and using the other CMC face.
   const localNames=[c1,exchangeMiddleM?m1:m0,c0,exchangeMiddleM?m0:m1];
   const model=createWindowConstruction({seed,identity:helium3.identity,bindings:Object.fromEntries(['C0','M0','C1','M1'].map((n,i)=>[n,b[localNames[i]]]))});const n=model.step(),e=model.step();
   if(itemKey(n.events[0].face)!==itemKey(available[0]))throw Error('Candidate did not use the retained free input port');
   const context=names.get(itemKey([n.bindings.C2]));if(!context)throw Error('Second neutron should use only retained geometric identities');
   const aliases=Object.fromEntries(marks.map((m,i)=>[m,i<4?localNames[i]:context]));
   choices.push({exchangeMiddleM,aliases,window:localNames.slice(0,3),neutron:n.items[1],pn:n.events[0],continuationElectron:e.items[2],continuationFace:e.events[1].face,geometryOnly:true});
  }
  alternatives.push(choices);
 }
 const proposed=alternatives[0][0].neutron;
 if(alternatives.flat().some(c=>c.neutron.key!==proposed.key)||items.some(i=>i.key===proposed.key))throw Error('The two proton ports do not identify one new neutron');
 const alias=alternatives[0][0].aliases,newNeutron={...copy(proposed),nodes:proposed.nodes.map(n=>alias[n]),window:null,continuation:null,candidateReaders:alternatives.flat().map(c=>({window:c.neutron.window.map(n=>c.aliases[n]),context:c.aliases.C2}))};
 const variants=[];
 for(const left of alternatives[0])for(const right of alternatives[1]){
  const reverseMOrder=left.aliases.M0!==right.aliases.M0;
  const steps=[
   {kind:'PN',event:oldPackets[0].events[0],direction:1},
   {kind:'shared-neutron',reverseMOrder:true},
   {kind:'PN',event:oldPackets[1].events[0],direction:-1},
   {kind:'proton-reader-hypothesis',at:protons[1].key,exchangeMiddleM:right.exchangeMiddleM},
   {kind:'PN',event:right.pn,direction:1},
   {kind:'shared-neutron',reverseMOrder},
   {kind:'PN',event:left.pn,direction:-1},
   {kind:'proton-reader-hypothesis',at:protons[0].key,exchangeMiddleM:left.exchangeMiddleM}
  ];
  const variant={choices:[left.exchangeMiddleM,right.exchangeMiddleM],steps};
  const basisTags=marks.map((_,i)=>[i+1,0]),result=applyHelium4CoreLoop(basisTags,variant),permutation=result.map(z=>z[0]-1);
  let value=basisTags,order=0;do{value=applyHelium4CoreLoop(value,variant);order++;}while(!equal(value,basisTags)&&order<121);
  variants.push({...variant,permutation,order,oneLoopIdentity:equal(result,basisTags),conditional:true});
 }
 const interfaces=[...copy(helium3.tunnel.interfaces),...alternatives.map((cs,i)=>({from:protons[i].key,to:proposed.key,face:copy(cs[0].pn.face),window:cs[0].pn.orderedFace.map(n=>cs[0].aliases[n])}))];
 return {status:'geometry-candidate-transport-underdetermined',items:[...copy(items),newNeutron],bindings:copy(b),counts:{proton:2,neutron:2,electron:2},interfaces,alternatives,variants,retainedPackets:oldPackets,
  newVertexCount:0,newCarrierCount:1,ordinaryNeutronExitToRetainedElectron:alternatives.flat().some(c=>items.filter(i=>i.species==='electron').some(e=>e.key===c.continuationElectron.key)),
  scope:'Unique six-carrier geometry. New proton-reader/context comparisons are hypotheses; four framing choices are retained rather than silently selected. Nontrivial holonomy is reported, not erased as a scalar phase. This unselected probe is not a viewer construction; the separate He-4 trial explicitly selects a conditional reader rule.'};
}
