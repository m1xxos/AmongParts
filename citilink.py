import time
import requests
from bs4 import BeautifulSoup
import json


proxies = {
  # 'http': 'http://10.10.1.10:3128',
  'https': 'http://188.170.233.110:3128',
}

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.5.810 Yowser/2.5 Safari/537.3"
}


def get_all_links(base_page):
    page = 1
    links = []
    while True:
        r = requests.get(base_page + "?p=" + str(page))
        if r.status_code == 404:
            break
        soup = BeautifulSoup(r.content, 'html.parser')
        products = soup.findAll("a", {"class": "ProductCardHorizontal__title"})
        for product in products:
            links.append("https://www.citilink.ru" + product['href'])
        page += 1
    with open("links.txt", "w+") as f:
        for prod_link in links:
            f.write(prod_link + '\n')
    # print(len(links))
    return links


def get_product_specs(base_page):
    stats = {}
    r = requests.get(base_page + "properties/")
    soup = BeautifulSoup(r.content, 'html.parser')
    not_available = soup.findAll("div", {"class": "ProductHeader__not-available"})
    product = soup.findAll("div", {"data-params": True, "class": "ProductHeader__button-block js--ButtonBlock"})
    params = json.loads(product[0]["data-params"])

    if not_available:
        stats["availability"] = False
        stats["price"] = 0
    else:
        stats["availability"] = True
        stats["price"] = params["price"]

    stats["name"] = params["shortName"]
    stats["brand"] = params["brandName"]
    stats["links"] = [base_page]
    stats["type"] = "gaming"
    return stats, soup


def get_motherboard_specs(base_page):
    print(base_page)
    stats, soup = get_product_specs(base_page)
    specs = soup.findAll("div", {"class": "Specifications__column Specifications__column_name"})
    for spec in specs:
        usb3 = 0
        usbc = 0
        thunderbolt = 0
        param_name = spec.next_element.text.strip()
        param_value = spec.next_sibling.text.strip()
        match param_name:
            case "Гнездо процессора":
                stats["socket"] = param_value
            case "Форм-фактор":
                stats["form_factor"] = param_value
            case "Чипсет":
                stats["chipset"] = param_value
            case "Слотов памяти DDR5":
                stats["memory_slots"] = int(param_value)
                stats["memory_type"] = "DDR5"
            case "Слотов памяти DDR4":
                stats["memory_slots"] = int(param_value)
                stats["memory_type"] = "DDR4"
            case "Слотов памяти DDR3":
                stats["memory_slots"] = int(param_value)
                stats["memory_type"] = "DDR3"
            case "Поддержка частот оперативной памяти":
                stats["memory_speed"] = param_value
            case "Максимальный объем оперативной памяти":
                stats["memory_maximum"] = param_value
            case "Режим работы оперативной памяти":
                stats["memory_channel"] = param_value
            case "Слотов PCI-E 2.0 x16":
                stats["pci_2"] = int(param_value)
            case "Слотов PCI-E 3.0 x16":
                stats["pci_3"] = int(param_value)
            case "Слотов PCI-E 4.0 x16":
                stats["pci_4"] = int(param_value)
            case "Слотов PCI-E 5.0 x16":
                stats["pci_5"] = int(param_value)
            case "Аудио контроллер":
                stats["audio_chip"] = param_value
            case "Звук":
                stats["audio_channel"] = param_value
            case "Разъемов SATA3":
                stats["sata_amount"] = int(param_value)
            case "Разъемов M.2":
                stats["m_2_amount"] = int(param_value)
            case "Поддержка SATA RAID":
                stats["raid"] = True
            case "Поддержка Intel Optane":
                stats["optane"] = True
            case "Сетевой интерфейс":
                stats["ethernet"] = param_value
            case "Разъем PS/2":
                stats["slot_ps2"] = param_value
            case "Кол-во внешних USB 2.0":
                stats["slot_usb2"] = int(param_value)
            case "Кол-во внешних USB 3.0":
                usb3 += int(param_value)
            case "Кол-во внешних USB 3.1":
                usb3 += int(param_value)
            case "Кол-во внешних USB 3.1 (Type-C)":
                usbc += int(param_value)
            case "Кол-во внешних USB 3.2 (Type-C)":
                usbc += int(param_value)
            case "Разъемов Display Port":
                stats["slot_display_port"] = int(param_value)
            case "Разъемов D-Sub (VGA)":
                stats["slot_vga"] = int(param_value)
            case "Разъемов DVI":
                stats["slot_dvi"] = int(param_value)
            case "Разъемов HDMI":
                stats["slot_hdmi"] = int(param_value)
            case "Разъемов Thunderbolt":
                thunderbolt += int(param_value)
            case "Разъемов Thunderbolt 4":
                thunderbolt += int(param_value)
            case "WiFi в стандартной поставке":
                stats["wi_fi"] = True
            case "Bluetooth в стандартной поставке":
                stats["bluetooth"] = True
            case "Поддержка SLI/CrossFire":
                stats["sli"] = param_value
            case "Питание материнской платы и процессора":
                stats["power"] = param_value
        if usb3:
            stats["slot_usb3"] = usb3
        if usbc:
            stats["slot_usbc"] = usbc
        if thunderbolt:
            stats["slot_thunderbolt"] = thunderbolt
    # print(stats)
    r = requests.post("http://127.0.0.1:8000/motherboard/", json=stats)


if __name__ == "__main__":
    cringe_links = []
    # motherboard_links = get_all_links("https://www.citilink.ru/catalog/materinskie-platy/")
    with open("links.txt") as file:
        motherboard_links = [row.strip() for row in file]
    for link in motherboard_links:
        # try:
        get_motherboard_specs(link)
        # except Exception as e:
        #     print(str(e))
        #     print("не робит")
        #     cringe_links.append(link)
        #     pass
    print(cringe_links)
    # get_motherboard_specs("https://www.citilink.ru/product/materinskaya-plata-gigabyte-b550m-ds3h-soc-am4-amd-b550-4xddr4-matx-ac-1407213/")
