import requests
import bs4
from urllib.parse import urljoin
import csv
import sys


def main():
    starting_url = sys.argv[1]
    response = requests.get(starting_url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")

    cities = name_and_number_of_city(soup)[0]
    numbers = name_and_number_of_city(soup)[1]

    incomplete_urls = part_of_links(soup)
    complete_urls = urls_of_cities(incomplete_urls)
    elections_data = data(complete_urls)
    candidate_parties = name_of_parties(complete_urls)
    merged_data = list(map(list, zip(cities, numbers, elections_data[0], elections_data[1], elections_data[2])))

    results_of_parties = elections_data[3]
    data_parties_separated = list(zip(*[iter(results_of_parties)] * len(candidate_parties)))
    data_parties_separated_lists = [list(i) for i in data_parties_separated]
    modified_data = complete_data(merged_data, data_parties_separated_lists)

    name_of_file = sys.argv[2]
    title = complete_title(candidate_parties)
    create_file(name_of_file, title, modified_data)


def name_and_number_of_city(soup):
    results = []
    results_1 = []
    for n in range(1, 4):
        numbers = soup.find_all("td", {"headers": f"t{n}sa1 t{n}sb1"})
        names = soup.find_all("td", {"headers": f"t{n}sa1 t{n}sb2"})
        for number in numbers:
            results.append(number.string)
        for name in names:
            results_1.append(name.string)
    return results, results_1


def part_of_links(soup):
    part_of_path = []
    for a_elem in soup.select("td.cislo"):
        if a_elem.find("a"):
            part_of_path.append(a_elem.find("a").get('href'))
        else:
            part_of_path.append("")
    return part_of_path


def urls_of_cities(part_of_path):
    urls = []
    for row in part_of_path:
        href = urljoin("https://volby.cz/pls/ps2017nss/", row)
        urls.append(href)
    return urls


def data(complete_urls):
    data_voters, data_envelopes, data_votes, data_parties = [], [], [], []
    for link in complete_urls:
        response_1 = requests.get(link)
        soup = bs4.BeautifulSoup(response_1.text, "html.parser")
        data_voters.append(soup.find("td", {"headers": "sa2"}).string.replace("\xa0", " "))
        data_envelopes.append(soup.find("td", {"headers": "sa3"}).string.replace("\xa0", " "))
        data_votes.append(soup.find("td", {"headers": "sa6"}).string.replace("\xa0", " "))
        for n in range(1, 3):
            voices = soup.find_all("td", {"headers": f"t{n}sa2 t{n}sb3"})
            for elem in voices:
                if elem.string != "-":
                    data_parties.append(elem.string.replace("\xa0", " "))
    return data_voters, data_envelopes, data_votes, data_parties


def name_of_parties(complete_urls):
    data_parties_names = []
    link = complete_urls[0]
    response = requests.get(link)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    for n in range(1, 3):
        names = soup.find_all("td", {"headers": f"t{n}sa1 t{n}sb2"})
        for elem in names:
            if elem.string != "-":
                data_parties_names.append(elem.string)
    return data_parties_names


def complete_data(merged_data, data_parties_separated_lists):
    for part in merged_data:
        final_data = data_parties_separated_lists.pop(0)
        for elem in final_data:
            part.append(elem)
    return merged_data


def complete_title(candidate_parties):
    title = ["Number of City", "City", "Voters in the list", "Released envelopes", "Valid votes"]
    for party in candidate_parties:
        title.append(party)
    return title


def create_file(name_of_file, title, sorted_data):
    with open(name_of_file, "w+", newline='', encoding="utf-16") as file:
        file_writer = csv.writer(file)
        file_writer.writerow(title)
        file_writer.writerows(sorted_data)

    return file_writer


if __name__ == "__main__":
    print("Sťahujem data z:", sys.argv[1])
    print("Ukládam data do súboru:", sys.argv[2])
    main()
    print("Ukončuji:", sys.argv[0])
    sys.exit(main())
