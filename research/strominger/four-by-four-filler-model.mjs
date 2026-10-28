// Candidate relative boundary of four retained depths x the aa/ab/ba/bb bank.
// This constructs a free slot-space comparison, not a new physical filler.
export const fillerChannels=Object.freeze(['aa','ab','ba','bb']);
export const fillerSlots=Object.freeze(Array.from({length:4},(_,depth)=>fillerChannels.map((channel,column)=>Object.freeze({index:depth*4+column,depth:depth+1,channel,role:column===0?'proton':column===3?'electron':'neutron'}))).flat());
const basis=i=>Array.from({length:16},(_,j)=>Number(i===j));
export function fillerEndpointReadout(values){
 if(values.length!==16||values.some(x=>!Number.isFinite(x)))throw Error('Sixteen finite scalar slot coordinates required');
 return {P:[0,4,8,12].reduce((s,i)=>s+values[i]/4,0),E:[3,7,11,15].reduce((s,i)=>s+values[i]/4,0)};
}
export function decomposeFillerSlots(values){
 const boundary=fillerEndpointReadout(values),collective=values.map((_,i)=>i%4===0?boundary.P:i%4===3?boundary.E:0);
 return {boundary,collective,residual:values.map((x,i)=>x-collective[i])};
}
export function makeFourByFourFiller(){
 const P=fillerSlots.map(s=>Number(s.channel==='aa')),E=fillerSlots.map(s=>Number(s.channel==='bb'));
 const neutral=fillerSlots.filter(s=>s.role==='neutron').map(s=>({kind:'native-N-slot',slot:s.index,vector:basis(s.index)}));
 const chargedContrasts=[];
 for(const [channel,column]of [['aa',0],['bb',3]])for(let depth=1;depth<4;depth++){
  const vector=basis(depth*4+column);vector[column]=-1;
  chargedContrasts.push({kind:channel==='aa'?'P-history-contrast':'E-history-contrast',depth:depth+1,vector});
 }
 // Q = projector onto the collective P line minus projector onto the
 // collective E line. This is a NEW boundary-only charge proposal.
 const collectiveChargeNumerator=P.map((_,i)=>P.map((__,j)=>P[i]*P[j]-E[i]*E[j]));
 return {slots:fillerSlots,collective:{P,E},boundaryRows:[P,E],residualBasis:[...neutral,...chargedContrasts],collectiveChargeNumerator,collectiveChargeDenominator:4,
  roleSignature:fillerSlots.map(s=>s.role==='proton'?1:s.role==='electron'?-1:0),
  scope:'Boundary rows sum endpoint slots; normalized readout takes their mean. Neutral here refers to the existing N-labelled channel subspace, not an inferred charge law.'};
}
