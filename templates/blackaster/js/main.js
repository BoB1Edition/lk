var token = '{{csrf_token}}';

$('.number').on('click', function() {
  dt = $(this).attr('data');
  $.ajax({
    headers: { "X-CSRFToken": token },
    beforeSend: function() {
      $('#result').empty();
      $('#result').html('<p>Примите звонок на Ваш телефон</p>');
    },
    method: 'POST',
    url: ('listen/' + dt),
    dataType: "html",
    success: function( data ) {
      console.log(data);
      if (data === 'None') {
          $('#result').html('<p>В данный момент прослушать звонок нельзя</p>');
      } else {
          $('#result').html('<p>Сейчас идет прослушивание звонка</p>');
      }
    }
  });
});
