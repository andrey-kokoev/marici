import {auditPhaseAssembly} from '../strominger/demos/particle-overlap-tetrahedron/phase-assembly-model.mjs';
import {phaseFrame, phaseAdvanceWitness, applyPhasePermutation} from '../strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs';

const identity = [0,1,2,3,4];
const same = (a,b) => JSON.stringify(a) === JSON.stringify(b);
const clone = x => structuredClone(x);
export const inversePermutation = p => p.map((_,i) => p.indexOf(i));
export const composePermutation = (state,p) => p.map(i => state[i]);

export function initialState(r) {
  return {chart:r.root, origin:0, permutation:[...identity], history:[]};
}
export function advance(r,state,index) {
  const e=r.edges[index];
  if (!e || state.chart!==e.from || ![0,1].includes(e.phaseDelta)) throw Error('Unadmitted source transition');
  if (r.charts[state.chart].species==='electron') throw Error('Terminal exit cannot be continued');
  if (e.phaseDelta) {
    const w=phaseAdvanceWitness(r.charts[e.from],r.charts[e.to],state.origin);
    if (!same(w.permutation,e.permutation)) throw Error('Changed phase witness');
  }
  return {chart:e.to,origin:state.origin+e.phaseDelta,
    permutation:composePermutation(state.permutation,e.permutation),history:[...state.history,index]};
}
export function traceWord(r,word) {
  const states=[initialState(r)];
  for (const index of word) states.push(advance(r,states.at(-1),index));
  return states;
}
export function undo(r,state,index) {
  const e=r.edges[index];
  if (!e || state.chart!==e.to || state.history.at(-1)!==index || state.origin<e.phaseDelta) throw Error('Inverse needs its actual retained prefix');
  if (!same(traceWord(r,state.history).at(-1),state)) throw Error('Mismatched retained prefix');
  const previous={chart:e.from,origin:state.origin-e.phaseDelta,
    permutation:composePermutation(state.permutation,inversePermutation(e.permutation)),history:state.history.slice(0,-1)};
  if (!same(advance(r,previous,index),state)) throw Error('Inverse did not restore full retained state');
  return previous;
}
// Candidates invert the chart/coefficient/origin packet. Executing another native
// command appends provenance; it does not erase an earlier command record.
export function nativeInverseIndices(r,index) {
  const e=r.edges[index], inverse=inversePermutation(e.permutation);
  return r.edges.flatMap((f,i) => f.from===e.to && f.to===e.from && f.phaseDelta===-e.phaseDelta && same(f.permutation,inverse) ? [i] : []);
}
function retainedView(r,s) { return {...clone(s),frame:phaseFrame(r.charts[s.chart],s.origin)}; }
function boundary(r,s,exit=false) {
  const f=phaseFrame(r.charts[s.chart],s.origin),o=exit?f.window.at(-1):f.window[0];
  if (o.role!=='C') throw Error('Chosen boundary is not C');
  return clone(o);
}
export function buildCExitCapGraph(r,maxExitCIndex=4) {
  if(!Number.isInteger(maxExitCIndex)||maxExitCIndex<2||maxExitCIndex>6) throw Error('C-exit cap must be in [2,6]');
  auditPhaseAssembly(r);
  const cap=maxExitCIndex-2,states=[],transitions=[],ids=new Map();
  const key=s=>s.chart+'@'+s.origin+':'+s.permutation.join('');
  function keep(s){const k=key(s);if(!ids.has(k)){ids.set(k,states.length);states.push({...clone(s),id:states.length,frame:phaseFrame(r.charts[s.chart],s.origin)});}return ids.get(k);}
  keep({chart:r.root,origin:0,permutation:[...identity],representativeWord:[]});
  for(let q=0;q<states.length;q++){
    const s=states[q];if(r.charts[s.chart].species==='electron') continue;
    r.edges.forEach((e,index)=>{if(e.from!==s.chart||s.origin+e.phaseDelta>cap)return;
      const t={chart:e.to,origin:s.origin+e.phaseDelta,permutation:composePermutation(s.permutation,e.permutation),representativeWord:[...s.representativeWord,index]};
      transitions.push({from:q,to:keep(t),sourceEdge:index});
    });
  }
  const exits=states.filter(s=>r.charts[s.chart].species==='electron').map(s=>s.id),live=new Set(exits);
  for(let changed=true;changed;){changed=false;for(const e of transitions)if(live.has(e.to)&&!live.has(e.from)){live.add(e.from);changed=true;}}
  return {maxExitCIndex,states,transitions,entry:0,exits,canReachExit:[...live].sort((a,b)=>a-b),
    representation:'Finite labelled graph of chart/origin/full-permutation packets. Distinct complete words retain distinct histories; merging graph nodes does not identify their words. C-exit index cap is not a derived count of elementary C/M operations.'};
}
export function buildAtlas(r,{maxTransitions=9}={}) {
  if (!Number.isInteger(maxTransitions) || maxTransitions<0 || maxTransitions>12) throw Error('Transition bound must be an integer in [0,12]');
  auditPhaseAssembly(r);
  const adjacency=r.charts.map(()=>[]);
  r.edges.forEach((e,i)=>adjacency[e.from].push(i));
  if (r.charts.some((c,i)=>c.species==='electron' && adjacency[i].length)) throw Error('Source exit is no longer terminal; retype first-hit semantics');
  const paths=[],frontier=[],counts=Array(maxTransitions+1).fill(0);
  let prefixes=0;
  function visit(trace) {
    prefixes++;
    const end=trace.at(-1),depth=end.history.length;
    if (r.charts[end.chart].species==='electron') {
      const inverseSteps=[];
      let cursor=clone(end);
      for (const index of [...end.history].reverse()) {
        const from=retainedView(r,cursor),nativeCandidates=nativeInverseIndices(r,index);
        cursor=undo(r,cursor,index);
        inverseSteps.push({inverseOf:index,from,to:retainedView(r,cursor),nativeCandidates,
          operation:nativeCandidates.length?'native-packet-inverse-exists':'formal-inverse-only'});
      }
      if (!same(cursor,initialState(r))) throw Error('Failed full reverse recovery');
      const entryC=boundary(r,trace[0]),exitC=boundary(r,end,true);
      counts[depth]++;
      paths.push({id:end.history.join('.'),length:depth,word:[...end.history],phaseAdvances:end.origin,
        entryC,exitC,trace:trace.map(s=>retainedView(r,s)),inverseSteps,
        reverseNativeAdmitted:inverseSteps.every(s=>s.nativeCandidates.length>0),
        inverseRecoversFullPrefix:true,
        CIndexSpan:exitC.index-entryC.index,
        withinC0ThroughC4:entryC.index===0 && exitC.index<=4});
      return;
    }
    if (depth===maxTransitions) { frontier.push(retainedView(r,end)); return; }
    for (const index of adjacency[end.chart]) visit([...trace,advance(r,end,index)]);
  }
  visit([initialState(r)]);
  // Independent layered path count: multiplicities are aggregated only for counting,
  // never as a quotient of the retained path records above.
  let layer=r.charts.map((_,i)=>i===r.root?1:0);
  const independentCounts=[];
  for(let depth=0;depth<=maxTransitions;depth++) {
    independentCounts.push(layer.reduce((n,k,i)=>n+(r.charts[i].species==='electron'?k:0),0));
    const next=layer.map(()=>0);
    for(let i=0;i<layer.length;i++) if(r.charts[i].species!=='electron') for(const edge of adjacency[i]) next[r.edges[edge].to]+=layer[i];
    layer=next;
  }
  if(!same(counts,independentCounts)) throw Error('Exhaustive enumeration disagrees with independent count');
  // A native zero-origin loop can be inserted arbitrarily often. The finite graph
  // represents those words; retaining their histories does not make the word set finite.
  let pumpingWitness=null;
  const shortest=[...paths].sort((a,b)=>a.length-b.length)[0];
  for(const i of adjacency[r.root]) {
    const e=r.edges[i];
    for(const j of adjacency[e.to]) if(r.edges[j].to===r.root) {
      const loop=traceWord(r,[i,j]).at(-1);
      if(loop.origin===0 && same(loop.permutation,identity) && shortest) {
        pumpingWitness={loop:[i,j],suffix:shortest.word,exitC:shortest.exitC,
          countForRepetitions:'2*n + suffix.length',originAfterLoop:0,
          coefficientsAndFrameRestored:true,historyRestored:false,
          unboundedWordsWithinC0ThroughC4:shortest.withinC0ThroughC4};
        break;
      }
    }
    if(pumpingWitness) break;
  }
  const CExitCapGraph=buildCExitCapGraph(r);
  return {schema:'marici.nima.bounded-phase-path-atlas.v1',
    bound:{maxTotalTransitions:maxTransitions,phaseAdvancesAreSeparate:true,
      sourceTransitionsHaveDerivedCMStageCost:false},
    boundaryConvention:'Entry=root proton first window occurrence C0; exit=terminal electron last window occurrence C_(origin+2). These are declared marked boundaries, not a derived physical interface.',
    reverseSemantics:'Formal undo reconstructs the retained earlier prefix. A native inverse candidate matches the chart/coefficient/origin packet; executing a new command appends provenance rather than erasing the original record.',
    source:{charts:clone(r.charts),edges:clone(r.edges),root:r.root,orientations:r.orientations},
    summary:{paths:paths.length,byLength:counts,prefixes,budgetFrontier:frontier.length,
      symbolicallyReversible:paths.length,nativeReverseAdmitted:paths.filter(p=>p.reverseNativeAdmitted).length,
      withinC0ThroughC4:paths.filter(p=>p.withinC0ThroughC4).length,
      CExitCapGraphStates:CExitCapGraph.states.length,CExitCapGraphTransitions:CExitCapGraph.transitions.length,
      CExitCapGraphExits:CExitCapGraph.exits.length,CExitCapGraphLiveStates:CExitCapGraph.canReachExit.length},
    pumpingWitness,CExitCapGraph,paths,frontier,
    scope:'All edge-labelled first-hit root-to-electron words of length at most the declared bound in this selected source graph, including repeated cells and charts. No enumeration of all geometries, coefficient values or physical processes; no collapse of full histories.'};
}
export function checkCoefficientRecovery(r,atlas) {
  const samples=[...identity.map(i=>identity.map(j=>[i===j?1:0,0])),
    ...identity.map(i=>identity.map(j=>[0,i===j?1:0])),[[2,-3],[4,5],[-6,7],[9,-7],[-5,6]]];
  let cases=0;
  for(const path of atlas.paths) for(const sample of samples) {
    let value=clone(sample);
    for(const i of path.word) value=applyPhasePermutation(value,r.edges[i].permutation);
    if(!same(value,applyPhasePermutation(sample,path.trace.at(-1).permutation))) throw Error('Wrong composed coefficient map');
    for(const i of [...path.word].reverse()) value=applyPhasePermutation(value,r.edges[i].permutation,-1);
    if(!same(value,sample)) throw Error('Coefficient inverse failed');
    cases++;
  }
  return cases;
}
