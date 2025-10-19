import argparse 
import logging
import sys
from pathlib import Path
from datetime import datetime
import shutil

logging.basicConfig(
    filename='organizer.log', 
    level=logging.INFO, 
    format='{asctime} - {levelname} - {message}',
    style='{'
)

categories={
    #docs
    '.pdf':'Documents',
    '.ppt':'Documents',
    '.doc':'Documents',
    '.docx':'Documents',
    '.txt':'Documents',
    '.rtf':'Documents',
    '.odt':'Documents',
    '.xls':'Documents',
    '.xlsx':'Documents',
    '.pptx':'Documents',

    #code
    '.c':'Code',
    '.cpp':'Code',
    '.json':'Code',
    '.css':'Code',
    '.html':'Code',
    '.java':'Code',
    '.py':'Code',
    '.php':'Code',
    '.sql':'Code',
    '.js':'Code',
    '.xml':'Code',
    '.h':'Code',

    #images
    '.jpg':'Images',
    '.png':'Images',
    '.svg':'Images',
    '.tiff':'Images',
    '.jpeg':'Images',
    '.webp':'Images',
    '.gif':'Images',
    '.bmp':'Images',

    #videos
    '.mp4':'Video',
    '.mov':'Video',
    '.mkv':'Video',
    '.wmv':'Video',
    '.flv':'Video',
    '.avi':'Video',

    #archives
    '.gz':'Archives',
    '.rar':'Archives',
    '.tar':'Archives',
    '.zip':'Archives',
    '.7z':'Archives',

}
    
def get_category(extension):
    return categories.get(extension.lower(), 'Other')

def handlie_duplicates(destination_path):
    if not destination_path.exists():
        return destination_path
    
    parent_name=destination_path.parent_name
    suffix=destination_path.suffix
    stem=destination_path.stem
    
    counter=1
    while True:
        new_name=f"{stem}({counter}){suffix}"
        new_path=parent_name/new_name
        if not new_path.exists():
            return new_path
        counter+=1

def organize_files(source_dir, dry_run=False):
    source_path=Path(source_dir)
    if not source_path.exists():
        logging.error(f"source directory dosesnt exist: {source_path}")
        return 0, 0
    if not source_path.is_dir():
        logging.error(f"sourcce path is not a directory: {source_path}")
        return 0, 0
    stats={
        'moved':0,
        'errors':0,
        'skipped':0
    }
    for file_path in source_path.rglob('*'):
        try:
            if not file_path.is_file():
                continue

            if any(cat_folder in file_path.parts for cat_folder in categories.values()):
                continue

            extension=file_path.suffix
            category=get_category(extension)
                
            category_dir= source_path/category
            if  not dry_run:
                category_dir.mkdir(exist_ok=True)
                
            destination_path=category_dir/file_path.name

            if destination_path.exists() and destination_path!=file_path:
                destination_path=handlie_duplicates(destination_path)
            if file_path.parent==category_dir:
                print(f"skipped(alrady organnized) : {file_path.name}")
                stats['skipped']+=1
                continue
            if dry_run:
                print(f"dry run- would move: {file_path} to {destination_path}")
                stats['moved']+=1
            else:

                try:
                    shutil.move(str(file_path), str(destination_path))
                    print(f"moved: {file_path.name} to {category}/{destination_path.name}")
                    stats['moved']+=1
                except PermissionError as e:
                    logging.error(f"permission denied moving {file_path}:{e}")
                    stats['errors']+=1
                except OSError as e:
                    logging.error(f"OS error,moving {file_path}:{e}")
                    stats['error']+=1
        except PermissionError as e:
            logging.error(f"Permission error accessing {file_path}: {e}")
            stats['errors'] += 1
        except Exception as e:
            logging.error(f"Unexpected error processing {file_path}: {e}")
            stats['errors'] += 1
    return stats

def generate_report(stats, dry_run=False):
    print("\n" + "=" * 50)
    if dry_run:
        logging.info("DRY RUN SUMMARY")
    else:
        logging.info("ORGANIZATION SUMMARY")
    print("=" * 50)
    print(f"Files successfully moved: {stats['moved']}")
    print(f"Files skipped: {stats['skipped']}")
    print(f"Errors encountered: {stats['errors']}")
    print("=" * 50)

def main():

    parser = argparse.ArgumentParser(
        description='Organize files in a directory by their extensions'
    )
    parser.add_argument(
        'source_dir',
        help='Source directory to organize'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview changes without actually moving files'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose logging'
    )
    
    args = parser.parse_args()
    
    # Setup logging
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
  
    print(f"Starting file organization{' (DRY RUN)' if args.dry_run else ''}")
    print(f"Source directory: {args.source_dir}")
    
    try:

        stats = organize_files(args.source_dir, args.dry_run)
        generate_report(stats, args.dry_run)
        
        if stats['errors'] > 0:
            sys.exit(1)
        else:
            sys.exit(0)
            
    except KeyboardInterrupt:
        print("Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Fatal error: {e}")
        print (f"Fatal error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()