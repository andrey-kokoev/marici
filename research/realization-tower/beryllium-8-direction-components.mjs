const colourNames=new Map([[0xffffff,'white'],[0x168fff,'blue'],[0xff3030,'red']]);
// Select a component in a fixed rim direction d without changing a retained
// route. q is the P/E orientation along that route, t its original rim turn.
// q*t*d = +1 selects white; -1 selects red. Pure colours stay unchanged.
export function buildBerylliumDirectionComponents(referenceColumns){
 if(referenceColumns.length!==8||new Set(referenceColumns.map(s=>s.id)).size!==8||referenceColumns.some(s=>!s.id.startsWith('be8:wire:')))
  throw Error('Expected the eight distinct Be-8 reference columns');
 return [1,-1].map(direction=>({
  id:direction===1?'be-reference-fixed-forward':'be-reference-fixed-reverse',direction,
  title:direction===1?'2 · Fixed direction: clockwise':'3 · Opposite direction: counterclockwise',
  columns:referenceColumns.map(s=>{
   if(!['+','-'].includes(s.polarities.t))throw Error('Missing retained turn');
   const sourceTurn=s.polarities.t==='+'?1:-1;
   const selectionSign=s.polarityDirection?s.polarityDirection*sourceTurn*direction:0;
   const colours=selectionSign?[selectionSign===1?0xffffff:0xff3030]:[...s.colours];
   if(colours.length!==1||!colourNames.has(colours[0]))throw Error('Expected one selected component');
   return {...s,polarities:{...s.polarities},direction,selectionSign,colours,
    selectedComponent:colourNames.get(colours[0]),sourceColours:[...s.colours],componentSelected:selectionSign!==0,
    guide:s.guide.map(p=>[...p]),edgeIds:[...s.edgeIds],
    paths:s.paths.map(path=>({...path,points:path.points.map(p=>[...p])}))};
  })
 }));
}
