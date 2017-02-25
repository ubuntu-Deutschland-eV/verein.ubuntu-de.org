# Local Development

Clone the git-Repository via

    $ git clone git@github.com:ubuntu-Deutschland-eV/verein.ubuntu-de.org.git

Furthermore install `python-virtualenv`, if you use Ubuntu via

    $ sudo apt install python-virtualenv

To install all dependencies, run

    $ make install

All articles, written in Markdown, lie in `content`. News can be placed directly in there,
more articles are in the `pages` subfolder.

To test locally, you can run

    $ make devserver

You can visit the site in your browser at `http://127.0.0.1:8000`. If you change
something of the content or the theme, the site should be rebuild in the background
automatically. Otherwise you can run the above command a second time to
restart the development server. To stop the development server run

    $ make stopserver

# Deployment

Build the HTML from the Markdown-files lying in `content`

    $ make publish

Everything in `output` can be put to the webserver.

# Theme

**You only have to build the CSS if you made any changes.**

We use the „Ubuntu vanilla theme for Vanilla framework“ by Canonical Ltd.
See https://github.com/ubuntudesign/ubuntu-vanilla-theme
It's licensed under LGPLv3.

Furthermore, commit the changes directly into
https://github.com/ubuntu-Deutschland-eV/ubuntu-vanilla-theme and
update just the submodle-reference in this repository.

To build the CSS run

    npm install
    gulp build

inside `themes/verein/vendor/ubuntu-vanilla-theme`. If you don't want
to install ruby's gem system-wide, you have to install `ruby` and `scss-lint`
(latter via `gem install scss-lint`) manually. Moreover, you have to add the
location of the gem-binaries to the `PATH` manually, f.e.:

    PATH=$HOME/.gem/ruby/2.3.0/bin:$PATH gulp build
