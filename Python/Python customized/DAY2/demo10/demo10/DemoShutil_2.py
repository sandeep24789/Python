import shutil

source="src"
backup="mathankumar"

# recursively copy the entire directory tree rooted at src to dest
# destination directory must not exist

shutil.copytree(source,backup)
