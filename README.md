# HJ Round

This project is a demonstration of how hellbox builds font files.

To try this project:
1. Clone this repository
2. Install the [`hell`](https://github.com/hellboxpy/hell) CLI
3. Install [`pipenv`](https://pipenv.readthedocs.io/en/latest/#install-pipenv-today)
4. Run `hell install` to get the python dependencies
5. Run `hell run` to build the font files

## Dependencies

A number of external dependencies are currently required. To get the with Homebrew, run the following commands:

```shell
brew tap bramstein/webfonttools
brew install sfnt2woff-zopfli
brew install woff2
brew install ttfautohint
```

Eventually these should be bundled with their respective chutes to the extent possible.