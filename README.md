# Google Layoff Prediction WIP
## Meta layoff scraper
Linkedin provides one page showing all the searching results for #layoff. I just scrape all the related result possible and re through the results using `https://www.linkedin.com/in.+?"`, and `<div class="feed-shared-inline-show-more-text feed-shared-update-v2__description feed-shared-inline-show-more-text--minimal-padding" tabindex="-1">.+?</div>` and store into person.csv, I made the alignment for one person corresponding with one layoff_thesis.

```csv
person, layoff_thesis
https://www.linkedin.com/in.+?, xxx
```

### Run scrape person
Read from person.csv and use linkedin_scaper python api to scrape every person from the list and append basic information, and I will remove all the meta unrelated id.

## Google/ Amazon layoff prediction
Since we know how much money last finantial year meta is losing, we can predict how much people, which people at which level doing what will be affected in Google/Amazon layoff.