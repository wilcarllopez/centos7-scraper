import csv
import time
from requests import get
from bs4 import BeautifulSoup

def csv_save(filename, filepath, size):
    pass


def timestamp_name():
    """Updates the time and date for the csv filename"""
    timestr = time.strftime("%Y-%m-%d-%H-%M")
    return timestr

def recursive_dir(table_row, past):
    """Recursion function to search files and directories, and save it to a csv file"""
    list = []
    test = table_row.text.split(" ", 1)[0]

    if test.endswith('/'):
        url = get(past + test)
        past += test
        soup = BeautifulSoup(url.text, 'html.parser')
        table = soup.find_all('tr')
        for file in table[3:-1]:
            list.append(recursive_dir(file, past))
    else:
        finalfilename = f"output-{str(timestamp_name())}.csv"
        with open(finalfilename, 'w+', newline='', encoding="utf-8") as csvFile:
            headwriter = csv.DictWriter(csvFile, fieldnames=["filename", "download_link ", "filesize"])
            headwriter.writeheader()
            writer = csv.writer(csvFile, delimiter=",")
            split = table_row.text.split(" ", 3)
            soup = BeautifulSoup(past, 'html.parser')
            filename = table_row.a['href']
            filepath = past + str(filename)
            size = split[3]
            row = [filename, filepath, size]
            writer.writerow(row)
    return list

def main():
    """Main function of the program"""
    base_url = "http://mirror.rise.ph/centos/7/"
    r = get(base_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    files = soup.find_all('tr')
    for file in files[3:-1]:
        recursive_dir(file, base_url)

if __name__ == '__main__':
    main()