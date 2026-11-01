export const isBranchingSeedView=state=>['beryllium-8','beryllium-9'].includes(state.processId)||state.processId==='sulfur-32'&&state.sulfurBranchSeed===true;
