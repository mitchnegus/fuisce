# Fuisce

Database management and testing for SQLAlchemy-based Flask apps.


## Why _Fuisce_?

_Fuisce_, or whiskey in Irish, is probably not going to grant you eternal life... but it may extend the longevity of your SQLAlchemy-based Flask app.
The package is designed to be a lightweight addition to any application, performing some of the database setup operations while coordinating database management for robust test suites.

For example, [the current edition of the Flask documentation](https://flask.palletsprojects.com/en/2.3.x/tutorial/tests/#setup-and-fixtures) suggests creating a temporary SQLite database for each test.
This is perfectly fine for simple applications, but adds substantial overhead (and test time) to applications with many tests, especially those if it is desirable to have that database contain some preloaded information.
Instead, it would be preferable to create and use one temporary database instance for the majority of tests that only require read-access to the database, and then only create additional test databases for the tests that modify the state of the database (e.g., SQLAlchemy transactions).[^mocking]
_Fuisce_ provides the infrastructure to create databases in both of these cases: a "persistent" database for read-only tests, and "ephemeral" databases for each transaction).
The persistent test database is used by default, but a `transaction_lifetime` decorator can be used to indicate that a given test should use an ephemeral copy.

[^mocking]: Yes, you could also just not create databases and mock the database return functions, but my experience has been that it is even more tedious to maintain a comprehensive set of mocked data to test various intricacies and edge cases while simultaneously ensuring that the mocks behave similarly enough to SQLAlchemy objects.


## Installation

_Fuisce_ is registered on the [Python Package Index (PyPI)](https://pypi.org/project/fuisce) for easy installation.
To install the package, simply run

```
pip install fuisce
```

The package requires a recent version of Python (3.9+).


## Usage

For an up-to-date API reference, build and read the docs:

```bash
make docs
# open `docs/build/html/index.html` in your browser
```

More details on using the _Fuisce_ package are forthcoming...


## License

This project is licensed under the GNU General Public License, Version 3.
It is fully open-source, and while you are more than welcome to fork, add, modify, etc. it is required that you keep any distributed changes and additions open-source.


## Changes

Changes between versions are tracked in the [changelog](CHANGELOG.md).
