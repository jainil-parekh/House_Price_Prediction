function getBathValue() {
  var uiBathrooms = document.getElementsByName("uiBathrooms");
  for (var i in uiBathrooms) {
    if (uiBathrooms[i].checked) {
      return parseInt(i) + 1;
    }
  }
  return -1; // Invalid Value
}

function getBHKValue() {
  var uiBHK = document.getElementsByName("uiBHK");
  for (var i in uiBHK) {
    if (uiBHK[i].checked) {
      return parseInt(i) + 1;
    }
  }
  return -1; // Invalid Value
}

function onClickedEstimatePrice() {
  var sqft = document.getElementById("uiSqft").value;
  var bhk = getBHKValue();
  var bathrooms = getBathValue();
  var location = document.getElementById("uiLocations").value;
  var estPrice = document.getElementById("uiEstimatedPrice");

  var url = "http://127.0.0.1:5000/predict_home_price";

  $.post(
    url,
    {
      total_sqft: parseFloat(sqft),
      bhk: bhk,
      bath: bathrooms,
      location: location,
    },
    function (data, status) {
      console.log(data); // Check the response in the console
      if (data && data.estimated_price) {
        estPrice.innerHTML = "<h2>" + data.estimated_price + " Lakh</h2>";
      } else {
        estPrice.innerHTML = "<h2>Error: Unable to estimate price</h2>";
      }
    }
  );
}

function onPageLoad() {
  console.log("document loaded");
  var url = "http://127.0.0.1:5000/get_location_names"; // Use this if you are NOT using nginx which is first 7 tutorials
  //   var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  $.get(url, function (data, status) {
    console.log("got response for get_location_names request");
    if (data) {
      var locations = data.locations;
      var uiLocations = document.getElementById("uiLocations");
      $("#uiLocations").empty();
      for (var i in locations) {
        var opt = new Option(locations[i]);
        $("#uiLocations").append(opt);
      }
    }
  });
}

onPageLoad();

// Define your onPageLoad function
function onPageLoad() {
  console.log("document loaded");
  var url = "http://127.0.0.1:5000/get_location_names";
  // Rest of your onPageLoad code...
}
