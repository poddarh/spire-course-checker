# spire-course-checker
SPIRE Course Checker for UMass Amherst

To make this work, first go to SPIRE and add the courses you want to be able to track with this to your shopping cart.

## Requirements:
 * python3
 * [selenium](http://seleniumhq.org/) `>=3.5` (can be installed using `pip`)
 * [geckodriver](https://github.com/mozilla/geckodriver/releases/latest)
 * [Firefox](https://ftp.mozilla.org/pub/firefox/releases/53.0.2/) `<=53` (Note that Firefox 54 or above might not work due to compatibility issues).

**Note:** You may be able to make it work with other browsers, but I haven't tested it with anything else. Lookup selenium documentation to see how to switch browsers.

## Usage:
```bash
$ python3 spire-checker.py <username> <password> <courses list...>
```

#### Example:
```bash
$ python3 spire-checker.py hpoddar password 'COMPSCI 326' '233-01'
```

**Note:** Currently this will only print the class name in the console. This has a function called `when_open` that you can edit to make it do whatever you'd like.
