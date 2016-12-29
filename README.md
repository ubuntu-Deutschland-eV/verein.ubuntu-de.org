# How to install pelican

Build and activate an virtualenv

    …/verein.ubuntu-de.org $ virtualenv3 virtualenv
    source virtualenv/bin/activate

Install all the dependencies via

    $ pip install -r requirments.txt

Build the HTML (to `output`) from the Markdown-files lying in `content`

    $ make publish

Everything in `output` can be put to the webserver.

If you just want to test locally, you can run (after activating the
virtualenv)

    $ make devserver

Thus, relative paths will be used. You can visit the site in your
browser at `http://127.0.0.1:8000`. If you change something of the
content or the theme, the site should be rebuild in the background
automatically. Otherwise you can run the above command a second time to
restart the development server. To stop the development server run

    $ make stopserver

# Theme

We use the „Ubuntu vanilla theme for Vanilla framework“ by Canonical Ltd.
See https://github.com/ubuntudesign/ubuntu-vanilla-theme
It's licensed under LGPLv3.

To build the CSS run

    npm install
    gulp build

inside `themes/verein/vendor/ubuntu-vanilla-theme`. If you don't want
to install ruby's gem system-wide, you have to install `ruby` and `scss-lint`
(latter via `gem install scss-lint`) manually. Moreover, you have to add the
location of the gem-binaries to the `PATH` manually, f.e.:

    PATH=$HOME/.gem/ruby/2.3.0/bin:$PATH gulp build

# TODO

 * equal width on desktop, even with small content
