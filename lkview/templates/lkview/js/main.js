var token = '{{csrf_token}}';

$('.Phones>li>a').on('click', function(event) {
    number = $(event.target).html();
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
      },
      method: 'POST',
      url: (window.location.origin+"/record/number/" + number + "/"),
      contentType: "application/json; charset=utf-8",
      dataType: "json",
      success: function( data ) {
        console.log(data)
        $('.circle').hide('slow');
        $('.circle').remove();
        $('#in').append('<h1>Входящие вызовы</h1>');
        $('#out').append('<h1>Исходящие вызовы</h1>');
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
            parent.append("<audio class='player' src=http://srvlk.ath.ru/ogg/"+filename.substr(1, filename.length - 4) +
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
      btns[index].hide();
      console.log(index)
    }
  });
});
