from pathlib import Path

for i in range(1, 26):
    filename = f"{i}_chapter_{i}.md"

    content = f"""---\nauthor: name\n---\n
# Hoofdstuk titel \n \n Hoofdstukinhoud hier.\n 
```{{figure}} ../figuren/naambestand.jpg\n :width: 100% \n :label: some_label_{i} \n \n onderschrift \n ```"""
        
    

    Path(filename).write_text(content, encoding="utf-8")