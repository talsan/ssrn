import requests
import random
import config
from lxml import html

jel_code_base_url = 'https://papers.ssrn.com/sol3/JELJOUR_Results.cfm'
jel_codes = [f'G{str(c).zfill(2)}' for c in range(0, 40)]

for jc in jel_codes:
    page_num = 1
    total_pages = 1e10
    while (page_num <= total_pages):
        response = requests.get(url=jel_code_base_url,
                                params={'npage': page_num, 'form_name': 'Jel', 'code': jc},
                                headers={'User-Agent': random.choice(config.USER_AGENT_LIST)}
                                )
        doc = html.fromstring(response.text)

        if page_num == 1:
            total_pages = int(doc.xpath('//div[@class="pagination"]//li[@class="total"]')[0].text)
            print(f'jel_code={jc} | {total_pages} total pages')

        papers = doc.xpath('//div[@class="table results papers-list"]/div[@class="tbody"]/div[contains(@class,"trow")]')
        print(f'jel_code={jc} | page={page_num} | {len(papers)} papers')

        for p in papers:
            desc = p.xpath('./div[@class="description"]')[0]

            title = desc.xpath('./h3/span/a')[0].text.strip()
            url = desc.xpath('./h3/span/a/@href')[0]
            afiliations = desc.xpath('./div[@class="afiliations"]')[0].text.strip()
            notes_list = [n.text for n in desc.xpath('./div[@class="note note-list"]//span')]
            authors_list = [{'author_name':a.text.strip(), 'author_url': a.xpath('./@href')[0]}
                            for a in desc.xpath('./div[@class="authors-list"]//a')]
            downloads = int(p.xpath('./div[@class="downloads"]/span')[1].text.replace(',',''))




