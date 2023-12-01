---
title: 7. Search Files and Directories
---

# Search Files and Directories

### **_Description_**

The "Search Files and Directories" function within the File Management Module is a powerful tool for locating specific files and directories based on your specified criteria. Whether you need to identify files with particular names, extensions, or other attributes, this function simplifies the process. It enables you to input a search criteria and a directory path, returning matching results to streamline your file system exploration.

### **_Usage_**

1. Open the terminal and type:

```bash
tt --files search [ARGS]
# or
tt -fm search [ARGS]
```

### ****Arguments****

- **--DIR (Required)**

**_Example:_**

```bash
tt --fm search --DIR C:\\Users\\MyUser\\ProjectName\\MyFolder
```

- **--CRITERIA (Required)**

**_Example:_**

```bash
tt --fm search --DIR C:\\Users\\MyUser\\ProjectName\\MyFolder --CRITERIA *.py
```

\*(Please make sure the criteria you provided is following the correct types: file name (filename), extension (_\*\*.py), or content (this is the content from myfile.txt)')_
