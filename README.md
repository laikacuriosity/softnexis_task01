Softnexis Inetrnship : task 01<br>
A powerful Python command-line tool that automatically organizes files in any directory by categorizing them based on file extensions. <br>

Features:<br>
Smart Categorization: Automatically sorts files into predefined categories (Documents, Images, Code, Video, Archives, etc.)<br>
Duplicate Handling: Intelligently renames files when duplicates are detected using incremental numbering<br>
Dry Run Mode: Preview changes before actually moving files<br>
Detailed Reporting: Get comprehensive statistics on moved, skipped, and errored files<br>
Safe Operations: Built-in error handling for permission issues and file system errors<br>
Logging: Maintains detailed logs of all operations in organizer.log<br>
Verbose Mode: Enable detailed debugging output when needed<br>
Skip Already Organized: Automatically skips files already in category folders<br>

Installation requirements<br>

Python 3.7 or higher<br>
No external dependencies required (uses only Python standard library)<br>

Setup<br>
1. Clone or Download<br>

git clone https://github.com/laikacuriosity/file-organizer.git
cd file-organizer

2. Simply download the script

wget https://raw.githubusercontent.com/yourusername/file-organizer/main/softnexis_task01.py

3. To make it executable (Linux/macOS)<br>
chmod +x softnexis_task01.py<br>

Usage:<br>
Basic Syntax<br>
python softnexis_task01.py <source_directory> [options]<br>

Examples<br>
1️. Organize Your Downloads Folder<br>
python softnexis_task01.py "C:\Users\YourName\Downloads"<br>

2️. Preview Changes (Dry Run - Recommended First!)<br>
python softnexis_task01.py "C:\Users\YourName\Downloads" --dry-run<br>

3️. Organize Current Directory<br>
python softnexis_task01.py . <br>

4️. Verbose Mode (Detailed Logging)<br>
python softnexis_task01.py "C:\Users\YourName\Documents" --verbose<br>

5️. Combine Options<br>
python softnexis_task01.py "/path/to/messy/folder" --dry-run --verbose<br>


File Categories:<br>

This solution organizes files into the following categories:

Documents : `.pdf`, `.doc`, `.docx`, `.txt`, `.rtf`, `.odt`, `.xls`, `.xlsx`, `.ppt`, `.pptx`<br>
Code: `.py`, `.java`, `.cpp`, `.c`, `.h`, `.js`, `.html`, `.css`, `.php`, `.sql`, `.json`, `.xml` 
Images : `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg`, `.tiff`, `.webp` <br>
Video : `.mp4`, `.avi`, `.mkv`, `.mov`, `.wmv`, `.flv` <br>
Archives : `.zip`, `.rar`, `.7z`, `.tar`, `.gz` <br>
Other : Any file extension not listed above <br>


Command-Line Options:<br>

`source_dir` : (Required) Directory path to organize <br>
`--dry-run` : Preview changes without moving files <br>
`--verbose` : Enable detailed logging output <br>
`--help` : Show help message and exit <br>


Output Example:<br>

Starting file organization<br>
Source directory: C:\Users\John\Downloads<br>

Moved: report.pdf to Documents/report.pdf<br>
Moved: vacation_photo.jpg to Images/vacation_photo.jpg<br>
Moved: script.py to Code/script.py<br>
Skipped (already organized): old_file.txt<br>


ORGANIZATION SUMMARY<br>

Files successfully moved: 15<br>
Files skipped: 3<br>
Errors encountered: 0<br>



 Advanced Features

1. Duplicate File Handling

When a file with the same name already exists in the destination folder:<br>
Original: report.pdf<br>
Duplicate 1: report(1).pdf<br>

2. Recursive Processing<br>

The tool automatically processes all subdirectories:<br>

Downloads/<br>
├── folder1/<br>
│   └── file1.pdf  → moves to Downloads/Documents/file1.pdf<br>
└── folder2/<br>
    └── file2.jpg  → moves to Downloads/Images/file2.jpg<br>


3. Skips Already Organized Files<br>

Files already in category folders are automatically skipped to prevent redundant operations.<br>

4. Logging<br>

All operations are logged to `organizer.log` in the script directory:<br>

2024-01-15 10:30:45 - INFO - Starting file organization<br>
2024-01-15 10:30:46 - INFO - Moved: report.pdf to Documents<br>
2024-01-15 10:30:47 - ERROR - Permission denied: protected_file.sys<br>
2024-01-15 10:30:48 - INFO - Organization completed successfully<br>

Important Notes:<br>

Always use --dry-run first to preview changes before actual file movement<br>
Backup important files before running the script on critical directories<br>
Files are moved, not copied (originals are removed from source location)<br>

Permissions<br>
The script requires read/write permissions for the target directory<br>
Run as administrator on Windows if permission errors occur<br>
Use sudo on Linux/macOS for system directories<br>

Excluded Directories<br>
The script skips files already in category folders to prevent re-organizing<br>
System folders and hidden files are processed.<br>


This solution is Customizable, allowing users to:<br>
1. Add new categories via editing the categories dictionary in the script:<br>
pythoncategories = {<br>
    # Add your custom category<br>
    '.md': 'Markdown',<br>
    '.epub': 'eBooks',<br>
    '.mp3': 'Music',<br>
    '.wav': 'Music',<br>
    
    # Existing categories<br>
    '.pdf': 'Documents',<br>
    '.jpg': 'Images',<br>
    
}<br>

2. Change Category Names<br>
Simply modify the category values:<br>
python'.pdf': 'MyDocuments',<br>
'.jpg': 'Photos',<br>       

Troubleshooting<br>
1. Error: "python is not recognized"<br>
Solution: Use full path to Python executable<br>
C:\Users\YourName\AppData\Local\Programs\Python\Python311\python.exe softnexis_task01.py .

2. Error: "Permission denied"<br>
Solution: Run as administrator<br>
Windows: Right-click Command Prompt → "Run as administrator"<br>
Linux/macOS: Use sudo python3 softnexis_task01.py /path<br>

3. Error: "Source directory doesn't exist"<br>
Solution: Check path spelling and use quotes<br>
bashpython softnexis_task01.py "C:\Users\John\My Documents"<br>

4.Files Not Moving<br>
Solution: Check if files are already in category folders (they'll be skipped)<br>


Contributions are welcome! Here's how you can help:<br>

1. Fork the repository<br>
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)<br>
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)<br>
4. Push to the branch (`git push origin feature/AmazingFeature`)<br>
5. Open a Pull Request<br>


Acknowledgments:<br>
Built with Python's powerful pathlib and shutil modules<br>
Inspired by the need for clean, organized file systems.<br>


Quick Start Guide:<br>
Windows Users<br>
powershell# Download the script<br>
# Open PowerShell in your Downloads folder<br>

# Test it first<br>
python softnexis_task01.py . --dry-run<br>

# If it looks good, organize!<br>
python softnexis_task01.py . <br>

Linux/macOS Users:<br><br>
# Download the script<br><br>
# Open terminal in your Downloads folder<br>

# Test it first<br>
python3 softnexis_task01.py . --dry-run<br>

# If it looks good, organize!<br>
python3 softnexis_task01.py .<br>
