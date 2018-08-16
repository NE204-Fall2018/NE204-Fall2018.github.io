# NE204 Static Site Generation with Pelican

## Install pelican

```bash
pip install pelican markdown
```

## Required themes and plugins

The project uses the bootstrap3 theme, and relies on some plugins (such as
i18n\_subsites for language support).
These dependencies can be met by cloning the 
[pelican themes](https://github.com/getpelican/pelican-themes.git) and
[pelican plugins](https://github.com/getpelican/pelican-plugins.git) repos.
By default, pelican searches for these repos in the `$HOME/repos` directory.
This can be changed in the `pelicanconf.py` config.
To get everything working out-of-the-box:

```
cd $HOME/repos
git clone https://github.com/getpelican/pelican-themes.git
git clone --recursive https://github.com/getpelican/pelican-plugins.git
```

## Building/Viewing the Site

The site can be built with `make html`.

To view the site locally after it has been successfully built:

```bash
cd output
python3 -m http.server
```

The site is then accessible at `localhost:8000`
