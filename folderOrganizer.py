from pathlib import Path
import sys

downloads = Path.home() / "Downloads"

folders = {
    ".pdf": "PDFs",
    ".jpg": "Images",
    ".png": "Images",
    ".jpeg": "Images",
    ".docx": "Docs",
    ".doc": "Docs",
    ".pptx": "PPTX", 
}

files_to_organize = []

def displayFiles():
    for file in downloads.iterdir():
        if file.is_file() and file.suffix.lower() in folders:
            files_to_organize.append(file.name)

    print(files_to_organize)

    print("Files to organize: ")
    for num, fileN in enumerate(files_to_organize, start=1):
        print(f"    {num}) {fileN}")        
    
    return displayFiles()        
        
        
        # print("Script name:", sys.argv[0])
