import requests
from bs4 import BeautifulSoup
from datetime import datetime

# 0 is today, 1 is yesterday, ...
crawle_date = 0


def get_papers():
    # if crawle_date is big (bigger then 4 or 5) increase 'show' parameter value
    paper_list = []
    date = None

    # subject list: AI, Learning, Computer Vision, Neural and Evolutionary Computing, Machine Learning
    class_list = ['cs.AI', 'cs.LG', 'cs.CV', 'cs.NE', 'stat.ML']

    for cls in class_list:
        # make url
        url = 'https://arxiv.org/list/%s/recent?show=100' % (cls)

        # request url
        req = requests.get(url)

        # parse
        soup = BeautifulSoup(req.text, 'html.parser')
        date = soup.select('h3')[crawle_date].text
        dlpage = soup.select('#dlpage > dl')[crawle_date]

        # crawl pdf link
        dt = dlpage.select('dt')
        pdf_links = []
        for link in dt:
            pdf_links.append(link.select('a')[2].get('href'))

        # crawl detail
        dd_list = dlpage.select('dd')
        detail_list=[]
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
            detail_list.append(paper_detail)

        # add pdf link to paper_detail
        for i in range(len(pdf_links)):
            detail_list[i]['pdf'] = pdf_links[i]

        paper_list.append({
            'class': cls,
            'papers': detail_list})

    date = datetime.strptime(date, "%a, %d %b %Y")
    date = date.strftime("%Y-%m-%d")

    paper_bunch = {'date': date, 'paper_list': paper_list}

    return paper_bunch
