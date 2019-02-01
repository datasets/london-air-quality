This dataset was scraped from [London data](https://data.london.gov.uk/) website.

The data shows roadside and background average readings for Nitric Oxide, Nitrogen Dioxide, Oxides of Nitrogen, Ozone, Particulate Matter (PM10 and PM2.5), and Sulphur Dioxide. Measured in Micrograms per Cubic Meter of Air (ug/m3). The spreadsheet shows which Index level each reading falls in, and contains charts showing pollutant levels by time of day per month.

## Data
Dataset used for this scraping have been found on [London Average Air Quality Levels](https://data.london.gov.uk/dataset/london-average-air-quality-levels).
 
Output data is located in `data` directory, it consists of two `csv` files:
* `monthly-averages.csv`
* `time-of-day-per-month.csv`

## Preparation
You will need Python 3.6 or greater and dataflows library to run the script

To update the data run the process script locally:

```
# Install dataflows
pip install dataflows

# Run the script
python london-air-quality.py
```

### License

Open Government Licence

> You are encouraged to use and re-use the Information that is available under this licence freely and flexibly, with only a few conditions.
Using Information under this licence
>Use of copyright and database right material expressly made available under this licence (the 'Information') indicates your acceptance of the terms and conditions below.
> The Licensor grants you a worldwide, royalty-free, perpetual, non-exclusive licence to use the Information subject to the conditions below.
> This licence does not affect your freedom under fair dealing or fair use or any other copyright or database right exceptions and limitations.

You may find further information [here](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)

