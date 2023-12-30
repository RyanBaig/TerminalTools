$(document).ready(function () {
  // Define a mapping of file extensions to icons
  var iconMapping = {
    mp3: "audio.svg",
    c: "c.svg",
    cer: "certificate.svg",
    bat: "console.svg",
    exe: "console.svg",
    cpp: "cpp.svg",
    css: "css.svg",
    db: "database.svg",
    disc: "disc.svg",
    docx: "document.svg",
    ttf: "font.svg",
    otf: "font.svg",
    gitignore: "git.svg",
    gitattributes: "git.svg",
    h: "h.svg",
    html: "html.svg",
    png: "image.svg",
    jpg: "image.svg",
    jpeg: "image.svg",
    webp: "image.svg",
    java: "java.svg",
    js: "javascript.svg",
    json: "json.svg",
    key: "key.svg",
    less: "less.svg",
    md: "markdown.svg",
    pdf: "pdf.svg",
    php: "php.svg",
    prettierc: "prettier.svg",
    scss: "sass.svg",
    svg: "svg.svg",
    ts: "typescript.svg",
    mp4: "video.svg",
    xml: "xml.svg",
    yaml: "yaml.svg",
    yml: "yaml.svg",
    zip: "zip.svg",
    xls: "excel.svg",
    xlsx: "excel.svg",
    ini: "settings.svg",
    ico: "image.svg",
    py: "python.svg",
    venv: "venv.svg",
    txt: "document.svg",
  };

  // Add the additional keys
  var additionalKeys = ["changelog", "readme.md", "npm", "config", "git"];

  // Map the additional keys to their respective icons
  additionalKeys.forEach(function (key) {
    iconMapping["changelog"] = "changelog.svg";
    iconMapping["readme.md"] = "readme.svg";
    iconMapping["npm"] = "npm.svg";
    iconMapping["config"] = "settings.svg";
    iconMapping["git"] = "git.svg";
  });

  // Add icons to each file
  $("#files li").each(function () {
    var fileName = $(this).text().trim();

    // Determine the icon based on whether it's a directory or a file
    var icon;
    // what is the thing of "but" in avascript? ans: a ternary operator
    // make it so if the filename doesnt have . but the filename is LICENSE then the icon is file.svg but if the filename doesnt have . and the filename isnt LICENSE then the folder.svg is the icon
    icon =
      iconMapping[fileName.split(".").pop()] ||
      (fileName === "LICENSE"
        ? "file.svg"
        : fileName.includes(".") && !iconMapping[fileName.split(".").pop()]
        ? "file.svg"
        : "folder.svg");

    // Set the background image dynamically
    var iconUrl = "http://localhost:5000/static/icons/" + icon;
    $(this)
      .find(".name")
      .css("background-image", 'url("' + iconUrl + '")');
  });
});

$(document).ready(function () {
  $("#search").on("input", function () {
    var searchTerm = $(this).val().toLowerCase();
    $("#files li").each(function () {
      var text = $(this).text().toLowerCase();
      var match = text.includes(searchTerm);
      $(this).toggle(match);
    });
  });
});
