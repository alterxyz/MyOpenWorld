import os
import shutil
import argparse

def rename_files(source_folder, target_folder):
    os.makedirs(target_folder, exist_ok=True)
    for filename in os.listdir(source_folder):
        if filename.endswith('.md'):
            filepath = os.path.join(source_folder, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                title = [line.split(': ')[1].strip() for line in lines if line.startswith('title:')][0]

            # Using full-width Chinese characters to replace some punctuation marks to be compatible with Windows file system naming rules.
            # 使用中文的全角字符替换部分标点符号替换了部分标点符号, 以便兼容Windows文件系统的命名规则
            title = title.translate(str.maketrans('？:"', '？： '))
            title = title.replace('/', '-').replace('"', '')
            
            new_filename = f"{title}.md"
            new_filepath = os.path.join(target_folder, new_filename)

            # Copy file to new location with new name
            shutil.copy(filepath, new_filepath)

def main(source_folder, target_folder):
    rename_files(source_folder, target_folder)
    print(f"Files have been renamed and copied to: {target_folder}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Rename markdown files based on their titles and copy to a new folder.")
    parser.add_argument('--source', type=str, default='sn_output', help='Path to the source folder containing the markdown files')
    parser.add_argument('--target', type=str, default='sn_renamed_output', help='Path to the target folder where renamed files will be stored')
    args = parser.parse_args()

    main(args.source, args.target)

