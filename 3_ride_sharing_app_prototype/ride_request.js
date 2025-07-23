fetch("/request_ride", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    lat: selectedLatLng.lat,
    lng: selectedLatLng.lng
  })
})
.then(res => res.json())
.then(data => {
  alert(data.message);
})
.catch(error => {
  alert("Error sending ride request.");
  console.error(error);
});
