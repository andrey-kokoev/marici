param([switch]$Fresh)
$ErrorActionPreference = 'Stop'
$PSNativeCommandUseErrorActionPreference = $false
if ($IsWindows -and (($env:PATHEXT -split ';') -notcontains '.EXE')) {
  $env:PATHEXT = if ($env:PATHEXT) { "$env:PATHEXT;.EXE" } else { '.EXE' }
}
$Root = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../../..'))
$Owner = Join-Path $Root 'research/voevodsky/agda'
$Native = Join-Path $Root 'research/nima/agda'
$Fixtures = Join-Path $Root 'research/voevodsky/fixtures/ramsey-native-region-family'
$Tools = Join-Path $env:USERPROFILE 'tools/cubical-agda'
$Agda = Join-Path $Tools 'agda-2.8.0/agda.exe'
$Library = Join-Path $Tools 'cubical-0.9'
$Results = Join-Path $Root 'research/voevodsky/results'
function Inventory([string]$Directory) {
  $h = [ordered]@{}
  foreach ($File in (Get-ChildItem $Directory -Recurse -File -Filter '*.agda' | Sort-Object FullName)) {
    $Key = [IO.Path]::GetRelativePath($Directory,$File.FullName).Replace('\','/')
    $FileHash = Get-FileHash -Algorithm SHA256 -LiteralPath $File.FullName
    if ($null -eq $FileHash -or $null -eq $FileHash.Hash) { throw "No source hash returned for $($File.FullName)" }
    $h[$Key] = $FileHash.Hash.ToLowerInvariant()
  }
  return ,$h
}
$Before = [ordered]@{native=Inventory $Native; owner=Inventory $Owner; library=Inventory $Library; fixtures=Inventory $Fixtures}
$CompilerBefore = (Get-FileHash -Algorithm SHA256 $Agda).Hash.ToLowerInvariant()
$ArgsBase = @('--safe','--cubical','--guardedness','--transliterate','-i',$Owner,'-i',$Native,
 '-i',(Join-Path $Root 'research/nima/adapters/native-application'),
 '-i',(Join-Path $Root 'research/nima/adapters/application-extension'),'-i',$Library)
if ($Fresh) { $ArgsBase += '--ignore-interfaces' }
$Started = [DateTime]::UtcNow.ToString('o')
$Positive = Join-Path $Owner 'RamseyRegionFamily.agda'
$Negative = Join-Path $Fixtures 'RamseyRegionFamilyWrongPremise.agda'
Push-Location $Root
try {
  & $Agda @ArgsBase $Positive 2>&1 | Tee-Object -FilePath (Join-Path $Results 'agda-RamseyRegionFamily.log')
  $PositiveCode = $LASTEXITCODE
  if ($PositiveCode -eq 0) {
    & $Agda @ArgsBase '-i' $Fixtures $Negative 2>&1 | Tee-Object -FilePath (Join-Path $Results 'agda-RamseyRegionFamilyWrongPremise.log')
    $NegativeCode = $LASTEXITCODE
  } else { $NegativeCode = -999 }
} finally { Pop-Location }
$After = [ordered]@{native=Inventory $Native; owner=Inventory $Owner; library=Inventory $Library; fixtures=Inventory $Fixtures}
$CompilerAfter = (Get-FileHash -Algorithm SHA256 $Agda).Hash.ToLowerInvariant()
$Stable = (($Before | ConvertTo-Json -Depth 6 -Compress) -ceq ($After | ConvertTo-Json -Depth 6 -Compress)) -and ($CompilerBefore -ceq $CompilerAfter)
$NegativeText = if ($NegativeCode -ne -999) { Get-Content -Raw (Join-Path $Results 'agda-RamseyRegionFamilyWrongPremise.log') } else { '' }
$NegativeExpected = $NegativeCode -ne 0 -and $NegativeCode -ne -999 -and $NegativeText.Contains('RamseyRegionFamilyWrongPremise.agda') -and ($NegativeText.Contains('!=') -or $NegativeText.Contains('not equal'))
$Passed = $PositiveCode -eq 0 -and $NegativeExpected -and $Stable
[ordered]@{
 schema='marici.voevodsky.native-region-family.agda-check.v1'; started_at=$Started; finished_at=[DateTime]::UtcNow.ToString('o')
 compiler=$Agda; compiler_sha256=$CompilerAfter; ignore_interfaces=[bool]$Fresh; inputs_stable_during_check=$Stable
 positive_exit_code=$PositiveCode; wrong_premise_exit_code=$NegativeCode; wrong_premise_rejected_as_expected=$NegativeExpected; passed=$Passed
 positive_source_sha256=(Get-FileHash -Algorithm SHA256 $Positive).Hash.ToLowerInvariant()
 negative_source_sha256=(Get-FileHash -Algorithm SHA256 $Negative).Hash.ToLowerInvariant()
 source_inventory=$After
} | ConvertTo-Json -Depth 7 | Set-Content -Encoding utf8 (Join-Path $Results 'agda-RamseyRegionFamily.json')
if (!$Passed) { exit 1 }
