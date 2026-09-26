$ErrorActionPreference = 'Stop'
$Root = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../../..'))
$Sources = Join-Path $Root 'research/nima/agda'
$Results = Join-Path $Root 'research/nima/results'
$Tools = Join-Path $env:USERPROFILE 'tools/cubical-agda'
$Receipt = Join-Path $Results 'native-amplitude-resolution-formal-audit.json'
if (Test-Path $Receipt) { Remove-Item $Receipt }
Push-Location $Root
try {
  & (Join-Path $PSScriptRoot 'check_cubical_agda.ps1') -Module ScalarAmplitudeResolveFixture -Fresh
  if ($LASTEXITCODE -ne 0) { throw 'Positive compilation failed' }
  $Positive = Join-Path $Results 'agda-ScalarAmplitudeResolveFixture.json'
  $Specs = @(
    @{Name='AmplitudeResolveBadSeed'; Markers=@('zero-seed')},
    @{Name='AmplitudeResolveBadReadout'; Markers=@('144 != 145', 'refl')}
  )
  $Controls = @()
  foreach ($Spec in $Specs) {
    $File = Join-Path $Sources "negative/$($Spec.Name).agda"
    $Output = & (Join-Path $Tools 'agda-2.8.0/agda.exe') --transliterate -i $Sources -i (Join-Path $Tools 'cubical-0.9') $File 2>&1
    $Code = $LASTEXITCODE
    $Text = $Output | Out-String
    $Text | Set-Content -Encoding utf8 (Join-Path $Results "agda-$($Spec.Name).log")
    if ($Code -eq 0 -or !$Text.Contains('[UnequalTerms]')) { throw "Wrong rejection: $($Spec.Name)`n$Text" }
    foreach ($Marker in $Spec.Markers) {
      if (!$Text.Contains($Marker)) { throw "Wrong rejection marker: $($Spec.Name)/$Marker`n$Text" }
    }
    $Controls += @{module=$Spec.Name; exit_code=$Code; correctly_rejected=$true;
      source_sha256=(Get-FileHash -Algorithm SHA256 $File).Hash; expected_markers=$Spec.Markers}
  }
  @{status='native-amplitude-resolution-formal-checked'; controls=$Controls;
    positive_receipt_sha256=(Get-FileHash -Algorithm SHA256 $Positive).Hash;
    checker_sha256=(Get-FileHash -Algorithm SHA256 $PSCommandPath).Hash;
    finished_at=[DateTime]::UtcNow.ToString('o');
    scope='All finite marked expressions: native Resolve construction, old Resolve construction, readout compatibility, semiring diagram expansion; concrete six-point fixture. Not a proof of arbitrary-n Python enumeration/compiler correctness.'
  } | ConvertTo-Json -Depth 5 | Set-Content -Encoding utf8 $Receipt
} finally { Pop-Location }
