#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  weather_4_city.py
#  
#  Copyright 2016 Arturo <arturo@papalinux>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
''' This python script returns current weather of city you enter.
    API : Yahoo Weather API (https://developer.yahoo.com/weather/)
    How to run this script:
    $python yahoo-weatherAPI.py
    Enter City Name :
    Seoul
    Output : Current Weather in seoul: Light Rain, 41F/5C, (Sun, 29 Nov 2015 7:59 pm KST)
'''


#Chinseok Lee revised my code in his gist. His work is professional.
#link: https://gist.github.com/allieus/4fa672395b75e9e7b907

import urllib.request, urllib.parse, json, ssl
scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)

def celsius(fahrenheit):
  ''' change Fahrenheit to Celsius '''
  return ((int(fahrenheit) - 32) * 5/9)

#request and open URL
city = input("Enter your city: ")
baseurl = 'https://query.yahooapis.com/v1/public/yql?q='
yql_query = 'select item.condition from weather.forecast where woeid in (select woeid from geo.places(1) where text="%s")'% city
yql_url = baseurl + urllib.parse.quote(yql_query, encoding='utf-8') + '&format=json&env=store://datatables.org/alltableswithkeys'
result = urllib.request.urlopen(yql_url, context=scontext).read()

#data parsing
data = json.loads(result.decode('utf-8'))

#output
try:
    parsed = data['query']['results']['channel']['item']['condition']
    word = (parsed['text'])
    temp = ('%sF/%dC' % (parsed['temp'], int(celsius(parsed['temp']))))
    time = (parsed['date'])
    print (('Current weather in %s: %s, %s, (%s)') % (city, word, temp, time))

except (ValueError, KeyError, TypeError):
    print ('Not Found')
