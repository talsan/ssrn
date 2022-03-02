# SSRN Abstract Scraper
Scrapes & Collects SSRN Abstracts

## Process Summary
1. `url_collector.py` - scrape abstract url's for a given JEL code, crawling though *only the first 10 pages*
2. `url_downloader.py` - download the content of each abstract url

## SSRN JEL Codes
https://papers.ssrn.com/sol3/displayjel.cfm

### Example of Log (Printed to Screen)
```
processing G00
-------------------------
requested https://papers.ssrn.com/sol3/JELJOUR_Results.cfm?npage=1&form_name=Jel&code=G00&lim=false
post-request-sleeping for 6 seconds ... 
jel_code=G00 | 50 total pages
jel_code=G00 | page=1 | 50 papers
saved json jel=G00__page=1__date=20220301

requested https://papers.ssrn.com/sol3/JELJOUR_Results.cfm?npage=2&form_name=Jel&code=G00&lim=false
post-request-sleeping for 2 seconds ... 
jel_code=G00 | page=2 | 50 papers
saved json jel=G00__page=2__date=20220301
```
