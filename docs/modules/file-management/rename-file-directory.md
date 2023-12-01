---
title: 5. Rename File or Directory
---

# Rename File or Directory

### **_Description_**

The "Rename File or Directory" function within the File Management Module is a versatile tool for renaming files or directories. Whether you need to update the names of your files, improve organization, or ensure clarity in your file system, this function simplifies the process. It allows you to specify the existing file or directory path and provide the new name, facilitating efficient renaming.

### **_Usage_**

1. Open the terminal and type:

```bash
tt --files rename [ARGS]
# or
tt -fm rename [ARGS]
```

### ****Arguments****

- **--PATH (Required)**

**_Example:_**

```bash
tt --fm rename --PATH C:\\Users\\MyUser\\ProjectName\\MyFolder1
```

- **--NEWNAME (Required)**

**_Example:_**

```bash
tt --fm rename --PATH C:\\Users\\MyUser\\ProjectName\\MyFolder1 --NEWNAME C:\\Users\\MyUser\\ProjectName\\MyFolder2
```
