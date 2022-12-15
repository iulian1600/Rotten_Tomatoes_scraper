chromedriver_LINUX_v_107

    The first line of this file contains the name of the
chromedriver package. Bellow are listed all options:
chromedriver_win32_v_109.exe
chromedriver_mac64_v_109
chromedriver_mac_arm64_v_109

    This is a simple script that saves reviews data
from https://www.rottentomatoes.com. It uses selenium and chromedriver,
so Google Chrome must be installed. The script will iterate through the
links from URL.txt, and will write in a csv file requested data. Only the
first 20 reviews will be processed. If is needed I can make it iterate
through all reviews, and also calculate the number of reviews/reviewer >50,
but that would result in a longer execution time, which is around 3 minutes
for one link at this stage.

https://github.com/iulian1600/Rotten_Tomatoes_scraper.git
