import os
from pathlib import Path
import shutil
import argparse

parser = argparse.ArgumentParser(description='4estGimp HDTP')
parser.add_argument('--path', type=Path, default=Path.cwd(), help='Path to Working Directory')
parser.add_argument('--cao-path', type=Path, default=Path.cwd().parent.joinpath("CAO/Cathedral_Assets_Optimizer.exe"), help='Path to Cathedral Assets Optimizer')
args = parser.parse_args()

if args.path and isinstance(args.path, Path):
    WORKING_DIR = args.path
elif args.path and isinstance(args.path, str):
    WORKING_DIR = Path(args.path)
else:
    WORKING_DIR = Path.cwd()

print("Extract the mods to the 7 folders as per the PDF instructions BEFORE running this file.")
input("Press Enter to continue...")

def copy_texture_folders(source_folders, destination):
    """Copy texture folders to destination"""
    for folder in source_folders:
        print(f"Copying {folder} to {destination}")
        shutil.copytree(WORKING_DIR/folder, destination, dirs_exist_ok=True)
    print("Copy Complete")

def delete_conflict_files(file_paths):
    """Delete specific conflicting files"""
    print("Deleting conflicting files")
    for path in file_paths:
        if os.path.exists(path):
            print(f"Deleting {path}")
            os.remove(path)
        else:
            print(f"File {path} does not exist")
        print("Deletion Complete")

def launch_cao(location=Path.cwd().parent.joinpath("CAO/Cathedral_Assets_Optimizer.exe")):
    """Launch Cathedral Assets Optimizer"""
    os.startfile(location)

copy_texture_folders("01_FlaconOil", "Combined_Files")
copy_texture_folders("02_FlaconOil", "Combined_Files")
copy_texture_folders("03_FlaconOil", "Combined_Files")

CONFLICTING_FILES = [
    f"{WORKING_DIR}\\Combined_Files\\textures\\setdressing\\officeOfficeBoxPapers01_Clean_d.dds",
    f"{WORKING_DIR}\\Combined_Files\\textures\\setdressing\\officeOfficeBoxPapers01_Clean_n.dds",
    f"{WORKING_DIR}\\Combined_Files\\textures\\setdressing\\officeOfficeBoxPapers01_d.dds",
    f"{WORKING_DIR}\\Combined_Files\\textures\\setdressing\\officeOfficeBoxPapers01_n.dds",
    f"{WORKING_DIR}\\Combined_Files\\textures\\setdressing\\Tires\\Tires01_d.DDS",
    f"{WORKING_DIR}\\Combined_Files\\textures\\setdressing\\Tires\\Tires01_n.DDS",
    f"{WORKING_DIR}\\Combined_Files\\textures\\setdressing\\Tires\\Tires01_s.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\Bricks01_d.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\Bricks01_n.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\Bricks01_s.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\Bricks01Painted01_d.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\Bricks01Painted01_s.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\Bricks01R_d.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\Bricks01R_n.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\Bricks01R_s.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\Bricks01Trim_d.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\Bricks01Trim_n.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\Bricks01Trim_s.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\Bricks02_d.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\Bricks02R_d.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\Bricks02Trim_d.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\BricksDarkRed01_d.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\BricksFactory01_d.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\BricksFactory01R_d.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\BricksGreen01_d.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\BricksGreen01_n.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\BricksGS01_d.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\BricksGS01_s.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\BricksRed01_d.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\BricksWhite01_d.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\BricksWhite01_n.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\BricksWhite01_s.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\BricksWhite01R_d.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\BrickTrim01_d.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\BrickTrim01_n.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\BrickTrim01_s.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\BrickWhite02Win01_d.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\BrickWhite02Win01_n.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\Debris01_d.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\Debris01_n.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\Debris01_s.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\Debris02_d.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\Plaster01_d.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\Plaster01_n.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\Plaster01_s.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\Plaster02_d.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\Plaster02_n.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\Plaster02_s.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\ResAwningFabric01_d.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\ResAwningFabric01_n.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\ResAwningFabric01_s.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\ResAwningFabric02_d.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\resawningfabric03_d.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\resawningfabric03_s.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\ResAwningFabric04_d.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\WoodFloor01_d.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\WoodFloor01_n.DDS",
    f"{WORKING_DIR}\\04_Langley\\textures\\architecture\\buildings\\WoodFloor01_s.DDS",
    f"{WORKING_DIR}\\04_Langley\\materials\\architecture\\buildings\\BrickBrownstone01.bgsm",
    f"{WORKING_DIR}\\04_Langley\\materials\\architecture\\buildings\\BrickBrownstonePainted01.bgsm",
    f"{WORKING_DIR}\\04_Langley\\materials\\architecture\\buildings\\BrickBrownstonePainted02.bgsm",
    f"{WORKING_DIR}\\04_Langley\\materials\\architecture\\buildings\\BrickGreenLt01.bgsm",
    f"{WORKING_DIR}\\04_Langley\\materials\\architecture\\buildings\\BrickRed01.BGSM",
    f"{WORKING_DIR}\\04_Langley\\materials\\architecture\\buildings\\BrickRedDamageDecal01.BGSM",
    f"{WORKING_DIR}\\04_Langley\\materials\\architecture\\buildings\\BricksFactory01.BGSM",
    f"{WORKING_DIR}\\04_Langley\\materials\\architecture\\buildings\\BrickSolidWhitePaint01.bgsm",
    f"{WORKING_DIR}\\04_Langley\\materials\\architecture\\buildings\\BrickTan01.BGSM",
    f"{WORKING_DIR}\\04_Langley\\materials\\architecture\\buildings\\BrickTanLt01.bgsm"
]
delete_conflict_files(CONFLICTING_FILES)
copy_texture_folders("04_Langley", "Combined_Files")
copy_texture_folders("05_Valius", "Combined_Files")
copy_texture_folders("06_NMC", "Combined_Files")
copy_texture_folders("07_Lucid", "Combined_Files")
copy_texture_folders("08_SavrenX", "Combined_Files")

print("4estGimp - HDTP has completed copying files to the Combined_Files folder. Now to make 2 ba2 files.")
print("CRITICAL - follow the PDF instructions! Use Cathedral Asset Optimizer to create 4estGimp HDTP BA2 Files.")
if isinstance(args.cao_path, Path):
    launch_cao(args.cao_path)
elif isinstance(args.cao_path, str):
    launch_cao(Path(args.cao_path))
else:
    launch_cao()

print("Compress the 3 files in the BA2\\data folder to a .zip .rar or .7z folder.  Again, see the installation PDF.")
print("Thank You")
input("Press Enter to close...")
