# Minghong Xu 81491461
import mapquest

class STEPS:
    def print_steps(self, result):
        for i in result['route']['legs']:
            for j in i['maneuvers']:
                print(j['narrative'])

class TOTALDISTANCE:
    def print_totaldistance(self, result):
        distance = round(result['route']['distance'])
        print('\nTOTAL DISTANCE: ' + str(distance) + ' miles')
        

class TOTALTIME:
    def print_totaltime(self, result):
        time = round((result['route']['time']) / 60)
        print('\nTOTAL TIME: ' + str(time) + ' minutes')


class LATLONG:
    def print_latlong(self, result):
        for i in result['route']['locations']:
            lat = i['latLng']['lat']
            if lat <= 0:
                lat = abs(lat)
                lat = '{:.2f}'.format(lat) + 'S'
                print(lat)
            elif lat > 0:
                lat = '{:.2f}'.format(lat) + 'N'
                print(lat)

            lng = i['latLng']['lng']
            if lng <= 0:
                lng = abs(lng)
                lng = '{:.2f}'.format(lng) + 'W'
                print(lng)
            elif lng > 0:
                lng = '{:.2f}'.format(lng) +  'E'
                print(lng)


        

class ELEVATION:
    def print_elevations(self, result):       
        for i in result['elevationProfile']:
            print(round(i['height'] * 3.28))



#Takes a parsed JSON response and prints the steps to the destination

#'Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors.'

#NO ROUTE FOUND
#MAPQUEST ERROR
