mapboxgl.accessToken = 'pk.eyJ1IjoidHJlZXZld2hpdGUiLCJhIjoiY2t6eTdwdWNnMDhqdjJ2cGNmc3BteGQ0NCJ9.j8xZDb0U_4ZMn4WFlLlefw';

var map = new mapboxgl.Map({
    container: 'map',
    center: [-3.5345, 50.7365],
    pitch: 45,
    zoom: 16,
    style: 'mapbox://styles/mapbox/streets-v11'
});

map.addControl(new mapboxgl.NavigationControl());

map.on('load', () => {
    const layers = map.getStyle().layers;

    const labelLayerId = layers.find(
        (layer) => layer.type === 'symbol' && layer.layout['text-field']
    ).id;

    map.addLayer(
        {
            'id': 'add-3d-buildings',
            'source': 'composite',
            'source-layer': 'building',
            'filter': ['==', 'extrude', 'true'],
            'type': 'fill-extrusion',
            'minzoom': 15,
            'paint': {
                'fill-extrusion-color': '#aaa',
                'fill-extrusion-height': [
                    'interpolate',
                    ['linear'],
                    ['zoom'],
                    15,
                    0,
                    15.05,
                    ['get', 'height']
                ],
                'fill-extrusion-base': [
                    'interpolate',
                    ['linear'],
                    ['zoom'],
                    15,
                    0,
                    15.05,
                    ['get', 'min_height']
                ],
                'fill-extrusion-opacity': 0.6
            }
        },
        labelLayerId
    );

    map.addSource('places', {
        'type': 'geojson',
        'data': {
            'type': 'FeatureCollection',
            'features': [
                {
                    'type': 'Feature',
                    'properties': {
                        'description':
                            '<strong>Harison Building</strong><p>Currently Controlled by {{ harrisonOwner }}</p>',
                        'icon': 'circle-white-2'
                    },
                    'geometry': {
                        'type': 'Point',
                        'coordinates': [-3.5325, 50.73765]
                    }
                },
                {
                    'type': 'Feature',
                    'properties': {
                        'description':
                            '<strong>Inspiration Center</strong><p>Currently Controlled by {{ inovationOwner }}</p>',
                        'icon': 'circle-white-2'
                    },
                    'geometry': {
                        'type': 'Point',
                        'coordinates': [-3.53121, 50.7383]
                    }
                },
                {
                    'type': 'Feature',
                    'properties': {
                        'description':
                            '<strong>Innovation Center</strong><p>Currently Controlled by {{ inovationOwner }}</p>',
                        'icon': 'circle-white-2'
                    },
                    'geometry': {
                        'type': 'Point',
                        'coordinates': [-3.53063, 50.73808]
                    }
                },
                {
                    'type': 'Feature',
                    'properties': {
                        'description':
                            '<strong>Laver Building</strong><p>Currently Controlled by {{ inovationOwner %}}</p>',
                        'icon': 'circle-white-2'
                    },
                    'geometry': {
                        'type': 'Point',
                        'coordinates': [-3.53347, 50.73733]
                    }
                }
            ]
        }
    })

    map.addLayer({
        'id': 'places',
        'type': 'symbol',
        'source': 'places',
        'layout': {
            'icon-image': '{icon}',
            'icon-allow-overlap': true
        }
    });

    map.on('click', 'places', (e) => {
        // Copy coordinates array.
        const coordinates = e.features[0].geometry.coordinates.slice();
        const description = e.features[0].properties.description;

        // Ensure that if the map is zoomed out such that multiple
        // copies of the feature are visible, the popup appears
        // over the copy being pointed to.
        while (Math.abs(e.lngLat.lng - coordinates[0]) > 180) {
            coordinates[0] += e.lngLat.lng > coordinates[0] ? 360 : -360;
        }

        new mapboxgl.Popup()
            .setLngLat(coordinates)
            .setHTML(description)
            .addTo(map);
    });

    // Change the cursor to a pointer when the mouse is over the places layer.
    map.on('mouseenter', 'places', () => {
        map.getCanvas().style.cursor = 'pointer';
    });

    // Change it back to a pointer when it leaves.
    map.on('mouseleave', 'places', () => {
        map.getCanvas().style.cursor = '';
    });
    map.addControl(
        new mapboxgl.GeolocateControl({
            positionOptions: {
            enableHighAccuracy: true
            },
            // When active the map will receive updates to the device's location as it changes.
            trackUserLocation: true,
            // Draw an arrow next to the location dot to indicate which direction the device is heading.
            showUserHeading: true
        })
    );
});
