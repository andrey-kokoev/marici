import {studyNeutronCoherence} from './neutron-space-coherence.mjs';
import {auditFrameReturn} from './frame-return.mjs';
// Full neutral coherence for the new single-anchor/delegated-terminal model.
export function studyBottleneckNeutronCoherence(full){
 const result=studyNeutronCoherence(full.model,{localCoverage:'actual-interface-ports'}),topology=result.comparison.topology;
 const bridgeChecks=[];
 for(const support of full.interface.channelSupports){
  const pair=topology.edges.filter(e=>e.support===support);if(pair.length!==2)throw Error('Missing channel support');
  const [e]=pair,seen=new Set([e.from]),q=[e.from];
  for(let i=0;i<q.length;i++)for(const f of topology.edges)if(f.support!==support&&f.from===q[i]&&!seen.has(f.to)){seen.add(f.to);q.push(f.to);}
  if(seen.has(e.to))throw Error('Channel has a neutral bypass');
  bridgeChecks.push({support,isBridge:true,isBasisChord:result.comparison.basis.some(w=>w.chord===support)});
 }
 if(!bridgeChecks.length)throw Error('Missing declared bottleneck');
 const bridgeTwisted=structuredClone(topology),I=[[1,0,0],[0,1,0],[0,0,1]],rotations=[[[0,-1,0],[1,0,0],[0,0,1]],[[1,0,0],[0,0,-1],[0,1,0]]];
 for(const e of bridgeTwisted.edges)e.transport=structuredClone(I);
 full.interface.channelSupports.forEach((support,i)=>{
  const e=bridgeTwisted.edges.find(e=>e.support===support),r=bridgeTwisted.edges.find(r=>r.id===e.reverse),rotation=rotations[i%rotations.length];e.transport=structuredClone(rotation);r.transport=rotation[0].map((_,j)=>rotation.map(row=>row[j]));
 });
 const bridgeTwistControl=auditFrameReturn(bridgeTwisted);
 return {...result,mode:full.mode,bridgeChecks,bridgeTwistControl,
  interpretation:'The bottleneck is a bridge, not a new cycle. Inverse-consistent bridge rotations do not obstruct closed-loop coherence and are not fixed by it. A cyclic support twist does obstruct path-independent transport. Neither control supplies a physical connection.'};
}
