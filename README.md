Sentiment-Personality Insights app on IBM Bluemix using Python, Django, IBM Insights for Twitter service and Watson services. This is a web based application that pulls data from twitter, performs sentiment analysis and derives the personality traits of the people who tweet positively/negatively about a brand.

The data is obtained through the IBM Insights for Twitter service, which also performs sentiment analysis on the tweets. The positive and negative sentiment tweets are then separated and non-English tweets are recognized and translated using Watson Language Identification and Machine Translation services. These tweets are then aggregated and fed into the Personality Insights service.

The personality traits of the positive and negative users can be compared on a chart which can also be drilled down to identify individual facets that make up a personality trait. The app can be used by organizations to determine the differences in personality between people who like/dislike their brand and target their advertising accordingly.

    Download the code from Github.
    Open manifest.yml file and change the application name to a unique host name
    Follow the directions in the related IBM developerWorks article to download, install and configure the necessary dependencies.
    Follow the steps and deploy the application to BlueMix.
    The app uses the following services: IBM Insights for Twitter, Language Translation and Personality Insights

The app video is available at: https://github.com/vmathur87/insights-twitter/files/92842/app_demo.zip
