# centos7-scraper
A python script to scrape all of the filenames, download links and filesizes in all of the inside pages of this page: http://mirror.rise.ph/centos/7/
## Usage
To use the script, must install the PyGithub library.
```python
pip install PyGithub
```
For more info, the code below shows the -h for the script.
```python
usage: github_api.py [-h] [-d] [-a] [search_term] [account_token]

positional arguments:
  search_term       Input to search repository. To search with white space
  account_token     Github username for authentication

optional arguments:
  -h, --help        show this help message and exit
  -d, --descending  Search result to descending order based on stars
  -a, --ascending   Search result to ascending order based on stars

```
## Pytest
To use the test.py from the .\tests folder. User must install pytest.
To use test, type the following:
```
pytest test.py
```
To check the coverage, install pytest-cov then type:
```
pytest --cov=listdir test.py
```
Below shows the coverage
```
Name                                                                     Stmts   Miss  Cover   Missing
------------------------------------------------------------------------------------------------------
C:\Users\TEU_USER\Documents\Python Training\search-github\githubAPI.py      41     31    24%   9-30, 39-40, 44-53                                                       
                                                                            71     24    66%
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

