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
  };

  // Add the additional keys
  var additionalKeys = ["changelog", "readme.md", "npm", "config"];

  // Map the additional keys to their respective icons
  additionalKeys.forEach(function (key) {
    iconMapping["changelog"] = "changelog.svg";
    iconMapping["readme.md"] = "readme.svg";
    iconMapping["npm"] = "npm.svg";
    iconMapping["config"] = "settings.svg";
  });

  // Add icons to each file
  $("#files li").each(function () {
    var fileName = $(this).text().trim();
    var isDirectory = $(this).data("is-dir");

    // Determine the icon based on whether it's a directory or a file
    var icon;
    if (!fileName.includes(".")) {
      // If the file name doesn't contain a dot (.), assume it's a directory
      icon = "folder.svg";
    } else {
      var fileExtension = fileName.split(".").pop();
      icon = iconMapping[fileExtension] || "file.svg"; // Default to a generic file icon if extension not found
    }

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
