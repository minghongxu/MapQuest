# Minghong Xu 81491461
import mapquest
import outputs

def user_interface():
    loc_list = []
    output_list = []
    loc_number = input("Input the number of locations ")
    for i in range(int(loc_number)):
        a = input("Input location： ")
        loc_list.append(a)
    output_number = input("Input the number of outputs you want ")
    for j in range(int(output_number)):
        b = input("Input kind of output： ")
        output_list.append(b)

    route_result = mapquest.url_dict(mapquest.build_route_url(loc_list))
    e = []
    for i in route_result['route']['locations']:
        lat = i['latLng']['lat']
        e.append(lat)
        lng = i['latLng']['lng']
        e.append(lng)
    s = str(e).strip('[]{}')
    for k in output_list:
        if k == 'LATLONG':
            print('LATLONGS')
            outputs.LATLONG().print_latlong(route_result)
        elif k == 'STEPS':
            print('DIRECTIONS')
            outputs.STEPS().print_steps(route_result)
        elif k == 'TOTALTIME':
            outputs.TOTALTIME().print_totaltime(route_result)
        elif k == 'TOTALDISTANCE':
            outputs.TOTALDISTANCE().print_totaldistance(route_result)
        elif k == 'ELEVATION':
            print('ELEVATIONS')
            eve_result = mapquest.url_dict(mapquest.build_elevation_url(s))
            outputs.ELEVATION().print_elevations(eve_result)

    print()
    print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')
    
if __name__ == '__main__':
    user_interface()
