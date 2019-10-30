import csv
from requests import get
from bs4 import BeautifulSoup

def csv_save():
    finalfilename = f"output-{str(timestamp_name())}.csv"
    with open(finalfilename, 'w+', newline='', encoding="utf-8") as csvFile:
        headwriter = csv.DictWriter(csvFile, fieldnames=["File Name", "", "URL", "Programming Language",
                                                         "Last Updated"])
        headwriter.writeheader()
        writer = csv.writer(csvFile, delimiter=",")
        writer.writerow()

def recursive_dir(table_row):
    list = []
    if table_row.find('a').endswith('/'):
        url = get("http://mirror.rise.ph/centos/7/"+table_row.text.split(" "))
        soup = BeautifulSoup(url.text, 'html.parser')
        table = soup.find_all('tr')
        for file in table[3:]:
            list.append(recursive_dir(file))
    else:
        url = get("http://mirror.rise.ph/centos/7/" + table_row.text.split(" "))
        soup = BeautifulSoup(url.text, 'html.parser')
        filename = soup.find('a', href=True)
        list.append(filename)
    print(list)
    return list

def main():
    base_url = "http://mirror.rise.ph/centos/7/"
    r = get(base_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    files = soup.find_all('tr')
    list = []
    for file in files[3:]:
        list.append(file)
        recursive_dir(file)
if __name__ == '__main__':
    main()