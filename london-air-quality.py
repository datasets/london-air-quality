import datetime

from dataflows import PackageWrapper, ResourceWrapper, Flow, load, dump_to_path


def date_formatter(date):
    if str(date).split('-')[0].isdigit():
        return str(date).split(' ')[0]
    elif len(str(date).split('-')[0]) == 4:
        return datetime.datetime.strptime(str(date), '%B-%Y').strftime('%Y-%m') + '-01'
    else:
        return datetime.datetime.strptime(str(date), '%b-%Y').strftime('%Y-%m') + '-01'


def tweak_row(row):
    for key, value in row.items():
        row[key] = str(value)
        if str(value) == '':
            row[key] = None
        if 'Month' in key:
            row[key] = date_formatter(value)
        if value == '.':
            row[key] = None


def set_format_and_name_air_quality(package: PackageWrapper):

    package.pkg.descriptor['title'] = 'Air quality'
    package.pkg.descriptor['name'] = 'air-quality'

    package.pkg.descriptor['licenses'] = [{
        "name": "OGL",
        "path": 'http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/',
        "title": 'Open Government Licence'
    }]

    package.pkg.descriptor['resources'][0]['path'] = 'data/monthly-averages.csv'
    package.pkg.descriptor['resources'][0]['name'] = 'monthly-averages'

    package.pkg.descriptor['resources'][1]['path'] = 'data/time-of-day-per-month.csv'
    package.pkg.descriptor['resources'][1]['name'] = 'time-of-day-per-month'

    yield package.pkg
    res_iter = iter(package)
    first: ResourceWrapper = next(res_iter)
    second: ResourceWrapper = next(res_iter)
    yield first.it
    yield second.it
    yield from package


link = 'https://data.london.gov.uk/download/london-average-air-quality-levels/acce7f88-70f0-4fd0-9160-f02a9d96b2c3/' \
       'air-quality-london.xls'

Flow(
    load(link,
         format="xls",
         headers=[1, 2],
         fill_merged_cells=True,
         sheet=3),
    load(link,
         format="xls",
         headers=[1, 2],
         fill_merged_cells=True,
         sheet=4),
    tweak_row,
    set_format_and_name_air_quality,
    dump_to_path(),
).process()
