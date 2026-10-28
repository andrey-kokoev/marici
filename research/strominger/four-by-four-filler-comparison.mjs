import {makeFourByFourFiller,decomposeFillerSlots} from './four-by-four-filler-model.mjs';
import {makeSevenContextFourDepth} from './seven-context-four-depth-model.mjs';
const channels=['aa','ab','ba','bb'];
export function evaluateNativeFillerComparison(source=[[2,1],[3,-2],[5,3],[7,-4],[11,5]]){
 const operator=makeFourByFourFiller(),native=makeSevenContextFourDepth();
 const trace=native.run(source);
 const input=trace.banks.flatMap(bank=>channels.map(channel=>structuredClone(bank[channel].coefficients)));
 const empty=()=>Array.from({length:16},()=>Array.from({length:5},()=>[0,0]));
 const collective=empty(),residual=empty(),charge=empty();
 const boundary={P:Array.from({length:5},()=>[0,0]),E:Array.from({length:5},()=>[0,0])};
 for(let c=0;c<5;c++)for(let part=0;part<2;part++){
  const values=input.map(v=>v[c][part]),d=decomposeFillerSlots(values);
  boundary.P[c][part]=d.boundary.P;boundary.E[c][part]=d.boundary.E;
  for(let i=0;i<16;i++){
   collective[i][c][part]=d.collective[i];residual[i][c][part]=d.residual[i];
   charge[i][c][part]=operator.collectiveChargeNumerator[i].reduce((s,q,j)=>s+q*values[j],0)/operator.collectiveChargeDenominator;
  }
 }
 const modes=operator.residualBasis.map((basis,index)=>{
  const slot=basis.slot??((basis.depth-1)*4+(basis.kind==='P-history-contrast'?0:3));
  return {index,kind:basis.kind,depth:basis.depth??operator.slots[slot].depth,channel:operator.slots[slot].channel,vector:basis.vector,coefficients:structuredClone(residual[slot])};
 });
 let maxReconstructionError=0,maxNeutralCharge=0,maxBasisReconstructionError=0;
 for(let i=0;i<16;i++)for(let c=0;c<5;c++)for(let part=0;part<2;part++){
  maxReconstructionError=Math.max(maxReconstructionError,Math.abs(input[i][c][part]-collective[i][c][part]-residual[i][c][part]));
  maxNeutralCharge=Math.max(maxNeutralCharge,Math.abs(operator.collectiveChargeNumerator[i].reduce((s,q,j)=>s+q*residual[j][c][part],0)/4));
  const rebuilt=modes.reduce((s,m)=>s+m.vector[i]*m.coefficients[c][part],0);
  maxBasisReconstructionError=Math.max(maxBasisReconstructionError,Math.abs(rebuilt-residual[i][c][part]));
 }
 if(maxReconstructionError||maxNeutralCharge||maxBasisReconstructionError)throw Error('Filler comparison confirmation failed');
 return {source:'single native P/E packet; four retained depths; aa/ab/ba/bb',slots:operator.slots,input,collective,residual,charge,boundary,modes,
  spectrum:{positive:1,negative:1,neutral:14},confirmation:{maxReconstructionError,maxNeutralCharge,maxBasisReconstructionError,allFiveComplexCoefficients:true},
  status:'candidate-boundary-operator',scope:'Free slot modes, not fourteen independent native neutron states. Native replay still depends on five complex input coefficients; the operator is not an admitted native transport.',
  nativeRealization:{inputComplexCoefficients:5,packetOccurrences:16,storedComplexCoordinates:80,independentNewNeutronStatesEstablished:false},
  history:trace.final.history};
}
