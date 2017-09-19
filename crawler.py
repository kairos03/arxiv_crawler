import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_papers():
    req = requests.get('https://arxiv.org/list/cs.AI/recent?show=50')

    soup = BeautifulSoup(req.text, 'html.parser')

    date = soup.select('h3')[0].text

    dlpage = soup.select('#dlpage > dl')[0]

    paper_list = []

    # crawl pdf link
    dt = dlpage.select('dt')
    pdf_links = []
    for link in dt:
        pdf_links.append(link.select('a')[2].get('href'))

    # crawl detail
    dd_list = dlpage.select('dd')
    for dd in dd_list:
        div = dd.select('div')
        title = div[1].text.replace('\n', '').replace('  ', ' ')[7:]
        author = div[2].text.replace('\n', '')[8:]
        subject = div[-1].text.replace('\n', '')[10:]

        paper_detail = {
            'title': title,
            'author': author,
            'subject': subject
        }

        paper_list.append(paper_detail)

    # add pdf link to paper_detail
    for i in range(len(pdf_links)):
        paper_list[i]['pdf'] = pdf_links[i]

    date = datetime.strptime(date, "%a, %d %b %Y")
    date = date.strftime("%Y-%m-%d")

    papers = {'date': date, 'paper_list': paper_list}

    return papers
