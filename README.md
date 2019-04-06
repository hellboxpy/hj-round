# HJ Round

This project is a demonstration of how hellbox builds font files.

To try this project:
1. Clone this repository
2. Install the `hell` CLI
3. Install `pipenv`
3. Run `hell install` and `hell` run

## Dependencies

A number of external dependencies are currently required. To get the with Homebrew, run the following commands:

```shell
brew tap bramstein/webfonttools
brew install sfnt2woff-zopfli
brew install woff2
brew install ttfautohint
```

Eventually these should be bundled with their respective chutes to the extent possible.