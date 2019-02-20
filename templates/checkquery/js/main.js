var token = '{{csrf_token}}';

$('.queue').on('click', function() {
  dt = $(this).attr('data');
  $.ajax({
    headers: { "X-CSRFToken": token },
    beforeSend: function() {
      $('#result').empty();
      $('#result').append('\
      <div class="circle">\
      <div class="loader">\
      <div class="loader">\
      <div class="loader">\
         <div class="loader">\
\
         </div>\
      </div>\
  </div>\
</div>\
</div> ');
    },
    method: 'POST',
    url: ('queue/' + dt),
    dataType: "html",
    success: function( data ) {
      $('#result').empty();
      console.log(data);
      $('#result').html(data);
    }
  });
});
