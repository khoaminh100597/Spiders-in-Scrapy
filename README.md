# Spiders-in-Scrapy

This repo is used for an example of using spiders in Scrapy

## To do

To put our spider to work, go to the project’s top level directory and run:

`scrapy crawl 'name_of_your_spider'`

Example: scrapy crawl  examplespider1

## Storing the scraped data

The simplest way to store the scraped data is by using Feed exports, with the following command:

`scrapy crawl quotes -o quotes.json`

That will generate an quotes.json file containing all scraped items, serialized in JSON.

Example: scrapy crawl examplespider1 -o open data.json
