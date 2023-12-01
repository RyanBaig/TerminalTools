---
title: 6. Copy File or Directory
---

# Copy File or Directory

### **_Description_**

The "Copy File or Directory" function within the File Management Module is a versatile tool for duplicating files or directories. Whether you need to create backups, duplicate project files, or replicate entire directories, this function simplifies the process. It allows you to specify both the source and destination paths, ensuring a precise and controlled copying operation.

### **_Usage_**

1. Open the terminal and type:

```bash
tt --files copy [ARGS]
# or
tt -fm copy [ARGS]
```

### \***\*Arguments\*\***

- **--SOURCE (Required)**

**_Example:_**

```bash
tt --fm copy --SOURCE C:\\Users\\MyUser\\ProjectName\\sqlite.db
```

- **--DEST (Required)**

**_Example:_**

```bash
tt --fm copy --SOURCE C:\\Users\\MyUser\\ProjectName --DEST C:\\Users\\MyUser\\Backups\\ProjectName
```
