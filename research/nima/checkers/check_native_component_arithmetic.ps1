param([switch]$Fresh, [switch]$Worker)
$ErrorActionPreference = 'Stop'
# Normalize executable discovery in this checker only. The structured-command
# environment did not provide a usable PATHEXT; PowerShell caches it at startup.
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
$Receipt = Join-Path $Results 'native-component-arithmetic-formal-audit.json'
if (Test-Path $Receipt) { Remove-Item $Receipt }
& (Join-Path $PSScriptRoot 'check_cubical_agda.ps1') -Module NativeComponentArithmetic -Fresh:$Fresh
if ($LASTEXITCODE -ne 0) { throw 'Positive compilation failed' }
$Positive = Join-Path $Results 'agda-NativeComponentArithmetic.json'
$Controls = @()
$Specs = @(
  @{Name='ComponentProductAsAddition'; Marker='6 != 5'},
  @{Name='ComponentMultiplicityCollapse'; Marker='2 != 1'}
)
foreach ($Spec in $Specs) {
  $Name = $Spec.Name
  $File = Join-Path $Sources "negative/$Name.agda"
  $Output = & (Join-Path $Tools 'agda-2.8.0/agda.exe') --transliterate -i $Sources -i (Join-Path $Tools 'cubical-0.9') $File 2>&1
  $Code = $LASTEXITCODE
  $Text = $Output | Out-String
  $Text | Set-Content -Encoding utf8 (Join-Path $Results "agda-$Name.log")
  if ($Code -eq 0 -or !$Text.Contains('[UnequalTerms]') -or !$Text.Contains('refl') -or !$Text.Contains($Spec.Marker)) {
    throw "Wrong rejection: $Name`n$Text"
  }
  $Controls += @{module=$Name; exit_code=$Code; correctly_rejected=$true; expected_marker=$Spec.Marker;
    source_sha256=(Get-FileHash -Algorithm SHA256 $File).Hash}
}
@{status='native-component-arithmetic-formal-checked'; controls=$Controls;
  positive_receipt_sha256=(Get-FileHash -Algorithm SHA256 $Positive).Hash;
  checker_sha256=(Get-FileHash -Algorithm SHA256 $PSCommandPath).Hash;
  finished_at=[DateTime]::UtcNow.ToString('o'); fresh=[bool]$Fresh;
  scope='Initial commutative semiring on inductive component words; native Resolve and semiring readout squares for every finite expression. Geometric normal form conditional. No signed/fraction completion or physical weight derivation.'
} | ConvertTo-Json -Depth 5 | Set-Content -Encoding utf8 $Receipt
exit 0
