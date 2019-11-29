## How to use?

Install python 3.7
Intall selenium :   pip install selenium

* PLEASE PLACE YOUR OPERATING SYSTEM CHROMEDRIVER FOLDER AND SCRIPT IN THE SAME DIRECTORY

Your system is windows, please choose chromedriver_win32
		Mac, please choose chromedriver_mac64
		Ubuntu/Linux, please choose chromedriver_linux64

## How to run?

Run script: python BuyingYeezySupplyShoes.py --url https://yeezysupply.com/Q87HU -d 0.2 -t 2 -n 2 --use-proxy

-d (--delay): delay time to open tab (default 0.2s)

-t (--rtime): time range allow to open tabs, get through this time will stop to open tabs (default 2s)

-n (--number): number of opened tab in the same time (default 2 tabs)

--use-proxy: this allow to use Free Proxy VPN from https://free-proxy-list.net (default No)

*Note: You must add -u (--url) to argument, the others is optional

