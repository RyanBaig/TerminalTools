---
title: 3. Display Database
---

# 3. Display Database

### **_Description_**

The "Display Database" function provides a convenient way to retrieve and visualize data stored within a specific table in an SQLite database. It simplifies data access and presentation, making it easier to explore and analyze the information contained in your databases. Whether you're working on data analysis, reporting, or database management, this function streamlines the process of fetching and displaying data from your SQLite databases.

### **_Usage_**

1. Open the terminal and type:

```bash
tt --db displaydb [ARGS]
# or
tt -dbm displaydb [ARGS]
```

### **_Arguments_**

- **--DBPATH (Required)**

**_Example:_**

```bash
tt --db displaydb --DBPATH C:\\Users\\MyUser\\ProjectName\\sqlite.db
```

- **--TABLENAME (Required)**

**_Example:_**

```bash
tt --db displaydb --TABLENAME MyTable --DBPATH C:\\Users\\MyUser\\ProjectName\\sqlite.db
```
