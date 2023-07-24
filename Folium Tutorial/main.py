import folium

if __name__ == '__main__':
    print('Start')
    mapPath = "folium-map.html"
    centerCoord = [37.566345, 126.977893]
    # generate a list of random coordinates in a list called markerCoord
    markerCoord = [37.566345, 126.977893]

    vmap = folium.Map(centerCoord, zoom_start=9)

    folium.vector_layers.Circle(
        location=markerCoord,
        radius=2000,
        color="red",
        fill=True,
        fill_color="red",
        tooltip="No fly zone"

    ).add_to(vmap)

    vmap.save(mapPath)
#
# [-5.06360, 83.93998],
# [33.10999, -103.86537],