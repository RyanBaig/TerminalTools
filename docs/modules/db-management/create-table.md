---
title: 4. Create Table
---

# 4. Create Table

### **_Description_**

Creates a new table in an existing database with the specified columns.

### **_Usage_**

1. Open the terminal and type:

```bash
tt --db createtable [ARGS]
# or
tt -dbm createtable [ARGS]
```

### **_Arguments_**

- **--DBPATH (Required)**

**_Example:_**

```bash
tt --db createtable --DBPATH C:\\Users\\MyUser\\ProjectName\\sqlite.db
```

- **--TABLENAME (Required)**

**_Example:_**

```bash
tt --db createtable --TABLENAME MyTable --DBPATH C:\\Users\\MyUser\\ProjectName\\sqlite.db
```

- **--COLUMNS (Required)**

**_Example:_**

```bash
tt --db createtable --COLUMNS 'id(INTEGER PRIMARY_KEY), name(TEXT), age(INTEGER)' --DBPATH C:\\Users\\MyUser\\ProjectName\\sqlite.db --TABLENAME MyTable
```

_(Please make sure there are single quotes (') or double-quotes (") around the column args.)_
