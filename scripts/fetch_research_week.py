#!/usr/bin/env python3
"""Fetch PubMed candidates for editorial review; never invent summaries or publish."""
import argparse
import datetime as dt
import json
from pathlib import Path
import subprocess
import time
import urllib.parse
import xml.etree.ElementTree as ET


def fetch(endpoint, params):
    url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/' + endpoint
    url += '?' + urllib.parse.urlencode(params)
    return subprocess.check_output(['curl', '-fsSL', '--retry', '3', '--max-time', '90', url])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--end', help='Inclusive ISO end date; defaults to yesterday in Asia/Shanghai')
    parser.add_argument('--output', required=True, type=Path, help='Evidence directory outside the public site')
    args = parser.parse_args()
    today = dt.datetime.now(dt.timezone(dt.timedelta(hours=8))).date()
    end = dt.date.fromisoformat(args.end) if args.end else today - dt.timedelta(days=1)
    start = end - dt.timedelta(days=6)
    query = Path(__file__).with_name('research-query.txt').read_text().strip()
    term = query + ' AND ("' + start.strftime('%Y/%m/%d') + '"[Date - Publication] : "' + end.strftime('%Y/%m/%d') + '"[Date - Publication])'
    args.output.mkdir(parents=True, exist_ok=True)
    raw = fetch('esearch.fcgi', {'db': 'pubmed', 'term': term, 'retmode': 'json', 'retmax': 9999, 'sort': 'pub_date'})
    result = json.loads(raw)['esearchresult']
    (args.output / 'search.json').write_bytes(raw)
    if result.get('errorlist') or result.get('ERROR'):
        raise RuntimeError('PubMed query error: ' + str(result))
    ids = result['idlist']
    if int(result['count']) != len(ids):
        raise RuntimeError('Incomplete result set; stop rather than publish partial results')
    articles = []
    for offset in range(0, len(ids), 100):
        time.sleep(0.4)
        xml = fetch('efetch.fcgi', {'db': 'pubmed', 'id': ','.join(ids[offset:offset+100]), 'retmode': 'xml'})
        (args.output / ('articles-' + str(offset) + '.xml')).write_bytes(xml)
        for item in ET.fromstring(xml).findall('./PubmedArticle'):
            article = item.find('./MedlineCitation/Article')
            electronic = article.find('ArticleDate[@DateType="Electronic"]')
            online = None
            if electronic is not None:
                online = '-'.join(electronic.findtext(k) for k in ['Year', 'Month', 'Day'])
            articles.append({
                'pmid': item.findtext('./MedlineCitation/PMID'),
                'title': ''.join(article.find('ArticleTitle').itertext()),
                'journal': article.findtext('./Journal/Title'),
                'doi': item.findtext('./PubmedData/ArticleIdList/ArticleId[@IdType="doi"]'),
                'online_date': online,
                'online_in_window': start.isoformat() <= online <= end.isoformat() if online else None,
                'publication_date': dict((x.tag, x.text) for x in article.find('./Journal/JournalIssue/PubDate')),
                'abstract': '\n'.join(''.join(x.itertext()) for x in article.findall('./Abstract/AbstractText')),
                'types': [x.text for x in article.findall('./PublicationTypeList/PublicationType')],
                'authors': [' '.join(filter(None, [x.findtext('LastName'), x.findtext('Initials')])) or x.findtext('CollectiveName', '') for x in article.findall('./AuthorList/Author')]
            })
    if {a['pmid'] for a in articles} != set(ids):
        raise RuntimeError('Missing or unsupported records; manual review required')
    output = {'start': start.isoformat(), 'end': end.isoformat(), 'retrieved': today.isoformat(), 'query': term, 'count': len(articles), 'articles': articles}
    (args.output / 'candidates.json').write_text(json.dumps(output, ensure_ascii=False, indent=2))
    print('Saved', len(articles), 'records for', start, 'through', end, 'to', args.output)


if __name__ == '__main__':
    main()
