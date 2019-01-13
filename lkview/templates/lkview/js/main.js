var token = '{{csrf_token}}';

$('.Phones>li>a').on('click', function(event) {
    number = $(event.target).html();
    number = number.trim()
      $.ajax( {
        headers: { "X-CSRFToken": token },
        beforeSend: function() {
        $('#in').empty();
        $('#out').empty();
        $('#data').append('\
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
      compile : function() {
        $('.circle').hide('slow');
        $('.circle').remove();
        $('#norec').remove();
      },
      method: 'POST',
      url: (window.location.origin+"/record/number/" + number + "/"),
      contentType: "application/json; charset=utf-8",
      dataType: "json",
      success: function( data ) {
        $('.circle').hide('slow');
        $('.circle').remove();
        /*if(data.length == 0) {
          console.log('data.length: ' + data.length)
          $('#data').append('<h2 id="norec">Записей не найдено</h2>');
          $('#in').remove();
          $('#out').remove();
          return;
        }*/
        $('#in').append('<h2>Входящие вызовы</h2>');
        $('#out').append('<h2>Исходящие вызовы</h2>');
        for(var i in data) {
          if(data[i]['direction'] === 'in') {
            str = "<li class=\"btn btn-block btn-primary\" filename=\""
            + data[i]['filename'] +"\">"+data[i]['data'] + " " + data[i]['extern'] +"</li>";
            li = $('#in').append(str);
            li.children().last().wrap("<p class=record></p>");
          }
          else {
            str = "<li class=\"btn btn-block btn-primary\" filename=\""
            + data[i]['filename'] +"\">"+data[i]['data'] + " " + data[i]['extern'] +"</li>";
            li = $('#out').append(str);
            li.children().last().wrap("<p class=record></p>");
          }
        }
      }
    }).done(function() {
      $('.record li').on('click', function(event){
        filename = this.attributes.filename.value;
        parent = $(this.parentElement)
        $.ajax ( {
          headers: { "X-CSRFToken": token },
          beforeSend : function() {
            $('.player').hide('slow');
            $('.player').remove();
          },
          method: 'POST',
          url: (window.location.origin+"/convert" + filename),
          contentType: "application/json; charset=utf-8",
          dataType: "json",
          success: function( data ) {
            parent.append("<audio class='player' src=https://srvlk.ath.ru/ogg/"+filename.substr(1, filename.length - 4) +
            "ogg controls>play record</audio>");
          }
        }).done(function(){
          $('.player').show('slow')
        });
      });
    });
});


$('#filter').on('input',function(e) {
  f = $('input.form-control');
  btns = $('li.btn');
  btns.filter(function(index) {
    if (!btns[index].innerText.includes(f.val())) {
      $(btns[index]).hide();
    }
    else {
      $(btns[index]).show();
    }
  });
});
