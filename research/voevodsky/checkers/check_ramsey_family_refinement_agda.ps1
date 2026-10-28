param([switch]$Fresh)
$ErrorActionPreference='Stop';$PSNativeCommandUseErrorActionPreference=$false
if($IsWindows -and (($env:PATHEXT -split ';') -notcontains '.EXE')){$env:PATHEXT=if($env:PATHEXT){"$env:PATHEXT;.EXE"}else{'.EXE'}}
$Root=[IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../../..'))
$Owner=Join-Path $Root 'research/voevodsky/agda';$Native=Join-Path $Root 'research/nima/agda'
$Fixtures=Join-Path $Root 'research/voevodsky/fixtures/ramsey-family-refinement'
$Tools=Join-Path $env:USERPROFILE 'tools/cubical-agda';$Agda=Join-Path $Tools 'agda-2.8.0/agda.exe'
$Library=Join-Path $Tools 'cubical-0.9';$Results=Join-Path $Root 'research/voevodsky/results'
function Inventory([string]$Directory){
 $h=[ordered]@{}
 foreach($f in (Get-ChildItem $Directory -Recurse -File -Filter '*.agda'|Sort-Object FullName)){
  $k=[IO.Path]::GetRelativePath($Directory,$f.FullName).Replace('\','/')
  $v=Get-FileHash -Algorithm SHA256 -LiteralPath $f.FullName
  if($null -eq $v -or $null -eq $v.Hash){throw "No source hash for $($f.FullName)"};$h[$k]=$v.Hash.ToLowerInvariant()
 };return ,$h
}
$Before=[ordered]@{native=Inventory $Native;owner=Inventory $Owner;fixtures=Inventory $Fixtures;library=Inventory $Library}
$CompilerBefore=(Get-FileHash -Algorithm SHA256 -LiteralPath $Agda).Hash.ToLowerInvariant()
$Argv=@('--safe','--cubical','--guardedness','--transliterate','-i',$Owner,'-i',$Native,'-i',$Fixtures,
 '-i',(Join-Path $Root 'research/nima/adapters/native-application'),'-i',(Join-Path $Root 'research/nima/adapters/application-extension'),'-i',$Library)
if($Fresh){$Argv+='--ignore-interfaces'}
$Started=[DateTime]::UtcNow.ToString('o');$Codes=[ordered]@{};$Hashes=[ordered]@{}
$Modules=@('RamseyFamilyRefinement','RamseyFamilyFreshNativeOnly','RamseyFamilyFreshRebuild','RamseyFamilyWrongSeed','RamseyFamilyWrongQuery')
Push-Location $Root
try{
 foreach($Name in $Modules){
  $Directory=if($Name -eq 'RamseyFamilyRefinement'){$Owner}else{$Fixtures};$Source=Join-Path $Directory "$Name.agda"
  & $Agda @Argv $Source 2>&1|Tee-Object -FilePath (Join-Path $Results "agda-$Name.log")
  $Codes[$Name]=$LASTEXITCODE;$Hashes[$Name]=(Get-FileHash -Algorithm SHA256 -LiteralPath $Source).Hash.ToLowerInvariant()
  if($Name -eq 'RamseyFamilyRefinement' -and $LASTEXITCODE -ne 0){break}
 }
}finally{Pop-Location}
$After=[ordered]@{native=Inventory $Native;owner=Inventory $Owner;fixtures=Inventory $Fixtures;library=Inventory $Library}
$CompilerAfter=(Get-FileHash -Algorithm SHA256 -LiteralPath $Agda).Hash.ToLowerInvariant()
$Stable=(($Before|ConvertTo-Json -Depth 7 -Compress) -ceq ($After|ConvertTo-Json -Depth 7 -Compress)) -and ($CompilerBefore -ceq $CompilerAfter)
$Passed=$Stable -and $Codes.Count -eq 5 -and $Codes['RamseyFamilyRefinement'] -eq 0 -and $Codes['RamseyFamilyFreshNativeOnly'] -eq 0
foreach($Name in @('RamseyFamilyFreshRebuild','RamseyFamilyWrongSeed','RamseyFamilyWrongQuery')){
 $Log=Join-Path $Results "agda-$Name.log";$Text=if(Test-Path $Log){Get-Content -Raw $Log}else{''}
 $Passed=$Passed -and $Codes.Contains($Name) -and $Codes[$Name] -ne 0 -and $Text.Contains("$Name.agda") -and ($Text.Contains('!=') -or $Text.Contains('not equal'))
}
[ordered]@{schema='marici.voevodsky.family-refinement.agda-check.v1';started_at=$Started;finished_at=[DateTime]::UtcNow.ToString('o')
 passed=[bool]$Passed;ignore_interfaces=[bool]$Fresh;inputs_stable_during_check=[bool]$Stable;compiler_sha256=$CompilerAfter
 module_exit_codes=$Codes;module_source_sha256=$Hashes;source_inventory=$After
}|ConvertTo-Json -Depth 8|Set-Content -Encoding utf8 (Join-Path $Results 'agda-RamseyFamilyRefinement.json')
if(!$Passed){exit 1}
