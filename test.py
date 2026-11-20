from pathlib import Path
import sys
from collections import defaultdict
import shutil

downloads = Path.home() / "Downloads"
documents = Path.home() / "Documents"


folders = {
    ".pdf": "PDFs",
    ".jpg": "Images",
    ".png": "Images",
    ".jpeg": "Images",
    ".docx": "Docs",
    ".doc": "Docs",
    ".pptx": "PPTX",
    ".txt" : "Notepad"
}

filesToOrganize = []

#FILE
def scanFiles():
    groups = defaultdict(list)
    for file in downloads.iterdir():
        if file.is_file() and file.suffix.lower() in folders:
            groups[folders[file.suffix.lower()]].append(file)
    
    return groups

def displayFiles(groups):
    flat = []
    num = 1

    for group, files in groups.items():
        print(f"{group.upper()}:")
        for file in files:
            print(f"    {num}) {file.name}")
            flat.append(file)
            num += 1
        print()
    return flat

def chooseFile(files):
    while True:
        choice = input("Choose a file number (q to quit): ").strip().lower()
        if choice == "q":
            sys.exit(0)

        parts = choice.split()

        if parts and all(p.isdigit() and 1 <= int(p) <= len(files) for p in parts):
            return [files[i - 1] for i in sorted(set(int(p) for p in parts))]
        print("Invalid choice, try again")

#FOLDER
def scanFolders():
    foldersList = sorted(f for f in documents.iterdir() if f.is_dir())

    return foldersList

def displayFolders(foldersList):
    print("Folders in Documents:")
    for num, folder in enumerate(foldersList, start=1):
        print(f"    {num}) {folder.name}")
    return foldersList

def chooseFolder(folderList):
    while True:
            choice = input("Choose a folder number (q to quit): ").strip().lower()
            if choice == "q":
                sys.exit(0)
            if choice.isdigit() and 1 <= int(choice) <= len(folderList):
                wrongFolder = input("Move to this folder? y/n: ").strip().lower()
                if wrongFolder == "n":
                    continue
                if wrongFolder == "y":
                    chosenFolder = folderList[int(choice) - 1] 
                    print(f"File was moved into: {chosenFolder.name}.")
                    return folderList[int(choice) - 1] 
            print("Invalid choice, try again")

def moveFile(selected, target):
    skippedFiles = []
    movedFiles = []
    for f in selected:
        destination = target / f.name
        if destination.exists():
            skippedFiles.append(f.name)
            continue
        shutil.move(str(f), str(destination))
        movedFiles.append(f.name)
    
    return skippedFiles, movedFiles

#MAIN
def main():
    while True: 
        scanFile = scanFiles()
        files = displayFiles(scanFile)
        if not files:
            print("nothing to organize")
            sys.exit(0)

        selected = chooseFile(files)

        scanFolder = scanFolders()
        folderListDisplay = displayFolders(scanFolder)
        target = chooseFolder(folderListDisplay)

        skippedFiles, movedFiles = moveFile(selected, target)
        
        for mFile in movedFiles:
            print(f"Moved file: {mFile}")

        for sFile in skippedFiles:
            print(f"Files skipped: {sFile}")
        
        while True:
            moveMoreFiles = input("Do you want to move more files? y/n: ").strip().lower()
            moveMoreAns = ("y", "n")
            if moveMoreFiles not in moveMoreAns:
                print("Invalid answer, try again")
            else:
                break
        if moveMoreFiles == "y":
            continue
        if moveMoreFiles == "n":
            break

if __name__ == "__main__":
    main()
