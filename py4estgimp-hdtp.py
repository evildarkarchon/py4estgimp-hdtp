import os
from pathlib import Path
import subprocess

WorkingDir = Path.cwd()

def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"File {file_path} deleted successfully.")
    except FileNotFoundError:
        print(f"File {file_path} does not exist.")
    except PermissionError:
        print(f"Permission denied to delete file {file_path}.")
    except Exception as e:
        print(f"An error occurred while deleting the file: {e}")

print("Extract the mods to the 7 folders as per the PDF instructions BEFORE running this file.")

print("R0B0COPY is about to run for FlaconOil's Complete Retexture Project.")
subprocess.run(["robocopy", f"{WorkingDir}\\01_FlaconOil", f"{WorkingDir}\\Combined_Files", "/s"], shell=True)
subprocess.run(["robocopy", f"{WorkingDir}\\02_FlaconOil", f"{WorkingDir}\\Combined_Files", "/s"], shell=True)
subprocess.run(["robocopy", f"{WorkingDir}\\03_FlaconOil", f"{WorkingDir}\\Combined_Files", "/s"], shell=True)

print("R0B0COPY is complete.")

print("Conflicting Files from from FlaconOil are about to be deleted.")
files_to_delete = [
    f"{WorkingDir}\\Combined_Files\\textures\\setdressing\\officeOfficeBoxPapers01_Clean_d.dds",
    f"{WorkingDir}\\Combined_Files\\textures\\setdressing\\officeOfficeBoxPapers01_Clean_n.dds",
    f"{WorkingDir}\\Combined_Files\\textures\\setdressing\\officeOfficeBoxPapers01_d.dds",
    f"{WorkingDir}\\Combined_Files\\textures\\setdressing\\officeOfficeBoxPapers01_n.dds",
    f"{WorkingDir}\\Combined_Files\\textures\\setdressing\\Tires\\Tires01_d.DDS",
    f"{WorkingDir}\\Combined_Files\\textures\\setdressing\\Tires\\Tires01_n.DDS",
    f"{WorkingDir}\\Combined_Files\\textures\\setdressing\\Tires\\Tires01_s.DDS"
]
for file_path in files_to_delete:
    delete_file(file_path)
print("Deletion Complete")

print("Conflicting Files from from Langley are about to be deleted.")
files_to_delete = [
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\Bricks01_d.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\Bricks01_n.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\Bricks01_s.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\Bricks01Painted01_d.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\Bricks01Painted01_s.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\Bricks01R_d.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\Bricks01R_n.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\Bricks01R_s.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\Bricks01Trim_d.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\Bricks01Trim_n.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\Bricks01Trim_s.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\Bricks02_d.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\Bricks02R_d.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\Bricks02Trim_d.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\BricksDarkRed01_d.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\BricksFactory01_d.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\BricksFactory01R_d.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\BricksGreen01_d.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\BricksGreen01_n.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\BricksGS01_d.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\BricksGS01_s.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\BricksRed01_d.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\BricksWhite01_d.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\BricksWhite01_n.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\BricksWhite01_s.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\BricksWhite01R_d.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\BrickTrim01_d.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\BrickTrim01_n.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\BrickTrim01_s.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\BrickWhite02Win01_d.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\BrickWhite02Win01_n.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\Debris01_d.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\Debris01_n.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\Debris01_s.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\Debris02_d.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\Plaster01_d.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\Plaster01_n.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\Plaster01_s.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\Plaster02_d.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\Plaster02_n.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\Plaster02_s.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\ResAwningFabric01_d.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\ResAwningFabric01_n.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\ResAwningFabric01_s.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\ResAwningFabric02_d.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\resawningfabric03_d.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\resawningfabric03_s.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\ResAwningFabric04_d.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\WoodFloor01_d.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\WoodFloor01_n.DDS",
    f"{WorkingDir}\\04_Langley\\textures\\architecture\\buildings\\WoodFloor01_s.DDS",
    f"{WorkingDir}\\04_Langley\\materials\\architecture\\buildings\\BrickBrownstone01.bgsm",
    f"{WorkingDir}\\04_Langley\\materials\\architecture\\buildings\\BrickBrownstonePainted01.bgsm",
    f"{WorkingDir}\\04_Langley\\materials\\architecture\\buildings\\BrickBrownstonePainted02.bgsm",
    f"{WorkingDir}\\04_Langley\\materials\\architecture\\buildings\\BrickGreenLt01.bgsm",
    f"{WorkingDir}\\04_Langley\\materials\\architecture\\buildings\\BrickRed01.BGSM",
    f"{WorkingDir}\\04_Langley\\materials\\architecture\\buildings\\BrickRedDamageDecal01.BGSM",
    f"{WorkingDir}\\04_Langley\\materials\\architecture\\buildings\\BricksFactory01.BGSM",
    f"{WorkingDir}\\04_Langley\\materials\\architecture\\buildings\\BrickSolidWhitePaint01.bgsm",
    f"{WorkingDir}\\04_Langley\\materials\\architecture\\buildings\\BrickTan01.BGSM",
    f"{WorkingDir}\\04_Langley\\materials\\architecture\\buildings\\BrickTanLt01.bgsm"
]

for file_path in files_to_delete:
    delete_file(file_path)
print("Deletion Complete")

print("R0B0COPY is about to run for Langleys HD Textures Workshop.")
subprocess.run(["robocopy", f"{WorkingDir}\\04_Langley", f"{WorkingDir}\\Combined_Files", "/s"], shell=True)
print("R0B0COPY is complete.")

print("R0B0COPY is about to run for High Resolution Texture Pack 2K and 4K - Valius.")
subprocess.run(["robocopy", f"{WorkingDir}\\05_Valius", f"{WorkingDir}\\Combined_Files", "/s"], shell=True)
print("R0B0COPY is complete.")

print("R0B0COPY is about to run for NMC's Texture Bundle.")
subprocess.run(["robocopy", f"{WorkingDir}\\06_NMC", f"{WorkingDir}\\Combined_Files", "/s"], shell=True)
print("R0B0COPY is complete.")

print("R0B0COPY is about to run for Lucid's Texture Upgrades.")
subprocess.run(["robocopy", f"{WorkingDir}\\07_Lucid", f"{WorkingDir}\\Combined_Files", "/s"], shell=True)
print("R0B0COPY is complete.")

print("R0B0COPY is about to run for SavrenX TilesRubble01.")
subprocess.run(["robocopy", f"{WorkingDir}\\08_SavrenX", f"{WorkingDir}\\Combined_Files", "/s"], shell=True)
print("R0B0COPY is complete.")

print("4estGimp - HDTP has completed copying files to the Combined_Files folder. Now to make 2 ba2 files.")
print("CRITICAL - follow the PDF instructions! Use Cathedral Asset Optimizer to create 4estGimp HDTP BA2 Files.")
subprocess.run(["start", "", "Cathedral_Assets_Optimizer_Shortcut.lnk"], shell=True)

print("Compress the 3 files in the BA2\\data folder to a .zip .rar or .7z folder.  Again, see the installation PDF.")
print("Thank You")
input("Press Enter to close...")
