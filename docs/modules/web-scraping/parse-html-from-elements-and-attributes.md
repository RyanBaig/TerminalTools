---
title: 2. Parse HTML Content and Retrieve Data from Elements/Attributes
---

# 2. Parse HTML Content and Retrieve Data from Elements/Attributes

### **_Description_**

The HTML parsing function in this module enables you to extract specific data from elements and attributes on webpages. You need to provide the URL of the webpage, the target HTML element to search for, and an optional attribute to retrieve specific results. This functionality is valuable for web scraping, data mining, and content extraction.

### **_Usage_**

1. Open the terminal and type:

```bash
tt --webscr parsehtml [ARGS]
# or
tt -web parsehtml [ARGS]
```

### ***Arguments***

- **--URL (Required)**

**_Example:_**

```bash
tt --webscr parsehtml --URL https://quotes.toscrape.com
```

- **--ELEMENT (Required)**

**_Example:_**

```bash
tt --webscr parsehtml --URL https://quotes.toscrape.com --ELEMENT a
```

- **--ATTRIBUTE (Optional)**

**_Example:_**

```bash
tt --webscr parsehtml --URL https://quotes.toscrape.com --ELEMENT a --ATTRIBUTE 'tag'
# The above code means to search the webpage for an <a> element with any attribute with value 'tag'
# it could be 'href' or 'class'.
```