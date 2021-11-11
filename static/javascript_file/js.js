var autocomplete, marker, infowindow, map;

function initMap() {

    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: -33.56, lng: 151.21},
        zoom: 13
    });

    infowindow = new google.maps.InfoWindow();
    marker = new google.maps.Marker({
        map: map
    });

    var inputs = document.querySelector('#address');
    autocomplete = new google.maps.places.Autocomplete(inputs);

    google.maps.event.addListener(autocomplete, 'place_changed', function () {

        marker.setVisible(false);
        infowindow.close();

        var place = autocomplete.getPlace();
        if (!place.geometry) {
            alert('Error');
        }
        if (place.geometry.viewport) {
            map.fitBounds(place.geometry.viewport);
        } else {
            alert('Error');
        }

        marker.setIcon({
            url: place.icon,
            scaledSize: new google.maps.Size(35, 35)
        });

        marker.setPosition(place.geometry.location);
        marker.setVisible(true);

        var address = '';
        console.log(place.address_components);
        if (place.address_components) {
            address = [
                (place.address_components[0] && place.address_components[0].short_name || ''),
                (place.address_components[1] && place.address_components[1].short_name || ''),
                (place.address_components[2] && place.address_components[2].short_name || '')
            ].join(' ');
        }

        infowindow.setContent('<div><strong>' + place.name + '</strong><br>' + address);
        infowindow.open(map, marker)
    });
}
