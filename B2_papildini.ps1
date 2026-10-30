Write-Host "Sākam eksportu"

$diski = Get-PSDrive -PSProvider FileSystem | Select-Object Name, Used, Free

$diski | Export-Csv -Path "diski.csv" -NoTypeInformation -Encoding UTF8
