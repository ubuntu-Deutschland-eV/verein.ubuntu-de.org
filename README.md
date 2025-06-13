![](https://github.com/ubuntu-Deutschland-eV/verein.ubuntu-de.org/workflows/Build%20HTML%20of%20site/badge.svg?branch=master)

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
automatically.

# Deployment

Build the HTML from the Markdown-files lying in `content`

    $ make publish

Everything in `output` can be put to the webserver.

After every push to github, github actions will automatically build a new
ZIP-archive with the contents of the output directory. The archive can be
found at <https://github.com/ubuntu-Deutschland-eV/verein.ubuntu-de.org/actions?query=workflow%3A%22Build+HTML+of+site%22>.

# Theme

**You only have to build the CSS if you made any changes.**

As theme we use a slightly modified version of „Ubuntu vanilla theme for Vanilla framework“ by Canonical Ltd.
The framework was located at <https://github.com/ubuntudesign/ubuntu-vanilla-theme>.
It's licensed under LGPLv3.

Customizations are made in <https://github.com/ubuntu-Deutschland-eV/ubuntu-vanilla-theme>.

To build the CSS run

    npm install
    gulp build

inside `themes/verein/vendor/ubuntu-vanilla-theme`. If you don't want
to install ruby's gem system-wide, you have to install `ruby` and `scss-lint`
(latter via `gem install scss-lint`) manually. Moreover, you have to add the
location of the gem-binaries to the `PATH` manually, f.e.:

    PATH=$HOME/.gem/ruby/2.3.0/bin:$PATH gulp build

Afterwards, update the subtree in this repository:

If the theme repo is not added as remote locally, add it via

	$ git remote add -f ubuntu-vanilla-theme https://github.com/ubuntu-Deutschland-eV/ubuntu-vanilla-theme.git

Then add the changes to this repository:

	$ git fetch ubuntu-vanilla-theme customizations
	$ git subtree pull --prefix themes/verein/vendor/ubuntu-vanilla-theme ubuntu-vanilla-theme customizations --squash
