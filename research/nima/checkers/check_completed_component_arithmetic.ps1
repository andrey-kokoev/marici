param([switch]$Fresh, [switch]$Worker)
$ErrorActionPreference = 'Stop'
if (!$Worker) {
  $PreviousPathExt = $env:PATHEXT
  $env:PATHEXT = '.COM;.EXE;.BAT;.CMD'
  try {
    $Arguments = @('-NoProfile', '-File', ('"' + $PSCommandPath + '"'), '-Worker')
    if ($Fresh) { $Arguments += '-Fresh' }
    $Child = Start-Process -FilePath (Join-Path $PSHOME 'pwsh.exe') -ArgumentList $Arguments -NoNewWindow -Wait -PassThru
    exit $Child.ExitCode
  } finally { $env:PATHEXT = $PreviousPathExt }
}
$Root = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../../..'))
$Sources = Join-Path $Root 'research/nima/agda'
$Results = Join-Path $Root 'research/nima/results'
$Tools = Join-Path $env:USERPROFILE 'tools/cubical-agda'
$Receipt = Join-Path $Results 'completed-component-arithmetic-formal-audit.json'
if (Test-Path $Receipt) { Remove-Item $Receipt }
& (Join-Path $PSScriptRoot 'check_cubical_agda.ps1') -Module NativeRationalComponentArithmetic -Fresh:$Fresh
if ($LASTEXITCODE -ne 0) { throw 'Positive compilation failed' }
$Positive = Join-Path $Results 'agda-NativeRationalComponentArithmetic.json'
$Controls = @()
$Specs = @(
  @{Name='ComponentZeroDenominator'; Markers=@('[InstanceNoCandidate]', 'Constraint 0')},
  @{Name='ComponentBadFractionCancellation'; Markers=@('[UnequalTerms]', '6 != 4')},
  @{Name='ComponentBadSignedCancellation'; Markers=@('[UnequalTerms]', '0 != 1')},
  @{Name='ComponentBadScalarReadout'; Markers=@('[UnequalTerms]', '3600 != 4200')}
)
foreach ($Spec in $Specs) {
  $Name = $Spec.Name
  $File = Join-Path $Sources "negative/$Name.agda"
  $Output = & (Join-Path $Tools 'agda-2.8.0/agda.exe') --transliterate -i $Sources -i (Join-Path $Tools 'cubical-0.9') $File 2>&1
  $Code = $LASTEXITCODE
  $Text = $Output | Out-String
  $Text | Set-Content -Encoding utf8 (Join-Path $Results "agda-$Name.log")
  if ($Code -eq 0) { throw "Unexpectedly accepted: $Name" }
  foreach ($Marker in $Spec.Markers) {
    if (!$Text.Contains($Marker)) { throw "Wrong rejection: $Name / $Marker`n$Text" }
  }
  $Controls += @{module=$Name; exit_code=$Code; correctly_rejected=$true; expected_markers=$Spec.Markers;
    source_sha256=(Get-FileHash -Algorithm SHA256 $File).Hash}
}
@{status='completed-component-arithmetic-formal-checked'; controls=$Controls;
  positive_receipt_sha256=(Get-FileHash -Algorithm SHA256 $Positive).Hash;
  checker_sha256=(Get-FileHash -Algorithm SHA256 $PSCommandPath).Hash;
  finished_at=[DateTime]::UtcNow.ToString('o'); fresh=[bool]$Fresh;
  scope='Signed-pair and positive-denominator rational quotients, derived operations and readout equivalences; native readout squares for all finite expressions; actual scalar 6/25. Physical weights and geometric component hypothesis remain supplied.'
} | ConvertTo-Json -Depth 5 | Set-Content -Encoding utf8 $Receipt
exit 0
