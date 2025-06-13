# Ubuntu vanilla theme for Vanilla framework

A extension of [Vanilla framework](https://github.com/ubuntudesign/vanilla-framework), written in [Sass](http://sass-lang.com/).

## Local usage

Install the Node package into your project:

``` bash
npm install ubuntu-vanilla-theme  # Installs the theme with the framework within
```

Configure Sass import paths.

Composer:

```
add_import_path "node_modules"
```

Gulp:

```javascript
gulp.task('sass', function() {
    return gulp.src('[your-sass-directory]/**/*.scss')
      .pipe(sass({
        includePaths: ['node_modules']
      }))
});
```

Then reference it from your own Sass file that is built to generate your sites CSS:

``` sass
// Import the theme
@import "ubuntu-vanilla-theme/scss/theme";
// Run the theme
@include ubuntu-vanilla-theme;
```

You can override any of the settings in [_global-settings.scss](scss/_global-settings.scss).

## Notes

You may find that after upgrading Node you get an error message like;

` throw new Error('"libsass" bindings not found. Try reinstalling "node-sass"?'); `

This can be resolved by installing then reinstalling node-sass;

```
  npm uninstall --save-dev gulp-sass
  npm install --save-dev gulp-sass@2
```

Code licensed [LGPLv3](http://opensource.org/licenses/lgpl-3.0.html) by [Canonical Ltd.](http://www.canonical.com/).
