function add_topic_clicked() {
  var this_form = $('#topic_create_form');
  $.ajax({
    type: 'POST', // define the type of HTTP verb we want to use (POST for our form)
    url: dutils.urls.resolve('topic_create'), // the url where we want to POST
    data: this_form.serialize(), // our data object
    dataType: 'json', // what type of data do we expect back from the server
    encode: true
  })
  // The query failed.  Data should contain the error stuff.
  .fail(function(data) {
    alert(JSON.stringify(data));
  })
  // use the success callback to trigger a page reload
  .success(function(data) {
    location.reload(true); // true forces the reload from server
  })
  // using the done promise callback
  .done(function(data) {
    // log data to the console so we can see
    console.log(data);
  });
}
