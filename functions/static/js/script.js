// THE PART WHICH ASSIGNS ICONS
$(document).ready(function () {
  // Define a mapping of file extensions to icons
  var fileIconMapping = {
    bat: "console.svg",
    c: "c.svg",
    cc: "cpp.svg",
    cer: "certificate.svg",
    cpp: "cpp.svg",
    css: "css.svg",
    db: "database.svg",
    docx: "word.svg",
    exe: "exe.svg",
    file: "file.svg",
    gitattributes: "git.svg",
    gitignore: "git.svg",
    h: "h.svg",
    html: "html.svg",
    ico: "image.svg",
    ini: "settings.svg",
    iso: "disc.svg",
    java: "java.svg",
    jinja: "jinja.svg",
    jpeg: "image.svg",
    jpg: "image.svg",
    js: "javascript.svg",
    json: "json.svg",
    key: "key.svg",
    less: "less.svg",
    license: "certificate.svg",
    md: "markdown.svg",
    mp3: "audio.svg",
    mp4: "video.svg",
    otf: "font.svg",
    pdf: "pdf.svg",
    php: "php.svg",
    png: "image.svg",
    prettierc: "prettier.svg",
    py: "python.svg",
    scss: "sass.svg",
    sh: "console.svg",
    sql: "database.svg",
    svg: "svg.svg",
    ts: "typescript.svg",
    ttf: "font.svg",
    txt: "document.svg",
    webp: "image.svg",
    xls: "excel.svg",
    xlsx: "excel.svg",
    xml: "xml.svg",
    yaml: "yaml.svg",
    yml: "yaml.svg",
    zip: "zip.svg",
  };

  var folderIconMapping = {
    folder: "folder.svg", // Default folder icon
    venv: "folder-venv.svg",
    android: "folder-android.svg",
    ".vscode": "folder-vscode.svg",
    android: "folder-android.svg",
    api: "folder-api.svg",
    config: "folder-config.svg",
    container: "folder-container.svg",
    css: "folder-css.svg",
    database: "folder-database.svg",
    debug: "folder-debug.svg",
    dist: "folder-dist.svg",
    docker: "folder-docker.svg",
    docs: "folder-docs.svg",
    extension: "folder-plugin.svg",
    extensions: "folder-plugin.svg",
    firebase: "folder-firebase.svg",
    folder: "folder.svg",
    functions: "folder-functions.svg",
    git: "folder-git.svg",
    github: "folder-github.svg",
    gitlab: "folder-gitlab.svg",
    "go back": "folder-ci.svg",
    helper: "folder-helper.svg",
    home: "folder-home.svg",
    icons: "folder-images.svg",
    images: "folder-images.svg",
    include: "folder-include.svg",
    ios: "folder-ios.svg",
    java: "folder-java.svg",
    javascript: "folder-javascript.svg",
    jinja: "folder-jinja.svg",
    job: "folder-job.svg",
    js: "folder-javascript.svg",
    json: "folder-json.svg",
    lib: "folder-lib.svg",
    log: "folder-log.svg",
    markdown: "folder-markdown.svg",
    middleware: "folder-middleware.svg",
    netlify: "folder-netlify.svg",
    nextjs: "folder-nextjs.svg",
    node: "folder-node.svg",
    nuxt: "folder-nuxt.svg",
    other: "folder-other.svg",
    packages: "folder-packages.svg",
    pdf: "folder-pdf.svg",
    php: "folder-php.svg",
    pipe: "folder-pipe.svg",
    plugin: "folder-plugin.svg",
    project: "folder-project.svg",
    projects: "folder-project.svg",
    public: "folder-public.svg",
    python: "folder-python.svg",
    queue: "folder-queue.svg",
    routes: "folder-routes.svg",
    rules: "folder-rules.svg",
    sass: "folder-sass.svg",
    scripts: "folder-scripts.svg",
    server: "folder-server.svg",
    serverless: "folder-serverless.svg",
    sqlite: "folder-database.svg",
    src: "folder-src.svg",
    static: "folder-static.svg",
    storybook: "folder-storybook.svg",
    stylus: "folder-stylus.svg",
    sublime: "folder-sublime.svg",
    supabase: "folder-supabase.svg",
    svelte: "folder-svelte.svg",
    svg: "folder-svg.svg",
    tasks: "folder-tasks.svg",
    template: "folder-template.svg",
    templates: "folder-template.svg",
    test: "folder-test.svg",
    theme: "folder-theme.svg",
    tools: "folder-tools.svg",
    typescript: "folder-typescript.svg",
    unity: "folder-unity.svg",
    utils: "folder-utils.svg",
    venv: "folder-venv.svg",
    vercel: "folder-vercel.svg",
    video: "folder-video.svg",
    videos: "folder-video.svg",
    views: "folder-views.svg",
    wakatime: "folder-wakatime.svg",
    windows: "folder-windows.svg",
    wordpress: "folder-wordpress.svg",
    yarn: "folder-yarn.svg",
    __pycache__: "folder-python.svg",
    ".git": "folder-git.svg",
  };

  // Add the additional keys
  var additionalKeys = [
    "changelog",
    "readme",
    "README",
    "npm",
    "config",
    "git",
  ];

  // Map the additional keys to their respective icons
  additionalKeys.forEach(function (key) {
    fileIconMapping[key] = key + ".svg";
  });
  fileIconMapping["readme"] = "readme" + ".svg";

  // Add icons to each file
  $("#files li").each(function () {
    var isDirectory = $(this).find(".icon").hasClass("folder");
    var isFile = $(this).find(".icon").hasClass("file");
    var fileNameElement = $(this).find(".name");
    var fileName = fileNameElement.text().trim();

    // Determine the icon based on whether it's a directory or a file
    var icon;

    // Make it so if the file name is README.md or readme, it uses readme.svg icon
    switch (true) {
      case fileName.toLowerCase() === "readme.md" ||
        fileName.toLowerCase() === "readme":
        icon = fileIconMapping["readme"];
        break;
      case fileName.toLowerCase() === "changelog.md" ||
        fileName.toLowerCase() === "changelog":
        icon = fileIconMapping["changelog"];
        break;
      case fileName.toLowerCase() === "license.md" ||
        fileName.toLowerCase() === "license":
        icon = fileIconMapping["license"];
        break;
      case isDirectory:
        icon =
          folderIconMapping[fileName.toLowerCase()] ||
          folderIconMapping["folder"];
        break;
      case isFile:
        var fileExtension = fileName.split(".").pop();
        icon = fileIconMapping[fileExtension] || fileIconMapping["file"];
        break;
      default:
        // Handle cases where neither "folder" nor "file" class is present
        icon = folderIconMapping["folder"];
        break;
    }


    // Set the background image dynamically
    var iconUrl = "http://localhost:5000/static/icons/" + icon;
    fileNameElement.css("background-image", 'url("' + iconUrl + '")');
  });
});

