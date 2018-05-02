'use strict';
/**
 * Created by asus on 10.04.18.
 */
var xhr = new XMLHttpRequest();
var parser = new DOMParser();

function getConditions(lat, lon) {
    var url = 'https://nominatim.openstreetmap.org/reverse?lat=' + lat + '&lon=' + lon + '&format=json&accept-language=en';

    xhr.open("GET", url, false);
    xhr.send();
    var json_result = JSON.parse(xhr.responseText);
    var osm_type = json_result.osm_type;
    if (osm_type == 'way') {

        var way_id = json_result.osm_id;
        var result = localStorage.getItem(way_id);
        if (result) {
            console.log('No change.');
            result = JSON.parse(result);
            console.log(result);
            return result;
        }
        console.log('New Way!');
        result = {};
        var url2 = 'https://api.openstreetmap.org/api/0.6/way/' + way_id;
        xhr.open("GET", url2, false);
        xhr.send();

        var xmlDoc = parser.parseFromString(xhr.responseText, "text/xml");

        var j = xml2json(xmlDoc, ' ');
        var tag = JSON.parse(j).osm.way.tag;

        //convert
        for (var i = 0; i < tag.length; i++) {
            result[tag[i]["@k"]] = tag[i]["@v"];
        }
        console.log(result);
        localStorage.setItem(way_id, JSON.stringify(result));
        return result;
    }
    return {};
    // console.log(xhr.status);
    // console.log(json_result);
    // console.log(osm_type);
    // console.log(way_id);

}