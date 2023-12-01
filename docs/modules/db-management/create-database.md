---
title: 2. Create Database
---

# 2. Create Database

### **_Description_**

The "Create Database" function is a fundamental tool for managing databases. It allows you to create a new SQLite database and define a table within it with the specified columns. This function simplifies the process of database creation and table setup, enabling effective organization and storage of your data.

### **_Usage_**

1. Open the terminal and type:

```bash
tt --db createdb [ARGS]
# or
tt -dbm createdb [ARGS]
```

### **_Arguments_**

- **--DIRPATH (Required)**

**_Example:_**

```bash
tt --db createdb --DIRPATH C:\\Users\\MyUser\\ProjectName\\sqlite.db
```

- \*_--TABLENAME (Required)_

**_Example:_**

```bash
tt --db createdb --TABLENAME MyTable --DIRPATH C:\\Users\\MyUser\\ProjectName\\sqlite.db
```

- **--COLUMNS (Required)**

**_Example:_**

```bash
tt --db createdb --COLUMNS 'id(INTEGER PRIMARY_KEY), name(TEXT), age(INTEGER)' --DIRPATH C:\\Users\\MyUser\\ProjectName\\sqlite.db --TABLENAME MyTable
```

_(Please make sure there are single quotes (') or double-quotes (") around the column args.)_