// SEARCH PART
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

/*
 *                 FOLDER ICONS
 *               ----------------
 * Android: For Android specific development files ()
 * API: For API related files()
 * Config: For configuration files()
 * Container: For containerization related files()
 * CSS: For CSS files()
 * Database: For database files or configuration1
 * Debug: For debugging tools or files2
 * Dist: For distribution files2
 * Docker: For Docker related files2
 * Docs: For documentation files
 * Firebase: For Firebase specific files2
 * Functions: For serverless functions2
 * Git: For Git repository files
 * GitHub: For GitHub related files
 * GitLab: For GitLab related files2
 * Helper: For helper scripts or functions
 * Home: For project root directory2
 * Images: For image files2
 * Include: For included files or libraries2
 * iOS: For iOS specific development files2
 * Java: For Java files2
 * JavaScript: For JavaScript files
 * Jinja: For Jinja templates2
 * Job: For job or task related files
 * Lib: For libraries or dependencies
 * Log: For log files2
 * Markdown: For markdown files
 * Middleware: For middleware related files
 * Netlify: For Netlify specific files
 * Next(nextjs): For Next.js framework files
 * Node: For Node.js files
 * Nuxt: For Nuxt.js framework files11
 * Other: For miscellaneous files11
 * Packages: For package management related files11
 * PDF: For PDF files
 * PHP: For PHP files
 * Pipe: For data processing pipelines
 * Plugin: For plugins or extensions11
 * Project: For project root directory
 * Public: For publicly accessible files
 * Python: For Python files
 * Queue: For message queue related files
 * Routes: For routing configuration files
 * Sass: For Sass files
 * Scripts: For custom scripts
 * Rules: For configuration rules222
 * Server: For server-side code1
 * Serverless: For serverless functions1111
 * Src: For source code
 * Storybook: For UI component development with Storybook11
 * Stylus: For Stylus files
 * Sublime: For Sublime Text specific files
 * Supabase: For Supabase backend platform related files
 * Svelte: For Svelte framework files
 * SVG: For SVG files1111
 * Tasks: For task management related files
 * Template: For templates or boilerplate code
 * Test: For test files222
 * Theme: For UI theme files
 * Tools: For developer tools or scripts
 * TypeScript: For TypeScript files22222
 * Unity: For Unity game engine related files
 * Utils: For utility functions or libraries
 * Vercel: For Vercel deployment platform related files
 * Video: For video files
 * Views: For UI templates or components
 * VSCode: For VS Code specific files222
 * Wakatime: For time tracking with Wakatime
 * Windows: For Windows specific files
 * WordPress: For WordPress platform related files
 * Yarn: For Yarn package management related files222
 */