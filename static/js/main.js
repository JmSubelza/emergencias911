/**
 * Created by SOPORTE-SISTEMAS on 19/10/2016.
 */
function initMap() {
    var LatLog = new google.maps.LatLng(-17.783308, -63.182118);
    var MapSettings = {
        zoom: 16,
        center: LatLog,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        tilt: 45,
        overviewMapControl: true,
        overviewMapControlOptions: {
            opened: true
        }
    };

    var map = new google.maps.Map(document.getElementById("maps"), MapSettings);

    var marker = new google.maps.Marker({
        position: LatLog,
        map: map,
        draggable: true,
        title: 'Arrastrame'
    });

    google.maps.event.addListener(marker, 'position_changed', function () {
        getMarkerCoords(marker)
    });

    function getMarkerCoords() {
        var markerCoords = marker.getPosition();
        $('#id_lat').val(markerCoords.lat().toFixed(6));
        $('#id_lng').val(markerCoords.lng().toFixed(6));

    }
};

function initMapEdit(Lat, Log) {
    var LatLog = new google.maps.LatLng(Lat, Log);
    var MapSettings = {
        zoom: 16,
        center: LatLog,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        tilt: 45,
        overviewMapControl: true,
        overviewMapControlOptions: {
            opened: true
        }
    };

    var map = new google.maps.Map(document.getElementById("maps"), MapSettings);

    var marker = new google.maps.Marker({
        position: LatLog,
        map: map,
        draggable: true,
        title: 'Arrastrame'
    });

    google.maps.event.addListener(marker, 'position_changed', function () {
        getMarkerCoords(marker)
    });

    function getMarkerCoords() {
        var markerCoords = marker.getPosition();
        $('#id_lat').val(markerCoords.lat().toFixed(6));
        $('#id_lng').val(markerCoords.lng().toFixed(6));

    }
};
