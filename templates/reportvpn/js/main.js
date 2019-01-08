var token = '{{csrf_token}}';

$('form').on('submit', function(e){
  login = $('#login').val()
  databegin = $('#databegin').val()
  dataend = $('#dataend').val()
  e.preventDefault();
  $.ajax({
    async: false,
    headers: { "X-CSRFToken": token },
    beforeSend: function() {
      $('#result').empty();
    },
    method: 'POST',
    url: ('result/'),
    processData: false,
    data: JSON.stringify({
      'Login': login,
      'databegin': databegin,
      'dataend': dataend,
    }),
    contentType: "application/json; charset=utf-8",
    //data: ({ Markers: markers }),
    dataType: "html",
    success: function( data ) {
      console.log(data);
      $('#result').html(data);

    }
  });
  return false;
});
