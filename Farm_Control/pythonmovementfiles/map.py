# import gmplot package
import gmplot
#import gps communication .py
#changee lists to s1 and s2
latitude_list = [ 17.4567417, 17.5587901, 17.6245545]
longitude_list = [ 78.2913637, 78.007699, 77.9266135 ]
gmap = gmplot.GoogleMapPlotter(17.438139, 78.3936413, 11)
gmap.scatter( latitude_list, longitude_list, '# FF0000', size = 40, marker = False)
# polygon method Draw a polygon with
# the help of coordinates
gmap.polygon(latitude_list, longitude_list, color = 'cornflowerblue')
gmap.apikey = "Your_API_KEY"
gmap.draw( "C:\\Users\\" )