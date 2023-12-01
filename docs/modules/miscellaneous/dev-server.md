---
title: 2. Dev Server
---

# Dev Server

### **_Description_**

Open a local development server on http://localhost:8080 for previewing your website/project. Super Useful for Frontend Development.

### **_Usage_**

1. Open the terminal and type:

```bash
tt --misc devserver [ARGS]
# or
tt -m devserver [ARGS]
```

### **_Aliases_**

- `tt -m devserver`
- `tt -m dev`
- `tt --misc devserver`
- `tt --misc dev`

### ****Arguments****

- **--CMD (Required)**

**_Example:_**

```bash
tt -m dev --CMD start
# or
tt -m dev --CMD stop
```

P.S: I am currently working for some mechanism so it automatically refreshes if some change is detected in the files in the user's CWD (Curent Working Directory).
