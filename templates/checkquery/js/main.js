var token = '{{csrf_token}}';

$('.queue').on('click', function() {
  dt = $(this).attr('data');
  $.ajax({
    headers: { "X-CSRFToken": token },
    beforeSend: function() {
      $('#result').empty();
    },
    method: 'POST',
    url: ('queue/' + dt),
    dataType: "html",
    success: function( data ) {
      console.log(data);
      $('#result').html(data);
    }
  });
});
