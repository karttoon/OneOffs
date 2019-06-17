# OneOffs
Small random scripts for various things I find myself needing to repeat/automate

Brief descriptions follow -

youtube_maltego.py
* Extracts comments from YouTube videos for overlap analysis. Can comment out a field to print to CLI instead of Maltego if node limit reached.

bowiefuscator.py
* Created for one phase of LabyREnth 2017 Docs 5 challenge, it obfuscates PowerShell with the power of David Bowie.

urlquote.py
* Percent encode/decode strings used in URLs.

control.php
* Used with INETSIM to control responses back to malware C2 calling PHP.

cuckoo_submit.py
* Submit files to Cuckoo servers with different configs and read reports by passing ID.

maltego2misp.py
* Convert Maltego graph files to importable OpenIOC MISP reports.

pe_meta.py
* Print PE meta data such as FileVersion, InternalName, FileDescription, etc.

caretperm.py
* Takes a string and prints caret injected permutations for Windows CLI obfuscation/evasion.

psorder.py
* Takes base64 encoded PowerShell and replaces obfuscated ordered string arrays with whatever string they would normally build.

psreplace.py
* Takes base64 encoded PowerShell and replaces obfuscated char strings to attempt and extract URLs.

yararich.py
* Generate a YARA rule off of embedded Rich Header inside of PE files.

ole_pkgscrape.py
* Extracts all embedded OLE Packages from Microsoft Office 97-2003 documents (oletools also accomplishes this).
