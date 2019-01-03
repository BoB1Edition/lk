var token = '{{csrf_token}}';

$('button').on('click', function(){
  $.ajax({
    headers: { "X-CSRFToken": token },
    beforeSend: function() {
      $('#result').empty();
    },
    method: 'POST',
    url: ('result/'),
    data: {
      'Login': 'login'
    },
    dataType: "html",
    success: function( data ) {
      console.log(data);
      $('#result').html(data);
  }
});
