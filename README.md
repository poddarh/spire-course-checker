# spire-course-checker
SPIRE Course Checker for UMass Amherst

## Requirements:
* python3
 * [selenium](http://seleniumhq.org/) `>=3.5` (can be installed using `pip`)
 * [geckodriver](https://github.com/mozilla/geckodriver/releases/latest)
 * [Firefox](https://ftp.mozilla.org/pub/firefox/releases/53.0.2/) `<=53` (Note that Firefox 54 or above might not work due to compatibility issues).

**Note:** You may be able to make it work with other browsers, but I haven't tested it with anything else. Lookup selenium documentation to see how to switch browsers.

## Usage:
To make this work, first go to SPIRE and add the courses you want to be able to track with this to your shopping cart.

```bash
$ python3 spire-checker.py <username> <courses list...>
```
Courses list is a comma seperated list of classes. It is matched against the `Classes` column in the classes table on the shopping cart page.

#### Example:
```bash
$ python3 spire-checker.py hpoddar 'COMPSCI 326' '233-01' '35492'
```

**Note:** Currently this will only print the class name in the console. This has a function called `when_open` that you can edit to make it do whatever you'd like.
